def swapp(arr,i,j):
    arr[i], arr[j] = arr[j], arr[i]

def pt(arr, start, end):
    pi = start
    swap = start
    i = start+1
    while i <= end:
        if arr[pi] > arr[i]:
            swap += 1
            swapp(arr,swap,i)
        i += 1
    swapp(arr,swap,pi)
    return swap

def qs(arr,start,end):
    if start<end:
        pi = pt(arr, start, end)
        qs(arr,start,pi-1)
        qs(arr,pi+1,end)
    return arr


# arr = [6,7,5]
# print(arr)
# pt(arr,1,2)
# print(arr)
# arr = [4,6,1,7,3,2,5]
arr = [11,9,29,7,2,15,28]
qs(arr,0,len(arr)-1)
print(arr)
