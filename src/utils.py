from markdownutils import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")


    with open(from_path, 'r', encoding="utf-8") as m:
        markdown_read = m.read()
        print("1--",m)

    with open(template_path, 'r', encoding="utf-8") as t:
        template_read = t.read()
        print("2--",t)
    
    html_node = markdown_to_html_node(markdown_read)
    string_html = html_node.to_html()

    title_page = extract_title(markdown_read)

    template = template_read.replace("{{ Title }}",title_page).replace("{{ Content }}", string_html)

    with open(dest_path, 'w', encoding="utf-8") as f:
        f.write(template)

        