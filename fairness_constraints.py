import sys

def cost():
    if len(sys.argv) != 4:
        print("Usage: python main.py <input file> <type> <output file>")
        return
    type = sys.argv[2]
    return 0