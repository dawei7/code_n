## Description

You are given a 2D string array `responses` where each $\text{responses}[i]$ is an array of strings representing survey responses from the $$i^{\text{th}}$$ day.

Return the **most common** response across all days after removing **duplicate** responses within each $\text{responses}[i]$. If there is a tie, return the *lexicographically smallest* response.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]

**Output:** "good"

**Explanation:**

- After removing duplicates within each list, $responses = [["good", "ok"], ["ok", "bad", "good"], ["good"], ["bad"]]$.

- `"good"` appears 3 times, `"ok"` appears 2 times, and `"bad"` appears 2 times.

- Return `"good"` because it has the highest frequency.

</div>
#### Example 2

<div class="example-block">
**Input:** responses = [["good","ok","good"],["ok","bad"],["bad","notsure"],["great","good"]]

**Output:** "bad"

**Explanation:**

- After removing duplicates within each list we have $responses = [["good", "ok"], ["ok", "bad"], ["bad", "notsure"], ["great", "good"]]$.

- `"bad"`, `"good"`, and `"ok"` each occur 2 times.

- The output is `"bad"` because it is the lexicographically smallest amongst the words with the highest frequency.

</div>
### Constraints

- $1 \le \text{responses.length} \le 1000$

- $1 \le \text{responses}[i].length \le 1000$

- $1 \le \text{responses}[i][j].length \le 10$

- $\text{responses}[i][j]$ consists of only lowercase English letters