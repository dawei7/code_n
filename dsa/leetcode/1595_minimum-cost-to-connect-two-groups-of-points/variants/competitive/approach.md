## General
### Beginner-Friendly Intuition & Strategy
The core task in **Minimum Cost to Connect Two Groups of Points** is to two groups of points where the first group has $\text{size}_{1}$ points, the second group has $\text{size}_{2}$ points, and $\text{size}_{1} \ge \text{size}_{2}$. Instead of recalculating the exact same subproblems over and over again, this solution uses **Dynamic Programming**. We break the larger problem down into smaller overlapping subproblems, solve each subproblem once, and store its result in a memory table. When building the final answer, we simply look up previously calculated answers.

### Step-by-Step Execution Guide
**Step 1: Setup & Base Cases**  
We create a Dynamic Programming table and initialize known base cases.  
**Step 2: Core Processing & Traversal**  
1. Iterate sequentially through each element.  
2. Apply operational rules to update state variables.  
**Step 3: Completion & Return**  
Bitwise operators (`&`, `|`, `^`, `<<`, `>>`) allow ultra-fast bitmask updates in $O(1)$ hardware instructions.  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Single Element / Border Cases:** Loop bounds handle single items and empty inputs naturally.


## Complexity detail
- **Time Complexity**: $O(mn2^n)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(m2^n)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
