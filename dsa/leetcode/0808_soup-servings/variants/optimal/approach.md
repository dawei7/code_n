## General
### Beginner-Friendly Intuition & Strategy
The core task in **Soup Servings** is to You have two soups, **A** and **B**, each starting with `n` mL. On every turn, one of the following four serving operations is chosen *at random*, each with probability `0.25` **independent** of all previous turns:. Instead of recalculating the exact same subproblems over and over again, this solution uses **Dynamic Programming**. We break the larger problem down into smaller overlapping subproblems, solve each subproblem once, and store its result in a memory table. When building the final answer, we simply look up previously calculated answers.

### Step-by-Step Execution Guide
**Step 1: Setup & Initial State**  
We create a Dynamic Programming table (array or matrix) and fill in the known base cases (e.g. 0 for empty sets or 1 for single steps).  
**Step 2: Core Processing & Decisions**  
1. Iterate sequentially through each element in the input.  
2. Apply the operational rules to update running state variables.  
3. Continue until all elements are evaluated.  
**Step 3: Completion & Result Return**  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Single Element / Border Cases:** Loop bounds handle single items and empty inputs naturally without array index out-of-bounds exceptions.


## Complexity detail
- **Time Complexity**: $O(s^2)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(s^2)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
