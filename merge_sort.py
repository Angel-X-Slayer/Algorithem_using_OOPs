class MergeSort:
    def __init__(self, data):
        self.data = data
 
    def sort(self):
        if len(self.data) > 1:
            mid = len(self.data)//2
            left_half = self.data[:mid]
            right_half = self.data[mid:]
 
            left_half = MergeSort(left_half)
            left_half.sort()
 
            right_half = MergeSort(right_half)
            right_half.sort()
 
            i = 0
            j = 0
            k = 0
            while i < len(left_half.data) and j < len(right_half.data):
                if left_half.data[i] < right_half.data[j]:
                    self.data[k] = left_half.data[i]
                    i = i + 1
                else:
                    self.data[k] = right_half.data[j]
                    j = j + 1
                k = k + 1
 
            while i < len(left_half.data):
                self.data[k] = left_half.data[i]
                i = i + 1
                k = k + 1
 
            while j < len(right_half.data):
                self.data[k] = right_half.data[j]
                j = j + 1
                k = k + 1
            return self.data
        else:
            return(-1)
 
# Driver code to test above
if __name__ == '__main__':
    data=list(map(int,input("enter array elements : ").split(' ')))
    print("Given array is :")
    print(data)
    m_sort = MergeSort(data)
    k=m_sort.sort()
    if k==-1:
        print("invalid output")
    else:

        print("Sorted array is: ")

        print(k)

















# # class Sort:
# #     def __init__(self,arr):
# #         self.arr=arr
# #         self.op=[]
# #     def merge_sort(self,arr):
# #         if len(self.arr)>1:
# #             mid=len(self.arr)//2
# #             la=self.arr[:mid]
# #             ra=self.arr[mid:]
# #             self.merge_sort(la)
# #             self.merge_sort(ra)
# #             i=0
# #             j=0
# #             k=0
# #             while i<len(self.la) and j<len(self.ra):
# #                 if self.la[i]<self.ra[j]:
# #                     self.op.append(self.la[i])
# #                     i+=1
# #                 else:
# #                     self.op.append(self.ra[j])
# #                     j+=1
# #             while i<len(self.la):
# #                 self.op.append(self.la[i])
# #                 i+=1
# #             while j<len(self.ra):
# #                 self.op.append(self.ra[j])
# #                 j+=1
# #             return(self.op)
# #         else:
# #             return(-1)


# class Sort:
#     def __init__(self,arr):
#         self.arr=arr
#         self.la=[]
#         self.ra=[]
#     def merge_sort(self,l,r):
#         if len(self.arr)>1:
#             mid=(l+r)//2
#             self.la=self.arr[:mid]
#             self.ra=self.arr[mid:]
#             self.merge_sort(0,mid-1)
#             self.merge_sort(mid+1,len(arr)-1)
#             j=0
#             k=0
#             while i<len(self.la) and j<len(self.ra):
#                 if self.la[i]<self.ra[j]:
#                     self.op.append(self.la[i])
#                     i+=1
#                 else:
#                     self.op.append(self.ra[j])
#                     j+=1
#             while i<len(self.la):
#                 self.op.append(self.la[i])
#                 i+=1
#             while j<len(self.ra):
#                 self.op.append(self.ra[j])
#                 j+=1
#             return(self.op)
#         else:
#             return(-1)



# arr=list(map(int,input("enter array elements : ").split(' ')))
# sr=Sort(arr)
# k=sr.merge_sort(0,len(arr)-1)
# if k!=-1:
#     print(k)
# else:
#     print("Wrong Input")



# # class MergeSort:
# #     def __init__(self, array):
# #         self.array = array
# #         self.length = len(array)
    
# #     # Function to merge two subarrays
# #     def merge(self, l, m, r):
# #         if l < r:
# #             m = (l + (r - 1)) // 2
# #             # Sort first and second halves
# #             self.merge(l, m)
# #             self.merge(m + 1, r)
# #             self.merge(l, m, r)

# #         # Create two temp arrays
# #             n1 = m - l + 1
# #             n2 = r - m
# #             Left = [0] * n1
# #             Right = [0] * n2
# #             # Copy data to temp arrays Left[] and Right[]
# #             for i in range(0, n1):
# #                 Left[i] = self.array[l + i]
# #             for j in range(0, n2):
# #                 Right[j] = self.array[m + 1 + j]
# #             # Merge the temp arrays back into array[l..r]
# #             i = 0  # Initial index of first subarray
# #             j = 0  # Initial index of second subarray
# #             k = l  # Initial index of merged subarray
# #             while i < n1 and j < n2:
# #                 if Left[i] <= Right[j]:
# #                     self.array[k] = Left[i]
# #                     i += 1
# #                 else:
# #                     self.array[k] = Right[j]
# #                     j += 1
# #                 k += 1
# #             # Copy the remaining elements of Left[], if any
# #             while i < n1:
# #                 self.array[k] = Left[i]
# #                 i += 1
# #                 k += 1
# #             # Copy the remaining elements of Right[], if any
# #             while j < n2:
# #                 self.array[k] = Right[j]
# #                 j += 1
# #                 k += 1
    
