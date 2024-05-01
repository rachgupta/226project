import random
import json
import sys
import pickle
import os

#Method 1: Generating random data assuming equal numbers in all 6 groups
def generate_equal_data(num, filename):

    #IDs start here
    num_bi_men = num
    num_gay_men = num
    num_straight_men = num
    num_bi_women = num
    num_gay_women = num
    num_straight_women = num

    total_participants = num_bi_men +num_gay_men+num_straight_men+num_bi_women+num_gay_women+num_straight_women

    all_preferences = {}
    group_assignments = {1: [], 2: [], 3:[], 4: [], 5: [], 6: []}
    for i in range(1, total_participants + 1):
        group_num = 0
        #bi men
        if(i < num_bi_men + 1):
            group_num = 1
        #gay men
        elif(0 <= (i - num_bi_men - 1)  < num_gay_men):
            group_num = 2
        #straight men
        elif(0 <= (i - num_bi_men - num_gay_men - 1) < num_straight_men):
            group_num = 3
        #bi women
        elif(0 <= (i - num_bi_men - num_gay_men - num_straight_men - 1) < num_bi_women):
            group_num = 4
        #straight women
        elif(0 <= (i - num_bi_men - num_gay_men - num_straight_men - num_bi_women - 1) < num_gay_women):
            group_num = 5
        #gay women
        elif(i < total_participants + 1):
            group_num = 6
        group_assignments[group_num].append(i)
    
    for i in range(1, total_participants + 1):
        #bi men
        if(i < num_bi_men + 1):
            preferences = group_assignments[1]+group_assignments[2]+group_assignments[5]+group_assignments[4]
        #gay men
        elif(0 <= (i - num_bi_men - 1)  < num_gay_men):
            preferences = group_assignments[1]+group_assignments[2]
        #straight men
        elif(0 <= (i - num_bi_men - num_gay_men - 1) < num_straight_men):
            preferences = group_assignments[4]+group_assignments[5]
        #bi women
        elif(0 <= (i - num_bi_men - num_gay_men - num_straight_men - 1) < num_bi_women):
            preferences = group_assignments[4]+group_assignments[6]+group_assignments[3]+group_assignments[1]
        #straight women
        elif(0 <= (i - num_bi_men - num_gay_men - num_straight_men - num_bi_women - 1) < num_straight_women):
            preferences = group_assignments[1]+group_assignments[3]
        #gay women
        elif(i < total_participants + 1):
            preferences = group_assignments[4]+group_assignments[6]
        
        random.shuffle(preferences)
        if i in preferences:
            preferences.remove(i)
        all_preferences[i] = preferences
    
    #pickle the group assignments and preference dictionary for the fairness_constraints.py
    new_filename = os.path.splitext(filename)[0]
    
    group_filename = new_filename + '_group.pkl'
    with open(group_filename, 'wb') as f:
        pickle.dump(group_assignments, f)
        
    dict_filename = new_filename + '_dict.pkl'
    with open(dict_filename, 'wb') as f:
        pickle.dump(all_preferences, f)
        
    #write the preferences in the format specified by the SRI_IP github repo
    with open(filename, "w") as file:
        file.write(str(total_participants) + '\n')
        for key, value in all_preferences.items():
            line = ' '.join(map(str, value))
            file.write(line + '\n')
#Method 2: Generating random data assuming proportional numbers
def generate_proportional_data(num, filename, proportion_straight):
    ##proportion from command line
    total_lgbt = int((1-proportion_straight) * num)
    total_straight = int(proportion_straight * num)
    gay_count = total_lgbt//2
    bi_count = total_lgbt - gay_count
    straight_count = total_straight
    total_count = gay_count + bi_count + straight_count
    if total_count != num:
        straight_count += (num - total_count)
    num_gay_men = gay_count // 2
    num_gay_women = gay_count - num_gay_men
    num_bi_men = bi_count // 2
    num_bi_women = bi_count - num_bi_men
    num_straight_men = straight_count // 2
    num_straight_women = straight_count - num_straight_men
    total_participants = num
    all_preferences = {}
    group_assignments = {1: [], 2: [], 3:[], 4: [], 5: [], 6: []}
    for i in range(1, total_participants + 1):
        group_num = 0
        #bi men
        if(i < num_bi_men + 1):
            group_num = 1
        #gay men
        elif(0 <= (i - num_bi_men - 1)  < num_gay_men):
            group_num = 2
        #straight men
        elif(0 <= (i - num_bi_men - num_gay_men - 1) < num_straight_men):
            group_num = 3
        #bi women
        elif(0 <= (i - num_bi_men - num_gay_men - num_straight_men - 1) < num_bi_women):
            group_num = 4
        #straight women
        elif(0 <= (i - num_bi_men - num_gay_men - num_straight_men - num_bi_women - 1) < num_gay_women):
            group_num = 5
        #gay women
        elif(i < total_participants + 1):
            group_num = 6
        group_assignments[group_num].append(i)
    for i in range(1, total_participants + 1):
        #bi men
        if(i < num_bi_men + 1):
            preferences = group_assignments[1]+group_assignments[2]+group_assignments[5]+group_assignments[4]
        #gay men
        elif(0 <= (i - num_bi_men - 1)  < num_gay_men):
            preferences = group_assignments[1]+group_assignments[2]
        #straight men
        elif(0 <= (i - num_bi_men - num_gay_men - 1) < num_straight_men):
            preferences = group_assignments[4]+group_assignments[5]
        #bi women
        elif(0 <= (i - num_bi_men - num_gay_men - num_straight_men - 1) < num_bi_women):
            preferences = group_assignments[4]+group_assignments[6]+group_assignments[3]+group_assignments[1]
        #straight women
        elif(0 <= (i - num_bi_men - num_gay_men - num_straight_men - num_bi_women - 1) < num_straight_women):
            preferences = group_assignments[1] + group_assignments[3]
        #gay women
        elif(i < total_participants + 1):
            preferences = group_assignments[4]+group_assignments[6]
        random.shuffle(preferences)
        if i in preferences:
            preferences.remove(i)
        all_preferences[i] = preferences

    #pickling relevant files
    new_filename = os.path.splitext(filename)[0]
    group_filename = new_filename + '_group.pkl'
    with open(group_filename, 'wb') as f:  # open a text file
        pickle.dump(group_assignments, f)
        
    dict_filename = new_filename + '_dict.pkl'
    with open(dict_filename, 'wb') as f:  # open a text file
        pickle.dump(all_preferences, f)
        
    #formatting as per SRI_IP
    with open(filename, "w") as file:
        file.write(str(total_participants) + '\n')
        for key, value in all_preferences.items():
            line = ' '.join(map(str, value))
            file.write(line + '\n')    
    return
