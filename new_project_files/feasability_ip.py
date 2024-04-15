import pulp
from pulp import LpVariable, LpProblem, LpBinary, LpMaximize
import json

def solve_stable_roommates(V, E):
    # Initialize the problem
    prob = LpProblem("StableRoommates", LpMaximize)
    
    # Decision variables
    x = LpVariable.dicts("x", ((u, v) for u in V for v in V if {u, v} in E), cat=LpBinary)

    # Objective function (no explicit objective function for feasibility problem)
    
    # Constraints
    # At most one match per agent
    for v in V:
        prob += sum(x[u, v] for u in V if {u, v} in E) <= 1, f"At most one match per agent {v}"
    
    # Compatibility constraint
    for u, v in x.keys():
        if {u, v} not in E:
            prob += x[u, v] == 0, f"Compatibility constraint {u}, {v}"
    
    # Stability constraint
    for u, v in E:
        prob += sum(x[u, i] for i in [w for w in N[u] if w != v and (u, w) in E]) \
          + sum(x[v, j] for j in [w for w in N[v] if w != u and (v, w) in E]) \
          + x[u, v] >= 1, f"Stability constraint {u}, {v}"
    
    # Solve the problem
    prob.solve()
    
    # Extract the solution
    solution = {(u, v): int(x[u, v].varValue) for u, v in x.keys()}
    
    return solution

def create_graph(preferences):
    # Initialize arrays
    edges = []
    vertices = list(preferences.keys())

    # Create edges and neighbors
    for u, prefs in preferences.items():
        for v in prefs:
            if int(u) in preferences[str(v)]:  # Check if v also prefers u
                edges.append({u, v})

    return edges, vertices

with open("equal_random2.json", "r") as file:
    preferences = json.load(file)
E,V = create_graph(preferences)
N = preferences
solution = solve_stable_roommates(V, E)
print("Solution:")
for pair, value in solution.items():
    print(pair, value)