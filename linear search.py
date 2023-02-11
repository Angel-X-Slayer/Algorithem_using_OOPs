class Linear_Search:
    def __init__(self,arr,find):
        self.arr=arr
        self.find=find
    def search(self):
        for i in range (len(self.arr)):
            if self.arr[i]==self.find:
                return(1,i)
        return(0,-1)

arr=list(map(int,input("enter array elements : ").split(' ')))
# arr=[1,2,3,4,5,6]
find=int(input("Enter the element to find :"))
sc=Linear_Search(arr,find)
k,l=sc.search()
if k==0:
    print("no item found")
else:
    print(f"item forund in {l}th position")

