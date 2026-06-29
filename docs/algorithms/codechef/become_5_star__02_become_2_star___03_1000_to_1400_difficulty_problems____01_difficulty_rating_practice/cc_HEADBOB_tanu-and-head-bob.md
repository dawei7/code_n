# Tanu and Head-bob

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HEADBOB |
| Difficulty Rating | 1065 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [HEADBOB](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/HEADBOB) |

---

## Problem Statement

Tanu has got interested in signs and gestures that we use for communication. One such gesture is the head-bob.
When we want to signal "Yes" to someone, we move the head up-and-down. For "No", the head is moved left-and-right, rotating about the vertical axis.
 There is a peculiar way of gesturing "Yes", commonly seen in India, by moving head sideways (rotating about the forward-back axis). This is called the * Indian head-bob*.

Tanu observed many people on the railways station, and made a list of gestures that they made. Usual "Yes" gesture is recorded as "**Y**", no as "**N**" and Indian "Yes" gesture as "**I**". (Assume no foreigner uses the Indian "Yes" gesture and vice-versa). Identify which of them were Indians, which were not Indian, and which one you cannot be sure about.

### InputFirst line contains T, number of people observed by Tanu.
Each person is described in two lines. First line of the description contains a single integer N, the number of gestures recorded for this person. Next line contains a string of N characters, each character can be "Y", "N" or "I".

### OutputFor each person, print "INDIAN" if he/she is from India, "NOT INDIAN" if not from India, and "NOT SURE" if the information is insufficient to make a decision.

### Constraints``**For 30 points: **1 ≤ T,N ≤ 100**For 70 points: **1 ≤ T,N ≤ 1000

---

## Examples

**Example 1**

**Input**

```text
3
5
NNNYY
6
NNINNI
4
NNNN
```

**Output**

```text
NOT INDIAN
INDIAN
NOT SURE
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
NNNYY
```

**Output for this case**

```text
NOT INDIAN
```



#### Test case 2

**Input for this case**

```text
6
NNINNI
```

**Output for this case**

```text
INDIAN
```



#### Test case 3

**Input for this case**

```text
4
NNNN
```

**Output for this case**

```text
NOT SURE
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/HEADBOB)

[Contest](http://www.codechef.com/LTIME17/problems/HEADBOB)

**Author:** [Piyush Kumar](http://www.codechef.com/users/piyushkumar)

**Tester:** [Minako Kojima](http://www.codechef.com/users/xiaodao)

**Editorialist:** [Pawel Kacprzak](http://www.codechef.com/users/pkacprzak)

### DIFFICULTY:

CAKEWALK

### PREREQUISITES:

Adhoc

### PROBLEM:

Indian people use only gestures identified by ‘I’ and ‘N’. Non Indian people use only gestures identified by ‘Y’ and ‘N’. Given a string consisting of only ‘Y’, ‘N’ and ‘I’, decide if the string represents an Indian person, non Indian person or it is impossible to determine which one it represents. For each of these decision answers are: “INDIAN”, “NOT INDIAN” and “NOT SURE”.

### QUICK EXPLANATION:

You need to decide if the string contains at least one ‘Y’ or at least one ‘I’ or neither of these letters is presented in the string.

### EXPLANATION:

Problem statement ensures that it is impossible to have both ‘Y’ and ‘I’ in the string.

Based on that fact we can easily compute the answer.

If the string contains at least one ‘I’, then any other letter in is it ‘I’ or ‘N’, so the person represented by this string is Indian, hence the answer is “INDIAN”.

On the other hand, if the string contains at least one ‘Y’, then any other letter in it is ‘Y’ or ‘N’, so the person represented by this string is non Indian, hence the answer is “NOT INDIAN”.

Otherwise, if there is no ‘I’ and ‘Y’ in the string, each letter in it is ‘N’, so we cannot be sure if it represents Indian or non Indian, hence the answer is “NOT SURE”.

In order to do that, you can iterate over the string in a single loop:

# Pseudo Code
`
	found = 0
	for(i = 0; i < s.length(); ++i)
             if (s[i] != 'N')
		if(s[i] == 'Y')
		    res = "NOT INDIAN"
		else if (s[i] == 'I')
		    res = "INDIAN"
		found = 1
		break
	if(found==0)
	    res = "NOT SURE"

	print res

`

# Complexity

O(n) since we just need a single pass over the string

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/LTIME17/Setter/HEADBOB.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/LTIME17/Setter/HEADBOB.cpp).

### RELATED PROBLEMS:

</details>
