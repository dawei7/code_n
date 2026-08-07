## General
### Beginner-Friendly Intuition & Strategy
The core task in **Count Number of Rectangles Containing Each Point** is to a 2D integer array `rectangles` where $\text{rectangles}[i] = [l_{i}, h_{i}]$ indicates that $$i^{\text{th}}$$ rectangle has a length of $l_{i}$ and a height of $h_{i}$. You are also given a 2D integer array `points` where $\text{points}[j] = [x_{j}, y_{j}]$ is a point with co.... The algorithm processes the input using a single-pass linear iteration, maintaining state variables that update as each element is inspected to produce the result cleanly.

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
- **Single Element / Border Cases:** Loop bounds handle single items and empty inputs naturally without array index out-of-bounds exceptions.


## Complexity detail
- **Time Complexity**: $O(R log R + P H log R)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(R + H)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
