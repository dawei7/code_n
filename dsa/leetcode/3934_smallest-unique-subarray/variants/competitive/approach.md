## General
### Beginner-Friendly Intuition & Strategy
The core task in **Smallest Unique Subarray** is to an integer array `nums`. Instead of scanning every element one by one in $O(n)$ time, this solution uses **Binary Search**. Think of looking up a word in a dictionary: you open it in the middle, see if your word comes before or after, and discard half of the remaining pages. By halving the candidate window at each step, we find the answer in fast logarithmic $O(\log n)$ time.

### Step-by-Step Execution Guide
**Step 1: Setup & Initial State**  
We initialize an empty hash map (`dict`). This map will act as our fast memory bank, storing elements and their corresponding indices or frequencies as we scan through the data.  
**Step 2: Core Processing & Decisions**  
1. Calculate `mid = (left + right) // 2`.  
2. Compare `array[mid]` with our target value.  
3. If `array[mid] == target`, we have found our answer!  
4. If `array[mid] < target`, the target must lie in the right half, so we set `left = mid + 1`.  
5. If `array[mid] > target`, the target must lie in the left half, so we set `right = mid - 1`.  
6. Repeat until `left > right`.  
**Step 3: Completion & Result Return**  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Large Numbers:** Modulo arithmetic prevents numerical overflow.
- **Single Element / Border Cases:** Loop bounds handle single items and empty inputs naturally without array index out-of-bounds exceptions.


## Complexity detail
- **Time Complexity**: $O(n)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(n)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
