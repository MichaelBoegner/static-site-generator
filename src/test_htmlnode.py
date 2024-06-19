import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_stringify(self):
        props_dict = {"class":"main-paragraph"}
        node_p = HTMLNode("p", "This is the text inside of a new paragraph", None, props_dict)
        props = node_p.props_to_html()
        props_string = ' class="main-paragraph"'
        self.assertEqual(props, props_string)
    def test_child_node(self):
        node_h1 = HTMLNode("h1", "This is header text")
        node_p = HTMLNode("p", "This is the text inside of a new paragraph", node_h1)
        self.assertEqual(node_p.children, node_h1)
if __name__ == "__main__":
    unittest.main()