from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "links"
    IMAGE = "images"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url
    
    def __eq__(self, nodo):
        if self.text == nodo.text and self.text_type == nodo.text_type and self.url == nodo.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def text_node_to_html_node(self):
        if self.text_type == TextType.NORMAL: 
            """ This should become a LeafNode with no tag, just a raw text value."""
            return LeafNode(value=self.text)
        if self.text_type == TextType.BOLD:
            """ This should become a LeafNode with a "b" tag and the text."""
            return LeafNode(tag="b",value=self.text)
        if self.text_type == TextType.ITALIC:
            """ i tag, text"""
            return LeafNode(tag="i",value=self.text)
        if self.text_type == TextType.CODE:   
            """ code tag, text"""
            return LeafNode(tag="code",value=self.text)
        if self.text_type == TextType.LINK:   
            """ a tag, anchor text, and "href" prop."""
            return LeafNode(tag="a",value=self.text, props={"href": self.url, "target": "_blank"})
        if self.text_type == TextType.IMAGE:   
            """ img tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)."""
            return LeafNode(tag="img", value="", props={"src": self.url, "alt": self.text})
        else:
            raise ValueError("Not a valid type of TextType")