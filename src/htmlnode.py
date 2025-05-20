class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        #tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        #value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        #children - A list of HTMLNode objects representing the children of this node
        #props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
        #
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result  = ""
        if self.props == None:
            return result
        for prop in self.props:
            result += f' {prop}="{self.props[prop]}"'
        return result
    
    def __repr__(self):
        return f"HTMLNode tag is {self.tag}, value is {self.value}, children are {self.children}, and props are {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        else:
            result = self.props_to_html()
            new_tag = f'<{self.tag}{result}>{self.value}</{self.tag}>'
            return new_tag
