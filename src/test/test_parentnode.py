import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_missing_tag(self):
        node = ParentNode(tag=None, children=[])
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "Missing tag")
        
    def test_missing_children(self):
        node = ParentNode(tag="div", children=None)
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception), "Missing children")

    def test_single_child(self):
        child = LeafNode(value="Single child", tag="p")
        node = ParentNode(tag="div", children=[child])
        self.assertEqual(node.to_html(), "<div><p>Single child</p></div>")

    def test_multiple_children(self):
        child1 = LeafNode(value="Child 1", tag="p")
        child2 = LeafNode(value="Child 2", tag="p")
        node = ParentNode(tag="div", children=[child1, child2])
        self.assertEqual(node.to_html(), "<div><p>Child 1</p><p>Child 2</p></div>")

    def test_nested_parent_nodes(self):
        inner_child = LeafNode(value="Inner child", tag="span")
        inner_parent = ParentNode(tag="section", children=[inner_child])
        outer_parent = ParentNode(tag="div", children=[inner_parent])
        self.assertEqual(outer_parent.to_html(), "<div><section><span>Inner child</span></section></div>")

    def test_with_props(self):
        child = LeafNode(value="Child with props", tag="p")
        node = ParentNode(tag="div", children=[child], props={"class": "container"})
        self.assertEqual(node.to_html(), '<div class="container"><p>Child with props</p></div>')

    def test_empty_children(self):
        node = ParentNode(tag="div", children=[])
        self.assertEqual(node.to_html(), "<div></div>")


