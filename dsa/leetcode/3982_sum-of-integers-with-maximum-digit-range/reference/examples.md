## Examples

**Example 1**

- Input: `nums = [5724,111,350]`
- Output: `6074`
- **Explanation:** The digit details for every array position are:

  | `i` | `nums[i]` | Largest | Smallest | Digit Range |
  |---:|---:|---:|---:|---:|
  | 0 | 5724 | 7 | 2 | 5 |
  | 1 | 111 | 1 | 1 | 0 |
  | 2 | 350 | 5 | 0 | 5 |

  The maximum digit range is $5$. The values `5724` and `350` attain it, so the result is `5724 + 350 = 6074`.

**Example 2**

- Input: `nums = [90,900]`
- Output: `990`
- **Explanation:** Both integers have the same extreme decimal digits:

  | `i` | `nums[i]` | Largest | Smallest | Digit Range |
  |---:|---:|---:|---:|---:|
  | 0 | 90 | 9 | 0 | 9 |
  | 1 | 900 | 9 | 0 | 9 |

  The maximum digit range is $9$, and both values attain it. Their sum is `90 + 900 = 990`.
