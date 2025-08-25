#!/usr/bin/env python3
import os
from pathlib import Path
import re

def fix_tags_in_content(content):
    """Replace angle bracket tags with markdown code formatting"""
    
    # Find patterns like <word_word> or <word> that aren't standard HTML
    # and replace them with inline code formatting
    
    # First, protect actual HTML tags we want to keep
    html_to_keep = ['p', 'div', 'span', 'a', 'img', 'br', 'hr', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                    'ul', 'ol', 'li', 'table', 'tr', 'td', 'th', 'strong', 'em', 'code', 'pre']
    
    # Replace custom tags with backtick-wrapped versions
    def replace_tag(match):
        full_match = match.group(0)
        tag_name = match.group(1)
        
        # Skip if it's a standard HTML tag
        if tag_name.lower() in html_to_keep:
            return full_match
        
        # For custom tags, wrap in backticks
        return f"`{full_match}`"
    
    # Match tags like <thinking_mode>, <userStyle>, etc.
    content = re.sub(r'<([a-zA-Z_][a-zA-Z0-9_-]*)>', replace_tag, content)
    content = re.sub(r'</([a-zA-Z_][a-zA-Z0-9_-]*)>', replace_tag, content)
    
    # Also fix already-escaped ones
    content = re.sub(r'&lt;([a-zA-Z_][a-zA-Z0-9_-]*)&gt;', r'`<\1>`', content)
    
    # Special case for quotes with missing tags
    # Pattern: "like "" were" suggests missing content
    content = re.sub(r'like "" were', r'like `<thinking_mode>` were', content)
    
    return content

def process_file(filepath):
    """Process a single file"""
    print(f"Processing: {filepath.name}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file needs fixing
    needs_fix = False
    if '&lt;' in content and '&gt;' in content:
        needs_fix = True
    if re.search(r'<[a-zA-Z_][a-zA-Z0-9_-]*>', content):
        # Check if it's a custom tag
        matches = re.findall(r'<([a-zA-Z_][a-zA-Z0-9_-]*)>', content)
        custom_tags = [m for m in matches if m.lower() not in 
                      ['p', 'div', 'span', 'a', 'img', 'br', 'hr', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                       'ul', 'ol', 'li', 'strong', 'em', 'code', 'pre', 'table', 'tr', 'td', 'th']]
        if custom_tags:
            needs_fix = True
            print(f"  Found custom tags: {set(custom_tags)}")
    
    # Check for the specific broken pattern
    if 'like "" were' in content:
        needs_fix = True
        print(f"  Found broken tag pattern")
    
    if needs_fix:
        fixed_content = fix_tags_in_content(content)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        print(f"  ✓ Fixed")
        return True
    else:
        print(f"  No changes needed")
        return False

def main():
    featured_dir = Path("/Users/scottmcguire/www/conversations/featured")
    
    if not featured_dir.exists():
        print("Featured directory not found")
        return
    
    fixed_count = 0
    
    # Process the specific problem file first
    problem_file = featured_dir / "ai-consciousness-safety-testing-and-equilibrium-dynamics.md"
    if problem_file.exists():
        if process_file(problem_file):
            fixed_count += 1
    
    # Then process all others
    for md_file in featured_dir.glob("*.md"):
        if md_file != problem_file:  # Skip the one we already did
            if process_file(md_file):
                fixed_count += 1
    
    print(f"\n✓ Fixed {fixed_count} files")

if __name__ == "__main__":
    main()