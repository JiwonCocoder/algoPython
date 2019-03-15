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

    def __init__(self, r = None, l = None):
        self.root = r
        self.size = 0
        self.last = l
    def get_size(self):
        return self.size

    def add(self, data):
        new_node = Node(data)
        if self.root:
            self.root.set_prev(new_node)
        new_node.set_next(self.root)
        self.root = new_node
        self.size +=1

    def search(self, number):
        node_searched = self.last 
        for i in range (1, number):
            node_searched= node_searched.get_next()
            if node_searched == None:
                node_searched = self.root

        self.last = node_searched.get_next()
        if self.last == None:
            self.last = self.root
        return node_searched.data
         
    def print_list(self):
        node_searched = self.root
        while node_searched:
            print(node_searched.get_data())
            node_searched = node_searched.next
        print

    def remove(self, data):
        node_removed = self.root

        while node_removed:
            if node_removed.get_data() == data:
                prev = node_removed.get_prev()
                next = node_removed.get_next()
                #self.last = node_removed.get_next()
                if prev :
                    prev.set_next(next)
                
                else:
                    self.root = node_removed.get_next()

                if next:
                    next.set_prev(prev)
                
                self.size -=1  
                return self.size
            
            else:
                node_removed = node_removed.get_next()
        return False
input1, input2 = input().split()
#print(input1)
#print(input2)
myList = DoublyLinkedList()
count = int(input1)
for i in range(count , 0 , -1 ):
    myList.add(i)
myList.last = myList.root
outputList = []
while True:
    output=myList.search(int(input2))
    outputList.append(output)
    #print("willberemoved",output)
    myList.remove(output)
    #myList.print_list()
    #print(myList.get_size())
    #print()
    if(myList.size == 0) :
        new_str = "<"
        for i in range(0, count):
            new_str = new_str +str(outputList[i])
            if i != count-1 :
                new_str = new_str +", "
            else :
                new_str = new_str + ">"
        print(new_str)
        break
    