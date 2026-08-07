## General
### Beginner-Friendly Intuition & Strategy
The core task in **Random Point in Non-overlapping Rectangles** is to an array of non-overlapping axis-aligned rectangles `rects` where $\text{rects}[i] = [a_{i}, b_{i}, x_{i}, y_{i}]$ indicates that $(a_{i}, b_{i})$ is the bottom-left corner point of the $$i^{\text{th}}$$ rectangle and $(x_{i}, y_{i})$ is the top-right corner point of the $$i^{.... The algorithm processes the input using a single-pass linear iteration, maintaining state variables that update as each element is inspected to produce the result cleanly.

### Step-by-Step Execution Guide
**Step 1: Setup & Initial State**  
We set up tracking variables (accumulators, counters, or pointers) to hold intermediate results as we process the input.  
**Step 2: Core Processing & Decisions**  
1. Iterate sequentially through each element in the input.  
2. Apply the operational rules to update running state variables.  
3. Continue until all elements are evaluated.  
**Step 3: Completion & Result Return**  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Large Numbers:** Modulo arithmetic prevents numerical overflow.
- **Single Element / Border Cases:** Loop bounds handle single items and empty inputs naturally without array index out-of-bounds exceptions.


## Complexity detail
- **Time Complexity**: $O(r + d \log r)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(r + d)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
