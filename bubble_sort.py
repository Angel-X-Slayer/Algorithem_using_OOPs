class Sort:
    def __init__(self,arr):
        self.arr=arr
    def bubble_sort(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr)-1):
                if self.arr[j]>self.arr[j+1]:
                    self.arr[j],self.arr[j+1]=self.arr[j+1],self.arr[j]
                else:
                    pass
        return(self.arr)

arr=list(map(int,input("enter array elements : ").split(' ')))
sr=Sort(arr)
k=sr.bubble_sort()
print(k)