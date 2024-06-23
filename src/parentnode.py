from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        self.children = children
        self.tag=tag
        self.props=props
    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode has no tag")
        if self.children == None:
            raise ValueError("ParentNode object must have children")
        props_converted = self.props_to_html()
        html = ""
        for child in self.children:
            html = html + child.to_html()
        html = f"<{self.tag}{props_converted}>{html}</{self.tag}>"
        print("this is html", html)
        return html
        
    def __repr__(self):
        return f"ParentNode(tag: {self.tag}, props: {self.props}, children: {self.children})"