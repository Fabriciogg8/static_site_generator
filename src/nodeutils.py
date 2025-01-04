import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for i in old_nodes:
        if delimiter in i.text:
            text = i.text.split(delimiter)
       
            node_list.append(TextNode(text[0], i.text_type))
            node_list.append(TextNode(text[1], text_type))
            node_list.append(TextNode(text[2], i.text_type))
        else:
            node_list.append(TextNode(i.text, i.text_type))
    return node_list


def extract_markdown_images(text):
    images = re.findall(r"\!\[(.*?)\]\((.*?)\)",text) 
    return images

def extract_markdown_links(text):
    links = re.findall(r"\[(.*?)\]\((.*?)\)",text) 
    return links


def split_nodes_link(old_nodes):
    result_nodes = []
    for node in old_nodes:
        current_text = node.text
        current_text_type = node.text_type
        current_url = node.url
        # Obtener todos los enlaces
        links = extract_markdown_links(current_text)
        for link_text, link_url in links:
            # Dividir usando el markdown completo del enlace
            markdown_link = f"[{link_text}]({link_url})"
            parts = current_text.split(markdown_link, 1)
            # Agregar el texto antes del enlace
            if parts[0]:
                result_nodes.append(TextNode(parts[0], TextType.NORMAL))
            # Agregar el enlace
            result_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            # Actualizar el texto restante
            current_text = parts[1] if len(parts) > 1 else ""
        
        # No olvides el texto restante después del último enlace
        if current_text:
            result_nodes.append(TextNode(current_text, current_text_type, current_url))
            
    return result_nodes

def split_nodes_image(old_nodes):
    result_nodes = []
    for node in old_nodes:
        current_text = node.text
        current_text_type = node.text_type
        current_url = node.url
        # Obtener todos los enlaces
        images = extract_markdown_images(current_text)
        for images_text, images_url in images:
            # Dividir usando el markdown completo del enlace
            markdown_link = f"![{images_text}]({images_url})"
            parts = current_text.split(markdown_link, 1)
            # Agregar el texto antes del enlace
            if parts[0]:
                result_nodes.append(TextNode(parts[0], current_text_type, current_url))
            # Agregar el enlace
            result_nodes.append(TextNode(images_text, TextType.IMAGE, images_url))
            # Actualizar el texto restante
            current_text = parts[1] if len(parts) > 1 else ""
        
        # No olvides el texto restante después del último enlace
        if current_text:
            result_nodes.append(TextNode(current_text, current_text_type, current_url))
            
    return result_nodes



def text_to_textnodes(text):
    node = TextNode(text=text,text_type=TextType.NORMAL)
    bold = split_nodes_delimiter([node], "**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "*", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    image = split_nodes_image(code)
    link = split_nodes_link(image)
    return link



