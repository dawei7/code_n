## Description

You are given a 2D string array `responses` where each `responses[i]` is an array of strings representing survey responses from the `i^th` day.

Return the **most common** response across all days after removing **duplicate** responses within each `responses[i]`. If there is a tie, return the *<span data-keyword="lexicographically-smaller-string">lexicographically smallest</span>* response.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]</span>

**Output:** <span class="example-io">"good"</span>

**Explanation:**

	- After removing duplicates within each list, `responses = [["good", "ok"], ["ok", "bad", "good"], ["good"], ["bad"]]`.

	- `"good"` appears 3 times, `"ok"` appears 2 times, and `"bad"` appears 2 times.

	- Return `"good"` because it has the highest frequency.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">responses = [["good","ok","good"],["ok","bad"],["bad","notsure"],["great","good"]]</span>

**Output:** <span class="example-io">"bad"</span>

**Explanation:**

	- After removing duplicates within each list we have `responses = [["good", "ok"], ["ok", "bad"], ["bad", "notsure"], ["great", "good"]]`.

	- `"bad"`, `"good"`, and `"ok"` each occur 2 times.

	- The output is `"bad"` because it is the lexicographically smallest amongst the words with the highest frequency.

</div>

**Constraints:**

	- `1 <= responses.length <= 1000`

	- `1 <= responses[i].length <= 1000`

	- `1 <= responses[i][j].length <= 10`

	- `responses[i][j]` consists of only lowercase English letters
