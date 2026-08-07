## General
Given a string array `features` where $\text{features}[i]$ is a single word that represents the name of a feature of the latest product you are working on. You have made a survey where users have reported which features the..., the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(W+F\log F)$ — Operation count bound.
- **Space Complexity**: $O(F+U)$ — Auxiliary memory allocation bound.
