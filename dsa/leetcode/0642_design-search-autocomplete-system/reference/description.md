### 1. Description

Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character `'#'`).

You are given a string array `sentences` and an integer array `times` both of length `n` where $\text{sentences}[i]$ is a previously typed sentence and $\text{times}[i]$ is the corresponding number of times the sentence was typed. For each input character except `'#'`, return the top `3` historical hot sentences that have the same prefix as the part of the sentence already typed.

Here are the specific rules:

- The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.

- The returned top `3` hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).

- If less than `3` hot sentences exist, return as many as you can.

- When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.

Implement the `AutocompleteSystem` class:

- `AutocompleteSystem(String[] sentences, int[] times)` Initializes the object with the `sentences` and `times` arrays.

- `List<String> input(char c)` This indicates that the user typed the character `c`.

		<li>Returns an empty array `[]` if $c = '#'$ and stores the inputted sentence in the system.

- Returns the top `3` historical hot sentences that have the same prefix as the part of the sentence already typed. If there are fewer than `3` matches, return them all.

	</li>

### 2. Function Contract

**Inputs**

- `sentences`: The historical sentences known when the system is constructed.
- `times`: The corresponding historical frequencies; $\text{times}[i]$ belongs to $\text{sentences}[i]$.
- `c`: The single character supplied to an `input(c)` call.

Construct `AutocompleteSystem(sentences, times)` from the parallel history arrays. Ordinary lowercase letters and spaces extend the current sentence prefix. For each such character, `input` returns at most three matching historical sentences ordered by decreasing hot degree and then by increasing ASCII-code order.

When $c = '#'$, add the completed current sentence to the history or increase its existing frequency, clear the current search, and return `[]`. The next ordinary character begins a new search.

In the app-local operation trace, construction produces `null`, and each later result occupies the position of its corresponding `input` call.

### 3. Examples

#### Example 1

```
**Input**
["AutocompleteSystem", "input", "input", "input", "input"]
[[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
**Output**
[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]

**Explanation**
AutocompleteSystem obj = new AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]);
obj.input("i"); // return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
obj.input(" "); // return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
obj.input("a"); // return []. There are no sentences that have prefix "i a".
obj.input("#"); // return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.
```

### 4. Constraints

- $n = \text{sentences.length}$

- $n = \text{times.length}$

- $1 \le n \le 100$

- $1 \le \text{sentences}[i].length \le 100$

- $1 \le \text{times}[i] \le 50$

- `c` is a lowercase English letter, a hash `'#'`, or space `' '`.

- Each tested sentence will be a sequence of characters `c` that end with the character `'#'`.

- Each tested sentence will have a length in the range `[1, 200]`.

- The words in each input sentence are separated by single spaces.

- At most `5000` calls will be made to `input`.