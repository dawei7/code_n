## Examples

**Example 1**

- **Input:** `m = 4, operations = [["join",[[1,2]]],["join",[[2,3]]],["join",[[4]]],["request",[1,3]],["request",[2,2]],["leave",[1]],["request",[2,1]],["leave",[2]],["join",[[]]]]`
- **Output:** `[1, 2, 3, [2], [1, 2], null, [], null, 1]`
- **Explanation:** User 1 obtains chunk 3 from user 2. After user 1 leaves, nobody owns chunk 1. IDs 1 and 2 are both free before the final join, so the smaller ID 1 is reused.

**Example 2**

- **Input:** `m = 3, operations = [["join",[[]]],["join",[[1]]],["request",[1,1]],["request",[1,1]]]`
- **Output:** `[1, 2, [2], [1, 2]]`
- **Explanation:** The first request reports only the preexisting owner and then gives chunk 1 to user 1. The second request therefore includes both users.

**Example 3**

- **Input:** `m = 2, operations = [["join",[[1,2]]],["join",[[2]]],["leave",[1]],["request",[2,1]],["join",[[1]]],["request",[2,1]]]`
- **Output:** `[1, 2, null, [], 1, [1]]`
- **Explanation:** Leaving removes every chunk formerly supplied by user 1. Rejoining under the reused ID restores only the chunks explicitly supplied to that new user.
