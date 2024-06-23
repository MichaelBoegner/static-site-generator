import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text", None),
                LeafNode("italic text","i"),
                LeafNode("Normal text", None),
            ],
            "p",
            {"class": "brown"}
        )
        expected = '<p class="brown"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        actual = node.to_html()
        self.assertEqual(expected, actual)
    def test_to_html_with_branch_no_props(self):
        node = ParentNode(
            [
                LeafNode("Bold text", "b"),
                ParentNode(
                    [
                        LeafNode("italic text","i"),
                        LeafNode("Normal text", None),
                    ],
                    "div"
                ),
                LeafNode("italic text","i"),
                LeafNode("Normal text", None),
            ],
            "p",
            {"class": "brown"}
        )
        expected = '<p class="brown"><b>Bold text</b><div><i>italic text</i>Normal text</div><i>italic text</i>Normal text</p>'
        actual = node.to_html()
        self.assertEqual(expected, actual)
    def test_to_html_with_branch_no_props(self):
        node = ParentNode(
            [
                LeafNode("Bold text", "b"),
                ParentNode(
                    [
                        LeafNode("italic text","i"),
                        LeafNode("Normal text", None),
                    ],
                    "div",
                    {"target": "button"}
                ),
                LeafNode("italic text","i"),
                LeafNode("Normal text", None),
            ],
            "p",
            {"class": "brown"}
        )
        expected = '<p class="brown"><b>Bold text</b><div target="button"><i>italic text</i>Normal text</div><i>italic text</i>Normal text</p>'
        actual = node.to_html()
        self.assertEqual(expected, actual)
        
if __name__ == "__main__":
    unittest.main()