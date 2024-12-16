#Defining a function
def palindrome(A):
    rev = len(A)-1
    Indexing = 0
    while(Indexing<rev):
        if(A[Indexing]!=A[rev]):
            return False
        Indexing += 1
        rev -=1
        return True
A = (1, 2, 3, 3, 2, 1)
if(palindrome(A)):
    print("This is a Palindrome.")
else:
    print("This is not a Palindrome.")
