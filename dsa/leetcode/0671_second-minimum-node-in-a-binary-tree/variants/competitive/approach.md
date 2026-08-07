## General
### Beginner-Friendly Intuition & Strategy
The core task in **Second Minimum Node In a Binary Tree** is to a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly `two` or `zero` sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property $.... To avoid nested loops that slow down execution, this solution uses a **Hash Table (Hash Map / Hash Set)**. Think of a index index-cards file: instead of scanning through all cards to check if a number exists, the hash table allows us to instantly look up any value in constant $O(1)$ time.

### Step-by-Step Execution Guide
**Step 1: Setup & Initial State**  
We initialize an empty hash set (`set`) to remember elements we have already seen, ensuring we never process duplicate items.  
**Step 2: Core Processing & Decisions**  
1. Iterate sequentially through each element in the input.  
2. Apply the operational rules to update running state variables.  
3. Continue until all elements are evaluated.  
**Step 3: Completion & Result Return**  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Empty / Null Inputs:** Early guard checks return empty results immediately without crashing.
- **Single Element / Border Cases:** Loop bounds handle single items and empty inputs naturally without array index out-of-bounds exceptions.


## Complexity detail
- **Time Complexity**: $O(N)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(H)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
