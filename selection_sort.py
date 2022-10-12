class Solution: 
        
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            current=arr[i]
            curr_index=i
            if(i+1<len(arr)):
                min=arr[i+1:][0]
            for j in range(len(arr[i+1:])):
                if arr[i+1:][j]<=min:
                    min=arr[i+1:][j]
                    index=j+i+1
            if(min<=current):
                arr[i]=min
                arr[index]=current
        return arr
