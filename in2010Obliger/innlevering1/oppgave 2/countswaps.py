# her lar jeg filen stå nesten uendret slik jeg lastet den ned fra resurssiden 
class CountSwaps(list):
    swaps = 0

    def swap(self, i, j):
        self.swaps += 1
        self[i], self[j] = self[j], self[i]

    #denne skrev jeg selv for mergesort telling av swaps, men endte opp med ikke å bruke den
    def countOneSwap(self):
        self.swaps+=1