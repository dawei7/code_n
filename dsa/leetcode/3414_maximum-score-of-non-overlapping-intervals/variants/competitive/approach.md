## General
### Beginner-Friendly Intuition & Strategy
The core task in **Maximum Score of Non-overlapping Intervals** is to a 2D integer array `intervals`, where $\text{intervals}[i] = [l_{i}, r_{i}, \text{weight}_{i}]$. Interval `i` starts at position $l_{i}$ and ends at $r_{i}$, and has a weight of $\text{weight}_{i}$. You can choose *up to* 4 **non-overlapping** intervals. The **score** of the c.... Instead of recalculating the exact same subproblems over and over again, this solution uses **Dynamic Programming**. We break the larger problem down into smaller overlapping subproblems, solve each subproblem once, and store its result in a memory table. When building the final answer, we simply look up previously calculated answers.

### Step-by-Step Execution Guide
**Step 1: Setup & Initial State**  
We initialize an empty hash map (`dict`). This map will act as our fast memory bank, storing elements and their corresponding indices or frequencies as we scan through the data.  
**Step 2: Core Processing & Decisions**  
1. Inspect the elements at `array[left]` and `array[right]`.  
2. Compute the current metric (e.g. sum or container area).  
3. Compare against our target requirement.  
4. Advance `left += 1` or retreat `right -= 1` depending on whether we need a larger or smaller value.  
**Step 3: Completion & Result Return**  
Bitwise operators (`&`, `|`, `^`, `<<`, `>>`) allow ultra-fast bitmask updates for set operations in $O(1)$ hardware instructions.  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Single Element / Border Cases:** Loop bounds handle single items and empty inputs naturally without array index out-of-bounds exceptions.


## Complexity detail
- **Time Complexity**: $O(n log n)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(n)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
