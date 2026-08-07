### 1. Description

You are given two string arrays $\text{positive}_{feedback}$ and $\text{negative}_{feedback}$, containing the words denoting positive and negative feedback, respectively. Note that **no** word is both positive and negative.

Initially every student has `0` points. Each positive word in a feedback report **increases** the points of a student by `3`, whereas each negative word **decreases** the points by `1`.

You are given `n` feedback reports, represented by a **0-indexed** string array `report` and a **0-indexed** integer array $\text{student}_{id}$, where $\text{student}_{id}[i]$ represents the ID of the student who has received the feedback report $\text{report}[i]$. The ID of each student is **unique**.

Given an integer `k`, return *the top *`k`* students after ranking them in **non-increasing** order by their points*. In case more than one student has the same points, the one with the lower ID ranks higher.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $\text{positive}_{feedback} = ["smart","brilliant","studious"], \text{negative}_{feedback} = ["not"], report = ["this student is studious","the student is smart"], \text{student}_{id} = [1,2], k = 2$
- **Output:** `[1,2]`
- **Explanation:**
Both the students have 1 positive feedback and 3 points but since student 1 has a lower ID he ranks higher.
#### Example 2

- **Input:** $\text{positive}_{feedback} = ["smart","brilliant","studious"], \text{negative}_{feedback} = ["not"], report = ["this student is not studious","the student is smart"], \text{student}_{id} = [1,2], k = 2$
- **Output:** `[2,1]`
- **Explanation:**
- The student with ID 1 has 1 positive feedback and 1 negative feedback, so he has 3-1=2 points.
- The student with ID 2 has 1 positive feedback, so he has 3 points.
Since student 2 has more points, [2,1] is returned.

### 4. Constraints

- $1 \le \text{positive}_{feedback}.length, \text{negative}_{feedback}.length \le 10^{4}$

- $1 \le \text{positive}_{feedback}[i].length, \text{negative}_{feedback}[j].length \le 100$

- Both $\text{positive}_{feedback}[i]$ and $\text{negative}_{feedback}[j]$ consists of lowercase English letters.

- No word is present in both $\text{positive}_{feedback}$ and $\text{negative}_{feedback}$.

- $n = \text{report.length} = \text{student}_{id}.length$

- $1 \le n \le 10^{4}$

- $\text{report}[i]$ consists of lowercase English letters and spaces `' '`.

- There is a single space between consecutive words of $\text{report}[i]$.

- $1 \le \text{report}[i].length \le 100$

- $1 \le \text{student}_{id}[i] \le 10^{9}$

- All the values of $\text{student}_{id}[i]$ are **unique**.

- $1 \le k \le n$