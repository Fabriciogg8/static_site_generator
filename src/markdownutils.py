from htmlnode import HTMLNode, ParentNode, LeafNode
from nodeutils import text_to_textnodes

def markdown_to_blocks(markdown):
    new_markdown = markdown.split("\n\n")
    new_markdown_striped = []
    for i in new_markdown:
        value = i.strip()
        if value != "":
            new_markdown_striped.append(value)
    return new_markdown_striped


def block_to_block_type(markdown):
    if markdown.startswith("#"):
        value = markdown.split(" ")[0]
        heading_value = len(value)
        return f"heading{heading_value}"
    elif markdown.startswith("```") and markdown.endswith("```"):
        return "code"
    elif markdown.startswith(">"):
        return "quote"
    elif markdown.startswith("* ") or markdown.startswith("- "):
        return "unordered list"
    elif markdown.startswith("1. "):
        new_list_markdown = markdown.split("\n\n")
        for i in range(len(new_list_markdown)):
            if new_list_markdown[i].startswith(f"{i+1}. "):
                return "ordered list"
    # elif markdown.startswith("*") or markdown.startswith("**") or markdown.startswith("[") or markdown.startswith("!["):
    else:
        list_of_nodes = []
        print(markdown)
        inline_block = text_to_textnodes(markdown) # Returns a list of TextNodes
        for i in inline_block:
            value = i.text_node_to_html_node()
            list_of_nodes.append(value)
        return list_of_nodes
    # else:
    #     return "normal"
    

def create_tag(text):
    if text == "heading1":
        return "h1"
    elif text == "heading2":
        return "h2"
    elif text == "heading3":
        return "h3"
    elif text == "heading4":
        return "h4"
    elif text == "heading5":
        return "h5"
    elif text == "heading6":
        return "h6"
  
    elif text == "code":
        return 'pre'
    elif text == "quote":
        return 'blockquote'
    elif text == "unordered list":
        return 'ul'
    elif text == "ordered list":
        return 'ol'
    elif type(text) == list:
        return "leaf"
    else:
        return 'p'

def get_text_from_markdown(text, block_type):
    # if block_type == "heading1" or block_type == "heading2" or block_type == "heading3" or block_type == "heading4" or block_type == "heading5" or block_type == "heading6":
    #     text
    #     return text.replace("#","").strip()
  
    if block_type == "code":
        text_value = text.replace('```',"").strip()
        return LeafNode(value=text_value, tag="code").to_html()

    elif block_type == "quote":
        return text.replace('>',"").strip()
    
    elif block_type == "unordered list":
        text_list = []
        new_list_markdown = text.split("\n")
        for node in range(len(new_list_markdown)):
            text_only = new_list_markdown[node][2:]
            inline_block = text_to_textnodes(text_only) # Returns a list of TextNodes
            children_list = []
            for i in inline_block:
                children_list.append(i.text_node_to_html_node())
            node = ParentNode(tag="li", children=children_list)
            text_list.append(node.to_html())
        html_string = ''.join([str(node) for node in text_list])
        return html_string
        
    elif block_type == "ordered list":
        text_list = []
        new_list_markdown = text.split("\n")
        for i in range(len(new_list_markdown)):
            text_only = new_list_markdown[i].replace(f"{i+1}. ","")
            inline_block = text_to_textnodes(text_only) # Returns a list of TextNodes
            children_list = []
            for i in inline_block:
              
                children_list.append(i.text_node_to_html_node())
            node = ParentNode(tag="li", children=children_list)
            text_list.append(node.to_html())
        html_string = ''.join([str(node) for node in text_list])
        return html_string
    else:
        return text

def markdown_to_html_node(markdown):
    """
        Full markdown to a single parent HTMLNode.
        That one parent HTMLNode should of course contain many child
        HTMLNode objects representing the nested elements
    """
    blocks = markdown_to_blocks(markdown) 
    list_children_nodes = []
    values = 1
    for block in blocks:
        block_type = block_to_block_type(block)
        tag_type = create_tag(block_type)
        if tag_type == "leaf":
            for node in block_type:
                list_children_nodes.append(node)
        elif "h" in tag_type:
            block = block.replace("#","").strip()
            child_nodes = text_to_textnodes(block)
            children_list = []
            for i in child_nodes:
                children_list.append(i.text_node_to_html_node())
            node = ParentNode(tag=tag_type, children=children_list)
            list_children_nodes.append(node)
        else:
            text_value = get_text_from_markdown(block,block_type)
            node = LeafNode(tag=tag_type,value=text_value)
            list_children_nodes.append(node)
    html_node = ParentNode(tag="div", children=list_children_nodes) 
    return html_node 
   

def extract_title(markdown):
    if markdown.startswith("# "):
        markdown = markdown.split("\n")
        markdown = markdown[0].replace("# ","")
        return markdown
    else:
        raise Exception("This text isn´t a H1")