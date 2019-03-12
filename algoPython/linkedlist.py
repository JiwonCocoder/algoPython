#파이썬은 포인터라는 개념도 없을뿐더러 필요하지도 않다
'''
Node라는 이름의 클래스를 선언하며 이 클래스로 객체가 생성될 때 __init__메서드를 호출한다.
이 Node 클래스는 데이터를 저장하는 dta와 링크를 저장하는 next를 멤버로 갖고 있다. 
이 link를 이용해서 다음 노드를 가리키기때문에 data가 연속적으로 저장되어 있지 않아도 괜찮은것.               
'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
 
 #연결리슽트의 초기화
def init_list():
     global node_A
     node_A=Node("B")
     node_B=Node("C")
     node_C=Node("D")
     node_D=Node("E")
     node_A.next=node_B
     node_B.next=node_C
     node_C.next=node_D

#연결리스트 출력
def print_list():
    global node_A
    node = node_A
    while node:
        print(node.data)
        node = node.next
    print

#삽입
def insert_list(data):
    global node_A
    node_new = Node(data)
    node_P = node_A
    node_T = node_A.next
    #when, insert point is head  
    if node_A.data > data:
        #node_temp: a instance, Node_A's copy
        node_temp = Node(node_A.data)
        node_temp.next = node_A.next
        #Then, node_A replaces node_new
        node_A = node_new
        #node_new 's next is node_A(prev)
        node_A.next = node_temp
        return
    while node_T.data <= data :
        node_P = node_T
        node_T = node_T.next
    node_new.next = node_T
    node_P.next = node_new

#삭제
def delete_list(data):
    global node_A
    node_prev = node_A
    node_next = node_prev.next

    if node_prev.data == data :
        #node_next replaces node_A
        node_next = node_A
        del node_A
        return
    while node_next :
        if node_next.data == data :
            node_prev.next = node_next.next
            del node_next
            break
        node_prev = node_next
        node_next = node_next.next


if __name__=='__main__':
    init_list()
    print_list()
    insert_list("A")
    print_list()
    delete_list("B")
    print_list()      