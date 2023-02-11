class Search:
    def __init__(self,arr,find):
        self.arr=arr
        self.find=find
    def binary_search(self,left,right):
        mid=(left+right)//2
        if left>right:
            return(-1)
        if self.arr[mid]==self.find:
            return(mid)
        if self.arr[mid]>self.find:
            return(self.binary_search(0,mid))
        else:
            return(self.binary_search(mid+1,len(self.arr)-1))


arr=list(map(int,input("enter array elements : ").split(' ')))
find=int(input("Enter to find:"))
sc=Search(arr,find)
i=sc.binary_search(0,len(arr)-1)
if i==(-1):
    print("no item found")
else:
    print(f"item found in {i+1}th position")