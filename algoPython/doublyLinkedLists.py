class Node(object):
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next
    
    def get_next (self) :
        return self.next
    
    def set_next (self, next) :
        self.next = next

    def get_prev (self) :
        return self.prev
    
    def set_prev (self, prev) :
        self.prev = prev

    def get_data (self) :
        return self.data
    
    def set_data (self, data) :
        self.data = data 

class DoublyLinkedList (object) :

    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, data):
        new_node = Node(data)
        if self.root:
            self.root.set_prev(new_node)
        new_node.set_next(self.root)
        self.root = new_node

    def search(self, data):
        node_searched = self.root
        while (node_searched and node_searched.get_data() != data):
            node_searched = node_searched.get_next()
        if node_searched:
            return True
        else:
            return False 

    def remove(self, data):
        node_removed = self.root

        while node_removed:
            if node_removed.get_data() == data:
                prev = node_removed.get_prev()
                next = node_removed.get_next()
                if prev :
                    prev.set_next(next)
                
                else:
                    self.root = node_removed.get_next()

                if next:
                    next.set_prev(prev)
                return True
            
            else:
                node_removed = node_removed.get_next()
        return False            


myList = DoublyLinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.remove(8)
print(myList.remove(12))
print(myList.search(5))