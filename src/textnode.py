from leafnode import LeafNode
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, second_node):
        return self.__dict__ == second_node.__dict__
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    def text_node_to_html_node(self):
        if self.text_type == "text":
            return LeafNode(self.text, None, None)
        if self.text_type == "bold":
            return LeafNode(self.text, "b", None)
        if self.text_type == "italic":
            return LeafNode(self.text, "i", None)
        if self.text_type == "code":
            return LeafNode(self.text, "code", None)
        if self.text_type == "link":
            return LeafNode(self.text, "a", None)
        if self.text_type == "image":
            props = {
                "src": f"{self.url}",
                "alt": f"{self.text}"
            }
            return LeafNode(None, "img", props)
        raise ValueError("self.text_type must be one of the following values: 'text',\
                         'bold', 'italic', 'code', 'link', 'image'")
    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        for old_node in old_nodes:
            old_node = old_node.split(f"{delimiter}")
            for i in range(0, len(old_node)):
                print("this is old node", old_node)

    