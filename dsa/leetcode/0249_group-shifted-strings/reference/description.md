## Description

Perform the following shift operations on a string:

- **Right shift**: Replace every letter with the **successive** letter of the English alphabet, where 'z' is replaced by 'a'. For example, `"abc"` can be right-shifted to `"bcd" `or `"xyz"` can be right-shifted to `"yza"`.

- **Left shift**: Replace every letter with the **preceding** letter of the English alphabet, where 'a' is replaced by 'z'. For example, `"bcd"` can be left-shifted to `"abc" or `"yza"` can be left-shifted to `"xyz"`.

We can keep shifting the string in both directions to form an **endless** **shifting sequence**.

- For example, shift `"abc"` to form the sequence: `... <-> "abc" <-> "bcd" <-> ... <-> "xyz" <-> "yza" <-> ...`.` <-> "zab" <-> "abc" <-> ...`

You are given an array of strings `strings`, group together all $\text{strings}[i]$ that belong to the same shifting sequence. You may return the answer in **any order**.
### Function Contract

**Inputs**

- `strings`: Array of strings `List[str]`.

**Return value**

Return `List[List[str]]` containing grouped strings belonging to the same shifting sequence.

### Examples
#### Example 1

<div class="example-block">
**Input:** strings = ["abc","bcd","acef","xyz","az","ba","a","z"]

**Output:** [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

</div>
#### Example 2

<div class="example-block">
**Input:** strings = ["a"]

**Output:** [["a"]]

</div>
### Constraints

- $1 \le \text{strings.length} \le 200$

- $1 \le \text{strings}[i].length \le 50$

- $\text{strings}[i]$ consists of lowercase English letters.