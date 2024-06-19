from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(value, tag, props, None)
        self.tag=tag
        self.value=value
        self.props=props
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        if self.props == None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        props_converted = self.props_to_html()
        return f'<{self.tag}{props_converted}>{self.value}</{self.tag}>'