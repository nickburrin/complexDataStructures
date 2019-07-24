from hashmap import HashMap
from treeNode import TreeNode

# hashMap = HashMap(20)
# hashMap.assign('gabbro', 'igneous')
# hashMap.assign('sandstone', 'sedimentary')
# hashMap.assign('gneiss', 'metamorphic')

# print(hashMap.retrieve('gabbro'))
# print(hashMap.retrieve('sandstone'))
# print(hashMap.retrieve('gneiss'))

root = TreeNode("CEO")
first_child = TreeNode("Vice-President")
second_child = TreeNode("Head of Marketing")
third_child = TreeNode("Marketing Assistant")

root.add_child(first_child)
root.add_child(second_child)
second_child.add_child(third_child)

root.traverse()