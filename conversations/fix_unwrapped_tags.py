#!/usr/bin/env python3
import os
from pathlib import Path
import re

def fix_unwrapped_tags(content):
    """Fix tags that aren't wrapped in backticks by escaping them"""
    
    # Find patterns like <word> or <word_word> that aren't in backticks
    # and escape them with &lt; and &gt;
    
    # First, protect already backticked content
    backticked = []
    def protect_backticked(match):
        backticked.append(match.group(0))
        return f"%%%BACKTICK{len(backticked)-1}%%%"
    
    # Protect backticked content
    content = re.sub(r'``[^`]+``', protect_backticked, content)
    content = re.sub(r'`[^`]+`', protect_backticked, content)
    
    # Now escape any remaining < and > that look like custom tags
    # Common HTML tags to skip
    html_tags = ['p', 'div', 'span', 'a', 'img', 'br', 'hr', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                 'ul', 'ol', 'li', 'table', 'tr', 'td', 'th', 'thead', 'tbody', 'strong', 'em',
                 'code', 'pre', 'blockquote', 'style', 'script']
    
    def escape_tag(match):
        tag_name = match.group(1)
        # Skip if it's a common HTML tag
        if tag_name.lower() in html_tags:
            return match.group(0)
        # Otherwise escape it
        return match.group(0).replace('<', '&lt;').replace('>', '&gt;')
    
    # Match opening and closing tags
    content = re.sub(r'</?([a-zA-Z_][a-zA-Z0-9_-]*)>', escape_tag, content)
    
    # Restore backticked content
    for i, protected in enumerate(backticked):
        content = content.replace(f"%%%BACKTICK{i}%%%", protected)
    
    return content

def process_featured_files():
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
        
        # Check if the file has unescaped tags outside of backticks
        # Save original for comparison
        original = content
        fixed_content = fix_unwrapped_tags(content)
        
        if fixed_content != original:
            print(f"  Fixed unwrapped tags in {md_file.name}")
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            processed += 1
    
    print(f"\nProcessed {processed} files with unwrapped tags")

if __name__ == "__main__":
    process_featured_files()