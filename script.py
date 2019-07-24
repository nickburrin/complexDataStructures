from hashmap import HashMap
from treeNode import TreeNode

# hashMap = HashMap(20)
# hashMap.assign('gabbro', 'igneous')
# hashMap.assign('sandstone', 'sedimentary')
# hashMap.assign('gneiss', 'metamorphic')

# print(hashMap.retrieve('gabbro'))
# print(hashMap.retrieve('sandstone'))
# print(hashMap.retrieve('gneiss'))

root = TreeNode("I am Root")
child = TreeNode("A wee sappling")
bad_seed = TreeNode("Root Rot!")

root.add_child(child)
root.add_child(bad_seed)

root.remove_child(bad_seed)