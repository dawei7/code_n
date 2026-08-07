## General
### Beginner-Friendly Intuition & Strategy
The core task in **Merge k Sorted Lists** is to an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order. To dynamically keep track of the minimum or maximum value without sorting the entire array repeatedly, this solution uses a **Min/Max Heap (Priority Queue)**. It allows us to insert elements and extract the smallest/largest value in fast logarithmic $O(\log k)$ time.

### Step-by-Step Execution Guide
**Step 1: Setup & Initial State**  
We set up tracking variables (accumulators, counters, or pointers) to hold intermediate results as we process the input.  
**Step 2: Core Processing & Decisions**  
1. Iterate sequentially through each element in the input.  
2. Apply the operational rules to update running state variables.  
3. Continue until all elements are evaluated.  
**Step 3: Completion & Result Return**  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Single Element / Border Cases:** Loop bounds handle single items and empty inputs naturally without array index out-of-bounds exceptions.


## Complexity detail
- **Time Complexity**: $O(N \log k)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(k)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
