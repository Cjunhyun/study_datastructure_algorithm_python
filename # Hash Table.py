# Hash Table 
'''
해쉬 테이블(Hash Table)

key에 value를 맵핑할수 있는 구조
key를 통해 value가 저장된 주소를 알 수 있어, 탐색속도가 빠름

Hash Function : 임의의 데이터를 고정된 길이의 값으로 리턴해주는 함수
Hash / Hash Value / Hash Address : 해시함수를 통해 리턴된 고정된 길이의 값
Hash Table : 키 값의 연산에 의해 직접 접근가능한 데이터 구조
Slot : 해쉬 테이블에서 한개의 데이터를 저장 할 수 있는 공간

keys -> Hash Function -> Hash Table(Slot, Slot, ...)

'''

class HashTable:

    def __init__(self, tb_size): #해시테이블의 크기를 받아와 배열을 만들기
        self.size = tb_size
        self.hash_table = [0 for a in range(self.size)]

    def getKey(self, data): #key를 얻는 함수
        self.key = ord(data[0]) # ord내장함수 -> 문자의 유니코드 값을 돌려주는 함수
        return self.key

    def hasFunction(self, key): #해쉬함수 : 키값을 테이블의 사이즈로 나누는 조건
        return key%self.size
    
    def getAddress(self, key): #주소를 만드는 함수
        myKey = self.getKey(key) #myKey에 키값을 얻어와
        hash_address = self.hasFunction(myKey) #해시함수에 넣어서 나온 값을 hash_address에 넣는다
        return hash_address

    def save(self, key, value): #value를 저장하는 함수
        hash_address = self.getAddress(key) #요청한 key값으로 주소를 만들어와
        self.hash_table[hash_address] = value #해당 주소에 value값을 추가
 
    def read(self, key): #key값을 통해 value를 얻어오는 함수
        hash_address = self.getAddress(key) #key값으로 주소를 얻어와
        return self.hash_table[hash_address] #해당 주소의 value를 리턴

    def delete(self,key): #key값을 통해 value를 삭제하는 함수
        hash_address = self.getAddress(key) #key값을 통해 주소를 얻어와

        if self.hash_table[hash_address] == 0 : #해당 주소가 비어있다면 False 리턴
            return False
        else :
            self.hash_table[hash_address] = 0 #해당 주소에 값이 있다면 0으로 바꾸고 True 리턴
            return True

hash_table = HashTable(8)
hash_table.save('a', '2222')
hash_table.save('b', '4444')
hash_table.save('c', '5555')
hash_table.save('d', '8888')

print(hash_table.hash_table)
print(hash_table.read('b'))

hash_table.delete('b')
print(hash_table.hash_table)

# 코드참고(https://jinyes-tistory.tistory.com/10)




