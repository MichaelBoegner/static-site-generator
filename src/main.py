from textnode import TextNode
from leafnode import LeafNode
from parentnode import ParentNode

def main():
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

    node.to_html()
    print(node)


if __name__ == "__main__":
    main()