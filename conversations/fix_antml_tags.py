#!/usr/bin/env python3
from pathlib import Path

# Read the file
file_path = Path("/Users/scottmcguire/www/conversations/featured/ai-consciousness-safety-testing-and-equilibrium-dynamics.md")
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

print("Searching for antml: tags...")

# Replace all variations of the thinking_mode tag
replacements = [
    ('<thinking_mode>', '&lt;thinking_mode&gt;'),
    ('</thinking_mode>', '&lt;/thinking_mode&gt;'),
]

for old, new in replacements:
    if old in content:
        count = content.count(old)
        print(f"Found {count} instances of '{old}'")
        content = content.replace(old, new)
        print(f"Replaced with '{new}'")

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("\nFile updated successfully")

# Verify line 23
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    if len(lines) > 22:
        print(f"\nLine 23 now reads: {lines[22].strip()}")