class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        props_converted = ""
        for key in self.props.keys():
            props_converted = props_converted + f' {key}="{self.props[key]}"'
        return props_converted
    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children}, {self.props}"