### 1. Description

You are given a string array `features` where $\text{features}[i]$ is a single word that represents the name of a feature of the latest product you are working on. You have made a survey where users have reported which features they like. You are given a string array `responses`, where each $\text{responses}[i]$ is a string containing space-separated words.

The **popularity** of a feature is the number of $\text{responses}[i]$ that contain the feature. You want to sort the features in non-increasing order by their popularity. If two features have the same popularity, order them by their original index in `features`. Notice that one response could contain the same feature multiple times; this feature is only counted once in its popularity.

Return *the features in sorted order.*

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

- **Input:** $features = ["cooler","lock","touch"], responses = ["i like cooler cooler","lock touch cool","locker like touch"]$
- **Output:** `["touch","cooler","lock"]`
- **Explanation:** appearances("cooler") = 1, appearances("lock") = 1, appearances("touch") = 2. Since "cooler" and "lock" both had 1 appearance, "cooler" comes first because "cooler" came first in the features array.

#### Example 2

- **Input:** $features = ["a","aa","b","c"], responses = ["a","a aa","a a a a a","b a"]$
- **Output:** `["a","aa","b","c"]`

### 4. Constraints

- $1 \le \text{features.length} \le 10^{4}$

- $1 \le \text{features}[i].length \le 10$

- `features` contains no duplicates.

- $\text{features}[i]$ consists of lowercase letters.

- $1 \le \text{responses.length} \le 10^{2}$

- $1 \le \text{responses}[i].length \le 10^{3}$

- $\text{responses}[i]$ consists of lowercase letters and spaces.

- $\text{responses}[i]$ contains no two consecutive spaces.

- $\text{responses}[i]$ has no leading or trailing spaces.
