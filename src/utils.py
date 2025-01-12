import os
import shutil
from nodeutils import *
from markdownutils import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")


    with open(from_path, 'r', encoding="utf-8") as m:
        markdown_read = m.read()
        #print("1--",m)

    with open(template_path, 'r', encoding="utf-8") as t:
        template_read = t.read()
        #print("2--",t)
    
    html_node = markdown_to_html_node(markdown_read)
    string_html = html_node.to_html()

    title_page = extract_title(markdown_read)

    template = template_read.replace("{{ Title }}",title_page).replace("{{ Content }}", string_html)

    with open(dest_path, 'w', encoding="utf-8") as f:
        f.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    value = os.listdir(path=dir_path_content)
    for i in value:
        #print(type(i))
        if "." not in i:
            value = f"{dir_path_content}/{i}"
            dest_value = f"{dest_dir_path}/{i}"
            generate_pages_recursive(dir_path_content=value,template_path=template_path,dest_dir_path=dest_value)
        else:
            name = i.replace(".md",".html")
            dir_path = f"{dir_path_content}/{i}"
            dest_path = f"{dest_dir_path}/{name}"
            
            generate_page(dir_path,template_path,dest_path)
    