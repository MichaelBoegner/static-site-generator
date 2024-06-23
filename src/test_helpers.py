import unittest
from helpers import split_nodes_delimiter
from textnode import TextNode

class TestParentNode(unittest.TestCase):
    def test_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", "text")
        actual = split_nodes_delimiter([node], "`", "code")  
        expected = [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text")
        ]
        self.assertEqual(expected, actual)
    
    def test_bold_delimiter(self):
        node = TextNode("This is text with a **bolded** word", "text")
        actual = split_nodes_delimiter([node], "**", "code")  
        expected = [
            TextNode("This is text with a ", "text"),
            TextNode("bolded", "bold"),
            TextNode(" word", "text")
        ]
        print("THIS IS ACTUAL = ", actual)
        self.assertEqual(expected, actual)
    