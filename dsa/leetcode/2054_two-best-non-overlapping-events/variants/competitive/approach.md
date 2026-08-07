## General
### Beginner-Friendly Intuition & Strategy
The core task in **Two Best Non-Overlapping Events** is to a **0-indexed** 2D integer array of `events` where $\text{events}[i] = [\text{startTime}_{i}, \text{endTime}_{i}, \text{value}_{i}]$. The $$i^{\text{th}}$$ event starts at $\text{startTime}_{i}$_ and ends at $\text{endTime}_{i}$, and if you attend this event, you will receive .... Instead of using nested loops that inspect every pair in $O(n^2)$ time, this algorithm uses the **Two-Pointer technique**. We place two markers (pointers)—typically one at the start (`left`) and one at the end (`right`) of a sorted array—and move them toward each other based on clear comparison rules, completing the search in a single efficient pass.

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
- **Time Complexity**: $O(n\log n)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(n)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
