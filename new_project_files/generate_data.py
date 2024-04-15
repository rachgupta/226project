import random
import json


#IDs start here
#0-19
num_bi_men = 5
#20-39
num_gay_men = 5
#40-59
num_straight_men = 5
#60-79
num_bi_women = 5
#80-99
num_gay_women = 5
#100-119
num_straight_women = 5

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
print(all_preferences)
    
with open("random_5each.txt", "w") as file:
    # Iterate over the dictionary items
    file.write(str(total_participants) + '\n')
    for key, value in all_preferences.items():
        # Convert the array to a space-separated string
        line = ' '.join(map(str, value))
        # Write the formatted string to the file
        file.write(line + '\n')