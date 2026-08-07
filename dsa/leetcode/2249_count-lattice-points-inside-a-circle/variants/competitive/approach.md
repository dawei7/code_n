## General
### Beginner-Friendly Intuition & Strategy
The core task in **Count Lattice Points Inside a Circle** is to a 2D integer array `circles` where $\text{circles}[i] = [x_{i}, y_{i}, r_{i}]$ represents the center $(x_{i}, y_{i})$ and radius $r_{i}$ of the $$i^{\text{th}}$$ circle drawn on a grid, return *the **number of lattice points** **that are present inside **at least one** circle*. To avoid nested loops that slow down execution, this solution uses a **Hash Table (Hash Map / Hash Set)**. Think of a index index-cards file: instead of scanning through all cards to check if a number exists, the hash table allows us to instantly look up any value in constant $O(1)$ time.

### Step-by-Step Execution Guide
**Step 1: Setup & Base Cases**  
We initialize an empty hash map (`dict`) to act as our fast memory bank, storing elements and their indices or frequencies.  
**Step 2: Core Processing & Traversal**  
1. Loop through each item in the input.  
2. Calculate target complement.  
3. Check if complement exists in hash map for $O(1)$ match.  
4. Store current value in hash map if not found.  
**Step 3: Completion & Return**  
Bitwise operators (`&`, `|`, `^`, `<<`, `>>`) allow ultra-fast bitmask updates in $O(1)$ hardware instructions.  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Single Element / Border Cases:** Loop bounds handle single items and empty inputs naturally.


## Complexity detail
- **Time Complexity**: $O(sum r_i^2)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(P)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
