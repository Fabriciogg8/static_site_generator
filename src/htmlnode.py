class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        text = ""
        for key, value in self.props.items():
            text += f' {key}="{value}"'
        return text

    def __repr__(self):
        # return f"HTMLNode({self.tag}, {self.value})"
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag=tag, value=value, props=props)
        

    def to_html(self):
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return f"{self.value}"
        else:
            if self.props != None:
                prop = self.props_to_html()
                return f"<{self.tag}{prop}>{self.value}</{self.tag}>"
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        # return f"HTMLNode({self.tag}, {self.value})"
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Missing tag")
        elif self.children == None:
            raise ValueError("Missing children")
        else:
            text = ""
            for i in self.children:
                text += i.to_html()
            if self.props != None:
                prop = self.props_to_html()
                return f"<{self.tag}{prop}>{text}</{self.tag}>"
            else:
                return f"<{self.tag}>{text}</{self.tag}>"
    
    def __repr__(self):
        # return f"HTMLNode({self.tag}, {self.value})"
        return f"ParentNode({self.tag}, {self.value}, {self.children},{self.props})"