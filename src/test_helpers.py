import unittest
from helpers import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_text_nodes,
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph_to_html,
    block_type_code_to_html,
    block_type_quote_to_html,
    block_type_heading_to_html,
    block_type_unordered_list_to_html,
    block_type_ordered_list_to_html,
    markdown_to_html_node,
    extract_title,
    generate_page,
    block_type_ordered_list,
    block_type_paragraph,
    block_type_code,
    block_type_heading,
    block_type_ordered_list,
    block_type_unordered_list,
    block_type_quote,
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
    
class TestMarkdownBlocks(unittest.TestCase):    
    def test_markdown_to_blocks(self):
        markdown = "This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items"
        expected = ["This is **bolded** paragraph", "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line", "* This is a list\n* with items"]
        actual = markdown_to_blocks(markdown)
        self.maxDiff = None
        self.assertEqual(expected, actual)
    
    def test_markdown_to_blocks_double_space(self):
        markdown = "This is **bolded** paragraph\n\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items"
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
    
    def test_block_to_block_type_unordered_list(self):
        block = "- This is a list\n- with items"
        expected = block_type_unordered_list
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

        block = "* This is a list\n* with items"
        expected = block_type_unordered_list
        actual = block_to_block_type(block)
        self.assertEqual(expected, actual)

    def test_block_to_block_type_heading(self):
        expected = block_type_heading
        actual = block_to_block_type("# This is a heading")
        self.assertEqual(expected, actual)

        actual = block_to_block_type("## This is a heading")
        self.assertEqual(expected, actual)

        actual = block_to_block_type("### This is a heading")
        self.assertEqual(expected, actual)

        actual = block_to_block_type("#### This is a heading")
        self.assertEqual(expected, actual)

        actual = block_to_block_type("##### This is a heading")
        self.assertEqual(expected, actual)

        actual = block_to_block_type("###### This is a heading")
        self.assertEqual(expected, actual)

        actual = block_to_block_type("######This is not a heading")
        self.assertNotEqual(expected, actual)

    def test_block_to_block_type_code(self):
        expected = block_type_code
        actual = block_to_block_type("```This is a code block```")
        self.assertEqual(expected, actual)

    def test_block_to_block_type_quote(self):
        expected = block_type_quote
        actual = block_to_block_type(">This is a quote block\n>New line in quote block")
        self.assertEqual(expected, actual)
    
    def test_block_to_block_type_ordered_list(self):
        expected = block_type_ordered_list
        actual = block_to_block_type("1. This is an ordered_list block\n2. New line in ordered_list block\n3. New line in ordered_list block")
        self.assertEqual(expected, actual)
    
    def test_block_to_block_type_paragraph(self):
        expected = block_type_paragraph
        actual = block_to_block_type("This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line")
        self.assertEqual(expected, actual)

    def test_block_type_paragraph_to_html(self):
        block = "This is **bolded** paragraph"
        expected =  "<p>This is **bolded** paragraph</p>"
        actual = block_type_paragraph_to_html(block)
        self.assertEqual(expected, actual)
    
    def test_block_type_paragraph_to_html_newline(self):
        block = "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line"
        expected =  "<p>This is another paragraph with *italic* text and `code` here<br>This is the same paragraph on a new line</p>"
        actual = block_type_paragraph_to_html(block)
        self.assertEqual(expected, actual)

    def test_block_type_code_to_html(self):
        block = "```This is a code block```"
        expected = "<pre><code>This is a code block</code></pre>"
        actual = block_type_code_to_html(block)
        self.assertEqual(expected, actual)
    
    def test_block_type_quote_to_html(self):
        block = "> This is a quote block\n> New line in quote block"
        expected = "<blockquote>This is a quote block\nNew line in quote block</blockquote>"
        actual = block_type_quote_to_html(block)
        self.assertEqual(expected, actual)

    def test_block_type_heading_to_html_h1(self):
        block = "# This is a heading"
        expected = "<h1>This is a heading</h1>"
        actual = block_type_heading_to_html(block)
        self.assertEqual(expected, actual)
    
    def test_block_type_heading_to_html_h2(self):
        block = "## This is a heading"
        expected = "<h2>This is a heading</h2>"
        actual = block_type_heading_to_html(block)
        self.assertEqual(expected, actual)

    def test_block_type_heading_to_html_h3(self):
        block = "### This is a heading"
        expected = "<h3>This is a heading</h3>"
        actual = block_type_heading_to_html(block)
        self.assertEqual(expected, actual)

    def test_block_type_heading_to_html_h4(self):
        block = "#### This is a heading"
        expected = "<h4>This is a heading</h4>"
        actual = block_type_heading_to_html(block)
        self.assertEqual(expected, actual)

    def test_block_type_heading_to_html_h5(self):
        block = "##### This is a heading"
        expected = "<h5>This is a heading</h5>"
        actual = block_type_heading_to_html(block)
        self.assertEqual(expected, actual)

    def test_block_type_heading_to_html_h6(self):
        block = "###### This is a heading"
        expected = "<h6>This is a heading</h6>"
        actual = block_type_heading_to_html(block)
        self.assertEqual(expected, actual)
    
    def test_block_type_unordered_list_to_html_hyphen(self):
        block = "- This is a list\n- with items"
        expected = "<ul><li>This is a list</li><li>with items</li></ul>"
        actual = block_type_unordered_list_to_html(block)
        self.assertEqual(expected, actual)

    def test_block_type_unordered_list_to_html_asterix(self):
        block = "* This is a list\n* with items"
        expected = "<ul><li>This is a list</li><li>with items</li></ul>"
        actual = block_type_unordered_list_to_html(block)
        self.assertEqual(expected, actual)

    def test_block_type_ordered_list_to_html(self):
        block = "1. This is an ordered list\n2. with items"
        expected = "<ol><li>This is an ordered list</li><li>with items</li></ol>"
        actual = block_type_ordered_list_to_html(block)
        self.assertEqual(expected, actual)

    def test_markdown_to_html_node(self):
        markdown = "This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items"
        expected = "<div><p>This is **bolded** paragraph</p><p>This is another paragraph with *italic* text and `code` here<br>This is the same paragraph on a new line</p><ul><li>This is a list</li><li>with items</li></ul></div>"
        actual = markdown_to_html_node(markdown)
        self.assertEqual(expected, actual)

    def test_extract_title(self):
        markdown = "# This is a title"
        expected = "This is a title"
        actual = extract_title(markdown)
        self.assertEqual(expected, actual)

    def test_extract_title_no_h1(self):
        markdown = "There is no h1 "
        self.assertRaises(ValueError, extract_title, markdown)

    def test_generate_page(self):
        from_path = "content/index.md"
        template_path = "template.html"
        dest_path = "public/index.html"
        generate_page(from_path, template_path, dest_path)