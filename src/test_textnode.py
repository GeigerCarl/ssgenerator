import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2, f"{node} does NOT equal {node2}!")
        self.assertEqual(node.url, None, f'{node} URL is not None!')

        node = TextNode("This is a text node", "italics", 'https://www.fakesite.net')
        node2 = TextNode("This is a text node", "italics", 'https://www.fakesite.net')
        self.assertEqual(node, node2, f"{node} does NOT equal {node2}!")

        node = TextNode("This is a text node", "bold", 'https://www.fakesite.net')
        self.assertEqual(node.url, "https://www.fakesite.net", f"{node} URL is not expected!")

    def test_noteq(self):
        node = TextNode("This is a text node", "bold", 'https://www.fakesite.net')
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2, f"{node} DOES equal {node2}!")

        node = TextNode("This is a text node", "bold", 'https://www.fakesite.net')
        node2 = TextNode("This is another text node", "bold", 'https://www.fakesite.net')
        self.assertNotEqual(node, node2, f"{node} DOES equal {node2}!")

        node = TextNode("This is a text node", "italics", 'https://www.fakesite.net')
        node2 = TextNode("This is a text node", "bold", 'https://www.fakesite.net')
        self.assertNotEqual(node, node2, f"{node} DOES equal {node2}!")

    def test_repr(self):
        node = TextNode("This is a text node", "bold", 'https://www.fakesite.net')
        self.assertEqual(f"{node}", "TextNode(This is a text node, bold, https://www.fakesite.net)",
                         f"Print output for {node} is not expected!")

if __name__ == "__main__":
    unittest.main()