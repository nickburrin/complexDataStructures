class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        print('Removing ' + child_node.value + ' from ' + self.value)
        self.children = [node for node in self.children if node != child_node]
