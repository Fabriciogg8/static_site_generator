from textnode import TextNode
from nodeutils import *
from markdownutils import *

def main():
    print(TextNode("This is a text node", "italic", "https://www.boot.dev"))
    
markdown="""#       Heading\n\n
"Paragraph with multiple newlines\n\n
### Another Heading"\n\n
> This is a quote.\n\n
1.  Bird
2.  McHale
3.  Parish  """

print(markdown_to_html_node(markdown))