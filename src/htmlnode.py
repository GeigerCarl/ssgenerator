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
        if self.props:
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
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("Value not set, but is required for leaf nodes.")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Tag not set, but is required for parent nodes.")
        if not self.children:
            raise ValueError("Children not set, but is required for parent nodes.")
        else:
            children_string = f""
            for child in self.children:
                children_string += child.to_html()
                
            return f"<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>"
