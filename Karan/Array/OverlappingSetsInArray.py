
"""
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
56. Merge Intervals

"""

arr = [[2,3],[4,5],[6,7],[8,9],[1,10]]

#[1,6]
arr.sort() #nlog(n)

print("SORTED: ",arr)
#print(len(arr))

start = None
end = None
overlap = []
for i in range(len(arr)):
    print("\n\nValue of i:",i)
    #print("arr[i-1][1] >= arr[i][0]", arr[i-1][1] ,arr[i][0], arr[i-1][1] >= arr[i][0])
    print("START_1:END_1", start, end)
    if start is None:
        start = arr[i][0]
        end = arr[i][1]
        print("START_1:END_1", start, end)

    elif (end >= arr[i][0]):
        
        
        print("START_2: END_2", start, end)
        print("arr[i-1][1] >= arr[i][0]", arr[i-1][1] ,arr[i][0], arr[i-1][1] >= arr[i][0])
        if end <= arr[i][1]:
            end = arr[i][1]
            print("START_3:END_3", start, end)


    else: 
        overlap.append([start, end])
        print("\n\nSTART_4:END_4", start, end)
        start = arr[i][0]
        end = arr[i][1]

if start is not None:
    overlap.append([start, end])



print("ANSERR::: ",overlap)

#Time Complexity: n + n(log(n))
#Space Complexity: n


#[[1,4],[2,3]]


a= [[2,3],[4,5],[6,7],[8,9],[1,10]]

a.sort()

print(a)



"""
Input: arr[] = {15,-2,2,-8,1,7,10,23}, n = 8
Output: 5
Explanation: The largest subarray with sum 0 is -2 2 -8 1 7.
https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

"""


arr = [15,-2,2,-8,1,7,10,23]









