# Correct Sentence

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CORTSENT |
| Difficulty Rating | 1485 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [CORTSENT](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/CORTSENT) |

---

## Problem Statement

Chef knows about two languages spoken in Chefland, but he is not proficient in any of them. The first language contains lowercase English letters between 'a' and 'm' inclusive and the second language contains only uppercase English letters between 'N' and 'Z' inclusive.

Due to Chef's limited vocabulary, he sometimes mixes the languages when forming a sentence — each word of Chef's sentence contains only characters from one of the languages, but different words may come from different languages.

You are given a sentence as a sequence of $K$ words $S_1, S_2, \ldots, S_K$. Determine whether it could be a sentence formed by Chef, i.e. if it contains only the characters from the two given languages and each word contains only characters from a single language.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains an integer $K$ followed by a space and $K$ space-separated strings $S_1, S_2, \ldots, S_K$.

### Output
For each test case, print a single line containing the string `"YES"` if the given sentence can be formed by Chef or `"NO"` if it cannot.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

### Constraints
- $1 \le T \le 10^5$
- $1 \leq K \leq 10$
- $1 \leq |S_i| \leq 100$ for each valid $i$
- the sum of lengths of all the strings on the input does not exceed $10^5$
- each string contains only lowercase and uppercase English letters

---

## Examples

**Example 1**

**Input**

```text
3
1 aN
2 ab NO
3 A N D
```

**Output**

```text
NO
YES
NO
```

**Explanation**

**Example case 1:** A single word cannot contain characters from both languages.

**Example case 2:** This could be a sentence formed by Chef since each word contains only characters from a single language.

**Example case 3:** Letters 'A' and 'D' do not belong to either of the two languages.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 aN
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
2 ab NO
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
3 A N D
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Practice](https://www.codechef.com/problems/CORTSENT)

[Contest: Division 1](https://www.codechef.com/START4A/problems/CORTSENT)

[Contest: Division 2](https://www.codechef.com/START4B/problems/CORTSENT)

[Contest: Division 3](https://www.codechef.com/START4C/problems/CORTSENT)

**Author:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Manan Grover](https://www.codechef.com/users/mexomerf)

**Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

None

# PROBLEM:

Chef knows two languages spoken in Chefland but isn’t proficient in any of them. The first language contains characters [a?m] and the second language contains characters [N?Z].

Given K words of the sentence as S_1, S_2,…, S_K tell whether it is a possible sentence framed by Chef, i.e, it contains only the characters from the two given languages and each word contains characters from a single language.

# EXPLANATION:

We are given K words of the sentence, we just need to check whether each word belongs to exactly one language.

A word belongs to the first language if all the characters of the word belong to [a-m], and it belongs to the second language if all the characters of the word belong to [N-Z]. If a word contains the characters of both the languages or some characters are neither in language first nor in second, then the sentence is not valid.

Pseudo Code to check the word
``// s is some word of a sentence

for(auto ch: s)
{
      if(ch>='a' && ch<='m')
        fst=false;
      else if(ch>='N' && ch<='Z')
        snd=false;
      else
        ok=false;
}

if(!fst && !snd)
    ok=false;

``

# TIME COMPLEXITY:

O(|S|) per test case

where |S| is the length of sentence

# SOLUTIONS:

Setter
````

Tester
````

Editorialist
``#include<bits/stdc++.h>
using namespace std;

#define int long long

void solve()
{
  int k;
  cin>>k;

  bool ok=true;

  for(int i=0;i<k;i++)
  {
    string s;
    cin>>s;

    if(!ok)
      continue;

    bool fst=true,snd=true;

    for(auto ch: s)
    {
      if(ch>='a' && ch<='m')
        fst=false;
      else if(ch>='N' && ch<='Z')
        snd=false;
      else
        ok=false;
    }

    if(!fst && !snd)
      ok=false;
  }

  if(ok)
    cout<<"Yes"<<"\n";
  else
    cout<<"NO"<<"\n";
}

int32_t main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int t;
  cin>>t;

  while(t--)
    solve();

return 0;
}
``

</details>
