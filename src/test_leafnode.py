import unittest
from leafnode import LeafNode, HTMLNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        leaf_node = LeafNode("This is a leaf node", "h1")
        parent_node = HTMLNode(None, "p", None, leaf_node)
        html_leaf = "<h1>This is a leaf node</h1>"
        self.assertEqual(leaf_node.to_html(), html_leaf)



if __name__ == "__main__":
    unittest.main()