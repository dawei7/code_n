## General
### Beginner-Friendly Intuition & Strategy
The core task in **Range Sum of Sorted Subarray Sums** is to the array `nums` consisting of `n` positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of $n * (n + 1) / 2$ numbers. Instead of using nested loops that inspect every pair in $O(n^2)$ time, this algorithm uses the **Two-Pointer technique**. We place two markers (pointers)—typically one at the start (`left`) and one at the end (`right`) of a sorted array—and move them toward each other based on clear comparison rules, completing the search in a single efficient pass.

### Step-by-Step Execution Guide
**Step 1: Setup & Initial State**  
We initialize an empty hash map (`dict`). This map will act as our fast memory bank, storing elements and their corresponding indices or frequencies as we scan through the data.  
**Step 2: Core Processing & Decisions**  
1. Inspect the elements at `array[left]` and `array[right]`.  
2. Compute the current metric (e.g. sum or container area).  
3. Compare against our target requirement.  
4. Advance `left += 1` or retreat `right -= 1` depending on whether we need a larger or smaller value.  
**Step 3: Completion & Result Return**  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Large Numbers:** Modulo arithmetic prevents numerical overflow.
- **Single Element / Border Cases:** Loop bounds handle single items and empty inputs naturally without array index out-of-bounds exceptions.


## Complexity detail
- **Time Complexity**: $O(n \log S)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(n)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
