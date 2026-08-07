## General
### Beginner-Friendly Intuition & Strategy
The core task in **Number of Same-End Substrings** is to a **0-indexed** string `s`, and a 2D array of integers `queries`, where $\text{queries}[i] = [l_{i}, r_{i}]$ indicates a substring of `s` starting from the index $l_{i}$ and ending at the index $r_{i}$ (both **inclusive**), i.e. $s[l_{i}..r_{i}]$. Instead of using nested loops that inspect every pair in $O(n^2)$ time, this algorithm uses the **Two-Pointer technique**. We place two markers (pointers)—typically one at the start (`left`) and one at the end (`right`) of a sorted array—and move them toward each other based on clear comparison rules, completing the search in a single efficient pass.

### Step-by-Step Execution Guide
**Step 1: Setup & Base Cases**  
We place `left = 0` at the start of the array and `right = len(array) - 1` at the end.  
**Step 2: Core Processing & Traversal**  
1. Compare elements at `array[left]` and `array[right]`.  
2. Advance `left` or retreat `right` based on comparison rules.  
**Step 3: Completion & Return**  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Single Element / Border Cases:** Loop bounds handle single items and empty inputs naturally.


## Complexity detail
- **Time Complexity**: $O(N + Q)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(N)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
