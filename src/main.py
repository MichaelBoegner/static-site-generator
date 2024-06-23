from textnode import TextNode
from leafnode import LeafNode
from parentnode import ParentNode
from helpers import split_nodes_delimiter

def main():
    node = TextNode("This is text with a `code block` word", "text")
    new_nodes = split_nodes_delimiter([node], "`", "code")  
    print(new_nodes)


if __name__ == "__main__":
    main()