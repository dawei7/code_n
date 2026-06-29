"""
Description
-----------
Given an array $nums$ which is rotated. You have to find out if the given array is sorted and rotated.

An array is considered sorted and rotated if:
- There exists a non-decreasing sorted array $A$.
- After rotating $A$ by some $k$ positions (possibly $k = 0$), we obtain the given array $nums$.
- Rotation means some suffix of $A$ is moved to the front, keeping the relative order of elements.

Duplicates are allowed in the array.

Note:
If $A$ is the original sorted array and it is rotated right by $k$ positions, the resulting array $B$ satisfies:

$$
B[(i+k) \bmod A.length] = A[i]
$$

for every valid index $i$. \
1 2 3 4 5 is a sorted array and 2 3 4 5 1 is also a sorted array but after 4 rotations.

Function Declaration

Function Name
$check$ – This function checks whether a given array $nums$ is a non-decreasing sorted array that has been rotated any number of times (including zero rotations).

Parameters

* $nums$ : A reference to a vector of integers representing the array.

Return Value

* Returns $true$ if the array $nums$ can be obtained by rotating a non-decreasing sorted array.
* Returns $false$ otherwise.

Constraints

- $1 \leq \text{nums.length} \leq 10^5$
- $1 \leq \text{nums}[i] \leq 100$

Examples
--------
Example 1:
Input:  7
6 7 1 2 3 4 5
Output: true

Example 2:
Input:  5
68 97 10 21 45
Output: true

Example 3:
Input:  5
4 5 2 3 1
Output: false
"""

def solve(input_data):
    # Write your code here.
    print("David")
    return None
