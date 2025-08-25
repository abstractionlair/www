#!/usr/bin/env python3
import os
from pathlib import Path
import re

def escape_html_in_markdown(content):
    """Escape HTML-like tags in markdown content while preserving actual markdown"""
    
    # Pattern to find potential HTML-like tags that aren't real HTML
    # This will match things like <thinking_mode>, <example>, etc.
    # but try to avoid real HTML and markdown syntax
    
    # First, protect code blocks (both inline and fenced)
    code_blocks = []
    
    # Protect fenced code blocks
    def protect_fenced(match):
        code_blocks.append(match.group(0))
        return f"%%%CODEBLOCK{len(code_blocks)-1}%%%"
    
    content = re.sub(r'```[\s\S]*?```', protect_fenced, content)
    
    # Protect inline code
    def protect_inline(match):
        code_blocks.append(match.group(0))
        return f"%%%CODEBLOCK{len(code_blocks)-1}%%%"
    
    content = re.sub(r'`[^`]+`', protect_inline, content)
    
    # Now escape angle brackets that look like custom tags
    # This regex finds <word> or </word> patterns that aren't common HTML tags
    common_html = ['p', 'div', 'span', 'a', 'img', 'br', 'hr', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                   'ul', 'ol', 'li', 'table', 'tr', 'td', 'th', 'thead', 'tbody', 'strong', 'em',
                   'code', 'pre', 'blockquote', 'style', 'script']
    
    def escape_tag(match):
        tag = match.group(1).lower()
        # If it's a common HTML tag, leave it alone
        if tag in common_html:
            return match.group(0)
        # Otherwise, escape it
        return match.group(0).replace('<', '&lt;').replace('>', '&gt;')
    
    # Match opening and closing tags
    content = re.sub(r'<(/?)([a-zA-Z_][a-zA-Z0-9_-]*)>', escape_tag, content)
    
    # Also escape standalone angle brackets that might be part of pseudo-tags
    content = re.sub(r'<([a-zA-Z_][a-zA-Z0-9_-]*(?:_[a-zA-Z0-9_-]+)*)>', 
                     lambda m: '&lt;' + m.group(1) + '&gt;', content)
    
    # Restore code blocks
    for i, block in enumerate(code_blocks):
        content = content.replace(f"%%%CODEBLOCK{i}%%%", block)
    
    return content

def process_featured_conversations():
    """Process all featured conversation files"""
    featured_dir = Path("/Users/scottmcguire/www/conversations/featured")
    
    if not featured_dir.exists():
        print("Featured directory not found")
        return
    
    processed = 0
    for md_file in featured_dir.glob("*.md"):
        print(f"Processing: {md_file.name}")
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if the file needs escaping
        if '<thinking_mode>' in content or '<thinking>' in content or re.search(r'<[a-zA-Z_][a-zA-Z0-9_-]*_mode>', content):
            print(f"  Found tags to escape in {md_file.name}")
            escaped_content = escape_html_in_markdown(content)
            
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(escaped_content)
            
            processed += 1
    
    print(f"\nProcessed {processed} files with HTML escaping")

def check_for_problematic_tags():
    """Check which files have problematic tags"""
    featured_dir = Path("/Users/scottmcguire/www/conversations/featured")
    
    print("Checking for problematic tags...")
    problematic = []
    
    for md_file in featured_dir.glob("*.md"):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for custom tags that might be interpreted as HTML
        matches = re.findall(r'<([a-zA-Z_][a-zA-Z0-9_-]*)>', content)
        if matches:
            # Filter out common HTML tags
            custom_tags = [m for m in matches if m.lower() not in 
                          ['p', 'div', 'span', 'a', 'img', 'br', 'hr', 'h1', 'h2', 'h3', 
                           'h4', 'h5', 'h6', 'ul', 'ol', 'li', 'strong', 'em', 'code', 'pre']]
            if custom_tags:
                print(f"  {md_file.name}: {set(custom_tags)}")
                problematic.append(md_file.name)
    
    return problematic

if __name__ == "__main__":
    # First check what needs fixing
    problematic = check_for_problematic_tags()
    
    if problematic:
        print(f"\nFound {len(problematic)} files with custom tags that need escaping")
        print("\nProcessing files...")
        process_featured_conversations()
    else:
        print("\nNo problematic tags found")
    
    print("\nDone!")