import pickle
import sys

def find_group_equal_score(group_costs):
    max_score = 0
    for i in range(6):
        for j in range(6):
            score = abs(group_costs[i]-group_costs[j])
            if score > max_score:
                max_score = score
    return max_score

def find_balanced_score(group_costs):
    return max(group_costs)

def find_cost(pairings, all_preferences, groups):
    group_costs = [0, 0, 0, 0, 0, 0]
    for pair in pairings:
        person1 = pair[0]
        person2 = pair[1]
        # find rank of person 2 on person 1's list
        rank1 = all_preferences[person1].index(person2)+1
        # find rank of person 1 on person 2's list
        rank2 = all_preferences[person2].index(person1)+1
        person1_group = find_group(person1, groups) # find which group person 1 belongs to
        person2_group = find_group(person2, groups) # find which group person 2 belongs to
        # update group costs
        group_costs[person1_group-1] += rank1
        group_costs[person2_group-1] += rank2
    return group_costs

def find_group(person, groups):
    for i in range(1,7):
        if person in groups[i]:
            return i

def load_data(dict_file, group_file, matches_file):
    # unpickle all preferences
    all_preferences = {}
    with open(dict_file, 'rb') as f:
        all_preferences = pickle.load(f)

    # unpickle group list
    groups = {}
    with open(group_file, 'rb') as f:
        groups = pickle.load(f)
    
    # read pairings
    pairings = {}
    with open(matches_file, 'r') as f:
        pairings = eval(f.read())
        pairings = list(pairings)

    return all_preferences, groups, pairings

def main(dict_file, group_file, matches_file):
    all_preferences, groups, pairings = load_data(dict_file, group_file, matches_file)

    group_costs = find_cost(pairings, all_preferences, groups)
    balanced_score = find_balanced_score(group_costs)
    group_equal_score = find_group_equal_score(group_costs)
    print(f"Balanced Score = {balanced_score}")
    print(f"Group Equal Score = {group_equal_score}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python test.py <dict_file> <group_file> <matches_file>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])