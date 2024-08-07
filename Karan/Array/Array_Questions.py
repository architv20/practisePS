
"""
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
56. Merge Intervals

"""

# arr = [[2,3],[4,5],[6,7],[8,9],[1,10]]

# #[1,6]
# arr.sort() #nlog(n)

# print("SORTED: ",arr)
# #print(len(arr))

# start = None
# end = None
# overlap = []
# for i in range(len(arr)):
#     print("\n\nValue of i:",i)
#     #print("arr[i-1][1] >= arr[i][0]", arr[i-1][1] ,arr[i][0], arr[i-1][1] >= arr[i][0])
#     print("START_1:END_1", start, end)
#     if start is None:
#         start = arr[i][0]
#         end = arr[i][1]
#         print("START_1:END_1", start, end)

#     elif (end >= arr[i][0]):
        
        
#         print("START_2: END_2", start, end)
#         print("arr[i-1][1] >= arr[i][0]", arr[i-1][1] ,arr[i][0], arr[i-1][1] >= arr[i][0])
#         if end <= arr[i][1]:
#             end = arr[i][1]
#             print("START_3:END_3", start, end)


#     else: 
#         overlap.append([start, end])
#         print("\n\nSTART_4:END_4", start, end)
#         start = arr[i][0]
#         end = arr[i][1]

# if start is not None:
#     overlap.append([start, end])



# print("ANSERR::: ",overlap)

#Time Complexity: n + n(log(n))
#Space Complexity: n


#[[1,4],[2,3]]


#a= [[2,3],[4,5],[6,7],[8,9],[1,10]]

#a.sort()

#print(a)



"""
Input: arr[] = {15,-2,2,-8,1,7,10,23}, n = 8
Output: 5
Explanation: The largest subarray with sum 0 is -2 2 -8 1 7.
https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

"""

"""
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""

#Brute Force --> Trave the matrix and look for 0 --> as soon as the 0s are encounterd mark it to -1


def setAll0sAsRowsAndColumns(a,m,n):
    def _markAllRows(i):
        for k in range(n):
                    if a[i][k] != 0:
                        a[i][k] = -1

    def _markAllCols(j):
        for k in range(m):
                    if a[k][j] != 0:
                        a[k][j] = -1


    for i in range(m):
        for j in range(n):
           
            if a[i][j] == 0:
                _markAllRows(i)
                _markAllCols(j)
        
    for i in range(m):
        for j in range(n):
            if a[i][j] == -1:
                a[i][j] = 0
    
    return a
            
#Time Complexity: O(n * m) * O(n)*O(m) + O(n * m) @ O(n*m) cube approx
#Space Complexity: O(1)

#Better approach:
#Provision a new array for row and columns with default values as -1 and then make it as 0 while travering the array

def setAll0sColsAndRows(a,m,n):
    rows = [-1] * m
    cols = [-1] * n

    # print(rows)
    # print(cols)
    for i in range(m):
         for j in range(n):
              if a[i][j] == 0:
                rows[i] = 0
                cols[j] = 0

    # print(rows)
    # print(cols)
    for i in range(m):
         for j in range(n):
                if rows[i] == 0:
                   a[i][j] = 0
                if cols[j] == 0:
                     a[i][j] = 0

  
    return a 
         



#Time Complexity  --> Square(O(n*m))
#Space Complexity --> O(m) + O(n)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

#setAll0sAsRowsAndColumns(matrix,3,4)

#setAll0sColsAndRows(matrix, 3,4)

#print(matrix)


#Optimal Solution --> In the previous approach the issue was with the Space Complexity for usign external Arrays for rows and cols

#Idea for the optimal solution is to 1st row and 1st columns as the arrays and update the values during 1st traversal
#for the 1st a[0][0], use an external variable to save value as col1:
#While iterating for the first time exclude 1st row and 1st column
#Once the updates are done the move on the next traversal:
    #Start updating the values from the inner matrix which exculdes 1st row and 1st col
    #Then start with 1st Row and lastly address 1st column


def OptimalSolution(a, m ,n):
    col0 = -1
    for i in range(m):
        for j in range(n):
            if a[i][j] == 0:
                    a[i][0] = 0
                    
                    if j!= 0:
                        a[0][j] = 0
                    else:
                         col0 = 0
    
                 
#     for i in range(1,m):
#          for j in range(1,n):
#             if a[i][0] == 0 or a[0][j] == 0:
#                 a[i][j] = 0

#     if a[0][0] == 0:
#          for j in range(m):
#               a[0][j] = 0
#     if col0 ==0:
#          for i in range(m):
#               a[i][0]=0
     

        

# # OptimalSolution(matrix, 3,4)
# # print(matrix)


#time Compllextity: O(n*m) + O(n*m) + O(n) + O(n)
#Space Complexity: o(1)

def secondLargest(a):
    l1 = a[0]
    l2 = a[1]

    for i in range(2, len(a)):
        if a[i] == l1 or a[i] == l2:
            continue
        elif a[i] > l1:
             l2 = l1
             l1 = a[i]
        elif a[i] > l2:
             l2 = a[i]
        
        print(l1,l2)     
        
# a = [4,5,3,45,444,2,2,444,2,1]

# secondLargest(a)


#Remove in place duplicates from sorted Array

def removeDup(a):
     i  = 1
     c = 0
     while i < len(a):
        if a[i] == a[i-1]:
            a.pop(i)
            c +=1
        else:
             i+=1
        return c


def removeDupOpt(a):
    i = 0
    for j in range(1,len(a)):
         if a[i] != a[j]:
              a[i+1] = a[j]
              i += 1
    
    return i + 1

a = [1,1,2,2,3,3,3]

print(removeDupOpt(a))
print(a)


        
def _returnIndex(arr,val,s,e):
    if len(arr) ==1:
         if arr[0] == val:
            return True
         else:
              False
    else:
         
         m = (s+e)//2
         if arr[m] == val:
              return True
         else:
              
              return _returnIndex(arr, val, s, m-1)

                     


def returnIndex(arr, val):
     return _returnIndex(arr,val, 0, len(arr)-1)     


a = [2,4,6,7,8,9,11,44,66]
print(returnIndex(a,6))



def threeSum(arr):
    arr.sort()
    resultSet = []
    for i in range(len(a)-3):
        if a[i] > 0:
            break
        if i > 0 and a[i] == a[i-1]:
            continue
        start = i 
        end = len(a) - 1
        temp = i + 1


        while temp <= end:
            hs = a[start] + a[temp] + a[end]

            if hs == 0:
                if start != end != temp:

                    resultSet.append([a[start],a[temp],a[end]])
                    if a[temp] == a[temp+1]:
                        continue
                    else:
                        temp += 1
                    if a[end] == a[end-1]:
                        continue
                    else:
                        end -= 1
                        
            elif hs > 0:
                temp += 1
            else:
                end -= 1
    return resultSet

a = [-1,0,1,2,-1,-4]

print(threeSum(a))
