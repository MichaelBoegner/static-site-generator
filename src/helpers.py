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
    image_check = re.findall(r"!\[\w+\]", text)
    print("THIS IS TEXT AFTER IMAGE CHECK: ", text)
    image_text_list = []
    for image_text in image_check:
        new_text = image_text.replace('!','')
        new_text = new_text.replace('[','')
        new_text = new_text.replace(']','')
        image_text_list.append(new_text)
    print("THIS IS IMAGE TEXT: ", image_text_list)
    if len(image_text_list) > 0:
        print("THIS IS TEXT BEFORE IMAGE_URL: ", text)
        image_url = re.findall(r"(http|ftp|https)\:\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])", text)
        listed_image_url = []
        for url in image_url:
            listed_image_url.append(list(url))
        for url in listed_image_url:
            url.insert(1, "://")
        print("THIS IS IMAGE URL: ", listed_image_url)
        
        new_image_url = []
        for url in listed_image_url:
            string = ''.join(url)
            new_image_url.append(string)
        print("THIS IS NEW IMAGE URL: ", new_image_url)
        for i in range(len(image_url)):
            markeddown_images.append((image_text_list[i], new_image_url[i]))
        print("THIS IS MARKDOWNIMAGES: ", markeddown_images)
    return markeddown_images