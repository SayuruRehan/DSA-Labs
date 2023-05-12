arr = []

for v in range(7):
    arr.append(int(input("Enter a number: ")))
    print(arr)

def partition(arr, p, r):
    i = (p - 1)
    pivot = arr[r]
    for j in range(p, r):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return(i+1)

def quickSort(arr, p , r):
    if p < r:
        q = partition(arr, p, r)
        quickSort(arr, p, q-1)
        quickSort(arr, q+1, r)

quickSort(arr, 0, len(arr)-1)
print("Sorted array: ")
for i in range(len(arr)):
    print(arr[i])
