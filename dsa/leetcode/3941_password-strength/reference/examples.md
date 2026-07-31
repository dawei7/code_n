## Examples

**Example 1**

- Input: `password = "aA1!"`
- Output: `11`
- Explanation: The distinct characters are `a`, `A`, `1`, and `!`. Their respective weights are $1$, $2$, $3$, and $5$, so the strength is $1+2+3+5=11$.

**Example 2**

- Input: `password = "bbB11#"`
- Output: `11`
- Explanation: Repeated copies do not add more points. The contributing characters are `b`, `B`, `1`, and `#`, again worth $1$, $2$, $3$, and $5$, for a total of $11$.
