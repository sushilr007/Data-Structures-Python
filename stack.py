import sys 
import time
stack = []      
def menu():
    print("************MAIN MENU**************")
    time.sleep(1)
    print()

    choice = input("""
    A: Push
    B: Pop
    C: display()
    Q: Quit

    Please enter your choice: """)

    if choice == "A" or choice == "a":
        push()
    elif choice == "B" or choice =="b":
        pop()
    elif choice=="D" or choice=="d":
        display()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select either A,B,C, or D.")
        print("Please try again")
def push(): #Pushing the element in stack
    print("How many numbers you want to push in stack")
    stack_size = int(input())
    print("Enter a number to push")
    for i in range(0, stack_size): 
        element = int(input()) 
        stack.append(element) # adding the element 
        print("Successfully inserted:",stack ) 
    menu()      
def pop(): #Poping the element from the stack
    if len(stack)<0:
        print("stack is empty")
    else:
        print("Removed element",stack.pop())
        menu()       
def display(): #Display the stack
    print(stack)
    menu()
menu()        