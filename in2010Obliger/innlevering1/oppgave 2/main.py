import sort_runner
import sys

# her lar jeg filen stå uendret slik jeg lastet den ned fra resurssiden 
def main(filename):
    with open(filename, 'r') as f:
        A = [int(x) for x in f.readlines()]
    sort_runner.run_algs_part1(A, filename)
    sort_runner.run_algs_part2(A, filename)

if __name__ == '__main__':
    main(sys.argv[1])