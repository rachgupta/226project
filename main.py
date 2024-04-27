from SRI_IP.src.model import solve_SRI, OptimalityCriteria
from SRI_IP.src.utils import read_instance
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <input file> <type> <output file>")
        return
    type = sys.argv[2]
    #    NONE = 0
    # EGALITARIAN = 1
    # FIRST_CHOICE_MAXIMAL = 2
    # RANK_MAXIMAL = 3
    # GENEROUS = 4
    # ALMOST_STABLE = 5
    pairings = solve_SRI(sys.argv[1], type)
    with open(sys.argv[3], 'w') as f:
        f.write(str(pairings))
    
    

if __name__ == "__main__":
    main()