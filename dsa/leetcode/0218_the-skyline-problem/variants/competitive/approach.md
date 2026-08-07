## General
### Beginner-Friendly Intuition & Strategy
The core task in **The Skyline Problem** is to A city's **skyline** is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return *the **skyline** formed by these buildings collectively*. Instead of recalculating the exact same subproblems over and over again, this solution uses **Dynamic Programming**. We break the larger problem down into smaller overlapping subproblems, solve each subproblem once, and store its result in a memory table. When building the final answer, we simply look up previously calculated answers.

### Step-by-Step Execution Guide
**Step 1: Setup & Initial State**  
We initialize an empty hash map (`dict`). This map will act as our fast memory bank, storing elements and their corresponding indices or frequencies as we scan through the data.  
**Step 2: Core Processing & Decisions**  
1. Loop through each item in the input.  
2. Calculate the required complement (e.g. `target - current_value`).  
3. Check if the complement is already in our hash map. If yes, we immediately return the matching pair!  
4. If no, store the current value and index in the hash map and move to the next item.  
**Step 3: Completion & Result Return**  
Bitwise operators (`&`, `|`, `^`, `<<`, `>>`) allow ultra-fast bitmask updates for set operations in $O(1)$ hardware instructions.  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Single Element / Border Cases:** Loop bounds handle single items and empty inputs naturally without array index out-of-bounds exceptions.


## Complexity detail
- **Time Complexity**: $O(n \log n)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(n)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
