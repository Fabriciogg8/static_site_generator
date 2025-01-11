import unittest
from markdownutils import markdown_to_blocks, block_to_block_type, markdown_to_html_node, extract_title
from textnode import TextNode, TextType 

class TestMarkdownUtils(unittest.TestCase):
    def test_markdown_to_blocks_basic(self):
        markdown = (
            "# This is a heading\n\n"
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n"
            "* This is the first list item in a list block\n"
            "* This is a list item\n"
            "* This is another list item"
        )
        result = markdown_to_blocks(markdown)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertEqual(result, expected)

    def test_markdown_to_blocks_empty(self):
        markdown = ""
        result = markdown_to_blocks(markdown)
        expected = []
        self.assertEqual(result, expected)

    def test_markdown_to_blocks_multiple_newlines(self):
        markdown = (
            "# Heading\n\n\n\n"
            "Paragraph with multiple newlines\n\n\n\n"
            "Another paragraph"
        )
        result = markdown_to_blocks(markdown)
        expected = [
            "# Heading",
            "Paragraph with multiple newlines",
            "Another paragraph"
        ]
        self.assertEqual(result, expected)

    def test_markdown_to_blocks_whitespace(self):
        markdown = "  \n\n  # Heading with leading and trailing whitespace  \n\n  Paragraph with whitespace  \n\n  "
        result = markdown_to_blocks(markdown)
        expected = [
            "# Heading with leading and trailing whitespace",
            "Paragraph with whitespace"
        ]
        self.assertEqual(result, expected)



    def test_block_to_block_type_heading(self):
        self.assertEqual(block_to_block_type("# This is a heading"), "heading1")
        self.assertEqual(block_to_block_type("## This is a subheading"), "heading2")
        self.assertEqual(block_to_block_type("### This is a subheading"), "heading3")
        self.assertEqual(block_to_block_type("#### This is a subheading"), "heading4")
        self.assertEqual(block_to_block_type("##### This is a subheading"), "heading5")
        self.assertEqual(block_to_block_type("###### This is a subheading"), "heading6")
    
    def test_block_to_block_type_code(self):
        code_block = "```\nprint('Hello, World!')\n```"
        self.assertEqual(block_to_block_type(code_block), "code")
    
    def test_block_to_block_type_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote"), "quote")
    
    def test_block_to_block_type_unordered_list(self):
        self.assertEqual(block_to_block_type("* This is a list item"), "unordered list")
        self.assertEqual(block_to_block_type("- This is another list item"), "unordered list")

    def test_block_to_block_type_ordered_list(self):
        ordered_list = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(ordered_list), "ordered list")
    
    def test_block_to_block_type_normal_paragraph(self):
        self.assertEqual(block_to_block_type("This is a normal paragraph of text."), "normal")

   

    def test_heading(self):
        markdown = '# Heading 1'
        node = markdown_to_html_node(markdown)
        self.assertEqual(str(node.to_html()), '<div><h1>Heading 1</h1></div>')

    def test_paragraph(self):
        markdown = 'This is a paragraph.'
        node = markdown_to_html_node(markdown)
        self.assertEqual(str(node.to_html()), '<div><p>This is a paragraph.</p></div>')

    def test_unordered_list(self):
        markdown = '- Item 1\n- Item 2'
        node = markdown_to_html_node(markdown)
        self.assertEqual(str(node.to_html()), '<div><ul><li>Item 1</li><li>Item 2</li></ul></div>')

    def test_ordered_list(self):
        markdown = '1. Item 1\n2. Item 2'
        node = markdown_to_html_node(markdown)
        self.assertEqual(str(node.to_html()), '<div><ol><li>Item 1</li><li>Item 2</li></ol></div>')

    def test_code_block(self):
        markdown = '```\ncode block\n```'
        node = markdown_to_html_node(markdown)
        self.assertEqual(str(node.to_html()), '<div><pre><code>code block</code></pre></div>')
    
    def test_subheading(self):
        markdown = '## Subheading 2'
        node = markdown_to_html_node(markdown)
        self.assertEqual(str(node.to_html()), '<div><h2>Subheading 2</h2></div>')

    def test_bold_text(self):
        markdown = '**This is bold**'
        node = markdown_to_html_node(markdown)
        self.assertEqual(str(node.to_html()), '<div><b>This is bold</b></div>')

    def test_italic_text(self):
        markdown = '*This is italic*'
        node = markdown_to_html_node(markdown)
        self.assertEqual(str(node.to_html()), '<div><i>This is italic</i></div>')
    
    def test_blockquote(self):
        markdown = '> This is a quote'
        node = markdown_to_html_node(markdown)
        self.assertEqual(str(node.to_html()), '<div><blockquote>This is a quote</blockquote></div>')

    def test_link(self):
        markdown = '[link text](https://example.com)'
        node = markdown_to_html_node(markdown)
        self.assertEqual(str(node.to_html()), '<div><a href="https://example.com" target="_blank">link text</a></div>')

    def test_nested_unordered_list(self):
        markdown = '- Item 1\n- Item 1.1\n- Item 2'
        node = markdown_to_html_node(markdown)
        self.assertEqual(str(node.to_html()), '<div><ul><li>Item 1</li><li>Item 1.1</li><li>Item 2</li></ul></div>')

    def test_bold_text_in_list(self):
        markdown = '* **Bold item 1**\n* Item 2'
        node = markdown_to_html_node(markdown)
        self.assertEqual(str(node.to_html()), '<div><ul><li><b>Bold item 1</b></li><li>Item 2</li></ul></div>')



    def test_extract_titles(self):
        markdown = "# This is a title"
        title_markdown = extract_title(markdown)
        self.assertEqual("This is a title",title_markdown)
    
    def test_extract_title_invalid(self): 
        with self.assertRaises(Exception) as context: 
            extract_title("Hello World") 
            self.assertTrue("This text isn’t a H1" in str(context.exception))