#Method 3: Generating weighted preferences based on random truth data assuming equal numbers
def generate_weighted_equal_data(num, filename):
    num_bi_men = num
    num_gay_men = num
    num_straight_men = num
    num_bi_women = num
    num_gay_women = num
    num_straight_women = num

    total_participants = num_bi_men +num_gay_men+num_straight_men+num_bi_women+num_gay_women+num_straight_women
    #now we make objective attractiveness scores from 1-100 for every person in the group
    attractiveness_scores = [random.randint(0, 100) for _ in range(total_participants)]
    
    all_preferences = {}
    group_assignments = {1: [], 2: [], 3:[], 4: [], 5: [], 6: []}
    for i in range(1, total_participants + 1):
        group_num = 0
        #bi men
        if(i < num_bi_men + 1):
            group_num = 1
        #gay men
        elif(0 <= (i - num_bi_men - 1)  < num_gay_men):
            group_num = 2
        #straight men
        elif(0 <= (i - num_bi_men - num_gay_men - 1) < num_straight_men):
            group_num = 3
        #bi women
        elif(0 <= (i - num_bi_men - num_gay_men - num_straight_men - 1) < num_bi_women):
            group_num = 4
        #straight women
        elif(0 <= (i - num_bi_men - num_gay_men - num_straight_men - num_bi_women - 1) < num_gay_women):
            group_num = 5
        #gay women
        elif(i < total_participants + 1):
            group_num = 6
        group_assignments[group_num].append(i)
        
    for i in range(1, total_participants + 1):
        #bi men
        if(i < num_bi_men + 1):
            preferences = group_assignments[1]+group_assignments[2]+group_assignments[5]+group_assignments[4]
        #gay men
        elif(0 <= (i - num_bi_men - 1)  < num_gay_men):
            preferences = group_assignments[1]+group_assignments[2]
        #straight men
        elif(0 <= (i - num_bi_men - num_gay_men - 1) < num_straight_men):
            preferences = group_assignments[4]+group_assignments[5]
        #bi women
        elif(0 <= (i - num_bi_men - num_gay_men - num_straight_men - 1) < num_bi_women):
            preferences = group_assignments[4]+group_assignments[6]+group_assignments[3]+group_assignments[1]
        #straight women
        elif(0 <= (i - num_bi_men - num_gay_men - num_straight_men - num_bi_women - 1) < num_straight_women):
            preferences = group_assignments[1]+group_assignments[3]
        #gay women
        elif(i < total_participants + 1):
            preferences = group_assignments[4]+group_assignments[6]
        
        random_floats = [random.uniform(0.75, 1.25) for _ in range(total_participants)]
        weighted_attractiveness = [float_num * int_num for float_num, int_num in zip(random_floats, attractiveness_scores)]
        sorted_prefs = sorted(preferences, key=lambda i: weighted_attractiveness[i-1])
        random.shuffle(preferences)
        if i in sorted_prefs:
            sorted_prefs.remove(i)
        all_preferences[i] = sorted_prefs
        
        new_filename = os.path.splitext(filename)[0]
    
        group_filename = new_filename + '_group.pkl'
        with open(group_filename, 'wb') as f:
            pickle.dump(group_assignments, f)
        
        dict_filename = new_filename + '_dict.pkl'
        with open(dict_filename, 'wb') as f:
            pickle.dump(all_preferences, f)
        
        with open(filename, "w") as file:
            file.write(str(total_participants) + '\n')
            for key, value in all_preferences.items():
                line = ' '.join(map(str, value))
                file.write(line + '\n')

    

#handling arguments (flag = 0 1 or 2 according to method)
if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python generate_data.py <number> <filename> <flag> <proportion_straight> ")
    else:
        if int(sys.argv[3]) == 0:
            generate_equal_data(int(sys.argv[1]), sys.argv[2])
        elif int(sys.argv[3]) == 1:
            generate_proportional_data(int(sys.argv[1]), sys.argv[2], float(sys.argv[4]))
        elif int(sys.argv[3]) == 2:
            generate_weighted_equal_data(int(sys.argv[1]), sys.argv[2])