class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class Linked_list:
    def __init__(self):
        self.head=None
        
    def adding_in_front(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.ref=self.head
            self.head=new_node
    
    def adding_at_end(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            n=self.head
            while n.ref!=None:
                n=n.ref
            n.ref=new_node

    def adding_after_specific_node(self,data,target):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            n=self.head
            while n!=None:
                if n.data==target:
                    new_node.ref=n.ref
                    n.ref=new_node
                    break
                else:
                    n=n.ref
            if n==None:
                # print("no target found !!!")
                return(-1)
            else:
                return(self.head)

    def adding_before_specific_node(self,data,target):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            n=self.head
            while n.ref.ref!=None:
                if n.ref.data==target:
                    new_node.ref=n.ref
                    n.ref=new_node
                    break
                else:
                    n=n.ref
            if n.ref==None:
                # print("no target found !!!")
                return(-1)
            else:
                return(self.head)
            

    def traversal(self):
        if self.head==None:
            print("empty linked List")
        else:
            n=self.head
            while n!=None:
                print(n.data,end=" -> ")
                n=n.ref


# arr=list(map(int,input("enter array elements : ").split(' '))) ## Adding node in front of the linked list
# obj=Linked_list()
# for i in arr:
#     obj.adding_in_front(i)
# obj.traversal()  ## end of the input

# arr=list(map(int,input("enter array elements : ").split(' '))) ## Adding node at the end of the linked list
# obj=Linked_list()
# for i in arr:
#     obj.adding_at_end(i)
# obj.traversal()  ## end of the input

# arr=list(map(int,input("enter array elements : ").split(' '))) ## Adding node after a specific node of the 
# target=int(input("enter the target node :"))                   ## linked list
# value=int(input("entre value to insert :"))
# obj=Linked_list()
# for i in arr:
#     obj.adding_in_front(i)
# k=obj.adding_after_specific_node(value,target)
# if k!=-1:
#     obj.traversal()
# else:
#     print("No target found!!!")  ## end of the input

arr=list(map(int,input("enter array elements : ").split(' '))) ## Adding node after a specific node of the 
target=int(input("enter the target node :"))                   ## linked list
value=int(input("entre value to insert :"))
obj=Linked_list()
for i in arr:
    obj.adding_at_end(i)
k=obj.adding_before_specific_node(value,target)
if k!=-1:
    obj.traversal()
else:
    print("No target found!!!")


    
