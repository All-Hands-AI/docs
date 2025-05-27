#!/usr/bin/env python3
import os
import re
import glob

def fix_mdx_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix common issues
    
    # 1. Fix malformed Accordion tags
    content = re.sub(r'<Accordion title="([^"]*)"<CodeGroup>', r'<Accordion title="\1">', content)
    content = re.sub(r'</Accordion<CodeGroup>', r'</Accordion>', content)
    
    # 2. Fix malformed CodeGroup tags
    content = re.sub(r'<CodeGroup>\s*```', r'<CodeGroup>', content)
    content = re.sub(r'```\s*</CodeGroup>', r'</CodeGroup>', content)
    
    # 3. Remove stray CodeGroup tags
    content = re.sub(r'<CodeGroup>\s*</CodeGroup>', r'', content)
    
    # 4. Fix nested tags
    content = re.sub(r'<([^>]+)<CodeGroup>', r'<\1>', content)
    
    # 5. Fix closing tags
    content = re.sub(r'</div<CodeGroup>', r'</div>', content)
    
    # 6. Fix malformed Note tags
    content = re.sub(r'<Note>\s*```', r'<Note>', content)
    content = re.sub(r'```\s*</Note>', r'</Note>', content)
    
    # 7. Fix malformed Warning tags
    content = re.sub(r'<Warning>\s*```', r'<Warning>', content)
    content = re.sub(r'```\s*</Warning>', r'</Warning>', content)
    
    # 8. Fix malformed Tip tags
    content = re.sub(r'<Tip>\s*```', r'<Tip>', content)
    content = re.sub(r'```\s*</Tip>', r'</Tip>', content)
    
    # 9. Fix malformed div tags with style
    content = re.sub(r'<div style=\{\{ ([^}]+) \}\}<CodeGroup>', r'<div style={{ \1 }}>', content)
    
    # 10. Fix malformed description in frontmatter
    pattern = r'---\s*title: "[^"]*"\s*description: "<([^>]+)>.*?---'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, r'---\ntitle: "\1"\ndescription: "OpenHands documentation"\n---', content, flags=re.DOTALL)
    
    # Write the fixed content back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    # Get all MDX files in the modules directory
    mdx_files = glob.glob('modules/**/*.mdx', recursive=True)
    md_files = glob.glob('modules/**/*.md', recursive=True)
    all_files = mdx_files + md_files
    
    fixed_count = 0
    for file_path in all_files:
        if fix_mdx_file(file_path):
            fixed_count += 1
            print(f"Fixed: {file_path}")
    
    print(f"\nFixed {fixed_count} files out of {len(all_files)}")

if __name__ == "__main__":
    main()