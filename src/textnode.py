class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text  # Text content of node
        self.text_type = text_type  # Type of text this node contains. Ex: 'bold'
        self.url = url  # URL of the link or image, defaults to None.

    def __eq__(self, other):
        return other.text == self.text and other.text_type == self.text_type and other.url == self.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"