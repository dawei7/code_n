## General
### Beginner-Friendly Intuition & Strategy
The core task in **Perfect Rectangle** is to an array `rectangles` where $\text{rectangles}[i] = [x_{i}, y_{i}, a_{i}, b_{i}]$ represents an axis-aligned rectangle. The bottom-left point of the rectangle is $(x_{i}, y_{i})$ and the top-right point of it is $(a_{i}, b_{i})$. Instead of using nested loops that inspect every pair in $O(n^2)$ time, this algorithm uses the **Two-Pointer technique**. We place two markers (pointers)—typically one at the start (`left`) and one at the end (`right`) of a sorted array—and move them toward each other based on clear comparison rules, completing the search in a single efficient pass.

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
- **Time Complexity**: $O(r)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(r)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
