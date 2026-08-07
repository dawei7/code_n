## General
### Beginner-Friendly Intuition & Strategy
The core task in **Eat Pizzas!** is to an integer array `pizzas` of size `n`, where $\text{pizzas}[i]$ represents the weight of the $$i^{\text{th}}$$ pizza. Every day, you eat **exactly** 4 pizzas. Due to your incredible metabolism, when you eat pizzas of weights `W`, `X`, `Y`, and `Z`, where $W \le X \le Y \le Z$,.... The algorithm processes the input using a single-pass linear iteration, maintaining state variables that update as each element is inspected to produce the result cleanly.

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
- **Time Complexity**: $O(n log n)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(n)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
