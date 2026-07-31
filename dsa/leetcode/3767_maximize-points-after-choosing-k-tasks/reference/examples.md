## Examples

**Example 1**

- Input: `technique1 = [5,2,10], technique2 = [10,3,8], k = 2`
- Output: `22`
- Explanation: At least two tasks must use technique 1. Use technique 1 for indices 1 and 2, earning 2 and 10 points, and technique 2 for index 0, earning 10 points. The maximum total is `2 + 10 + 10 = 22`.

**Example 2**

- Input: `technique1 = [10,20,30], technique2 = [5,15,25], k = 2`
- Output: `60`
- Explanation: The requirement is at least two technique-1 tasks, but technique 1 is better at all three indices. Assigning every task to technique 1 produces the maximum `10 + 20 + 30 = 60`.

**Example 3**

- Input: `technique1 = [1,2,3], technique2 = [4,5,6], k = 0`
- Output: `15`
- Explanation: With `k = 0`, no task is required to use technique 1. Technique 2 is better at every index, so choosing it for all tasks gives `4 + 5 + 6 = 15`.
