# Tourist Translations

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TOTR |
| Difficulty Rating | 1252 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [TOTR](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/TOTR) |

---

## Problem Statement

A tourist is visiting Byteland. The tourist knows English very well. The language of Byteland is rather different from English. To be exact it differs in following points:

- Bytelandian alphabet has the same letters as English one, but possibly different in meaning. Like 'A' in Bytelandian may be 'M' in English. However this does **not** mean that 'M' in Bytelandian must be 'A' in English. More formally, Bytelindian alphabet is a permutation of English alphabet. It will be given to you and could be any possible permutation. Don't assume any other condition.

- People of Byteland don't like to use invisible character for separating words. Hence instead of space (' ') they use underscore ('_'). Other punctuation symbols, like '?', '!' remain the same as in English.

The tourist is carrying "The dummies guide to Bytelandian", for translation. The book is serving his purpose nicely. But he is addicted to sharing on BaceFook, and shares his numerous conversations in Byteland on it. The conversations are rather long, and it is quite tedious to translate for his English friends, so he asks you to help him by writing a program to do the same.

### Input

The first line of the input contains an integer **T**, denoting the length of the conversation, and the string **M**, denoting the English translation of Bytelandian string **"abcdefghijklmnopqrstuvwxyz"**. **T** and **M** are separated by exactly one space. Then **T** lines follow, each containing a Bytelandian sentence **S** which you should translate into English. See constraints for details.

### Output

For each of the sentence in the input, output its English translation on a separate line. Replace each underscores ('_') with a space (' ') in the output. Each punctuation symbol (see below) should remain the same. Note that the uppercase letters in Bytelandian remain uppercase in English, and lowercase letters remain lowercase. See the example and its explanation for clarity.

### Constraints

- **1** ≤ **T** ≤ **100**

- **M** is a permutation of **"abcdefghijklmnopqrstuvwxyz"**

- Each sentence is non-empty and contains at most **100** characters

- Each sentence may contain only lowercase letters ('a'-'z'), uppercase letters ('A'-'Z'), underscores ('_') and punctuation symbols: dot ('.'), comma (','), exclamation ('!'), question-mark('?')

---

## Examples

**Example 1**

**Input**

```text
5 qwertyuiopasdfghjklzxcvbnm
Ph
Pcssi
Bpke_kdc_epclc_jcijsc_mihyo?
Epcf_kdc_liswhyo_EIED_hy_Vimcvpcn_Zkdvp_siyo_viyecle.
Ipp!
```

**Output**

```text
Hi
Hello
What are these people doing?
They are solving TOTR in Codechef March long contest.
Ohh!
```

**Explanation**

The string "qwertyuiopasdfghjklzxcvbnm" means that 'a' in Bytelandian is 'q' in English, 'b' in Bytelandian is 'w' in English, 'c' in Bytelandian is 'e' in English and so on.
Thus to translate "Ph" (first sentence in example) to English:
1) We find that 'p' in Bytelandian means 'h' in English. So we replace 'P' with 'H'.
2) Then we see that 'h' in Bytelandian means 'i' in English. So we replace 'h' with 'i'.
3) Therefore, the translation is "Hi".

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/TOTR)

[Contest](http://www.codechef.com/MARCH13/problems/TOTR)

### DIFFICULTY

CAKEWALK

### PREREQUISITES

Ad Hoc

### PROBLEM

The problem statement of Tourist Translations boils down to the following points

- You are given a mapping of the 26 english alphabets onto itself. (Let this be called **map**)

- Transform a string using this mapping while maitaining the **case**.

- Preserve punctuation.

- Replace ‘**_**’ with single **space**.

### EXPLANATION

For those new to programming, solving this problem should lead to discovery of how to map a character in the english alphabet to another. **map** is input in the form of a string of 26 characters, which contains a permutation of the characters.

- The first character is the what ‘a’ maps to.

- The second character is what ‘b’ maps to.

…

- The 26th character is what ‘z’ maps to.

This can be achieved by mapping characters in english to indexes in **map**, and then use the character at that index. Given a string **A** of english alphabets, this can be done as following

`
for i = 1 to length(A)
    A[i] = map[A[i] - 'a']
`

Of course, this is possible because characters in the **ASCII** charset are stored in a continuous block that starts at **65**, which is ‘**a**’. The above snippet has one bug right now. We are not detecting the **character case ** and trying to maintain it. Let us fix that.

`
for i = 1 to length(A)
    if A[i] = lower-case-alphabet
        A[i] = lower-case( map[A[i] - 'a'] )
    if A[i] = upper-case-alphabet
        A[i] = upper-case( map[A[i] - 'a'] )
`

Now, all that is needed is to handle the other two types of characters - **punctuation and underscores**.

`
for i = 1 to length(A)
    if A[i] = underscore
        A[i] = space
    if A[i] = lower-case-alphabet
        A[i] = lower-case( map[A[i] - 'a'] )
    if A[i] = upper-case-alphabet
        A[i] = upper-case( map[A[i] - 'a'] )
    /* Ignore punctuation */
`

Both the Setter’s and Tester’s solution use the approach described above.

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2013/March/Setter/TOTR.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2013/March/Tester/TOTR.cpp).

</details>
