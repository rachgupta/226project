# 226 Final Project
## Requirements
pip install gurobipy
Gurobipy Academic License
## Background:
The Stable Marriage Problem is a classic problem in mathematics and computer science that deals with finding a stable matching between two equally sized sets of elements, typically represented as men and women. The goal is to pair each element from the first set with exactly one element from the second set in such a way that there are no two elements, each from different sets, who would both prefer each other over their current partners.

Gale and Shapley first introduced the Stable Marriage Problem in 1962. In the Gale-Shapley algorithm, each member of one group proposes to members of the other group in order of their preference, and each member from the other group either accepts the proposal or rejects it, depending on their own preferences. The algorithm proceeds iteratively until each member has been either accepted or rejected, resulting in a stable matching. Irving's algorithm is an enhancement of the Gale-Shapley algorithm that aims to improve its efficiency by reducing the number of proposals made during the execution of the algorithm.

## Research Question:
How can we adapt the stable marriage problem to accommodate same-sex relationships through a reduction to a constrained version of the stable roommates problem, utilizing incomplete preference lists to account for individuals' sexual orientations?

## Algorithm:
Since SRI is NP-Hard, we are using constaint programming and integer programming from [this paper](https://arxiv.org/pdf/2110.02555.pdf) to solve Stable Queer Marriage Problem using a reduction to the Stable Roommates with Incomplete Lists Problem. 
