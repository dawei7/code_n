## General
### Beginner-Friendly Intuition & Strategy
The core task in **Number of Ways to Paint N × 3 Grid** is to You have a `grid` of size `n x 3` and you want to paint each cell of the grid with exactly one of the three colors: **Red**, **Yellow,** or **Green** while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides ha.... To avoid nested loops that slow down execution, this solution uses a **Hash Table (Hash Map / Hash Set)**. Think of a index index-cards file: instead of scanning through all cards to check if a number exists, the hash table allows us to instantly look up any value in constant $O(1)$ time.

### Step-by-Step Execution Guide
**Step 1: Setup & Initial State**  
We initialize an empty hash map (`dict`). This map will act as our fast memory bank, storing elements and their corresponding indices or frequencies as we scan through the data.  
**Step 2: Core Processing & Decisions**  
1. Loop through each item in the input.  
2. Calculate the required complement (e.g. `target - current_value`).  
3. Check if the complement is already in our hash map. If yes, we immediately return the matching pair!  
4. If no, store the current value and index in the hash map and move to the next item.  
**Step 3: Completion & Result Return**  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Large Numbers:** Modulo arithmetic prevents numerical overflow.
- **Single Element / Border Cases:** Loop bounds handle single items and empty inputs naturally without array index out-of-bounds exceptions.


## Complexity detail
- **Time Complexity**: $O(n)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(1)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
