# Double Linked List
'''
싱글링크드리스트에 prev라는 앞 노드를 가리키는 것이 추가된 형태.
싱글링크드리스트에 비해 탐색, 삽입, 삭제가 빠르다.

Null -> (Node, Prev, Next)  <-> (Node, Prev, Next) <-> (Node, Prev, Next) ... -> NUll

'''

class Node(object): #data, prev, next를 가지고있는 Node 오브젝트 생성
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DList(object): #더블링크드리스트 오브젝트
    def __init__(self): #head, tail 노드 생성과 / 연결 
        self.head = Node(None)
        self.tail = Node(None, self.head)
        self.head.next = self.tail
        self.size = 0

    def listSize(self): #리스트의 사이즈를 리턴
        return self.size

    def is_empty(self): #리스트가 비어있는지 확인
        if self.size != 0:
            return False
        else :
            return True

    def selectNode(self, idx): #특정 노드를 선택하는 함수
        if idx > self.size: #idx가 리스트의 크기보다 크면 인덱스오류
            print("index error")
            return None
        if idx ==0: #idx가 0 이면 헤드 리턴
            return self.head
        if idx == self.size: #idx가 리스트의 크기와 같다면 꼬리 리턴
            return self.tail
        
        if idx <= self.size//2: #idx가 리스트의 중간보다 앞이면 head부터 next
            target = self.head
            for i in range(idx):
                target = target.next    
            return target

        else:                   #idx가 리스트의 중간보다 뒤면 tail부터 prev
            target = self.tail
            for i in range(self.size -idx):
                target = target.prev
            return target

    def appendleft(self, data): # head에 data를 추가하는 매서드
        if self.is_empty(): # 리스트가 비어있다면 헤드에 넣고 꼬리는 none을 넣고 연결
            self.head = Node(data)
            self.tail = Node(None,self.head)
            self.head.next = self.tail

        else: #tmp에 원래 head를 넣어두고 head를 data로 바꾼후 tmp의 prev에 바뀐 head연결
            tmp = self.head
            self.head = Node(data, None, self.head)
            tmp.prev = self.head

        self.size +=1

    def append(self, data):#data를 추가하는 매서드
        if self.is_empty(): #리스트가 비어있다면 head에 넣고 tail과 연결
            self.head = Node(data)
            self.tail = Node(None,self.head)
            self.head.next = self.tail

        else: #tmp에 꼬리의 prev를 넣어두고 newNode에 넣을 data 넣고 tmp의 next에 newNode연결 꼬리의 prev에 newNode연결
            tmp = self.tail.prev
            newNode = Node(data, tmp, self.tail)
            tmp.next = newNode
            self.tail.prev = newNode

        self.size +=1

    def insert(self,data, idx): #특정 idx에 data를 넣는 매서드
        if self.is_empty(): #리스트가 비어있다면 헤드에 넣고 꼬리와 연결
            self.head = Node(data)
            self.tail = Node(None, self.head)
            self.head.next = self.tail
        else:
            tmp = self.selectNode(idx) #해당 idx의 노드를 tmp에 넣기
            if tmp == None: #tmp가 None이면 그냥 리턴
                return
            if tmp == self.head : #tmp가 헤드이면 appendleft 실행
                self.appendleft(data)
            elif tmp == self.tail: #tmp가 꼬리면 append 실행
                self.append(data)
            else:
                tmp_prev = tmp.prev #tmp_prev에 tmp의 prev 넣어두고
                newNode = Node(data, tmp_prev, tmp) #newNode에 data와 앞에는 tmp_prev 뒤에는 tmp 넣기
                tmp_prev.next = newNode #tmp prev의 next를 newNode로 연결
                tmp.prev = newNode #tmp 의 prev를 newNode로 연결
        self.size +=1

    def delete(self,idx): #삭제하는 매서드
        if self.is_empty(): #비어있다면 그냥 리턴
            print("empty")
            return
        else:
            tmp = self.selectNode(idx) #특정 idx의 노드를 tmp에 넣기
            if tmp == None: #tmp가 비어있다면 리턴
                return
            elif tmp == self.head: #tmp가 헤드면 기존해드의 next를 헤드로 만들기
                tmp = self.head
                self.head = self.head.next
            elif tmp == self.tail: #tmp가 꼬리면 기존꼬리의 prev를 꼬리로 만들기
                tmp = self.tail
                self.tail =self.tail.prev
            else: #tmp prev의 next를 tmp next로 // tmp next의 prev를 tmp prev로
                tmp.prev.next = tmp.next
                tmp.next.prev = tmp.prev
            del(tmp) #tmp삭제후 사이즈 -1
        self.size -=1

    def printlist(self): #리스트의 모든 데이터 프린트
        target = self.head #target을 헤드로 놓고
        while target != self.tail: #target이 꼬리가 될때까지
            if target.next != self.tail: #target의 next가 꼬리가 아니면
                print(target.data, '<->', end='') #<->을 넣으면서 프린트
            else: #target의 next가 꼬리면 그냥 프린트
                print(target.data)
            target = target.next #target을 next로




mylist = DList()
mylist.append('A')
mylist.printlist()
mylist.append('B')
mylist.printlist()
mylist.append('C')
mylist.printlist()
mylist.insert('D', 1)
mylist.printlist()
mylist.appendleft('E')
mylist.printlist()
print(mylist.listSize())
mylist.delete(0)
mylist.printlist()
mylist.delete(3)
mylist.printlist()
mylist.delete(0)
mylist.printlist()
mylist.appendleft('A')
mylist.printlist()

#코드참고(https://underflow101.tistory.com/4)








       
