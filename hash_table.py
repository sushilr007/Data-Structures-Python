import time
import sys

class HashTable:  
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        if not self.arr[arr_index]:
            return "No key found"
        else:
            for kv in self.arr[arr_index]:
                print("LOL",kv[0],key)
                if kv[0] == key:
                    return kv[1]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))        
            
        
    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("Successfully deleted value for key",key)
                del self.arr[arr_index][index]

    @staticmethod
    def menu():
        print("************MAIN MENU**************")
        time.sleep(1)
        choice = input("""
    A: Store key value pair in hash.
    B: Get a value using key. 
    C: Display Hash table.
    D: Remove value from hash.
    Q: Quit

    Please enter your choice: """)
        if choice == "A" or choice == "a":
                print("How many values you want to store in hash") 
                hs_len = int(input())
                for i in range(hs_len):
                    key,val = input("Enter a key and value: ").split()
                    t[key] = val
                t.menu()
        elif choice == "B" or choice == "b":
            print("Enter key name")
            key_name = input()
            print(t.__getitem__(key_name))
            t.menu()   
        elif choice == "C" or choice =="c":
            print(t.arr)
            t.menu()
        elif choice=="D" or choice=="d":
            print("Enter key to del value")
            key_name = input()
            del t[key_name]
            t.menu()
        elif choice=="Q" or choice=="q":
            sys.exit
        else:
            print("You must only select either A,B,C,D, or Q.")
            print("Please try again")
            menu()            
if __name__ == '__main__':
    t = HashTable()
    t.menu()    