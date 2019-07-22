from hashmap import HashMap

hashMap = HashMap(20)
hashMap.assign('gabbro', 'igneous')
hashMap.assign('sandstone', 'sedimentary')
hashMap.assign('gneiss', 'metamorphic')

print(hashMap.retrieve('gabbro'))
print(hashMap.retrieve('sandstone'))
print(hashMap.retrieve('gneiss'))