## Examples

**Example 1**

- **Input:** `items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]`
- **Output:** `[[1,87],[2,88]]`
- **Explanation:** Student 1 has scores `91`, `92`, `60`, `65`, `87`, and `100`. The five highest sum to `100 + 92 + 91 + 87 + 65 = 435`, so the average is `435 / 5 = 87`. Student 2 has scores `93`, `97`, `77`, `100`, and `76`; their sum gives `443 / 5 = 88.6`, which integer division converts to `88`.

**Example 2**

- **Input:** `items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]`
- **Output:** `[[1,100],[7,100]]`
