def sort(A):
    # Do insertion sort here. Use the Sorter's comparison- and swap
    # methods for automatically counting the swaps and comparisons.

    # Use A.swap(i, j) to swap the values at two indices i and j. The swap is
    # counted, when using this method. Comparisons are counted automatically.

    #dette er O(n^2)
    for i in range(1, len(A)):
        j=i
        while j>0 and A[j-1]> A[j]:
            #bruker swap metoden som fra klassen som fulgte med i kodeskjelettet fra resursiden
            A.swap(j-1, j)
            j=j-1

    return A