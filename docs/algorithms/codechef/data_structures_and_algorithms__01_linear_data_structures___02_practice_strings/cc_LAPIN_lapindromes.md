# Lapindromes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LAPIN |
| Difficulty Rating | 1159 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Strings |
| Official Link | [LAPIN](https://www.codechef.com/practice/course/1to2stars/LP1TO203/problems/LAPIN) |

---

## Problem Statement

*Lapindrome* is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example ***gaga*** is a lapindrome, since the two halves ***ga*** and ***ga*** have the same characters with same frequency. Also, ***abccab***, ***rotor*** and ***xyzxy*** are a few examples of lapindromes. Note that ***abbaab*** is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match.
 Your task is simple. Given a string, you need to tell if it is a lapindrome.

### Input:
First line of input contains a single integer **T**, the number of test cases.

Each test is a single line containing a string **S** composed of only lowercase English alphabet.

### Output:
For each test case, output on a separate line: "YES" if the string is a lapindrome and "NO" if it is not.

### Constraints:

- 1 ≤ **T** ≤ 100

- 2 ≤ |**S**| ≤ 1000, where |**S**| denotes the length of **S**

---

## Examples

**Example 1**

**Input**

```text
6
gaga
abcde
rotor
xyzxy
abbaab
ababc
```

**Output**

```text
YES
NO
YES
YES
NO
NO
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
gaga
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
abcde
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
rotor
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
xyzxy
```

**Output for this case**

```text
YES
```



#### Test case 5

**Input for this case**

```text
abbaab
```

**Output for this case**

```text
NO
```



#### Test case 6

**Input for this case**

```text
ababc
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)Problem Link:

[Practice](https://www.codechef.com/problems/LAPIN)

[Contest](https://www.codechef.com/JUNE13/problems/LAPIN)

[Video Editorial](https://youtu.be/WoFEJi5D8d0)

# [](#difficulty-2)Difficulty:

Cakewalk

# [](#pre-requisites-3)Pre-requisites:

ad-hoc

# [](#problem-4)Problem:

Given a string **S**, if we split it in the middle (if **S** has an odd number of characters, disregard the middle character), then if the frequency of each character is the same in both halves, **S** is called a “lapindrome”. Given the string **S**, test if it is a Lapindrome or not.

# [](#explanation-5)Explanation:

Maintain frequencies for the left half and the right half, for each character. After computing the frequency of each half, then check if the frequencies of all characters match. If so, output “YES”, else output “NO”.

Consider the following pseudocode:

``
bool isLapin(S)
	initialize cntL[] and cntR[] with 0
	L = S.length()
	for(i = 0; i < L/2; i++)
		cntL[S[i]-'a']++
	for(i = (L+1)/2; i < L; i++)
		cntR[S[i]-'a']++
	bool ret = true
	for(c = 0; c < 26; c++)
		if(cntL[c] != cntR[c])
			ret = false
	return ret

``

The time complexity for this is O(|S| + 26) per test-case.

# [](#setters-solution-6)Setter’s Solution:

Can be found [here](https://www.codechef.com/download/Solutions/2013/June/Setter/LAPIN.cpp)

# [](#testers-solution-7)Tester’s Solution:

Can be found [here](https://www.codechef.com/download/Solutions/2013/June/Tester/LAPIN.cpp)

### [](#video-editorial-8)Video Editorial

</details>
