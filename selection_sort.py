A = [23, 18, 66, 9, 21, 90, 32, 4]
a = [23, 6, 5]
start = 0
end = len(A) - 1

def FindLargest(A, start, end):
    loc = start
    i = start + 1

    while i <= end:
        if A[i] > A[loc]:
            A[loc] = A[i]
        i += 1

    return A[loc]

print(FindLargest(A, start, end))