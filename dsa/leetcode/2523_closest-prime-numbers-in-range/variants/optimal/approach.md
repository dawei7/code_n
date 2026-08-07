## General
### Beginner-Friendly Intuition & Strategy
The core task in **Closest Prime Numbers in Range** is to two positive integers `left` and `right`, find the two integers `num1` and `num2` such that:. Instead of using nested loops that inspect every pair in $O(n^2)$ time, this algorithm uses the **Two-Pointer technique**. We place two markers (pointers)—typically one at the start (`left`) and one at the end (`right`) of a sorted array—and move them toward each other based on clear comparison rules, completing the search in a single efficient pass.

### Step-by-Step Execution Guide
**Step 1: Setup & Base Cases**  
We place `left = 0` at the start of the array and `right = len(array) - 1` at the end.  
**Step 2: Core Processing & Traversal**  
1. Compare elements at `array[left]` and `array[right]`.  
2. Advance `left` or retreat `right` based on comparison rules.  
**Step 3: Completion & Return**  
Python's walrus operator (`:=`) is used to assign and evaluate variables inline, streamlining the loop.  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Empty / Null Inputs:** Early guard checks return empty results immediately without crashing.


## Complexity detail
- **Time Complexity**: $O(R log log R)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(R)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
