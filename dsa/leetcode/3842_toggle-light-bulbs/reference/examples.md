## Examples

**Example 1**

- Input: `bulbs = [10,30,20,10]`
- Output: `[20,30]`
- Explanation:
  - At `bulbs[0] = 10`, bulb 10 is off, so it is switched on.
  - At `bulbs[1] = 30`, bulb 30 is off, so it is switched on.
  - At `bulbs[2] = 20`, bulb 20 is off, so it is switched on.
  - At `bulbs[3] = 10`, bulb 10 is currently on, so it is switched off.
  - Bulbs 20 and 30 are therefore the bulbs left on at the end.

**Example 2**

- Input: `bulbs = [100,100]`
- Output: `[]`
- Explanation:
  - At `bulbs[0] = 100`, bulb 100 begins off and is switched on.
  - At `bulbs[1] = 100`, the same bulb is on and is switched off.
  - No light bulb remains on after both operations.
