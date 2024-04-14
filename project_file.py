import json
def SRI(preferences):
    # to find approximation for NP-hard problem
    return {}

with open("equal_random1.json", "r") as file:
    all_preferences = json.load(file)

# Execute the algorithm
matches = SRI(all_preferences)

# Print the matches
for partner, match in matches.items():
    print(f"{partner} is matched with {match}")
