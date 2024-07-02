from textnode import (
    TextNode,
    text_type_text,
)
import re

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
    markeddown_images = []
    image_check = re.findall(r"!\[([\w\s]+)\]", text)
    image_text_list = []
    for image_text in image_check:
        new_text = image_text.replace('!','').replace('[','').replace(']','')
        image_text_list.append(new_text)
    if len(image_text_list) > 0:
        image_url = re.findall(r"(http|ftp|https)\:\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])", text)
        listed_image_url = []
        for url in image_url:
            listed_image_url.append(list(url))
        for url in listed_image_url:
            url.insert(1, "://")        
        new_image_url = []
        for url in listed_image_url:
            string = ''.join(url)
            new_image_url.append(string)
        for i in range(0, len(image_url)):
            markeddown_images.append((image_text_list[i], new_image_url[i]))
    return markeddown_images

def extract_markdown_links(text):
    markeddown_links = []
    image_check = re.findall(r"\[\w+\]", text)
    image_text_list = []
    for image_text in image_check:
        new_text = image_text.replace('!','').replace('[','').replace(']','')
        image_text_list.append(new_text)
    if len(image_text_list) > 0:
        image_url = re.findall(r"(http|ftp|https)\:\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])", text)
        listed_image_url = []
        for url in image_url:
            listed_image_url.append(list(url))
        for url in listed_image_url:
            url.insert(1, "://")        
        new_image_url = []
        for url in listed_image_url:
            string = ''.join(url)
            new_image_url.append(string)
        for i in range(len(image_url)):
            markeddown_links.append((image_text_list[i], new_image_url[i]))
    return markeddown_links

def split_nodes_image(old_nodes):
    for old_node in old_nodes:
        markdown_images = extract_markdown_images(old_node.text)
    
    print("THIS IS MARKDOWN_IMAGES=   ", markdown_images)
    for markdown_image in markdown_images:
        print("THIS IS MARKDOWN_IMAGE=   ", markdown_image)