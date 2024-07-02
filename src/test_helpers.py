import unittest
from helpers import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image
from textnode import (
TextNode,
text_type_text, 
text_type_bold,
text_type_italic, 
text_type_code,
text_type_link, 
text_type_image, 
)

class TestParser(unittest.TestCase):
    def test_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        actual = split_nodes_delimiter([node], "`", text_type_code)  
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text)
        ]
        self.assertEqual(expected, actual)

    def test_code_delimiter_start(self):
        node = TextNode("`Code block` in the beginning of the sentence.", text_type_text)
        actual = split_nodes_delimiter([node], "`", text_type_code)  
        expected = [
            TextNode("Code block", text_type_code),
            TextNode(" in the beginning of the sentence.", text_type_text)
        ]
        self.assertEqual(expected, actual)
    
    def test_bold_delimiter(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        actual = split_nodes_delimiter([node], "**", text_type_bold)  
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("bolded", text_type_bold),
            TextNode(" word", text_type_text)
        ]
        self.assertEqual(expected, actual)
    
class TestMarkdownParsers(unittest.TestCase):
    # def test_extract_markdown_images(self):
    #     text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
    #     expected = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
    #     actual = extract_markdown_images(text)
    #     self.assertEqual(expected, actual)

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expected = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        actual = extract_markdown_links(text)
        self.assertEqual(expected, actual)

    def test_split_nodes_image(self):
        nodes = [TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",text_type_text)]
        expected = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode("second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
        ]
        actual = split_nodes_image(nodes)
        self.assertEqual(expected, actual)
        

