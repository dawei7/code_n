## General
### Beginner-Friendly Intuition & Strategy
The core task in **Minimum Number of Days to Disconnect Island** is to an `m x n` binary grid `grid` where `1` represents land and `0` represents water. An **island** is a maximal **4-directionally** (horizontal or vertical) connected group of `1`'s. Instead of scanning every element one by one in $O(n)$ time, this solution uses **Binary Search**. Think of looking up a word in a dictionary: you open it in the middle, see if your word comes before or after, and discard half of the remaining pages. By halving the candidate window at each step, we find the answer in fast logarithmic $O(\log n)$ time.

### Step-by-Step Execution Guide
**Step 1: Setup & Base Cases**  
We initialize an empty hash map (`dict`) to act as our fast memory bank, storing elements and their indices or frequencies.  
**Step 2: Core Processing & Traversal**  
1. Calculate `mid = (left + right) // 2`.  
2. Compare `array[mid]` with target value.  
3. Adjust `left = mid + 1` or `right = mid - 1` to halve the search window.  
**Step 3: Completion & Return**  
Bitwise operators (`&`, `|`, `^`, `<<`, `>>`) allow ultra-fast bitmask updates in $O(1)$ hardware instructions.  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Empty / Null Inputs:** Early guard checks return empty results immediately without crashing.


## Complexity detail
- **Time Complexity**: $O(RC)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(RC)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
