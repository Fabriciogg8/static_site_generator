import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a paragraph", ["a","h1"], {
            "href": "https://www.google.com", 
            "target": "_blank",
            })
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')