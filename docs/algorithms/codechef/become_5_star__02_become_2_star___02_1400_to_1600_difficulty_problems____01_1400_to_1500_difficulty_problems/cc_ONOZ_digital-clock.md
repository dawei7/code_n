# Digital clock

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ONOZ |
| Difficulty Rating | 1482 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [ONOZ](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/ONOZ) |

---

## Problem Statement

*3:33*

It's possible for all the digits displayed on a digital clock in the *hours:minutes* format to be identical. The time shown above (*3:33*) is an example of such a situation. Other examples are *2:2* and *1:11*. Note that the digits of *33:33* are identical, but it is not a valid time on a usual digital clock.

The above example was for a usual 24-hour format digital clock. Let's consider a more general clock, where an hour lasts **M** minutes and a day lasts **H** hours (therefore, the clock can show any number of hours between **0** and **H-1**, inclusive, and any number of minutes between **0** and **M-1**, inclusive). Both the hours and the minutes are shown **without leading zeroes** in decimal notation and their separator (e.g., ':') doesn't matter.

Can you tell how many minutes during a day will the digital clock have identical digits displayed on it?

### Input

- The first line of the input contains an integer **T** - the number of test cases.

- Each of the next **T** lines contains two space-separated integers **H** and **M** for one test case.

### Output

For each test case, output a single line corresponding to the answer of the problem.

### Constraints

- **1 ≤ T ≤ 50**

- **1 ≤ H, M ≤ 100**

---

## Examples

**Example 1**

**Input**

```text
6
24 60
34 50
10 11
10 12
11 11
1 1
```

**Output**

```text
19
20
10
11
10
1
```

**Explanation**

**Example case 1.** A clock shows two identical digits at times *0:0*, *1:1*, .., *9:9*, three identical digits at times *11:1*, *22:2*, *1:11*, *2:22*, *3:33*, *4:44*, *5:55*, and four identical digits at times *11:11* and *22:22*. So, there are 19 minutes during which the time displayed by the clock will have identical digits.

**Example case 2.** Compared to the previous case, the clock doesn't show *5:55*, but can show *33:3* and *33:33*.

**Example case 6.** In this example, our day consists of one hour and one hour consists of one minute. Hence, the entire day is just 1 minute - the only time the digital clock will display is 0:0 during the entire day, (i.e. the entire hour, i.e. entire minute). And 0:0 has all digits identical, so the answer is 1.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
24 60
```

**Output for this case**

```text
19
```



#### Test case 2

**Input for this case**

```text
34 50
```

**Output for this case**

```text
20
```



#### Test case 3

**Input for this case**

```text
10 11
```

**Output for this case**

```text
10
```



#### Test case 4

**Input for this case**

```text
10 12
```

**Output for this case**

```text
11
```



#### Test case 5

**Input for this case**

```text
11 11
```

**Output for this case**

```text
10
```



#### Test case 6

**Input for this case**

```text
1 1
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Contest](http://www.codechef.com/COOK68/problems/ONOZ)

[Practice](http://www.codechef.com/problems/ONOZ)

**Authors:** [Jaub Safin](http://www.codechef.com/users/xellos0)

**Testers:** [Vasya Antoniuk](http://www.codechef.com/users/antoniuk1)

**Translators:** [Vasya Antoniuk](http://www.codechef.com/users/antoniuk1) (Russian), [Team VNOI](http://www.codechef.com/users/vnoi) (Vietnamese) and [Hu Zecong](http://www.codechef.com/users/huzecong) (Mandarin)

**Editorialist:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

String processing

### PROBLEM:

You have a clock which ticks H hours. It ticks M minutes in an hour. Let h:m denote the time shown by the clock at some instant, where h is an integer without leading zeros denoting the current hour and M denoting the current minute. Note that both h and m don’t have leading zeros.

We define a duration h:m *good* if both h and m contain a single digit in their decimal representation. e.g. 2:22 is good where 2:3 is bad.

Note that the duration 02:22 is also good as it will be represented as 2:22 when we write h without leading zeros.

Find out number of good durations h:m such that 0 \leq h < H, 0 \leq m < M.

### QUICK EXPLANATION:

As values of H and M (\leq 100) are very small. We can simply use a brutefore approach.

Let us iterate over hour h from 0 to H - 1 and m from 0 to M-1, we represent h and m as strings and check whether both the strings are made of a unique character or not.

### EXPLANATION:

As stated in previous section, we can iterate over  h from 0 to H - 1 and m from 0 to M-1, we represent h and m as strings and check whether both the strings are made of some unique character or not.

**Pseudo Code**

``int ans = 0;
for (int h = 0; h < H; h++) {
    for (int m = 0; m < M; m++) {
        if (isGood(toString(h) + toString(m))) {
            ans++;
        }
    }
}
``

Now, let us learn few tricks of how to convert an integer into a string.

#### General method (not specific to any language)

We extract the digits of the number one by one and append to our answer string. See the code below.

``string ans = ""
while (n > 0) {
	ans += (char) (n % 10 + '0');
	n /= 10;
}
reverse(ans.begin(), ans.end())
``

#### C specific method

We can use itoa() function for converting an integer to a string.

``char * s = itoa(n)
``

#### C++ specific methods

In C++ 11, you can use to_string method.

``string s = to_sring(n)
``

You can also make use of string streams.

``ostringstream os;
os << n;
string s = os.str()
``

#### Java specific methods
``String ans = String.valueOf(n);
``

**Checking whether all the digits of a string are equal or not**

We can iterate over each character of the string and check whether it is equal to previous or not. If all the digits of the string are not equal, then there would be a character whose previous charater is not equal to that.

``for (int i = 1; i < s.size(); i++) {
	if (s[i] != s[i - 1]) {
		return false;
	}
}
return true;
``

Alternatively, you can insert the characters into a set and check whether size of set is one or not.

``set<char> st;
for (int i = 0; i < s.size(); i++) {
	st.insert(s[i]);
}
return st.size() == 1;
``

### Time Complexity:

We spend \mathcal{O}(H \cdot M) for iterating over h and m, then converting h and m to strings and the later processing requires operations equal to number of digits in both h and m.  As we note that h and m can not be larger than 100. So, it can be at max 3 + 3 = 6, which is \mathcal{O}(1).

So total time will be \mathcal{O}(H \cdot M) which is around 10^4 operations for each test case. There are around 50 test cases. So, we will make around 5 * 10^5 operations overall which will easily run under 1 secs as normally we have around 3 * 10^8 operations in a second.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[setter](https://www.codechef.com/download/Solutions/COOK68/Setter/ONOZ.cpp)

[tester](https://www.codechef.com/download/Solutions/COOK68/Tester/ONOZ.cpp)

</details>
