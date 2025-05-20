import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_different_text(self):
        node = TextNode("text 1", TextType.BOLD)
        node2 = TextNode("Text 2", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_different_texttypes(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_empty_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "http:\\www.nonsense.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()