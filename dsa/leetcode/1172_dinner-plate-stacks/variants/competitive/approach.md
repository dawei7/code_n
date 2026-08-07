## General
### Beginner-Friendly Intuition & Strategy
The core task in **Dinner Plate Stacks** is to You have an infinite number of stacks arranged in a row and numbered (left to right) from `0`, each of the stacks has the same maximum capacity. To dynamically keep track of the minimum or maximum value without sorting the entire array repeatedly, this solution uses a **Min/Max Heap (Priority Queue)**. It allows us to insert elements and extract the smallest/largest value in fast logarithmic $O(\log k)$ time.

### Step-by-Step Execution Guide
**Step 1: Setup & Base Cases**  
We set up tracking variables (accumulators, counters, or pointers) to hold intermediate results.  
**Step 2: Core Processing & Traversal**  
1. Iterate sequentially through each element.  
2. Apply operational rules to update state variables.  
**Step 3: Completion & Return**  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Empty / Null Inputs:** Early guard checks return empty results immediately without crashing.


## Complexity detail
- **Time Complexity**: $O(m\log s)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(v+s)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
