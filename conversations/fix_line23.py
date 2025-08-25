#!/usr/bin/env python3
from pathlib import Path

# Read the file
file_path = Path("/Users/scottmcguire/www/conversations/featured/ai-consciousness-safety-testing-and-equilibrium-dynamics.md")
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Fix line 23 (index 22)
if len(lines) > 22:
    line = lines[22]
    print(f"Original line 23: {line}")
    
    # Replace the antml:thinking_mode tag
    fixed_line = line.replace('<thinking_mode>', '&lt;thinking_mode&gt;')
    lines[22] = fixed_line
    
    print(f"Fixed line 23: {fixed_line}")
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print("File updated successfully")
else:
    print("File has fewer than 23 lines")