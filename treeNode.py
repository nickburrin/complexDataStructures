class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        print('Removing ' + child_node.value + ' from ' + self.value)
        new_children = []
        for node in self.children:
            if node.value != child_node.value:
                new_children.append(node)
        self.children = new_children
