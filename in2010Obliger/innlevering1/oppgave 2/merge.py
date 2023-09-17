import math

from countswaps import CountSwaps

def sort(A):
    # Do merge sort here. Use the Sorter's comparison- and swap
    # methods for automatically counting the swaps and comparisons.

    # Use A.swap(i, j) to swap the values at two indices i and j. The swap is
    # counted, when using this method. Comparisons are counted automatically.

    
    def merge(A1,A2,A):

        i= 0
        j=0
        returliste=[]

        while i < len(A1) and j < len(A2):
            if A1[i] <= A2[j]:
                returliste.append(A1[i])
                i=i+1
            else:
                returliste.append(A2[j])
                j=j+1
        while i < len(A1):
            returliste.append(A1[i])
            i=i+1
        while j < len(A2):
            returliste.append(A2[j])
            j=j+1
            
        return CountSwaps(returliste)
    
    #mergesort
    def mergeSort(A):
        if len(A)<=1:
            return A
        
        halvIndex = math.floor(len(A)/2)
        A1 = mergeSort(A[:halvIndex])
        A2 = mergeSort(A[halvIndex:])
        return merge(A1,A2,CountSwaps(A))
        
    return mergeSort(A)


