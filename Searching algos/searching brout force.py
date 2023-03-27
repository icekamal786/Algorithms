def search(n, A):
    i = 0
    try:
        while (i != len(A)):
            i= i+1
            if A[i] == n:
                return (i)
    except IndexError:
        return ("Number not found in the array")
        
        
# Driver's code
A = [1,2,3,4,5,6,6,7,7]
print(search(9,A))