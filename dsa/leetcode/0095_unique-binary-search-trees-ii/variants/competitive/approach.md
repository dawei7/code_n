## General
### Beginner-Friendly Intuition & Strategy
The core task in **Unique Binary Search Trees II** is to an integer `n`, return *all the structurally unique **BST'**s (binary search trees), which has exactly *`n`* nodes of unique values from* `1` *to* `n`. Return the answer in **any order**. The data is structured as a **Binary Tree** made of connected nodes. The algorithm traverses the tree recursively, visiting each node's left and right child pointers (`val`, `left`, `right`) to inspect or transform the tree structure.

### Step-by-Step Execution Guide
**Step 1: Setup & Initial State**  
We initialize a double-ended queue (`collections.deque`) to keep track of active window bounds or nodes waiting to be processed in order.  
**Step 2: Core Processing & Decisions**  
1. Iterate sequentially through each element in the input.  
2. Apply the operational rules to update running state variables.  
3. Continue until all elements are evaluated.  
**Step 3: Completion & Result Return**  
Bitwise operators (`&`, `|`, `^`, `<<`, `>>`) allow ultra-fast bitmask updates for set operations in $O(1)$ hardware instructions.  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Single Element / Border Cases:** Loop bounds handle single items and empty inputs naturally without array index out-of-bounds exceptions.


## Complexity detail
- **Time Complexity**: $O(n C_n)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(n C_n)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