# #     # Function to sort array using merge sort
# #     # def merge_sort(self, l, r):
        
# # # Driver code
# # arr = [12, 11, 13, 5, 6, 7]
# # sort = MergeSort(arr)
# # m=((len(arr)-1)+0)//2
# # sort.merge(0, len(arr)-1,m)
# # print ("Sorted array is:")
# # for i in range(sort.length):
# #     print ("%d" %sort.array[i])

# ############################################################################################################


# # class MergeSort: 
# # 	def __init__(self, arr): 
# # 		self.arr = arr 
# # 		self.temp_arr = [0]*len(arr) 

# # 	def mergeSort(self, left, right): 
# # 		if left < right: 
			
# # 			mid = (left+(right-1))//2
			
# # 			self.mergeSort(left, mid) 
# # 			self.mergeSort(mid + 1, right) 
# # 			self.merge(left, mid, right) 

# # 	def merge(self, left, mid, right): 
# # 		for i in range(left, right + 1): 
# # 			self.temp_arr[i] = self.arr[i] 
		
# # 		i = left 
# # 		j = mid + 1
# # 		k = left 
		
# # 		while i <= mid and j <= right: 
# # 			if self.temp_arr[i] <= self.temp_arr[j]: 
# # 				self.arr[k] = self.temp_arr[i] 
# # 				i += 1
# # 			else: 
# # 				self.arr[k] = self.temp_arr[j] 
# # 				j += 1
# # 			k += 1

# # 		while i <= mid: 
# # 			self.arr[k] = self.temp_arr[i] 
# # 			k += 1
# # 			i += 1

# # arr = [12, 11, 13, 5, 6, 7] 
# # ms = MergeSort(arr) 
# # ms.mergeSort(0, len(arr)-1) 
# # print ("Sorted array is:") 
# # for i in range(len(arr)): 
# # 	print ("%d" %arr[i]),





























# class MergeSort:
#     def __init__(self, data):
#         self.data = data
 
#     def sort(self):
#         if len(self.data) > 1:
#             mid = len(self.data)//2
#             left_half = self.data[:mid]
#             right_half = self.data[mid:]
 
#             left_half = MergeSort(left_half)
#             left_half.sort()
 
#             right_half = MergeSort(right_half)
#             right_half.sort()
 
#             i = 0
#             j = 0
#             k = 0
#             while i < len(left_half.data) and j < len(right_half.data):
#                 if left_half.data[i] < right_half.data[j]:
#                     self.data[k] = left_half.data[i]
#                     i = i + 1
#                 else:
#                     self.data[k] = right_half.data[j]
#                     j = j + 1
#                 k = k + 1
 
#             while i < len(left_half.data):
#                 self.data[k] = left_half.data[i]
#                 i = i + 1
#                 k = k + 1
 
#             while j < len(right_half.data):
#                 self.data[k] = right_half.data[j]
#                 j = j + 1
#                 k = k + 1
#         return(self.arr)
 

# arr=list(map(int,input("enter array elements : ").split(' ')))
# sr=MergeSort(arr)
# k=sr.sort()
# if k!=-1:
#     print(k)
# else:
#     print("Wrong Input")



# class MergeSort:
#     def __init__(self, data):
#         self.data = data
 
#     def sort(self):
#         if len(self.data) > 1:
#             mid = len(self.data)//2
#             left_half = self.data[:mid]
#             right_half = self.data[mid:]
 
#             left_half = MergeSort(left_half)
#             left_half.sort()
 
#             right_half = MergeSort(right_half)
#             right_half.sort()
 
#             i = 0
#             j = 0
#             k = 0
#             while i < len(left_half.data) and j < len(right_half.data):
#                 if left_half.data[i] < right_half.data[j]:
#                     self.data[k] = left_half.data[i]
#                     i = i + 1
#                 else:
#                     self.data[k] = right_half.data[j]
#                     j = j + 1
#                 k = k + 1
 
#             while i < len(left_half.data):
#                 self.data[k] = left_half.data[i]
#                 i = i + 1
#                 k = k + 1
 
#             while j < len(right_half.data):
#                 self.data[k] = right_half.data[j]
#                 j = j + 1
#                 k = k + 1
 
# if __name__ == "__main__":
#     data = [5, 3, 7, 9, 4, 1, 8, 2, 6]
#     merge_sort = MergeSort(data)
#     merge_sort.sort()
#     print(merge_sort.data)




