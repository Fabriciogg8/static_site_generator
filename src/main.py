import os
import shutil
from textnode import TextNode
from nodeutils import *
from markdownutils import *
from utils import *

def copy_recursive(src, dst):
    if os.path.isdir(src):
        if not os.path.exists(dst):
            os.mkdir(dst)
        items = os.listdir(src)
        for item in items:
            src_path = os.path.join(src, item)
            dst_path = os.path.join(dst, item)
            copy_recursive(src_path, dst_path)
    else:
        shutil.copy2(src, dst)
        print(f"Copied {src} to {dst}")

def main():
    src_dir = "./static"
    dst_dir = "./public"
    
    # Delete destination directory if it exists
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    
    # Copy directory recursively
    copy_recursive(src_dir, dst_dir)
    print("Copy complete.")

    generate_page("./content/index.md","./template.html","./public/index.html")



main()
