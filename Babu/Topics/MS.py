
def merge(arr1,arr2):
    pi1 = 0
    pi2 = 0
    arr3 = []
    while pi1 < len(arr1) and pi2 < len(arr2):
        if arr1[pi1] < arr2[pi2]:
            arr3.append(arr1[pi1])
            pi1 += 1
        else:
            arr3.append(arr2[pi2])
            pi2 += 1
    while pi1 < len(arr1):
        arr3.append(arr1[pi1])
        pi1 += 1
    while pi2 < len(arr2):
        arr3.append(arr2[pi2])
        pi2 += 1
    return arr3

def MS(arr):
    if len(arr) == 1:
        return arr
    mid = int(len(arr)/2)
    left = MS(arr[:mid])
    right = MS(arr[mid:])
    return merge(left,right)


if __name__ == "__main__":
    arr3 = [11,9,29,7,2,15,28,56]
    MS(arr3)
    print(arr3)

