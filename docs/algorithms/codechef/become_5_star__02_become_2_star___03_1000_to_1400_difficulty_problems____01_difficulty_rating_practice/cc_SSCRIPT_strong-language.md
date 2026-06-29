# Strong Language

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SSCRIPT |
| Difficulty Rating | 1291 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [SSCRIPT](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/SSCRIPT) |

---

## Problem Statement

A string is said to be using *strong language* if it contains at least $K$ consecutive characters '*'.

You are given a string $S$ with length $N$. Determine whether it uses strong language or not.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains a single string $S$ with length $N$.

### Output
Print a single line containing the string `"YES"` if the string contains strong language or `"NO"` if it does not (without quotes).

You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

### Constraints
- $1 \leq T \leq 10$
- $1 \leq K \leq N \leq 10^6$
- $S$ contains only lowercase English letters and characters '*'
- Sum of $N$ over all testcases is atmost $10^6$.

### Subtasks
**Subtask #1 (30 points):** $N \leq 10^4$, Sum of $N$ over all testcases is atmost $10^4$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
5 2
*a*b*
5 2
*a**b
5 1
abcde
```

**Output**

```text
NO
YES
NO
```

**Explanation**

**Example case 1:** Since there are no two consecutive characters '*', the string does not contain strong language.

**Example case 2:** There are two adjacent characters '*', so the string contains strong language.

**Example case 3:** Since there are no characters '*' in the string, it does not contain strong language.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2
*a*b*
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
5 2
*a**b
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
5 1
abcde
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SSCRIPT)

[Div-3 Contest](https://www.codechef.com/APRIL21C/problems/SSCRIPT)

***Author & Editorialist:*** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

***Testers:*** [Shubham Jain](https://www.codechef.com/users/TheOneYouWant), [Aryan Choudhary](https://www.codechef.com/users/aryanc403)

# DIFFICULTY:

Simple

# PREREQUISITES:

Running Sum

# PROBLEM:

Given a string S of length N and an integer K, tell whether there exists a substring of length K having each character as '*'.

# EXPLANATION:

**Subtask 1:** We can manually check all the possible N - K + 1 substrings of length K in \mathcal{O}(K * (N - K)) per test case.

**Subtask 2:** Assume the string starts with x_1  consecutive characters from the set [a, z] followed by x_2  consecutive characters '*' followed by x_3  consecutive characters from the set [a, z] and so on. So answer = max(x_{2i}) where i >= 1.

The values of x_i can be calculated linearly by comparing the present character with the previous character and incrementing the counter if they are the same or pushing the value of the counter in the vector and setting it to one if not. But it requires \mathcal{O}(N) extra space.

To avoid using vector, increment the counter only when the present character is a '*', else keep the value of counter as 0 and take the maximum value of the counter at each iteration as the answer.

So the final time complexity is \mathcal{O}(N) per test case.

# SOLUTIONS:

Setter's Solution
``                #include<bits/stdc++.h>

                using namespace std;

                const int maxt = 10, maxl = 1e6;

                int main()
                {
                    int t; cin >> t;
                    int tn = 0;
                    while(t--){
                        int n, k; cin >> n >> k; tn += n;
                        string s; cin >> s;
                        for(char c : s){
                            assert((c >= 'a' && c <= 'z') || c == '*');
                        }
                        int maxv = 0, cnt = 0;
                        // for(int i = 0; i <= n - k && maxv < k; i++){
                        //     if(s[i] != '*')continue;
                        //     int cnt = 0;
                        //     for(int j = i; j <= i + k - 1; j++){
                        //         if(s[j] != '*')break;
                        //         cnt++;
                        //     }
                        //     maxv = max(maxv, cnt);
                        // }
                        for(char c : s){
                            if(c == '*')cnt++;
                            else{
                                maxv = max(maxv, cnt); cnt = 0;
                            }
                        }
                        maxv = max(maxv, cnt);
                        string ans = maxv >= k ? "YeS" : "No";
                        cout << ans << endl;
                    }
                    assert(tn <= maxl);
                }
``

Tester's Solution
``                #include<bits/stdc++.h>

                using namespace std;

                const long long int mod = 1000000007L;
                long long int T,n,i,j,k,in,cnt,l,r,u,v,x,y;
                long long int m;
                string s;

                int main(void) {
                    ios_base::sync_with_stdio(false);cin.tie(NULL);
                    cin >> T;
                    while(T--)
                    {
                        cin >> n >> k >> s;
                        long long int mx=0,cnt=0;
                        for(auto x:s)
                        {
                            assert(('a'<=x&&x<='z')||(x=='*'));
                            if(x=='*')
                                cnt++;
                            else
                                cnt=0;
                            mx=max(mx,cnt);
                        }
                        cout<<(mx>=k?"YeS":"nO")<<endl;
                    }
                    return 0;
                }
``

</details>
