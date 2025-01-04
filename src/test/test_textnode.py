import unittest
from textnode import TextNode, TextType
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq_URL(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_not_eq_URL(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.otherurl.com")  # URL different
        self.assertNotEqual(node, node2)
    
    def test_not_eq_TextType(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.NORMAL, "https://www.otherurl.com")  # TextType different
        self.assertNotEqual(node, node2)

    def test_text_type_normal(self):
        node = TextNode("Normal text", TextType.NORMAL)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.to_html(), "Normal text")

    def test_text_type_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")

    def test_text_type_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")

    def test_text_type_code(self):
        node = TextNode("Code text", TextType.CODE)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.to_html(), "<code>Code text</code>")

    def test_text_type_link(self):
        node = TextNode("Link text", TextType.LINK, "https://www.example.com")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.to_html(), '<a href="https://www.example.com" target="_blank">Link text</a>')

    def test_text_type_image(self):
        node = TextNode("Image alt text", TextType.IMAGE, "https://www.example.com/image.jpg")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.to_html(), '<img src="https://www.example.com/image.jpg" alt="Image alt text"></img>')

    def test_unknown_text_type(self): 
        node = TextNode("Unknown text", TextType.NORMAL) # Inicializa con un tipo conocido 
        node.text_type = "unknown" # Cambia el tipo directamente 
        with self.assertRaises(ValueError) as context: 
            node.text_node_to_html_node() 
        self.assertEqual(str(context.exception), "Not a valid type of TextType")
    
    


