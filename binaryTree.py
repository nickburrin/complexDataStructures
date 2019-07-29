class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

class TreeNode(Node):
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def addChild(self, node):
        if node.value < self.value:
            if self.leftChild:
                self.leftChild.addChild(node)
            else:
                self.leftChild = node
        elif node.value > self.value:
            if self.rightChild:
                self.rightChild.addChild(node)
            else:
                self.rightChild = node
        else:
            print("Can't add duplicates, value: ", node.value, " already exists in the tree.")

    def visit(self):
        print(self.value)

class BinaryTree():
    def __init__(self, node):
        self.rootNode = node
        self.count = 0
        self.height = 1 # Not doing anything with this variable yet
    
    def addNode(self, node):
        self.rootNode.addChild(node)

    def inOrderTraversal(self, node):
        if node is not None:
            self.inOrderTraversal(node.leftChild)
            node.visit()
            self.inOrderTraversal(node.rightChild)

    def preOrderTraversal(self, node):
        if node is not None:
            node.visit()
            self.preOrderTraversal(node.leftChild)
            self.preOrderTraversal(node.rightChild)

    def postOrderTraversal(self, node):
        if node is not None:
            self.postOrderTraversal(node.leftChild)
            self.postOrderTraversal(node.rightChild)
            node.visit()

node1 = TreeNode(10)
node2 = TreeNode(2)
node3 = TreeNode(100)
node4 = TreeNode(35)
node5 = TreeNode(10) # duplicate
node6 = TreeNode(1)
node7 = TreeNode(-5)

tree = BinaryTree(node1)
tree.addNode(node2)
tree.addNode(node3)
tree.addNode(node4)
tree.addNode(node5)
tree.addNode(node6)
tree.addNode(node7)

print("In order traversal:")
tree.inOrderTraversal(tree.rootNode)
print()
print("Pre-order traversal:")
tree.preOrderTraversal(tree.rootNode)
print()
print("Post-order traversal:")
tree.postOrderTraversal(tree.rootNode)
print()