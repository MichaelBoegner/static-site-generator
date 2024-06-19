import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def is_equal_leaf(self):
        node = LeafNode("This is a leaf node", "p")
        node1 = LeafNode("This is a leaf node", "p")
        self.assertEqual(node, node1)


if __name__ == "__main__":
    unittest.main()