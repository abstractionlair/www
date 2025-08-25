#!/usr/bin/env python3
import os
from pathlib import Path
import re

def escape_tags_in_backticks(content):
    """Escape HTML tags that are within backticks"""
    
    # Pattern to find content within backticks
    # This will match `<something>` and replace with `&lt;something&gt;`
    def replace_in_backticks(match):
        code = match.group(1)
        # Escape < and > within the backticked content
        escaped = code.replace('<', '&lt;').replace('>', '&gt;')
        return f"`{escaped}`"
    
    # Find backticked content and escape tags within
    # Match single backticks with content containing < or >
    content = re.sub(r'`([^`]*[<>][^`]*)`', replace_in_backticks, content)
    
    # Also handle double backticks
    def replace_in_double_backticks(match):
        code = match.group(1)
        escaped = code.replace('<', '&lt;').replace('>', '&gt;')
        return f"``{escaped}``"
    
    content = re.sub(r'``([^`]*[<>][^`]*)``', replace_in_double_backticks, content)
    
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
        
        # Check if the file has backticked tags that need escaping
        if re.search(r'`[^`]*<[^`>]+>[^`]*`', content) or re.search(r'``[^`]*<[^`>]+>[^`]*``', content):
            print(f"  Found tags to escape in {md_file.name}")
            escaped_content = escape_tags_in_backticks(content)
            
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(escaped_content)
            
            processed += 1
    
    print(f"\nProcessed {processed} files with HTML escaping")

if __name__ == "__main__":
    process_featured_files()