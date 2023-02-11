class Search:
    def __init__(self,arr,find):
        self.arr=arr
        self.find=find

    def binary_search(self,arr):
        self.arr=sorted(self.arr)
        left=0
        right=len(self.arr)-1
        while left<=right:
            mid=(left+right)//2
            if self.arr[mid]==self.find:
                return(mid)
            elif self.arr[mid]>self.find:
                right=mid
            elif self.arr[mid]<self.find:
                left=mid
        return(-1)



arr=list(map(int,input("enter array elements : ").split(' ')))
find=int(input("Enter to find:"))
sc=Search(arr,find)
i=sc.binary_search(arr)
if i==(-1):
    print("no item found")
else:
    print(f"the item found in {i}th place")
