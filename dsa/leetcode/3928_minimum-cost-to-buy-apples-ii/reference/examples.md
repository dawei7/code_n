## Examples

**Example 1**

- Input: `n = 2, prices = [8,3], roads = [[0,1,1,2]]`
- Output: `[6,3]`
- Explanation: The only road has empty cost `1` and loaded cost `1 * 2 = 2`.

An equivalent text diagram labels the edge as `(cost, tax)`:

```text
shop 0 [price 8] --(1, 2)-- shop 1 [price 3]
```

| Start shop `i` | `prices[i]` | Purchase shop `j` | `prices[j]` | `cost` | `tax` | Empty travel | Loaded return | Route total | Minimum |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 1 | 3 | 1 | 2 | 1 | `1 * 2 = 2` | `1 + 2 + 3 = 6` | `min(8, 6) = 6` |
| 1 | 3 | 0 | 8 | 1 | 2 | 1 | `1 * 2 = 2` | `1 + 2 + 8 = 11` | `min(3, 11) = 3` |

Starting at shop `0`, buying at shop `1` lowers the total to `6`. Starting at shop `1`, its local price `3` beats the round-trip candidate `11`, giving `[6,3]`.

**Example 2**

- Input: `n = 3, prices = [9,4,6], roads = [[0,1,1,3],[1,2,4,2]]`
- Output: `[8,4,6]`
- Explanation: The shops form a chain with the following `(cost, tax)` road labels.

```text
shop 0 [price 9] --(1, 3)-- shop 1 [price 4] --(4, 2)-- shop 2 [price 6]
```

| Start shop `i` | `prices[i]` | Purchase shop `j` | `prices[j]` | `cost` | `tax` | Empty travel | Loaded return | Route total | Minimum |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 9 | 1 | 4 | 1 | 3 | 1 | `1 * 3 = 3` | `1 + 3 + 4 = 8` | `min(9, 8) = 8` |
| 1 | 4 | 2 | 6 | 4 | 2 | 4 | `4 * 2 = 8` | `4 + 8 + 6 = 18` | `min(4, 18) = 4` |
| 2 | 6 | 1 | 4 | 4 | 2 | 4 | `4 * 2 = 8` | `4 + 8 + 4 = 16` | `min(6, 16) = 6` |

Only the first starting shop benefits from traveling. The other two keep their local prices, so the result is `[8,4,6]`.

**Example 3**

- Input: `n = 3, prices = [10,11,1], roads = [[0,2,1,3],[1,2,3,4],[0,1,5,2]]`
- Output: `[5,11,1]`
- Explanation: All three shop pairs are connected; each edge below again shows `(cost, tax)`.

```text
             shop 1 [price 11]
             /                 \
         (5, 2)               (3, 4)
           /                     \
shop 0 [price 10] --(1, 3)-- shop 2 [price 1]
```

| Start shop `i` | `prices[i]` | Purchase shop `j` | `prices[j]` | `cost` | `tax` | Empty travel | Loaded return | Route total | Minimum |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 10 | 2 | 1 | 1 | 3 | 1 | `1 * 3 = 3` | `1 + 3 + 1 = 5` | `min(10, 5) = 5` |
| 1 | 11 | 2 | 1 | 3 | 4 | 3 | `3 * 4 = 12` | `3 + 12 + 1 = 16` | `min(11, 16) = 11` |
| 2 | 1 | 0 | 10 | 1 | 3 | 1 | `1 * 3 = 3` | `1 + 3 + 10 = 14` | `min(1, 14) = 1` |

The inexpensive apples at shop `2` justify a round trip only from shop `0`. Shops `1` and `2` buy locally, producing `[5,11,1]`.
