def irvings_algorithm(preferences):
    unmatched = set(preferences.keys())
    proposals = {}
    while unmatched:
        proposer = unmatched.pop()
        proposer_prefs = preferences[proposer]
        for preferred in proposer_prefs:
            if preferred not in proposals:
                proposals[preferred] = proposer
                break
            else:
                current_suitor = proposals[preferred]
                preferred_prefs = preferences[preferred]
                if preferred_prefs.index(proposer) < preferred_prefs.index(current_suitor):
                    unmatched.add(current_suitor)
                    proposals[preferred] = proposer
                    break
                else:
                    # Remove proposer from the preference list of preferred
                    proposer_prefs.remove(preferred)
        else:
            # If no match was found, add proposer back to unmatched
            unmatched.add(proposer)

    return proposals


# Example preferences dictionary where keys are individuals and values are preference lists
preferences = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C', 'A']
}

# Execute the algorithm
matches = irvings_algorithm(preferences)

# Print the matches
for partner, match in matches.items():
    print(f"{partner} is matched with {match}")
