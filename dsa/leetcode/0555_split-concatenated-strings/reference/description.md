### 1. Description

You are given an array of strings `strs`. You could concatenate these strings together into a loop, where for each string, you could choose to reverse it or not. Among all the possible loops

Return *the lexicographically largest string after cutting the loop, which will make the looped string into a regular one*.

Specifically, to find the lexicographically largest string, you need to experience two phases:

- Concatenate all the strings into a loop, where you can reverse some strings or not and connect them in the same order as given.

- Cut and make one breakpoint in any place of the loop, which will make the looped string into a regular one starting from the character at the cutpoint.

And your job is to find the lexicographically largest one among all the possible regular strings.

### 2. Function Contract

**Inputs**

- `strs`: a nonempty list of nonempty lowercase English strings.

Let $m = \lvert\texttt{strs}\rvert$ and let

$L = \sum_{w \in \texttt{strs}} \lvert w \rvert.$

Every legal result contains exactly $L$ characters. Reversal changes the order inside a block but not the circular
order of the $m$ blocks.

**Return value**

Return the lexicographically largest length-$L$ string obtainable after choosing all block orientations and opening
the resulting loop at one character boundary.

### 3. Examples

#### Example 1

- **Input:** $strs = ["abc","xyz"]$
- **Output:** `"zyxcba"`
- **Explanation:** You can get the looped string "-abcxyz-", "-abczyx-", "-cbaxyz-", "-cbazyx-", where '-' represents the looped status.
The answer string came from the fourth looped one, where you could cut from the middle character 'a' and get "zyxcba".
#### Example 2

- **Input:** $strs = ["abc"]$
- **Output:** `"cba"`

### 4. Constraints

- $1 \le \text{strs.length} \le 1000$

- $1 \le \text{strs}[i].length \le 1000$

- $1 \le sum(\text{strs}[i].length) \le 1000$

- $\text{strs}[i]$ consists of lowercase English letters.