A = [9, 5, 3, 1, 7, 6]
# for i in range(len(A) - 1):
#     for j in range(i+1, len(A)):
#         if A[i] > A[j]:
#             temp = A[i]
#             A[i] = A[j]
#             A[j] = temp

    # Bubble sort
# for i in range(len(A)):
#     for j in range(0, len(A) - i - 1):
#         if A[j] > A[j+1]:
#             temp = A[j]
#             A[j] = A[j+1]
#             A[j+1] = temp

# selection sort
for i in range(len(A)):
    minIndex = i
    for j in range(i+1, len(A)):
        if A[j] < A[minIndex]:
            minIndex = j
    temp = A[i]
    A[i] = A[minIndex]
    A[minIndex] = temp
print(A)