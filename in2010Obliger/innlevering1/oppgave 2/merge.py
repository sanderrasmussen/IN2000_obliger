import math

from countswaps import CountSwaps

def sort(A):
    # Do merge sort here. Use the Sorter's comparison- and swap
    # methods for automatically counting the swaps and comparisons.

    # Use A.swap(i, j) to swap the values at two indices i and j. The swap is
    # counted, when using this method. Comparisons are counted automatically.

    # siden dette er merge(sort) der vi setter elementer inn i nye lister så burde det ikke trenges å bruke A.swap(telle swaps)
    def merge(A1,A2,A):
        # dersom jeg skulle ha telt swaps her hadde jeg vel måttet tatt med meg det originale liste elementet hele veien gjennom rekursjonen, som etter min mening ville gjort koden min enda mer rotete
        i= 0
        j=0
        returliste=[]
        # bruker ikke A.swap fordi det ikke er noe som skal swappes
        while i < len(A1) and j < len(A2):
            if A1[i] <= A2[j]:
                returliste.append(A1[i]) #appender til ny liste som sendes videre i rekursjonen
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
    # dette er O(n log n) pga listene deles i to i hver gjennomkjøring
    def mergeSort(A):
        if len(A)<=1:
            return A
        
        halvIndex = math.floor(len(A)/2)
        A1 = mergeSort(A[:halvIndex])
        A2 = mergeSort(A[halvIndex:])
        return merge(A1,A2,CountSwaps(A))
        
    return mergeSort(A)


