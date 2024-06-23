from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    for old_node in old_nodes:
        first_delimiter = old_node.text.find(delimiter)
        second_delimiter = old_node.text.find(delimiter, first_delimiter+1)
        if second_delimiter == None:
            raise ValueError("Delimiter missing open or closing character.")
        new_nodes = []      
        if delimiter == "**":
            new_nodes.append(TextNode(old_node.text[:first_delimiter], "text"))
            new_nodes.append(TextNode(old_node.text[first_delimiter+2:second_delimiter], "bold"))
            new_nodes.append(TextNode(old_node.text[second_delimiter+2:], "text"))
        if delimiter == "`":
            new_nodes.append(TextNode(old_node.text[:first_delimiter], "text"))
            new_nodes.append(TextNode(old_node.text[first_delimiter+1:second_delimiter], "code"))
            new_nodes.append(TextNode(old_node.text[second_delimiter+1:], "text"))
        return new_nodes