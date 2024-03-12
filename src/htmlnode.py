class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html hasn't been implemented by this class.")

    def props_to_html(self):
        html_string = f''
        for key in self.props:
            html_string += f' {key}="{self.props[key]}"'
        return html_string

    def __repr__(self):
        return (f"HTMLNode: "
                f"\n\ttag: {self.tag}"
                f"\n\tvalue: {self.value}"
                f"\n\tchildren: {self.children}"
                f"\n\tprops: {self.props}")

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("Value not set, but is required for leaf nodes.")
        if not self.tag:
            return self.value
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"