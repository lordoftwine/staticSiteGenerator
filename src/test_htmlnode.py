import unittest

from htmlnode import HTMLNode, LeafNode

class testHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode("p", "Hello, world!", None, {})
        assert node.props_to_html() == ""
        
    def test_props_to_html_single_prop(self):
        node = HTMLNode("a", "Click me", None, {"href": "https://example.com"})
        assert node.props_to_html() == ' href="https://example.com"'

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')