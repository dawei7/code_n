## Examples

**Example 1**

- **Input:** `functions = [() => sleep(300), () => sleep(400), () => sleep(200)], n = 2`
- **Output:** `[300, 400, 500]`
- **Explanation:** Functions 0 and 1 start at t=0. Function 0 finishes at t=300, allowing Function 2 to start. Function 2 finishes at t=500. Function 1 finishes at t=400. Total time = 500.

**Example 2**

- **Input:** `functions = [() => sleep(300), () => sleep(400), () => sleep(200)], n = 5`
- **Output:** `[300, 400, 200]`
- **Explanation:** All 3 functions start at t=0 concurrently because $n \ge 3$. Total time = 400.

**Example 3**

- **Input:** `functions = [() => sleep(300), () => sleep(400), () => sleep(200)], n = 1`
- **Output:** `[300, 700, 900]`
- **Explanation:** $n=1$ forces strictly serial execution ($300 + 400 + 200 = 900$).
