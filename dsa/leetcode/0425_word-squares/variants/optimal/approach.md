## General
### Beginner-Friendly Intuition & Strategy
The core task in **Word Squares** is to an array of **unique** strings `words`, return *all the ***<a href="https://en.wikipedia.org/wiki/Word_square" target="_blank">word squares</a>*** you can build from *`words`. The same word from `words` can be used **multiple times**. You can return the answer in **any order**. The algorithm processes the input using a single-pass linear iteration, maintaining state variables that update as each element is inspected to produce the result cleanly.

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
- **Empty / Null Inputs:** Early guard checks return empty results immediately without crashing.
- **Single Element / Border Cases:** Loop bounds handle single items and empty inputs naturally without array index out-of-bounds exceptions.


## Complexity detail
- **Time Complexity**: $O(NL^2 + PL)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(NL^2 + L^2)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
