## Description

You are given a **positive** integer `n`.

We call an integer `k` fair if the number of **even** digits in `k` is equal to the number of **odd** digits in it.

Return *the **smallest** fair integer that is **greater than or equal** to *`n`.

**Example 1:**

```
**Input:** n = 2
**Output:** 10
**Explanation:** The smallest fair integer that is greater than or equal to 2 is 10.
10 is fair because it has an equal number of even and odd digits (one odd digit and one even digit).
```

**Example 2:**

```
**Input:** n = 403
**Output:** 1001
**Explanation:** The smallest fair integer that is greater than or equal to 403 is 1001.
1001 is fair because it has an equal number of even and odd digits (two odd digits and two even digits).
```

**Constraints:**

	- `1 <= n <= 10^9`
