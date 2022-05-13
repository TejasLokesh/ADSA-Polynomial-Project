#Declaring two lists to take the polynomials as input
eq1=[]
eq2=[]
def adding():
    #Loop to input poly 1
    print("Enter the Polynomial-1")
    while(True):
        term = []
        term.append(int(input("Enter the Co-efficient: ")))
        term.append(int(input("Enter the Power: ")))
        eq1.append(term)
        if(input("Do you want to continue? (Y/N)") in ['Y','y']):
            continue
        else:
            break
    #Loop to input poly 2
    print("Enter the Polynomial-2")
    while(True):
        term = []
        term.append(int(input("Enter the Co-efficient: ")))
        term.append(int(input("Enter the Power: ")))
        eq2.append(term)
        if(input("Do you want to continue? (Y/N)") in ['Y','y']):
            continue
        else:
            break
    #Declaring a dictionary totalEq to perform addition 
    totalEq = {}
    for i in eq1+eq2:
        x,y = i
        #Main addition step
        if y  in totalEq:
            totalEq[y]+=x
        else:
            totalEq[y] = x
    #Declaring linked list node class with three terms co_eff,power and next 
    class Node:
        def __init__(self,c,p) -> None:
            self.co_eff = c
            self.power = p
            self.next =None
    #Creatng the linked list and appending ll the terms of the polyomial
    head = Node(None,None)
    current = head
    #Sorted to ensure all the powers are in order and reversed to make it descendng order
    for i in reversed(sorted(totalEq)):
        newNode = Node(totalEq[i],i)
        current.next = newNode
        current = current.next
    head = head.next

    #Printing the linked list
    temp = head
    print("Visualization of the Linked List:\n ")
    while temp:
        #Dropping the terms with a coefficient of 0
        if temp.co_eff==0:
            temp = temp.next
            continue
        else:
            print([temp.co_eff,temp.power],end="->")
            temp = temp.next
    print(None)
    
    #Printing the linked list in polynomial form
    print("\nThe final polynomial after addition is: \n")
    temp = head
    while temp:
        if temp.co_eff==0:
            temp = temp.next
            continue
        else:
            print(f"{temp.co_eff}x^{temp.power}",end=" + ")
            temp = temp.next
    print("0",end=" ")
    print("= 0")
#Similar code to the above so all comments apply
def subtracting():
    print("Enter Polynomial-1")
    while(True):
        term = []
        term.append(int(input("Enter the Co-efficient: ")))
        term.append(int(input("Enter the Power: ")))
        eq1.append(term)
        if(input("Do you want to continue? (Y/N)") in ['Y','y']):
            continue
        else:
            break
    print("Enter Polynomial-2")
    while(True):
        term = []
        term.append(int(input("Enter the Co-efficient: ")))
        term.append(int(input("Enter the Power: ")))
        eq2.append(term)
        if(input("Do you want to continue? (Y/N)") in ['Y','y']):
            continue
        else:
            break

    totalEq = {}
    for i in eq1:
        co,p = i
        if p in totalEq:
            totalEq[p]+=co
        else:
            totalEq[p] = co
    #Main subtraction step
    for i in eq2:
        co,p = i
        if p in totalEq:
            totalEq[p]-=co
        else:
            totalEq[p]=-co

    class Node:
        def __init__(self,c,p) -> None:
            self.co_eff = c
            self.power = p
            self.next =None

    head = Node(None,None)
    current = head
    for i in reversed(sorted(totalEq)):
        newNode = Node(totalEq[i],i)
        current.next = newNode
        current = current.next
    head = head.next

    temp = head
    print("Visualization of the Linked List: ")
    while temp:
        if temp.co_eff==0:
            temp = temp.next
        else:
            print([temp.co_eff,temp.power],end="->")
            temp = temp.next
        print(None)

    print("\nThe final polynomial after subtraction is: \n")
    temp = head
    while temp:
        if temp.co_eff==0:
            temp = temp.next
            continue
        else:
            print(f"{temp.co_eff}x^{temp.power}",end=" + ")
            temp = temp.next
    print("0",end=" ")
    print("= 0")

#Main Function
choice=input("Enter A if you want to add two polynomials or S if you want to subtract them:")
if(choice=="a" or choice=="A"):
    adding()
elif(choice=="s" or choice=="S"):
    subtracting()
else:
    print("Invalid Choice, Exitting......!")
    exit





