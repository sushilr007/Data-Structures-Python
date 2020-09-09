class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def language_tree():
    root = TreeNode("Programming Languages")

    python = TreeNode("Python")
    python.add_child(TreeNode("Guido van Rossum"))
    python.add_child(TreeNode("December 1989"))


    java = TreeNode("Java")
    java.add_child(TreeNode(" James Gosling"))
    java.add_child(TreeNode("1995"))

    javascript = TreeNode("Javascript")
    javascript.add_child(TreeNode("Brendan Eich"))
    javascript.add_child(TreeNode("December 4, 1995"))

    root.add_child(python)
    root.add_child(java)
    root.add_child(javascript)

    root.print_tree()

if __name__ == '__main__':
    language_tree()