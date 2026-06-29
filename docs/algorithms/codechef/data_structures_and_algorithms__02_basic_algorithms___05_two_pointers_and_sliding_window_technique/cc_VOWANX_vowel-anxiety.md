# Vowel Anxiety

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | VOWANX |
| Difficulty Rating | 1823 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Two-Pointer |
| Official Link | [VOWANX](https://www.codechef.com/practice/course/two-pointers/POINTERP/problems/VOWANX) |

---

## Problem Statement

Utkarsh has recently started taking English-language classes to improve his reading and writing skills. However, he is still struggling to learn English. His teacher gave him the following problem to improve his vowel-identification skills:

There is a string $S$ of length $N$ consisting of lowercase English letters only. Utkarsh has to start from the first letter of the string.
Each time he encounters a vowel (i.e. a character from the set $\{a, e, i, o, u\}$) he has to **reverse** the entire substring that came before the vowel.

Utkarsh needs help verifying his answer. Can you print the final string after performing all the operations for him?

---

## Input Format

- First line will contain $T$, number of test cases. Then $T$ test cases follow.
- The first line of each test case contains $N$, the length of the string.
- The second line contains $S$, the string itself.

---

## Output Format

For each test case, output in a single line the final string after traversing $S$ from left to right and performing the necessary reversals.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^6$
- Sum of $N$ over all test cases does not exceed $10^6$.

---

## Examples

**Example 1**

**Input**

```text
2
10
abcdefghij
7
bcadage
```

**Output**

```text
hgfeabcdij
gacbade
```

**Explanation**

**Test case $1$:** The first letter is a vowel, but there is no substring before it to reverse, so we leave it as it is. Next, we reverse `abcd` and the string becomes `dcbaefghij`. Next we reach the vowel `i` and reverse `dcbaefgh` to get the string `hgfeabcdij`.

**Test case $2$:** Initially, we reverse `bc` and the string becomes `cbadage`. Next we reach the vowel `a` and reverse `cbad` to get the string `dabcage`. Finally we reach the vowel `e` and reverse `dabcag` to get the string `gacbade`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10
abcdefghij
```

**Output for this case**

```text
hgfeabcdij
```



#### Test case 2

**Input for this case**

```text
7
bcadage
```

**Output for this case**

```text
gacbade
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START46A/problems/VOWANX)

