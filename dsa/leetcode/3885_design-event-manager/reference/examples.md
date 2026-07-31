## Examples

**Example 1**

- Input: `["EventManager", "pollHighest", "updatePriority", "pollHighest", "pollHighest"]`
- Arguments: `[[[[5,7],[2,7],[9,4]]], [], [9,7], [], []]`

- Output: `[null,2,null,5,9]`
- Walkthrough: Construction activates events `5` and `2` at priority `7` and event `9` at priority `4`. The first poll breaks the top-priority tie by smaller ID and removes event `2`. Updating event `9` raises it to priority `7`. Events `5` and `9` then tie, so the next poll removes `5`; the final poll removes `9`.

**Example 2**

- Input: `["EventManager", "pollHighest", "pollHighest", "pollHighest"]`
- Arguments: `[[[[4,1],[7,2]]], [], [], []]`

- Output: `[null,7,4,-1]`
- Walkthrough: Event `7` has the greater priority and is removed first. Event `4` is removed next. With no active events left, the last poll returns `-1`.
