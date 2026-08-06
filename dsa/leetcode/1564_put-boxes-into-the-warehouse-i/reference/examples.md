## Examples

**Example 1**

- **Input:** `boxes = [4,3,4,1], warehouse = [5,3,3,4,1]`
- **Output:** `3`
- **Explanation:** First place box 1 in room 4 (height 1). Then place box 3 in room 1 or 2 (height 3). Finally place box 4 in room 0 (height 5). Total 3 boxes.

**Example 2**

- **Input:** `boxes = [1,2,2,3,4], warehouse = [3,4,1,2]`
- **Output:** `3`
- **Explanation:** Room 1 has effective height 3 (due to entrance room 0 of height 3). Room 2 has height 1, room 3 has effective height 1. Place box 1 in room 2, box 2 in room 3, and box 3 in room 0.

**Example 3**

- **Input:** `boxes = [1,2,3], warehouse = [1,2,3,4]`
- **Output:** `1`
- **Explanation:** Entrance room 0 has height 1, so no box larger than 1 can enter the warehouse.
