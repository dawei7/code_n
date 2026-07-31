## Examples

**Example 1**

- Input: `gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2]`
- Output: `3`
- Explanation: Start at station 3 with an empty tank and add `4` units. The complete trip is:

| Action | Tank afterward |
|---|---:|
| Fill at station 3 | `0 + 4 = 4` |
| Travel to 4, then add `5` | `4 - 1 + 5 = 8` |
| Travel to 0, then add `1` | `8 - 2 + 1 = 7` |
| Travel to 1, then add `2` | `7 - 3 + 2 = 6` |
| Travel to 2, then add `3` | `6 - 4 + 3 = 5` |
| Travel back to 3 | `5 - 5 = 0` |

The tank has exactly enough gas for the final leg, so the required starting index is `3`.

**Example 2**

- Input: `gas = [2, 3, 4], cost = [3, 4, 3]`
- Output: `-1`
- Explanation: Stations 0 and 1 cannot reach even their next station. Starting at station 2 progresses as follows:

| Action | Tank afterward |
|---|---:|
| Fill at station 2 | `0 + 4 = 4` |
| Travel to 0, then add `2` | `4 - 3 + 2 = 3` |
| Travel to 1, then add `3` | `3 - 3 + 3 = 3` |

Returning to station 2 would cost `4`, but only `3` units remain. Therefore no starting station can complete the circuit.
