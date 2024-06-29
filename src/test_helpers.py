import unittest
from helpers import split_nodes_delimiter
from textnode import TextNode

class Testhelpers(unittest.TestCase):
    def test_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", "text")
        actual = split_nodes_delimiter([node], "`", "code")  
        expected = [
            TextNode("This is text with a ", "text"),
            TextNode("code block", "code"),
            TextNode(" word", "text")
        ]
        self.assertEqual(expected, actual)

    def test_code_delimiter_start(self):
        node = TextNode("`Code block` in the beginning of the sentence.", "text")
        actual = split_nodes_delimiter([node], "`", "code")  
        expected = [
            TextNode("Code block", "code"),
            TextNode(" in the beginning of the sentence.", "text")
        ]
        self.assertEqual(expected, actual)
    
    def test_bold_delimiter(self):
        node = TextNode("This is text with a **bolded** word", "text")
        actual = split_nodes_delimiter([node], "**", "bold")  
        expected = [
            TextNode("This is text with a ", "text"),
            TextNode("bolded", "bold"),
            TextNode(" word", "text")
        ]
        print("THIS IS ACTUAL = ", actual)
        self.assertEqual(expected, actual)
    