class MinHeap:
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            return self.left_child_idx(idx)
        
        left_child = self.heap_list[self.left_child_idx(idx)]
        right_child = self.heap_list[self.right_child_idx(idx)]
        if(left_child < right_child):
            return self.left_child_idx(idx)
        else:
            return self.right_child_idx(idx)
    
    def add(self, element):
        print("Adding ", element," to ", self.heap_list)
        self.heap_list.append(element)
        self.count += 1
        self.heapify_up()
    
    def heapify_up(self):
        idx = self.count
        
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]
            if parent > child:
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child
            
            idx = self.parent_idx(idx)
        print('Heap Restored ',self.heap_list)

    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            smaller_child_idx = self.get_smaller_child_idx(idx)
            parent = self.heap_list[idx]
            child = self.heap_list[smaller_child_idx]
            if parent > child:
                self.heap_list[idx] = child
                self.heap_list[smaller_child_idx] = parent
            idx = smaller_child_idx
        print('Heap Restored!', self.heap_list)

    def retrieve_min(self):
        if self.count == 0:
            print('No items in heap')
            return None
        
        min = self.heap_list[1]
        print('Removing: ',min,' from ',self.heap_list)
        
        self.heap_list[1] = self.heap_list[self.count]
        self.heap_list.pop()
        self.count -= 1
        
        self.heapify_down()
        return min
