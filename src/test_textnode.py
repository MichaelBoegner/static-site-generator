import unittest
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("This is a text node", "italics")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
    def test_not_eq_URL(self):
        node = TextNode("This is a text node", "italics", "https://cats.com")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
    def test_URL_is_None(self):
        node = TextNode("This is a text node", "italics")
        node2 = TextNode("This is a text node", "bold")
        self.assertIsNone(node.url)
        self.assertIsNone(node2.url)
    

    
if __name__ == "__main__":
    unittest.main()