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

    def traverse(self):
        print('traversing...')
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current = nodes_to_visit.pop()
            print(current.value)
            nodes_to_visit.extend(current.children)
