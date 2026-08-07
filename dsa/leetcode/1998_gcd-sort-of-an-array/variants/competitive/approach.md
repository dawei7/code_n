## General
### Beginner-Friendly Intuition & Strategy
The core task in **GCD Sort of an Array** is to an integer array `nums`, and you can perform the following operation **any** number of times on `nums`:. The algorithm processes the input using a single-pass linear iteration, maintaining state variables that update as each element is inspected to produce the result cleanly.

### Step-by-Step Execution Guide
**Step 1: Setup & Base Cases**  
We set up tracking variables (accumulators, counters, or pointers) to hold intermediate results.  
**Step 2: Core Processing & Traversal**  
1. Iterate sequentially through each element.  
2. Apply operational rules to update state variables.  
**Step 3: Completion & Return**  
Bitwise operators (`&`, `|`, `^`, `<<`, `>>`) allow ultra-fast bitmask updates in $O(1)$ hardware instructions.  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Empty / Null Inputs:** Early guard checks return empty results immediately without crashing.


## Complexity detail
- **Time Complexity**: $O(M\log\log M+N\log M+N\log N)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(M)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
