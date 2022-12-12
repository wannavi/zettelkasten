import os 

from pathlib import Path

POSTS_DIR = Path('./posts')

for md_path in POSTS_DIR.glob('**/*.md'):
    file_name = md_path.stem

    new_dir_path = POSTS_DIR / 'new' / file_name
    new_dir_path.mkdir(parents=True, exist_ok=True)

    content = md_path.read_text()

    new_file_path = new_dir_path / 'index.mdx'
    new_file_path.write_text(content)
