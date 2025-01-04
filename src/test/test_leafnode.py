import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_value_none(self):
        node = LeafNode(value=None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_tag_none(self):
        node = LeafNode(value="Texto sin etiqueta")
        self.assertEqual(node.to_html(), "Texto sin etiqueta")

    def test_tag_with_value(self):
        node = LeafNode(value="Texto con etiqueta", tag="p")
        self.assertEqual(node.to_html(), "<p>Texto con etiqueta</p>")

    def test_tag_with_value_and_props(self):
        node = LeafNode(value="Texto con etiqueta y propiedades", tag="p", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<p href="https://www.google.com" target="_blank">Texto con etiqueta y propiedades</p>')


