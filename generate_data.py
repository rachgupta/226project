import random
import json
import sys
import pickle
import os
def generate_random_data(num, filename):

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
        elif(0 <= (i - num_bi_men - num_gay_men - num_straight_men - num_bi_women - 1) < num_gay_women):
            preferences = group_assignments[1]+group_assignments[3]
        #gay women
        elif(i < total_participants + 1):
            preferences = group_assignments[4]+group_assignments[6]
        random.shuffle(preferences)
        if i in preferences:
            preferences.remove(i)
        all_preferences[i] = preferences
    
    new_filename = os.path.splitext(filename)[0]
    
    group_filename = new_filename + '_group.pkl'
    with open(group_filename, 'wb') as f:  # open a text file
        pickle.dump(group_assignments, f)
        
    dict_filename = new_filename + '_dict.pkl'
    with open(dict_filename, 'wb') as f:  # open a text file
        pickle.dump(all_preferences, f)
        
    with open(filename, "w") as file:
        # Iterate over the dictionary items
        file.write(str(total_participants) + '\n')
        for key, value in all_preferences.items():
            # Convert the array to a space-separated string
            line = ' '.join(map(str, value))
            # Write the formatted string to the file
            file.write(line + '\n')

def generate_proportional_data(num, filename):
    ##PROPORTIONS ESTIMATED FROM 2021 DATA
    ##assumed 10% gay or bisexual
    ##assumed 5% homosexual, 5% bisexual, 90% straight
    total_lgbt = int(0.1 * num)
    total_straight = int(0.9 * num)
    gay_count = int(0.05 * num)
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
        elif(0 <= (i - num_bi_men - num_gay_men - num_straight_men - num_bi_women - 1) < num_gay_women):
            preferences = group_assignments[1]+group_assignments[3]
        #gay women
        elif(i < total_participants + 1):
            preferences = group_assignments[4]+group_assignments[6]
        random.shuffle(preferences)
        if i in preferences:
            preferences.remove(i)
        all_preferences[i] = preferences
        group_num = 0
        #bi men
        if(i < num_bi_men + 1):
            range_beginning = 1
            range_end = total_participants + 1
            group_num = 1
        #gay men
        elif(0 <= (i - num_bi_men - 1)  < num_gay_men):
            range_beginning = 1
            range_end = num_bi_men + num_gay_men + num_straight_men + 1
            group_num = 2
        #straight men
        elif(0 <= (i - num_bi_men - num_gay_men - 1) < num_straight_men):
            range_beginning = num_bi_men + num_gay_men + num_straight_men + 1
            range_end = total_participants + 1
            group_num = 3
        #bi women
        elif(0 <= (i - num_bi_men - num_gay_men - num_straight_men - 1) < num_bi_women):
            range_beginning = 1
            range_end = total_participants + 1
            group_num = 4
        #straight women
        elif(0 <= (i - num_bi_men - num_gay_men - num_straight_men - num_bi_women - 1) < num_gay_women):
            range_beginning = 1
            range_end = num_bi_men + num_gay_men + num_straight_men + 1
            group_num = 5
        #gay women
        elif(i < total_participants + 1):
            range_beginning = num_bi_men + num_gay_men + num_straight_men + 1
            range_end = total_participants + 1
            group_num = 6
        
        preferences = list(range(range_beginning, range_end))
        random.shuffle(preferences)
        if i in preferences:
            preferences.remove(i)
        all_preferences[i] = preferences
        group_assignments[group_num].append(i)

    
    new_filename = os.path.splitext(filename)[0]
    group_filename = new_filename + '_group.pkl'
    with open(group_filename, 'wb') as f:  # open a text file
        pickle.dump(group_assignments, f)
        
    dict_filename = new_filename + '_dict.pkl'
    with open(dict_filename, 'wb') as f:  # open a text file
        pickle.dump(all_preferences, f)
        
    with open(filename, "w") as file:
        # Iterate over the dictionary items
        file.write(str(total_participants) + '\n')
        for key, value in all_preferences.items():
            # Convert the array to a space-separated string
            line = ' '.join(map(str, value))
            # Write the formatted string to the file
            file.write(line + '\n')
    
    return
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate_data.py <number> <filename> <flag>")
    else:
        if int(sys.argv[3]) == 0:
            generate_random_data(int(sys.argv[1]), sys.argv[2])
        elif int(sys.argv[3]) == 1:
            generate_proportional_data(int(sys.argv[1]), sys.argv[2])