## General
Given a list of `accounts` where each element $\text{accounts}[i]$ is a list of strings, where the first element $\text{accounts}[i][0]$ is a name, and the rest of the elements are **emails** representing emails of the account, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access.

## Complexity detail
- **Time Complexity**: $O(E \log E)$ — Operation count bound.
- **Space Complexity**: $O(E)$ — Auxiliary memory allocation bound.
