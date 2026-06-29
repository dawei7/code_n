# Charges

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHARGES |
| Difficulty Rating | 1645 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [CHARGES](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/CHARGES) |

---

## Problem Statement

There are $N$ subatomic particles lined up in a row. There are two types: protons and electrons. Protons have a positive charge and are represented by $1$, while electrons have a negative charge and are represented by $0$.

Our current understanding of physics gives us a way to predict how the particles will be spaced out, if we know their charges. Two adjacent particles will be separated by $1$ unit if they have opposite charges, and $2$ units if they have the same charge.

When Chef is not in the kitchen, he is doing physics experiments on subatomic particles. He is testing the hypothesis by having $N$ particles in a row, and he will change the charge of a particle $K$ times. In the $i$-th update, he will change the charge of the $Q_i$-th particle. After each update, find the distance between the first and last particle.

**Note:** Each update is persistent for further updates.

### Input

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains three lines of input.
- The first line contains two integers $N$, $K$.
- The second line contains a string $S$ of length $N$, where $S_i$ represents the initial charge on $i$-th particle.
- The third line contains $K$ integers $Q_1, Q_2, \ldots, Q_K$, the positions of the changed particles.

### Output
For each test case, output $K$ lines, where the $i$-th line contains the answer after the updates $Q_1,\ldots, Q_i$ have been made.

