## General
### Beginner-Friendly Intuition & Strategy
The core task in **Count Artifacts That Can Be Extracted** is to There is an `n x n` **0-indexed** grid with some artifacts buried in it. You are given the integer `n` and a **0-indexed **2D integer array `artifacts` describing the positions of the rectangular artifacts where $\text{artifacts}[i] = [\text{r1}_{i}, \text{c1}_{i}, \text{r2}_{.... To avoid nested loops that slow down execution, this solution uses a **Hash Table (Hash Map / Hash Set)**. Think of a index index-cards file: instead of scanning through all cards to check if a number exists, the hash table allows us to instantly look up any value in constant $O(1)$ time.

### Step-by-Step Execution Guide
**Step 1: Setup & Base Cases**  
We initialize an empty hash map (`dict`) to act as our fast memory bank, storing elements and their indices or frequencies.  
**Step 2: Core Processing & Traversal**  
1. Loop through each item in the input.  
2. Calculate target complement.  
3. Check if complement exists in hash map for $O(1)$ match.  
4. Store current value in hash map if not found.  
**Step 3: Completion & Return**  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Empty / Null Inputs:** Early guard checks return empty results immediately without crashing.


## Complexity detail
- **Time Complexity**: $O(a + d)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(d)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
