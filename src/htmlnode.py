class HTMLNode:
    def __init__(self, value=None, tag=None, props=None, children=None):
        self.tag=tag
        self.value=value
        self.props=props
        self.children = children
    def to_html(self):
        return f"<{self.tag}>{self.value}</{self.tag}>"
    def props_to_html(self):
        props_converted = ""
        for key in self.props.keys():
            props_converted = props_converted + f' {key}="{self.props[key]}"'
        return props_converted
    def __repr__(self):
        return f"{self.value}, {self.tag}, {self.props}, {self.children}"
