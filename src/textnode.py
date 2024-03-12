from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text  # Text content of node
        self.text_type = text_type  # Type of text this node contains. Ex: 'bold'
        self.url = url  # URL of the link or image, defaults to None.

    def __eq__(self, other):
        return other.text == self.text and other.text_type == self.text_type and other.url == self.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    supported_text_types = ["text", "bold", "italic", "code", "link", "image"]
    if text_node.text_type not in supported_text_types:
        raise ValueError(f"{text_node.text_type} is not a supported text type.")
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text)
    if text_node.text_type == "bold":
        return LeafNode('b', text_node.text)
    if text_node.text_type == "italic":
        return LeafNode('i', text_node.text)
    if text_node.text_type == "code":
        return LeafNode('code', text_node.text)
    if text_node.text_type == "link":
        return LeafNode('a', text_node.text, {"href": text_node.url})
    if text_node.text_type == "image":
        return LeafNode('img', '', {"src": text_node.url, "alt": text_node.text})
    return None