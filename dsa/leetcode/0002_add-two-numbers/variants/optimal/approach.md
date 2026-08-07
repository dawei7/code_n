## General
### Beginner-Friendly Intuition & Strategy
The core task in **Add Two Numbers** is to two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. The input is a **Singly-Linked List** where elements are connected sequentially by pointers (`val`, `next`). The algorithm iterates through the list using pointer manipulation, updating linkages step-by-step without requiring extra array allocations.

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
- **Time Complexity**: $O(\max(n, m))$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(\max(n, m))$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
