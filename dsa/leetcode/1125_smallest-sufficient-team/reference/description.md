### 1. Description

In a project, you have a list of required skills $\text{req}_{skills}$, and a list of people. The $$i^{\text{th}}$$ person $\text{people}[i]$ contains a list of skills that the person has.

Consider a sufficient team: a set of people such that for every required skill in $\text{req}_{skills}$, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

- For example, $team = [0, 1, 3]$ represents the people with skills $\text{people}[0]$, $\text{people}[1]$, and $\text{people}[3]$.

Return *any sufficient team of the smallest possible size, represented by the index of each person*. You may return the answer in **any order**.

It is **guaranteed** an answer exists.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $\text{req}_{skills} = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]$
- **Output:** `[0,2]`
#### Example 2

- **Input:** $\text{req}_{skills} = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]$
- **Output:** `[1,2]`

### 4. Constraints

- $1 \le \text{req}_{skills}.length \le 16$

- $1 \le \text{req}_{skills}[i].length \le 16$

- $\text{req}_{skills}[i]$ consists of lowercase English letters.

- All the strings of $\text{req}_{skills}$ are **unique**.

- $1 \le \text{people.length} \le 60$

- $0 \le \text{people}[i].length \le 16$

- $1 \le \text{people}[i][j].length \le 16$

- $\text{people}[i][j]$ consists of lowercase English letters.

- All the strings of $\text{people}[i]$ are **unique**.

- Every skill in $\text{people}[i]$ is a skill in $\text{req}_{skills}$.

- It is guaranteed a sufficient team exists.