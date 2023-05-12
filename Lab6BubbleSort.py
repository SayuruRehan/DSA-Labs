#Bubble Sort

A=[]
for v in range(0,5):
    A.append(int(input("Enter number: ")))
print(A)

def bubbleSort(A):
    n = len(A)  #Taking length of array into n variable
    for i in range(1,n):
        for j in range(1,n-i+1):
            if A[j] < A[j-1]:   #checking condition
                A[j], A[j-1] = A[j-1], A[j] #Exchanging positions

bubbleSort(A)
print("Sorted Array: ")
print(A)
                
    
