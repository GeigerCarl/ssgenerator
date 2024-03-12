import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        new_htmlnode = HTMLNode(tag=None, value=None, children=None, props=None)
        # All values are None
        self.assertEqual(f"{new_htmlnode}", f"HTMLNode: "
                f"\n\ttag: {None}"
                f"\n\tvalue: {None}"
                f"\n\tchildren: {None}"
                f"\n\tprops: {None}", f"htmlnode {new_htmlnode} output is unexpected.")
        # Some values are None
        new_htmlnode = HTMLNode(tag='h1', value=None, children=[], props=None)
        self.assertEqual(f"{new_htmlnode}", f"HTMLNode: "
                f"\n\ttag: h1"
                f"\n\tvalue: {None}"
                f"\n\tchildren: {[]}"
                f"\n\tprops: {None}", f"htmlnode {new_htmlnode} output is unexpected.")
    
    def test_propstohtml(self):
        new_htmlnode = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(new_htmlnode.props_to_html(), ' href="https://www.google.com" target="_blank"')

class TestLeafNode(unittest.TestCase):
    def test_tohtml(self):
        # Confirm things break if you don't set value for LeafNodes
        got_exception = False
        try:
            bad_leafnode = LeafNode(None, None)
            bad_leafnode.to_html()
        except ValueError:
            got_exception = True
        self.assertTrue(got_exception, "Value was not set, but LeafNode's to_html function didn't fail.")

        # Now test that to_html does what we want.
        good_leafnode = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(good_leafnode.to_html(), f"<p>This is a paragraph of text.</p>")

        good_leafnode2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(good_leafnode2.to_html(), '<a href="https://www.google.com">Click me!</a>')

        text_leafnode = LeafNode(None, value="I'm by myself.")
        self.assertEqual(text_leafnode.to_html(), "I'm by myself.")

class TestParentNode(unittest.TestCase):
    def test_tohtml(self):
        # Confirm things break if you don't set tags or children for parent nodes
        got_exception = False
        try:
            bad_leafnode = ParentNode(None, [])
            bad_leafnode.to_html()
        except ValueError:
            got_exception = True
        self.assertTrue(got_exception, "Tag was not set, but ParentNode's to_html function didn't fail.")

        got_exception = False
        try:
            bad_leafnode = ParentNode("a", None)
            bad_leafnode.to_html()
        except ValueError:
            got_exception = True
        self.assertTrue(got_exception, "Children was not set, but ParentNode's to_html function didn't fail.")

        # Now test some nodes.

        parent_node1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(parent_node1.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

        parent_node2 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text", {"href": "https://www.google.com", "target": "_blank"}),
                ParentNode('p', [
                    LeafNode("i", "italic text")
                ]),
                LeafNode(None, "Normal text"),
                ParentNode(
                    'p',
                    [
                        LeafNode("b", "Bold text", {"href": "https://www.youtube.com"}),
                        LeafNode("i", "italic text")
                    ],
                    {"href": "https://www.wikipedia.com", "target": "_blank"}
                )
            ],
            {"href": "https://www.github.com/"}
        )
        expected_htmlstring = '<p href="https://www.github.com/"><b href="https://www.google.com" target="_blank">Bold text</b><p><i>italic text</i></p>Normal text<p href="https://www.wikipedia.com" target="_blank"><b href="https://www.youtube.com">Bold text</b><i>italic text</i></p></p>'
        self.assertEqual(parent_node2.to_html(), expected_htmlstring)