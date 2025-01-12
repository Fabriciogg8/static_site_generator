# test/test_nodeutils.py
import unittest
from nodeutils import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType

class TestNodeUtils(unittest.TestCase):
    def test_split_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL)
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_bold_delimiter(self):
        node = TextNode("This is **bold** text", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.NORMAL)
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_italic_delimiter(self):
        node = TextNode("This is *italic* text", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.NORMAL)
        ]
        self.assertEqual(new_nodes, expected)

    def test_no_delimiter(self):
        node = TextNode("This is normal text without delimiters", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [node]
        self.assertEqual(new_nodes, expected)

    def test_multiple_nodes(self):
        nodes = [
            TextNode("First node with `code` block", TextType.NORMAL),
            TextNode("Second node with **bold** text", TextType.NORMAL)
        ]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        expected = [
            TextNode("First node with ", TextType.NORMAL),
            TextNode("code", TextType.CODE),
            TextNode(" block", TextType.NORMAL),
            TextNode("Second node with ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.NORMAL)
        ]
        self.assertEqual(new_nodes, expected)


    def test_split_nodes_link(self):
        node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.NORMAL
        )
        new_nodes = split_nodes_link([node])
    
        expected = [
        TextNode("This is text with a link ", TextType.NORMAL, None),
        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        TextNode(" and ", TextType.NORMAL, None),
        TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
        ]
    
        assert new_nodes == expected, f"Expected {expected}, but got {new_nodes}"


    def test_split_nodes_image(self):
        node = TextNode(
        "This is text with an image ![boot dev logo](https://www.boot.dev/logo.png) and another ![youtube logo](https://www.youtube.com/logo.png)",
        TextType.NORMAL
        )
        new_nodes = split_nodes_image([node])
    
        expected = [
        TextNode("This is text with an image ", TextType.NORMAL, None),
        TextNode("boot dev logo", TextType.IMAGE, "https://www.boot.dev/logo.png"),
        TextNode(" and another ", TextType.NORMAL, None),
        TextNode("youtube logo", TextType.IMAGE, "https://www.youtube.com/logo.png")
        ]
    
        assert new_nodes == expected, f"Expected {expected}, but got {new_nodes}"

    def test_text_to_textnodes(self): 
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)" 
        result = text_to_textnodes(text) 
        expected = [ TextNode("This is ", TextType.NORMAL), 
                    TextNode("text", TextType.BOLD), 
                    TextNode(" with an ", TextType.NORMAL), 
                    TextNode("italic", TextType.ITALIC), 
                    TextNode(" word and a ", TextType.NORMAL), 
                    TextNode("code block", TextType.CODE), 
                    TextNode(" and an ", TextType.NORMAL), 
                    TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), 
                    TextNode(" and a ", TextType.NORMAL), 
                    TextNode("link", TextType.LINK, "https://boot.dev") ] 
        self.assertEqual(result, expected)


   
    
