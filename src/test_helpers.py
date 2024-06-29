import unittest
from helpers import split_nodes_delimiter, extract_markdown_images
from textnode import TextNode

class TestParser(unittest.TestCase):
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
        self.assertEqual(expected, actual)
    
class TestMarkdownImagesParser(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        expected = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        actual = extract_markdown_images(text)
        self.assertEqual(expected, actual)
