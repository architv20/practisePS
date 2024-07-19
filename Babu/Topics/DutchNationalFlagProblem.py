arr = [0,1,2,0,9,4,6,7,1,2,2,1,0]

def DNF(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while high>mid:
        if arr[mid] == 2:
            arr[mid] , arr[high] = arr[high], arr[mid]
            mid += 1
            high -= 1
        elif arr[mid] == 0:
            arr[mid] , arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1
        else:
            mid += 1


DNF(arr)

print(arr)
            