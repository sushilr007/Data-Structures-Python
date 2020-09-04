import time
import sys
#Create a node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

#Operations on LL
class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return ll.menu()
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)
        ll.menu()

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Position")

        if index==0:
            self.insert_at_begining(data)
            return ll.menu()

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1
        ll.menu()    

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Position")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    @staticmethod
    def menu():
        print("************MAIN MENU**************")
        time.sleep(1)
        choice = input("""
    A: Insert multiple values in linked list
    B: Insert value at position
    C: Remove value by postion
    D: Display linked list
    Q: Quit

    Please enter your choice: """)
        if choice == "A" or choice == "a":
                print("How many values you want to put in LL?")
                l_val = int(input())
                print("Enter all values to insert in LL:")
                val = []
                for i in range(l_val):
                    val.append(input())
                ll.insert_values(val)
                ll.menu()
        elif choice == "B" or choice == "b":
            print("Enter position")
            pos = int(input())
            print("Enter the values to insert")
            val = input()
            ll.insert_at(pos,val)   
        elif choice == "C" or choice =="c":
            print("Enter position")
            pos = int(input())
            ll.remove_at(pos)   
            ll.menu()
        elif choice=="D" or choice=="d":
            ll.print()
        elif choice=="Q" or choice=="q":
            sys.exit
        else:
            print("You must only select either A,B,D, or Q.")
            print("Please try again")
            ll.menu()
if __name__ == '__main__':
    ll = LinkedList()
    ll.menu()       