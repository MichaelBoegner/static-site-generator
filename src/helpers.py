from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    for old_node in old_nodes:
        old_node = old_node.text.split(f"{delimiter}")
        new_nodes = []
        for node in old_node:
            if text_type in node:
                new_nodes.append(TextNode(node, text_type))
            else:
                new_nodes.append(TextNode(node, "text"))
        return new_nodes