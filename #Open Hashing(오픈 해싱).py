#Open Hashing(오픈 해싱)

'''
-Open Hashing : 해시 테이블의 충돌 문제를 해결하는 방법 중 하나로 체이닝(Separate Chaining) 기법이라고도 한다.
-충돌이 일어날 경우 먼저 저장된 데이터에 링크드리스트를 만들어 중복해시 데이터를 연결한다
-파이썬에서는 링크드리스트를 이중 리스트 구조를 이용하여 간단하게 구현할 수 있다.

'''

class OpenHash :
    
    def __init__(self, table_size) : #테이블 사이즈를 받아와 해시테이블의 크기에 맞게 배열을 만든다
        self.size = table_size
        self.hash_table = [0 for a in range(self.size)]
        
    def getkey(self, data): #key를 얻는 함수
        self.key = ord(data[0]) #ord내장함수 -> 문자의 유니코드 값을 돌려주는 함수
        return self.key#data의 0번째 인덱스를 이용하여 key를 만들어 리턴

    def hashFunction(self, key):
        return key%self.size #해쉬함수 -> 키를 테이블크기로 나누어 나눈 나머지

    def getAddress(self, key): #주소를 받아오는 함수
        mykey = self.getkey(key) #mykey라는 변수에 key값을 얻어와
        hash_Address = self.hashFunction(mykey) #key값을 해시함수에 넣어 주소를 받아와 리턴
        return hash_Address


    def save(self, key, value): #값을 저장하는 함수
        hash_Address = self.getAddress(key) #key값을 이용해 주소를 받아오고

        if self.hash_table[hash_Address] != 0: #해당 주소의 테이블이 비어있지 않다면
            for a in range(len(self.hash_table[hash_Address])):#해당 주소의 슬롯 크기만큼 순회하며
                if self.hash_table[hash_Address][a][0] == key: #해당 주소의 키 값과 일치한다면
                    self.hash_table[hash_Address][a][1] = value #이중리스트로 만들어 키값 뒤에 value를 넣는다
                    return
            self.hash_table[hash_Address].append([key,value]) #해당 키값이 없으면 이중리스트로 뒤에 추가한다
        else:
            self.hash_table[hash_Address] = [[key,value]] #0이라면 비어있기에 이중리스트로 추가한다


    def read(self, key): #키값으로 값을 읽어오는 함수
        hash_Address = self.getAddress(key) #주소를 받아와

        if self.hash_table[hash_Address] != 0: #해당 주소가 비어있지 않다면
            for a in range(len(self.hash_table[hash_Address])): #이중리스트의 크기만큼 순회하며
                if self.hash_table[hash_Address][a][0] == key: #key값과 일치한다면
                    return self.hash_table[hash_Address][a][1] #해당 key값의 value 리턴

            return False #없다면 false 리턴

        else:
            return False #해당 주소가 비어있다면 없기에 false 리턴


    def delete(self,key): #특정 키값을 삭제하는 함수
        hash_Address = self.getAddress(key) #키값을 이용해 주소를 받아와

        if self.hash_table[hash_Address] != 0: #주소가 비어있지 않다면
            for a in range(len(self.hash_table[hash_Address])): #해당 주소의 이중리스트 크기만큼 순회하며
                if self.hash_table[hash_Address][a][0] == key: #key값과 일치한다면
                    if(len(self.hash_table[hash_Address])==1): #해당 주소의 이중리스트 크기가 1이면
                        self.hash_table[hash_Address] = 0 #하나뿐인 경우기에 0으로 바꿔주고
                    else:
                        del self.hash_table[hash_Address][a] #아니라면 a번째 인덱스를 지운다
                    return
            return False #해당 주소의 이중리스트를 순회해서 없었기에 false 리턴
        else:
            return False #해당 주소가 비어있는경우기에 false 리턴


h_table = OpenHash(8) #크기가 8인 오픈해시테이블 생성

h_table.save('aa','1111') #키가 aa이고 값이 1111인 데이터 저장
print(h_table.read('aa')) #키가 aa인 값 읽어오기

data1 = 'aa'
data2 = 'ab'

print(ord(data1[0])) #키 값이 중복된다는 걸 보여주기 위한
print(ord(data2[0]))

h_table.save('ab','2222') #해싱함수를 사용했을때 중복되는 값을 집어넣어본다
print(h_table.hash_table)

h_table.read('aa')
h_table.read('ab')

h_table.delete('aa')
print(h_table.hash_table)
print(h_table.delete('Data'))

h_table.delete('ab')
print(h_table.hash_table)

#코드참고(https://jinyes-tistory.tistory.com/11)