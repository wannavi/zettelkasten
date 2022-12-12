import os

from pathlib import Path

POSTS_DIR = Path('./posts')
MDX_HEADER = '''
---
title: {}
date : {}
---
'''

for md_path in POSTS_DIR.glob("**/*.md"):
    fname = md_path.stem
    date, title = fname.split(' ', 1)
    content = md_path.read_text()

    md_path.write_text(MDX_HEADER.format(title, '20' + date, '') + content)
