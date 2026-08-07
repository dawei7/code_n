## General
### Beginner-Friendly Intuition & Strategy
The core task in **Delete Nodes From Linked List Present in Array** is to an array of integers `nums` and the `head` of a linked list. Return the `head` of the modified linked list after **removing** all nodes from the linked list that have a value that exists in `nums`. The input is a **Singly-Linked List** where nodes are linked sequentially (`val`, `next`). The algorithm iterates through the list using pointer manipulation, updating linkages or traversing step-by-step without requiring extra array allocations.

### Step-by-Step Execution Guide
**Step 1: Setup & Base Cases**  
We set up tracking pointers (e.g. `prev`, `curr`, `head`) to navigate node linkages safely.  
**Step 2: Core Processing & Traversal**  
1. Advance through node linkages using `curr = curr.next`.  
2. Perform values computation or link reversals.  
3. Continue until `curr` reaches `None`.  
**Step 3: Completion & Return**  
When processing finishes, the algorithm outputs the final validated solution.

### Why This Handles Edge Cases Gracefully
- **Empty or Single-Node Lists:** Pointer checks (`while head:`) handle empty or single-element lists without throwing exceptions.


## Complexity detail
- **Time Complexity**: $O(m + n)$ — Detailed Analysis: The time complexity corresponds directly to the total number of operations required by the step-by-step execution loop described above.
- **Space Complexity**: $O(m)$ — Detailed Analysis: The space complexity reflects the auxiliary memory allocated for tracking structures, recursion stack depth, or hash maps during processing.
