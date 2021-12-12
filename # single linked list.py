# single linked list

'''
-링크드 리스트(Linked List)
떨어진 곳에 존재하는 데이터를 화살표(포인터)로 연결하는 구조

-구성
노드(Node) : 데이터 저장 단위(데이터값, 포인터)로 구성
포인터(Pointer)(reference) : 다음이나 이전노드의 위치를 가지고있는 공간

-특징
데이터공간을 미리 할당하지 않아도 됨
연결을 위한 별도의 공간이 필요
중간 데이터 삭제시, 부가적인 작업이 필요하다

-싱글링크드리스트(single linked list)
동적 메모리 할당을 이용해 노드를 한 방향으로만 연결한 리스트 구조
탐색 시 항상 첫 노드부터 차례로 찾아야한다
ex) head_node(item+reference) -> node(item+reference) -> node(item+reference) -> node(item+reference) ...

*노드생성
*리스트 사이즈
*노드 추가하는 매서드 
*원하는 노드를 찾는 매서드
*중간에 데이터를 추가하는 매서드
*특정 노드를 삭제하는 매서드
*모든 노드를 출력하는 매서드
*

'''

from typing import Sized

class Node: #노드 생성자
    def __init__(self, item, link) : #노드는 아이템과 다음 노드를 가르키는 링크로 구성
        self.item = item
        self.link = link

class Slist:

    
    def __init__(self): #연결리스트의 헤드와 크기를 알수있게하는 생성자
        self.head = Node(None)
        self.size = 0

    def size(self): #리스트의 크기를 리턴하는 함수
        return self.size

    def is_empty(self): #리스트가 비어있는지 확인
        if self.size == 0:
            return True
        else:
            return False

    def selectNode(self, idx): #특정 노드 선택하기
        if idx >= self.size :
            print("index error")
            return None
        if idx == 0 :
            return self.head
        else :
            sltNode = self.head
            for cnt in range(idx):
                sltNode = sltNode.next
            return sltNode

    def append(self, value): #특정값 추가
        if self.is_empty :
            self.head = Node(value)
            self.size += 1
        else:
            target = self.head
            while target.next != None:
                target = target.next
            newtail = Node(value)
            target.next = newtail
            self.size += 1

    def headAppend(self, value): #헤드에 추가
        if self.is_empty:
            self.head = Node(value)
            self.size +=1
        else:
            self.head = Node(value, self.head)
            self.size +=1

    def insert(self, value, idx): #특정 인덱스 추가하는 매서드
        if self.is_empty: #비어있다면 헤드에 추가
            self.head = Node(value)
            self.size +=1
        elif idx == 0: #인덱스가 0이면 헤드로 넣고 연결
            self.head = Node(value,self.head)
            self.size +=1
        else :
            tgt = self.selectNode( idx-1) #타겟 인덱스 전의 노드 가져오기
            if tgt == None : #tgt가 비어있다면 리턴
                return
            newNode = Node(value) #newNode라는 곳에 넣을 노드 넣어두고
            tgt_next = tgt.next #tgt_next라는 곳에 tgt의 다음 노드 넣어두고
            tgt.next = newNode #tgt의 next에 newNode를 넣은 후
            newNode.next = tgt_next #newNode의 next에 tgt_next 넣어서 연결
            self.size +=1

    def delete(self, idx):
        if self.is_empty:
            print("index error")
            return None
        elif idx >= self.size :
            print("index errror")
            return None
        elif idx == 0 :
            tgt = self.head
            self.head = tgt.next
            del(tgt)
            self.size -=1
        else:
            tgt = self.selectNode(idx-1)
            del_tgt = tgt.next
            tgt.next = del_tgt.next
            del(del_tgt)
            self.size -=1

    def printAll(self):
        tgt = self.head
        while tgt :
            if tgt.next != None:
                print(tgt.data, '->', end='')
                tgt = tgt.next
            else:
                print(tgt.next)
                tgt=tgt.next

mylist = Slist()
mylist.append('A')
mylist.printlist()
mylist.append('B')
mylist.printlist()
mylist.append('C')
mylist.printlist()
mylist.insert('D', 1)
mylist.printlist()
mylist.headAppend('E')
mylist.printlist()
print(mylist.listSize())
mylist.delete(0)
mylist.printlist()
mylist.delete(3)
mylist.printlist()
mylist.delete(0)
mylist.printlist()
mylist.headAppend('A')
mylist.printlist()




   






        