### Constraints
- $1 \leq T \leq 5$
- $1 \leq N, K \leq 10^5$
- $S$ contains only $0$ and $1$ characters.
- $1 \leq Q_i \leq N$
- The sum of $K$ over all testcases is at most $2 \cdot 10^5$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
3 3
010
2 1 3
```

**Output**

```text
4
3
2
```

**Explanation**

**Update 1:** After reversing the parity of particle $2$, the new configuration is $000$. Since all the particles have a similar charge, each is separated from the previous by a distance of $2$ units. So the location of particle $3$ is $2 + 2 = 4$ units from the first particle.

**Update 2:** After reversing the parity of particle $1$, the new configuration is $100$. Here, the charges of particles $1$ and $2$ differ, so they are separated by $1$ unit. The charges of particles $2$ and $3$ agree, so they are separated by $2$ units. So, the location of particle $3$ is $1 + 2 = 3$ units from the first particle.

**Update 3:** After reversing the charge of particle $3$, the new configuration is $101$. Here, particles $1$ and $2$ are separated by $1$ unit and particles $2$ and $3$ are separated by $1$ unit. So the location of particle $3$ is $1 + 1 = 2$ units from the first particle.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1 ](https://www.codechef.com/LTIME96A/problems/CHARGES)

[Contest Division 2 ](https://www.codechef.com/LTIME96B/problems/CHARGES)

[Contest Division 3 ](https://www.codechef.com/LTIME96C/problems/CHARGES)

[Practice ](https://www.codechef.com/problems/CHARGES)

**Setter:** [Daanish Mahajan ](https://www.codechef.com/users/daanish_adm)

**Tester:** [Riley Borgard](https://www.codechef.com/users/monogon)

**Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY

Cakewalk

# PREREQUISITES

Observation

# PROBLEM

Given a string S consisting of characters '0' and '1' with the first character fixed at position 0. Given K queries of the form Q_1, Q_2,…, Q_K where Q_i denotes reverse the parity of Q_ith character and print the location of Nth particle.

Assume that the same adjacent characters are 2 units apart and different adjacent characters are 1 unit apart.

# QUICK EXPLANATION

**Case 1**: N=1. Location of N^{th} characters remains same for all quries.

**Case 2**:  N>1

- Reversing the parity of 1^{st} and N^{th} character, either **increment** the location of N^{th} character by 1 or **decrement** it by 1.

- Reversing the parity of character at position P where 1< P <N.

- If the adjacent characters have different parity ( *i.e* S[P-1]!=S[P+1]), the location of the N^{th} character **doesn’t change**.

- If after changing the parity of S[P], if the adjacent character have same parity ( *i.e* S[P-1]=S[P+1]).

- If S[P]=S[P-1], means if S[P] has the same parity as its adjacent characters then the location of the N^{th} character will **increment** by 2.

- If S[P]!=S[P-1], means if S[P] has different parity compared to it’s adjacent characters then the location of the N^{th} character will **decrement** by 2.

**But why this is true?**

# EXPLANATION

Firstly we need to calculate the location of N^{th} character before performing the queries. Let L store the location of N^{th} character in the string. If the next character is the same as the previous add 2 to L else add 1 to L.

**Case 1: Proof**  - When the string length equals 1, changing the parity doesn’t change the N^{th} location as they are no other characters in the string to cause any change.

**Case 2: Proof** - N>1

- Reversing parity of character at position 1^{st} and N^{th}. Lets suppose we have S="10" and Q_1=1,Q_2=1. Initially, L=1. After performing Q_1 string S="00", and now we can see that the next character is same as the previous character ( *i.e* S[1]=S[2]) and that makes both the characters 2 units apart. Therefore, L is increment by 1 ( *i.e*  L+1=2). Now after performing Q_2 string S=“01”, and now the character S[0] and S[1] are 1 unit apart. Therefore, L is decremented by 1 ( *i.e*  L-1=1).

- Reversing the parity of character at position P where 1< P < N.

- Let’s take an example S="110" and Q_1=2. Initially L=3. Performing query Q_1 changes string  S=“100”, now we can see that previously S[1]==S[2] and now S[2]==S[3], meaning before the character at position S[2] was 2 units apart from S[1] and $1$unit apart from S[3] and now after the query is performed S[2] is 2 units apart from S[3] and 1 unit apart from S[1]. Hence, the location of N^{th} doesn’t change. So we can say that **when the adjacent characters have different parity** the **answer remains the same**.

- Let’s take an example S="010" and $Q1=2. Initially L=3. Performng query Q_1 changes string S="000". Intitally S[2] was 1 unit apart from both S[1] and S[3]. Now after the query is performed it is 2 units apart from both S[1] and S[3]. Hence, L =L+2. Now, after the query if S[P-1]==S[P]==S[P+1], then it **will increment** the L by 2. Similarly, after the query if S[P-1]==S[P+1] and S[P] has different parity then it **will decrement** the L by 2

# TIME COMPLEXITY

The time complexity is O(N) per test case.

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>

# define pb push_back
#define pii pair<int, int>
#define mp make_pair
# define ll long long int

using namespace std;

const int maxtq = 2e5, maxt = 5, maxn = 1e5, maxq = 1e5;

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int t; cin >> t;
    int tq = 0;
    while(t--){
        int n, q; cin >> n >> q; tq += q;
        string s; cin >> s;
        int len = 0; assert(s[0] == '0' || s[0] == '1');
        for(int i = 1; i < n; i++){
            assert(s[i] == '0' || s[i] == '1');
            if(s[i] == s[i - 1])len += 2;
            else len++;
        }
        int x;
        for(int i = 0; i < q; i++){
            cin >> x;
            x--;
            s[x] = s[x] == '0' ? '1' : '0';
            if(x > 0){
                if(s[x - 1] == s[x]){
                    len++;
                }else{
                    len--;
                }
            }
            if(x < n - 1){
                if(s[x + 1] == s[x]){
                    len++;
                }else{
                    len--;
                }
            }
            cout << len << endl;
        }
    }
    assert(tq <= maxtq);
}
``

Tester's Solution
``#include <bits/stdc++.h>

#define ll long long
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define vi vector<int>
#define pii pair<int, int>
#define rep(i, a, b) for(int i = (a); i < (b); i++)
using namespace std;
template<typename T>
using minpq = priority_queue<T, vector<T>, greater<T>>;

void solve() {
    int n, k;
    string s;
    cin >> n >> k >> s;
    int cnt[2] = {0, 0};
    rep(i, 1, n) {
        cnt[s[i] == s[i - 1]]++;
    }
    rep(q, 0, k) {
        int i;
        cin >> i;
        i--;
        if(i > 0) cnt[s[i] == s[i - 1]]--, cnt[s[i] != s[i - 1]]++;
        if(i < n - 1) cnt[s[i] == s[i + 1]]--, cnt[s[i] != s[i + 1]]++;
        s[i] ^= '0' ^ '1';
        cout << 2 * cnt[1] + cnt[0] << '\n';
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int te;
    cin >> te;
    while(te--) solve();
}
``

Editorialist's Solution
``#include<bits/stdc++.h>
using namespace std;

#define int long long int

void solve()
{
  int n, q;
  cin >> n >> q;
  string s;
  cin >> s;
  int location = 0;
  for (int i = 0; i < n - 1; i++)
  {
    if (s[i] == s[i + 1])
    {
      location += 2;
    }
    else {
      location++;
    }
  }

  while (q--)
  {
    int pos;
    cin >> pos;
    pos--;
    s[pos] = (s[pos] == '0' ? '1' : '0');

    if (pos == 0)
    {
      if (pos + 1 < n)
      {
        if (s[pos] == s[pos + 1])
          location++;
        else
          location--;
      }

    }
    else if (pos == n - 1)
    {
      if (pos - 1 >= 0)
      {
        if (s[pos] == s[pos - 1])
          location++;
        else {
          location--;
        }
      }

    }
    else {
      if (s[pos - 1] == s[pos + 1])
      {
        if (s[pos] == s[pos - 1])
          location += 2;
        else
          location -= 2;

      }

    }
    cout << location << endl;

  }
}
int32_t main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int t;
  cin >> t;

  while (t--)
    solve();

  return 0;
}
``

</details>
