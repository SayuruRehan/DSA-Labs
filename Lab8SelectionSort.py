#Selection Sort

A = []

for v in range(8):
    A.append(int(input("Enter a number: ")))
    
print("Initial array: ", A)

def selectionSort(A):
    n = len(A)
    for j in range(0, n-1):
        smallest = j
        for i in range(j+1, n):
            if A[smallest] > A[i]:
                smallest = i
            A[j], A[smallest] = A[smallest], A[j]

selectionSort(A)
print("Sorted Array: ", A)
