import unittest
from helpers import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_text_nodes,
    markdown_to_blocks
)
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
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        expected = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        actual = extract_markdown_images(text)
        self.assertEqual(expected, actual)

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
        
    def test_split_nodes_image_three_sections(self):
        nodes = [TextNode("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png), and this is also text with a ![third image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",text_type_text)]
        expected = [
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode("second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"),
            TextNode(", and this is also text with a ", text_type_text),
            TextNode("third image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
        ]
        actual = split_nodes_image(nodes)
        self.assertEqual(expected, actual)
        
    def test_split_nodes_links(self):
        nodes = [TextNode("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)", text_type_text)]
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link, "https://www.example.com"),
            TextNode(" and ", text_type_text),
            TextNode("another", text_type_link, "https://www.example.com/another")
        ]
        actual = split_nodes_link(nodes)
        self.assertEqual(expected, actual)

    def test_text_to_text_nodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]
        actual = text_to_text_nodes(text)
        self.assertEqual(expected, actual)

    def test_text_to_text_nodes_blank(self):
        text = ""
        expected = []
        actual = text_to_text_nodes(text)
        self.assertEqual(expected, actual)

    def test_text_to_text_nodes_type_str(self):
        text = []
        with self.assertRaises(ValueError):
            text_to_text_nodes(text)
    
    def test_markdown_to_blocks(self):
        markdown = "This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items"
        expected = ["This is **bolded** paragraph", "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line", "* This is a list\n* with items"]
        actual = markdown_to_blocks(markdown)
        self.maxDiff = None
        self.assertEqual(expected, actual)
    
    def test_markdown_to_blocks_type(self):
        markdown = []
        with self.assertRaises(ValueError):
            markdown_to_blocks(markdown)

    def test_markdown_to_blocks_blank(self):
        markdown = ""
        with self.assertRaises(ValueError):
            markdown_to_blocks(markdown)