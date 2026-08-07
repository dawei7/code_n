## Description

Given two strings `s` and `t`, transform string `s` into string `t` using the following operation any number of times:

	- Choose a **non-empty** substring in `s` and sort it in place so the characters are in **ascending order**.

		<li>For example, applying the operation on the underlined substring in `"1<u>4234</u>"` results in `"1<u>2344</u>"`.

	</li>

Return `true` if *it is possible to transform `s` into `t`*. Otherwise, return `false`.

A **substring** is a contiguous sequence of characters within a string.

**Example 1:**

```
**Input:** s = "84532", t = "34852"
**Output:** true
**Explanation:** You can transform s into t using the following sort operations:
"84<u>53</u>2" (from index 2 to 3) -> "84<u>35</u>2"
"<u>843</u>52" (from index 0 to 2) -> "<u>348</u>52"
```

**Example 2:**

```
**Input:** s = "34521", t = "23415"
**Output:** true
**Explanation:** You can transform s into t using the following sort operations:
"<u>3452</u>1" -> "<u>2345</u>1"
"234<u>51</u>" -> "234<u>15</u>"
```

**Example 3:**

```
**Input:** s = "12345", t = "12435"
**Output:** false
```

**Constraints:**

	- `s.length == t.length`

	- `1 <= s.length <= 10^5`

	- `s` and `t` consist of only digits.
