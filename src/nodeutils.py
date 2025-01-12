import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Divide los nodos de texto en partes utilizando un delimitador y alterna entre 
    el tipo de texto original y un nuevo tipo de texto para el delimitador.

    Args:
        old_nodes (list): Lista de nodos de texto originales a ser procesados.
        delimiter (str): El delimitador utilizado para dividir el texto.
        text_type (str): El tipo de texto que se aplicará a las partes delimitadas.

    Returns:
        list: Lista de nuevos nodos de texto con las partes divididas y los tipos de texto alternados.

    Ejemplo:
        Supongamos que tienes un nodo con el texto "Hello `code` World" y el delimitador es "`".
        La función dividirá este texto en tres partes: ['Hello ', 'code', ' World'] y alternará entre 
        el tipo de texto original y el tipo de texto especificado para el delimitador.

        Entrada:
            old_nodes = [TextNode("Hello `code` World", TextType.NORMAL)]
            delimiter = "`"
            text_type = TextType.CODE

        Salida:
            [TextNode("Hello ", TextType.NORMAL), TextNode("code", TextType.CODE), TextNode(" World", TextType.NORMAL)]
    """
    node_list = []
    for node in old_nodes:
        if delimiter in node.text:
            parts = node.text.split(delimiter)
            for i, part in enumerate(parts):
                # Alterna entre el tipo de texto original y el tipo de texto para el delimitador
                current_type = text_type if i % 2 != 0 else node.text_type
                node_list.append(TextNode(part, current_type))
        else:
            node_list.append(TextNode(node.text, node.text_type))
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



