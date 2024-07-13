from textnode import TextNode
from leafnode import LeafNode
from parentnode import ParentNode
from helpers import split_nodes_delimiter
from copier import directory_copier

def main():
    source_directory = "../static"
    dest_directory = "../public"

    directory_copier(source_directory, dest_directory)


if __name__ == "__main__":
    main()