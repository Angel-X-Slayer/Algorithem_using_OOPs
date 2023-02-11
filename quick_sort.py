class sort:
    def __init__(self,arr):
        self.arr=arr
    # def swap(self,right1):                                      ## how to pass the argumernts to                                                               
    #     temp=self.arr[left]                                     ## the Swap function and                                                       
    #     self.arr[left]=self.arr[right1]                         ## bypass the 20th and 22nd line with                 
    #     self.arr[right1]=temp                                   ## this swap function
    #     pass 
    def find_pivot(self,left,right):
        pivot=right
        right1=right-1
        while True:
            while left<=right1 and self.arr[left]<=self.arr[pivot]:
                left+=1
            while left<=right1 and self.arr[right1]>=self.arr[pivot]:
                right1-=1
            if right1<left:
                break
            else:
                self.arr[left],self.arr[right1]=self.arr[right1],self.arr[left]
                # self.swap(right1)
        self.arr[left],self.arr[pivot]=self.arr[pivot],self.arr[left]
        # self.swap(pivot)
        return(left)
    def quick_sort(self,left,right):
        if left<right:
            f=self.find_pivot(left,right)
            self.quick_sort(left,f-1)
            self.quick_sort(f+1,right)
        return(self.arr)


arr=list(map(int,input("enter array elements : ").split(' ')))
left=0
right=len(arr)-1
srt=sort(arr)
a=srt.quick_sort(left,right)
print(a)