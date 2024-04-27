from SRI_IP.src.model import solve_SRI, OptimalityCriteria
from SRI_IP.src.utils import read_instance
import sys
import pickle

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
    all_preferences = {}
    groups = {}
    with open('random_data_dict.pkl', 'rb') as f:
        all_preferences = pickle.load(f)

    with open('random_data_group.pkl', 'rb') as f:
        groups = pickle.load(f)
    
    with open(sys.argv[3], 'w') as f:
        f.write(str(pairings))
    
    cost(pairings, all_preferences, groups)
    
def cost(pairings, all_preferences, groups):
    group_costs = [0, 0, 0, 0, 0, 0]
    for pair in pairings:
        person1 = pair[0]
        person2 = pair[1]
        # find rank of person 2 on person 1's list
        rank1 = all_preferences[person1].index(person2)
        # find rank of person 1 on person 2's list
        rank2 = all_preferences[person2].index(person1)
        person1_group = find_group(person1, groups)-1 # find which group person 1 belongs to
        person2_group = find_group(person1, groups)-1 # find which group person 2 belongs to
        # update group costs
        group_costs[person1_group] += rank1
        group_costs[person2_group] += rank2
    return group_costs

def find_group(person, groups):
    for i in range(1,7):
        if person in groups[i]:
            return i

if __name__ == "__main__":
    main()