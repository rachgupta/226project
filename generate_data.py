import random
import json
import sys
def generate_data(num, filename):

    #IDs start here
    #0-19
    num_bi_men = num
    num_gay_men = num
    num_straight_men = num
    num_bi_women = num
    num_gay_women = num
    num_straight_women = num

    total_participants = num_bi_men +num_gay_men+num_straight_men+num_bi_women+num_gay_women+num_straight_women

    all_preferences = {}
    for i in range(1, total_participants):
        #bi men
        if(i < num_bi_men + 1):
            range_beginning = 1
            range_end = total_participants + 1
        #gay men
        elif(0 <= (i - num_bi_men - 1)  < num_gay_men):
            range_beginning = 1
            range_end = num_bi_men + num_gay_men + num_straight_men + 1
        #straight men
        elif(0 <= (i - num_bi_men - num_gay_men - 1) < num_straight_men):
            range_beginning = num_bi_men + num_gay_men + num_straight_men + 1
            range_end = total_participants + 1
        #bi women
        elif(0 <= (i - num_bi_men - num_gay_men - num_straight_men - 1) < num_bi_women):
            range_beginning = 1
            range_end = total_participants + 1
        #straight women
        elif(0 <= (i - num_bi_men - num_gay_men - num_straight_men - num_bi_women - 1) < num_gay_women):
            range_beginning = 1
            range_end = num_bi_men + num_gay_men + num_straight_men + 1
        #gay women
        elif(i < total_participants + 1):
            range_beginning = num_bi_men + num_gay_men + num_straight_men + 1
            range_end = total_participants + 1
        
        preferences = list(range(range_beginning, range_end))
        random.shuffle(preferences)
        if i in preferences:
            preferences.remove(i)
        all_preferences[i] = preferences
        
    with open(filename, "w") as file:
        # Iterate over the dictionary items
        file.write(str(total_participants) + '\n')
        for key, value in all_preferences.items():
            # Convert the array to a space-separated string
            line = ' '.join(map(str, value))
            # Write the formatted string to the file
            file.write(line + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_data.py <number> <filename>")
    else:
        generate_data(int(sys.argv[1]), sys.argv[2])