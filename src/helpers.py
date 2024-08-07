from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import (
    TextNode,
    text_type_text,
    text_type_image,
    text_type_link,
    text_type_bold,
    text_type_italic,
    text_type_code
)
import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):       
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(
                    image[0],
                    text_type_image,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes
        
def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(
                TextNode(
                    link[0],
                    text_type_link,
                    link[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))
    return new_nodes
        
def text_to_text_nodes(text):
    if not isinstance(text, (str)):
        raise ValueError("Paramater value not type string.")
    textnode = [TextNode(text, text_type_text)]
    new_nodes = split_nodes_image(textnode)
    new_nodes = split_nodes_link(new_nodes)
    new_nodes = split_nodes_delimiter(new_nodes, "**", text_type_bold)
    new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
    new_nodes = split_nodes_delimiter(new_nodes, "`", text_type_code)
    return new_nodes

def markdown_to_blocks(markdown):
    if not isinstance(markdown, (str)):
        raise ValueError("Paramater value not type string.")
    if len(markdown) == 0:
        raise ValueError("No text in markdown doc.")
    blocks = re.split(r'\n{2,}', markdown)
    filtered_blocks = [block for block in blocks if block.strip()]
    return filtered_blocks

def block_to_block_type(block):
    if list(block)[0] == "*" and list(block)[1] == " ":      
        if "\n" in block:
            newline_count = block.count("\n")
            asterix_count = block.count("* ")
            if newline_count != asterix_count - 1:
                raise ValueError("* needed for every new line in unordered list block")
        return block_type_unordered_list
    elif list(block)[0] == "-" and list(block)[1] == " ":
        if "\n" in block:
            newline_count = block.count("\n")
            hyphen_count = block.count("- ")
            if newline_count != hyphen_count - 1:
                raise ValueError("- needed for every new line in unordered list block")
        return block_type_unordered_list
    elif "# " in block or "## " in block or "### " in block or "#### " in block or "##### " in block or "###### " in block:
        return block_type_heading
    elif "```" in block:
        return block_type_code
    elif ">" in block:
        if "\n" in block:
            newline_count = block.count("\n")
            arrow_count = block.count(">")
            if newline_count != arrow_count-1:
                raise ValueError("> needed for every new line in quote block")
        return block_type_quote  
    elif "1. " in block:
        if "\n" in block:
            ordered_list_list = block.split("\n")
            for i in range(len(ordered_list_list)):
                if int(ordered_list_list[i][0]) != i + 1:
                    raise ValueError("Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.")
        return block_type_ordered_list
    else:
        return block_type_paragraph
    
def block_type_paragraph_to_html(block):
    if "\n" in block:
        block = block.replace("\n", "<br>")
    leaf_node = LeafNode(block, "p")
    return leaf_node.to_html()
    
def block_type_code_to_html(block):
    stripped_block = block.strip("```")
    leaf_node = [LeafNode(stripped_block, "code")]
    parent_node = ParentNode(leaf_node, "pre")
    return parent_node.to_html()

def block_type_quote_to_html(block):
    stripped_block = block.replace("> ", "")
    leaf_node = LeafNode(stripped_block, "blockquote")
    return leaf_node.to_html()

def block_type_heading_to_html(block):
    count = 0
    heading_type = ""
    for char in block:
        if char == "#":
            count += 1
            heading_type += "#"
        else: 
            break
    stripped_block = block.strip(f"{heading_type} ")
    leaf_node = LeafNode(stripped_block, f"h{count}")
    return leaf_node.to_html()

def block_type_unordered_list_to_html(block):
    if list(block)[0] == "*" and list(block)[1] == " ": 
        stripped_block = block.replace("* ","")
        stripped_block = stripped_block.split("\n")
    elif list(block)[0] == "-" and list(block)[1] == " ": 
        stripped_block = block.replace("- ","")
        stripped_block = stripped_block.split("\n")
    leaf_node = []
    for line in stripped_block:
        leaf_node.append(LeafNode(line, "li")) 
    parent_node = ParentNode(leaf_node, "ul")
    return parent_node.to_html()

def block_type_ordered_list_to_html(block):
    stripped_block = block.split("\n")
    leaf_node = []
    for line in stripped_block:
        line = "".join(list(line)[3:])
        leaf_node.append(LeafNode(line, "li")) 
    parent_node = ParentNode(leaf_node, "ol")
    return parent_node.to_html()

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_blocks = ""
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_paragraph:
            html_blocks += block_type_paragraph_to_html(block)
        elif block_type == block_type_code:
            html_blocks += block_type_code_to_html(block)
        elif block_type == block_type_quote:
            html_blocks += block_type_quote_to_html(block)
        elif block_type == block_type_heading:
            html_blocks += block_type_heading_to_html(block)
        elif block_type == block_type_unordered_list:
            html_blocks += block_type_unordered_list_to_html(block)
        elif block_type == block_type_ordered_list:
            html_blocks += block_type_ordered_list_to_html(block)
        
    return HTMLNode(html_blocks, "div").to_html()

def extract_title(markdown):
    if "# " in markdown:
        blocks = markdown_to_blocks(markdown)
        for block in blocks:
            if "# " in block:
                title = block.replace("# ", "")
                return title
    else:
        raise ValueError("Markdown doesn't contain h1")
    
def generate_page(from_path, template_path, dest_path):
    print("Generating page from `from_path` to `dest_path` using `template_path`.")
    
    with open(from_path, 'r') as file:
        md_content = file.read()
    
    with open(template_path, 'r') as file:
        template_content = file.read()
    
    html_string = markdown_to_html_node(md_content)
    html_text_nodes = text_to_text_nodes(html_string)
    new_html_string = ""
    for node in html_text_nodes:
        new_html_string += node.text_node_to_html_node().to_html()
    
    page_title = extract_title(md_content)
    
    template_content = template_content.replace("{{ Title }}", page_title)
    template_content = template_content.replace("{{ Content }}", new_html_string)
    
    with open(dest_path, 'w') as file:
        file.write(template_content)
    return

