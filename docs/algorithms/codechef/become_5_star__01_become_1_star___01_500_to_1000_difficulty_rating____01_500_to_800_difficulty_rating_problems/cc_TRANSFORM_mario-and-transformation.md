# Mario and Transformation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TRANSFORM |
| Difficulty Rating | 649 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [TRANSFORM](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/TRANSFORM) |

---

## Problem Statement

Mario transforms each time he eats a mushroom as follows:
- If he is currently `small`, he turns `normal`.
- If he is currently `normal`, he turns `huge`.
- If he is currently `huge`, he turns `small`.

Given that Mario was initially `normal`, find his size after eating $X$ mushrooms.

---

## Input Format

- The first line of input will contain one integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, containing one integer $X$.

---

## Output Format

For each test case, output in a single line Mario's size after eating $X$ mushrooms.

Print:
- $\texttt{NORMAL}$, if his final size is `normal`.
- $\texttt{HUGE}$, if his final size is `huge`.
- $\texttt{SMALL}$, if his final size is `small`.

You may print each character of the answer in either uppercase or lowercase (for example, the strings $\texttt{Huge}$, $\texttt{hUgE}$, $\texttt{huge}$ and $\texttt{HUGE}$ will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
2
4
12
```

**Output**

```text
SMALL
HUGE
NORMAL
```

**Explanation**

**Test case $1$:** Mario's initial size is `normal`. On eating the first mushroom, he turns `huge`. On eating the second mushroom, he turns `small`.

**Test case $2$:** Mario's initial size is `normal`. On eating the first mushroom, he turns `huge`. On eating the second mushroom, he turns `small`. On eating the third mushroom, he turns `normal`. On eating the fourth mushroom, he turns `huge`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
```

**Output for this case**

```text
SMALL
```



#### Test case 2

**Input for this case**

```text
4
```

**Output for this case**

```text
HUGE
```



#### Test case 3

**Input for this case**

```text
12
```

**Output for this case**

```text
NORMAL
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME107A/problems/TRANSFORM)

[Contest Division 2](https://www.codechef.com/LTIME107B/problems/TRANSFORM)

[Contest Division 3](https://www.codechef.com/LTIME107C/problems/TRANSFORM)

[Contest Division 4](https://www.codechef.com/LTIME107D/problems/TRANSFORM)

**Setter:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Trung Dang](https://www.codechef.com/users/kuroni)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Mario transforms each time he eats a mushroom as follows:

- If he is currently `small`, he turns `normal`.

- If he is currently `normal`, he turns `huge`.

- If he is currently `huge`, he turns `small`.

Given that Mario was initially `normal`, find his size after eating X mushrooms.

#
[](#explanation-5)EXPLANATION:

Notice that Mario’s states are arranged in a cycle of size 3. Therefore it is only necessary to do X \mod 3 transformations to achieve at his final state.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1) for each test case.

#
[](#solution-7)SOLUTION:

Setter's Solution
``#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int x;
	    cin>>x;
	    x %= 3;
	    if(x==0) cout<<"NOrMAL";
	    else if(x==1) cout<<"HUGE";
	    else cout<<"SMalL";
	    cout<<endl;
	}
	return 0;
}
``

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
// -------------------- Input Checker Start --------------------

long long readInt(long long l, long long r, char endd)
{
    long long x = 0;
    int cnt = 0, fi = -1;
    bool is_neg = false;
    while(true)
    {
        char g = getchar();
        if(g == '-')
        {
            assert(fi == -1);
            is_neg = true;
            continue;
        }
        if('0' <= g && g <= '9')
        {
            x *= 10;
            x += g - '0';
            if(cnt == 0)
                fi = g - '0';
            cnt++;
            assert(fi != 0 || cnt == 1);
            assert(fi != 0 || is_neg == false);
            assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
        }
        else if(g == endd)
        {
            if(is_neg)
                x = -x;
            if(!(l <= x && x <= r))
            {
                cerr << l << ' ' << r << ' ' << x << '\n';
                assert(false);
            }
            return x;
        }
        else
        {
            assert(false);
        }
    }
}

string readString(int l, int r, char endd)
{
    string ret = "";
    int cnt = 0;
    while(true)
    {
        char g = getchar();
        assert(g != -1);
        if(g == endd)
            break;
        cnt++;
        ret += g;
    }
    assert(l <= cnt && cnt <= r);
    return ret;
}

long long readIntSp(long long l, long long r) { return readInt(l, r, ' '); }
long long readIntLn(long long l, long long r) { return readInt(l, r, '\n'); }
string readStringLn(int l, int r) { return readString(l, r, '\n'); }
string readStringSp(int l, int r) { return readString(l, r, ' '); }
void readEOF() { assert(getchar() == EOF); }

vector<int> readVectorInt(int n, long long l, long long r)
{
    vector<int> a(n);
    for(int i = 0; i < n - 1; i++)
        a[i] = readIntSp(l, r);
    a[n - 1] = readIntLn(l, r);
    return a;
}

// -------------------- Input Checker End --------------------
string s[3]={"NORMAL","HUGE","SMALL"};
void solve(){
	int n;n=readInt(1,100,'\n');
	cout << s[n%3] << '\n';
}
int main(){
	ios::sync_with_stdio(false);
	int t;t=readInt(1,100,'\n');while(t--) solve();readEOF();
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<string> states = {"normal", "huge", "small"};
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        cout << states[n % 3] << '\n';
    }
}
``

</details>
