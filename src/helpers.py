from textnode import TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    new_node = []      
    for old_node in old_nodes:
        delimiter_indices = []
        for i in range(len(old_node.text)):
            if delimiter == "**":
                if old_node.text[i] == "*" and old_node.text[i+1] == "*":
                    delimiter_indices.append(i + 1)
            elif old_node.text[i] == delimiter:
                delimiter_indices.append(i)
        if len(delimiter_indices) % 2 > 0:
            raise ValueError("Delimiter missing open or closing character.")
        for i in range(len(delimiter_indices)):
            if i == 0:
                new_node.append(old_node.text[:delimiter_indices[i]])
            elif i == len(delimiter_indices)-1:
                new_node.append(old_node.text[delimiter_indices[i-1]:delimiter_indices[i]])
                new_node.append(old_node.text[delimiter_indices[i]:])
            else:
                new_node.append(old_node.text[delimiter_indices[i-1]:delimiter_indices[i]])
            print("THIS IS NEW NODES ====", new_node)
        new_nodes.append(new_node)
    