[Contest Division 2](https://www.codechef.com/START46B/problems/VOWANX)

[Contest Division 3](https://www.codechef.com/START46C/problems/VOWANX)

[Contest Division 4](https://www.codechef.com/START46D/problems/VOWANX)

[Practice](https://www.codechef.com/problems/VOWANX)

**Setter:** [Tanveer Singh](https://www.codechef.com/users/brobat)

**Testers:** [Nishank Suresh](https://www.codechef.com/users/iceknight1093) and [Abhinav sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Tanveer Singh](https://www.codechef.com/users/brobat)

#
[](#difficulty-2)DIFFICULTY

1823

#
[](#prerequisites-3)PREREQUISITES

Two pointers

#
[](#problem-4)PROBLEM

You are given a string S of length N. Start traversing the string from the left end. Everytime you encounter a vowel, **reverse** the entire substring that came before the vowel.

Print the final string after traversing from left to right and performing all the operations.

#
[](#explanation-5)EXPLANATION

-

The brute force solution to this is to traverse the string and reverse the entire substring before any vowel. Each reversal takes O(N) time, which would make the worst-case complexity of this approach O(N^2).

-

A more efficient way is to iterate from the right end of the string, and use 2-pointers technique.

Let’s say that the initial string is S and our final string is going to be T.

A useful observation is that any character S[i] will never be reversed more times than S[i - 1], that is, no character is reversed more times than the preceding character. In particular, the last character S[N - 1] will stay at the same position, i.e. T[N - 1] = S[N - 1].

Let’s iterate from the right end of the string. This way, we can keep account of the number of vowels that have been encountered so far, as this will equal the number of reversals that need to be performed. Let the number of vowels encountered be V. What matters to us is the **parity** of V. If we encounter an even number of vowels, then there will be an even number of reversals of the current character and it should end towards the right side of the string. Similarly, if we encounter an odd number of vowels, the current character should end towards the left side of the string.

Note that iterating from the right end is the key since, the position of a character S[i] is only determined by the characters following it. If we change any of the letters in the substring S[1] to S[i - 1], it will not affect the final positions of the characters S[i] to S[N - 1].

Explanation of sample test case

Consider the sample from the problem. The initial string S = abcdefghij. Let’s start from the right end. Initially, we encounter j and place it to the right end of T. Next up, we encounter i. Since i is a vowel but it itself won’t be reversed, we place it to the right end of T. Now the final 2 letters of T have been determined, they are ij.    Moreover, the number of vowels, V = 1.

Now, the next letter is h. Since V = 1, there will be one reversal and h will go to the front of the string. Similarly, the next two letters, f and g will go towards the front of the string. The string T now statrts with hgf and ends with ij. The middle letters are yet to be determined.

Next, we encounter e, which again goes to the front of the string, but now V is incremented and becomes 2. After this d, c, b, a will go to the back of the string, as they will be reversed twice. The final string T = hgfeabcdij.

#
[](#time-complexity-6)TIME COMPLEXITY

The time complexity is O(N).

#
[](#solutions-7)SOLUTIONS

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        vector <char> s(n);
        for(int i = 0; i < n; i++) {
            cin >> s[i];
        }
        vector <char> t(n);
        int l = 0;
        int r = n - 1;
        bool start = false;
        for(int i = n - 1; i >= 0; i--) {
            if(start) {
                t[l++] = s[i];
            } else {
                t[r--] = s[i];
            }
            if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u') {
                start = !start;
            }
        }
        for(int i = 0; i < n; i++) {
            cout << t[i];
        }
        cout << '\n';
    }

    return 0;
}
``

Tester's Solution 1
``#include <bits/stdc++.h>

using namespace std;

/*

------------------------Input Checker----------------------------------

*/

long long readInt(long long l,long long r,char endd){

    long long x=0;

    int cnt=0;

    int fi=-1;

    bool is_neg=false;

    while(true){

        char g=getchar();

        if(g=='-'){

            assert(fi==-1);

            is_neg=true;

            continue;

        }

        if('0'<=g && g<='9'){

            x*=10;

            x+=g-'0';

            if(cnt==0){

                fi=g-'0';

            }

            cnt++;

            assert(fi!=0 || cnt==1);

            assert(fi!=0 || is_neg==false);

            assert(!(cnt>19 || ( cnt==19 && fi>1) ));

        } else if(g==endd){

            if(is_neg){

                x= -x;

            }

            if(!(l <= x && x <= r))

            {

                cerr << l << ' ' << r << ' ' << x << '\n';

                assert(1 == 0);

            }

            return x;

        } else {

            assert(false);

        }

    }

}

string readString(int l,int r,char endd){

    string ret="";

    int cnt=0;

    while(true){

        char g=getchar();

        assert(g!=-1);

        if(g==endd){

            break;

        }

        cnt++;

        ret+=g;

    }

    assert(l<=cnt && cnt<=r);

    return ret;

}

long long readIntSp(long long l,long long r){

    return readInt(l,r,' ');

}

long long readIntLn(long long l,long long r){

    return readInt(l,r,'\n');

}

string readStringLn(int l,int r){

    return readString(l,r,'\n');

}

string readStringSp(int l,int r){

    return readString(l,r,' ');

}

/*

------------------------Main code starts here----------------------------------

*/

const int MAX_T = 1e5;

const int MAX_N = 1e5;

const int MAX_SUM_LEN = 1e5;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

#define ff first

#define ss second

#define mp make_pair

#define ll long long

#define rep(i,n) for(int i=0;i<n;i++)

#define rev(i,n) for(int i=n;i>=0;i--)

#define rep_a(i,a,n) for(int i=a;i<n;i++)

#define pb push_back

int sum_n = 0, sum_m = 0;

int max_n = 0, max_m = 0;

int yess = 0;

int nos = 0;

int total_ops = 0;

ll mod = 1000000007;

using ii = pair<ll,ll>;

bool ifvow(char c){

    if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u') return 1;

    return 0;

}

void solve(){

    int n = readIntLn(1,1e6);

    sum_n+=n;

    string s = readStringLn(n,n);

    for(auto h:s) assert(h>='a' && h<='z');

    vector<char> v(n,'-');

    int curr = 0, cnt = 0;

    rev(i,n-1){

        if(cnt==0){

            v[i]=s[i];

        }

        else{

            int tmp = curr+(cnt&1?-1:1)*i;

            if(cnt&1) tmp--;

            v[tmp] = s[i];

        }

        if(ifvow(s[i])){

            if(cnt&1) curr-=i;

            else curr+=i;

            cnt++;

        }

    }

    rep(i,n) cout<<v[i];

    cout<<'\n';

}

signed main()

{

    #ifndef ONLINE_JUDGE

    freopen("input.txt", "r" , stdin);

    freopen("output.txt", "w" , stdout);

    #endif

    fast;

    int t = 1;

    t = readIntLn(1,1e4);

    for(int i=1;i<=t;i++)

    {

    solve();

    }

    assert(getchar() == -1);

    assert(sum_n<=1e6);

    cerr<<"SUCCESS\n";

    cerr<<"Tests : " << t << '\n';

    cerr<<"Sum of lengths : " << sum_n <<" "<<sum_m<<'\n';

    // cerr<<"Maximum length : " << max_n <<'\n';

    // // cerr<<"Total operations : " << total_ops << '\n';

    // cerr<<"Answered yes : " << yess << '\n';

    // cerr<<"Answered no : " << nos << '\n';

    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";

}
``

Tester's Solution 2
``// O(nlogn) 'brute' with treap

#include "bits/stdc++.h"

using namespace std;

struct Node {

    Node *l = 0, *r = 0;

    char val;

    int y, c = 1;

    bool rev = 0;

    Node(char _val) : val(_val), y(rand()) {}

    void recalc();

    void push();

};

int cnt(Node* n) { return n ? n->c : 0; }

void Node::recalc() { c = cnt(l) + cnt(r) + 1; }

void Node::push() {

    if (!rev) return;

    swap(l, r);

    rev = 0;

    if (l) l->rev ^= 1;

    if (r) r->rev ^= 1;

}

pair<Node*, Node*> split(Node* n, int k) {

    if (!n) return {};

    n -> push();

    if (cnt(n->l) >= k) {

        auto pa = split(n->l, k);

        n->l = pa.second;

        n->recalc();

        return {pa.first, n};

    } else {

        auto pa = split(n->r, k - cnt(n->l) - 1);

        n->r = pa.first;

        n->recalc();

        return {n, pa.second};

    }

}

Node* merge(Node* l, Node* r) {

    if (!l) return r;

    if (!r) return l;

    l -> push(); r -> push();

    if (l->y > r->y) {

        l->r = merge(l->r, r);

        l->recalc();

        return l;

    } else {

        r->l = merge(l, r->l);

        r->recalc();

        return r;

    }

}

void reverse(Node*& t, int l, int r) {

    Node *a, *b, *c;

    tie(a,b) = split(t, l); tie(b,c) = split(b, r - l);

    b -> push();

    b -> rev ^= 1;

    t = merge(a, merge(b, c));

}

int main()

{

    ios::sync_with_stdio(0); cin.tie(0);

    const string vowels = "aeiou";

    int t; cin >> t;

    while (t--) {

        int n; cin >> n;

        string s; cin >> s;

        Node *treap = new Node(s[0]);

        for (int i = 1; i < n; ++i)

            treap = merge(treap, new Node(s[i]));

        auto isvowel = [&] (char c) {

            return vowels.find(c) != string::npos;

        };

        for (int i = 1; i < n; ++i) {

            if (isvowel(s[i])) reverse(treap, 0, i);

        }

        for (int i = 0; i < n; ++i) {

            Node *x; tie(x, treap) = split(treap, 1);

            cout << x->val;

        }

        cout << '\n';

    }

}
``

Feel free to share your approach. Suggestions are welcomed as always.

</details>
