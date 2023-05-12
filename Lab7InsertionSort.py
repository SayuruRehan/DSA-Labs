#Insertion sort

A=[]

n = 9 #number of elements as input

for v in range(0,n):
    number = int(input("Enter a number: "))
    if(number > 10 and number < 20):
        A.append(number)
    else:
        print("Invalid number")
    v = v + 1
print(A)

def insertionSort(A):
    for j in range(1,len(A)): #traverse through the length of the array
        key = A[j]
        i = j - 1
        while i >= 0 and key < A[i]:
            A[i+1] = A[i]
            i = i - 1
        A[i + 1] = key
        
insertionSort(A)
print("Sorted array: ", A)
