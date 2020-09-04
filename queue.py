from collections import deque 
import time
import sys
# Initializing a queue 
q = deque() 


def menu():
    print("************MAIN MENU**************")
    time.sleep(1)
    choice = input("""
    A: Insert
    B: Append
    C: Pop
    D: display
    Q: Quit

    Please enter your choice: """)

    if choice == "A" or choice == "a":
        insert()
    elif choice == "B" or choice == "b":
        append()   
    elif choice == "C" or choice =="c":
        pop()    
    elif choice=="D" or choice=="d":
        display()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A,B,D, or Q.")
        print("Please try again")
        menu()

def append():
    print("Enter a number to append")
    i = int(input())
    q.append(i)
    menu()

def insert():
    print("How many numbers you want to push in queue")
    queue_size = int(input())
    print("Enter a number to insert")
    for i in range(0, queue_size):
        element = input()
        q.append(element)
    menu()

def pop():
    if len(q)<0:
        print("Queue is empty")
        return 
    else:

        print("Removed element:-",q.popleft())
    menu()
def display():
    if len(q)<0:
        print("Queue is empty")
    else:    
        print(q)                
    menu()
menu()  