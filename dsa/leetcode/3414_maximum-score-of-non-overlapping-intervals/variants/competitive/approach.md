## General
### Beginner-Friendly Intuition & Strategy
The core task in **Maximum Score of Non-overlapping Intervals** is to a 2D integer array `intervals`, where $\text{intervals}[i] = [l_{i}, r_{i}, \text{weight}_{i}]$. Interval `i` starts at position $l_{i}$ and ends at $r_{i}$, and has a weight of $\text{weight}_{i}$. You can choose *up to* 4 **non-overlapping** intervals. The **score** of the c.... Instead of recalculating the exact same subproblems over and over again, this solution uses **Dynamic Programming**. We break the larger problem down into smaller overlapping subproblems, solve each subproblem once, and store its result in a memory table. When building the final answer, we simply look up previously calculated answers.

### Step-by-Step Execution Guide
**Step 1: Setup & Base Cases**  
We initialize an empty hash map (`dict`) to act as our fast memory bank, storing elements and their indices or frequencies.  
**Step 2: Core Processing & Traversal**  
1. Compare elements at `array[left]` and `array[right]`.  
2. Advance `left` or retreat `right` based on comparison rules.  
**Step 3: Completion & Return**  
Bitwise operators (`&`, `|`, `^`, `<<`, `>>`) allow ultra-fast bitmask updates in $O(1)$ hardware instructions.  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Single Element / Border Cases:** Loop bounds handle single items and empty inputs naturally.


## Complexity detail
- **Time Complexity**: $O(n log n)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(n)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
