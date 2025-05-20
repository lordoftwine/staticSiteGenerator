import unittest

from htmlnode import HTMLNode

class testHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode("p", "Hello, world!", None, {})
        assert node.props_to_html() == ""
        
    def test_props_to_html_single_prop(self):
        node = HTMLNode("a", "Click me", None, {"href": "https://example.com"})
        assert node.props_to_html() == ' href="https://example.com"'