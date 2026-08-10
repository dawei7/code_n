
## Solution

---

### Approach: Greedy

#### Intuition

The task requires returning the difference between the maximum and minimum values obtained by replacing digits in the number `num`. According to the rules of digits, to generate the **maximum** value, we should replace digits to make the number as large as possible, typically by replacing some digit with `'9'`. To generate the **minimum** value, we should do the opposite and replace some digit with `'0'` to make the number as small as possible. For ease of calculation, we first convert `num` to a string `s`, and then apply the following greedy rules:

+ To generate the maximum value: scan from left to right to find the first digit that is not `'9'`, and replace all occurrences of that digit with `'9'`.

+ To generate the minimum value: scan from left to right to find the first digit that is not `'0'`, and replace all occurrences of that digit with `'0'`. Since $s[0]$ is guaranteed not to be `'0'`, we can simply replace all occurrences of $s[0]$ with `'0'`.

Finally, return the difference between the maximum and minimum values obtained.

#### Implementation

```python
class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        t = s
        pos = 0
        while pos < len(s) and s[pos] == "9":
            pos += 1
        if pos < len(s):
            s = s.replace(s[pos], "9")
        t = t.replace(t[0], "0")
        return int(s) - int(t)
```

#### Complexity Analysis

Let $\textit{num}$ be the given number.

- Time complexity: $O(\log \textit{num})$.

  To generate the minimum and maximum values, we need to traverse each digit of $\textit{num}$. Since the number of digits in $\textit{num}$ is $O(\log \textit{num})$, the time required is also $O(\log \textit{num})$.

- Space complexity: $O(\log \textit{num})$.

  Similarly, to generate the minimum and maximum values, we need to store each digit of $\textit{num}$, requiring $O(\log \textit{num})$ space.