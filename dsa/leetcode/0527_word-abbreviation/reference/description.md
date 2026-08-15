### 1. Description

Given an array of **distinct** strings `words`, return *the minimal possible **abbreviations** for every word*.

The following are the rules for a string abbreviation:

- The **initial** abbreviation for each word is: the first character, then the number of characters in between, followed by the last character.

- If more than one word shares the **same** abbreviation, then perform the following operation:

		- **Increase** the prefix (characters in the first part) of each of their abbreviations by `1`.
- For example, say you start with the words `["abcdef","abndef"]` both initially abbreviated as `"a4f"`. Then, a sequence of operations would be `["a4f","a4f"]` -> `["ab3f","ab3f"]` -> `["abc2f","abn2f"]`.

- This operation is repeated until every abbreviation is **unique**.

	
- At the end, if an abbreviation did not make a word shorter, then keep it as the original word.

### 2. Function Contract

**Input**

- `words`: a list of distinct lowercase English words

**Return value**

- Return one abbreviation per input word in the same order. The abbreviations must be unique and follow the source
  rules, with each word retaining the shortest prefix that resolves its collisions.

### 3. Examples

#### Example 1

- **Input:** $words = ["like","god","internal","me","internet","interval","intension","face","intrusion"]$
- **Output:** `["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]`

#### Example 2

- **Input:** $words = ["aa","aaa"]$
- **Output:** `["aa","aaa"]`

### 4. Constraints

- $1 \le \text{words.length} \le 400$

- $2 \le \text{words}[i].length \le 400$

- $\text{words}[i]$ consists of lowercase English letters.

- All the strings of `words` are **unique**.
