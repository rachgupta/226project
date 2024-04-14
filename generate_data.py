import random
import json


#IDs start here
#0-19
num_bi_men = 10
#20-39
num_gay_men = 10
#40-59
num_straight_men = 10
#60-79
num_bi_women = 10
#80-99
num_gay_women = 10
#100-119
num_straight_women = 10

total_participants = num_bi_men +num_gay_men+num_straight_men+num_bi_women+num_gay_women+num_straight_women

all_preferences = {}
for i in range(total_participants):
    #bi men
    if(i < num_bi_men):
        range_beginning = 0
        range_end = total_participants
    #gay men
    elif(0 <= (i - num_bi_men)  < num_gay_men):
        range_beginning = 0
        range_end = num_bi_men + num_gay_men + num_straight_men
    #straight men
    elif(0 <= (i - num_bi_men - num_gay_men) < num_straight_men):
        range_beginning = num_bi_men + num_gay_men + num_straight_men
        range_end = total_participants
    #bi women
    elif(0 <= (i - num_bi_men - num_gay_men - num_straight_men) < num_bi_women):
        range_beginning = 0
        range_end = total_participants
    #straight women
    elif(0 <= (i - num_bi_men - num_gay_men - num_straight_men - num_bi_women) < num_gay_women):
        range_beginning = 0
        range_end = num_bi_men + num_gay_men + num_straight_men
    #gay women
    elif(i < total_participants):
        range_beginning = num_bi_men + num_gay_men + num_straight_men
        range_end = total_participants
      
    preferences = []  
    for j in range(range_beginning, range_end):
        preference = random.randint(range_beginning, range_end - 1)
        while preference == i:  # Ensure they don't rank themselves
            preference = random.randint(range_beginning, range_end - 1)
        preferences.append(preference)
    all_preferences[i] = preferences
    
# Print the matches
for k in all_preferences.keys():
    print(f"ID: {k}, Preferences: {all_preferences[k]}")
    
    
with open("equal_random2.json", "w") as file:
    json.dump(all_preferences, file)