# HTML Tags

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HTMLTAGS |
| Difficulty Rating | 1441 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [HTMLTAGS](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/HTMLTAGS) |

---

## Problem Statement

In addition to Competitive Programming, Chef recently developed an interest in Web Dev and started [learning HTML](https://www.codechef.com/learn/html). Now he wants to create his own HTML Code Editor. As a subproblem, he wants to check if a typed HTML closing tag has correct syntax or not.

A closing HTML tag **must**:
- Start with `""`
- Have only lower-case alpha-numeric characters as its body (between `""`). That is, each character of the body should either be a digit or a lower-case English letter.
- Have a non-empty body.

Help Chef by printing `"Success"` if the tag is fine. If not, print `"Error"`.

---

## Input Format

- The first line contains an integer $T$, the number of test cases. Then $T$ test cases follow.
- Each test case is a single line of input, a string describing the tag.

---

## Output Format

For each test case, output in a single line, `"Success"` if it is a valid closing tag and `"Error"` otherwise (without quotes).

You may print each character of the string in uppercase or lowercase (for example, the strings `"SuccEss"`, `"success"`, `"Success"`, `"SUCCESS"` etc. will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq$ $\mathrm{length}(\mathrm{Tag})$ $\leq 1000$
- The characters of the string belong to the ASCII range $[33, 126]$ (note that this excludes space.)

---

## Examples

**Example 1**

**Input**

```text
5 
</h1>  
Clearly_Invalid  
</singlabharat>  
</5>  
<//aA>
```

**Output**

```text
Success  
Error  
Success
Success
Error
```

**Explanation**

**Test Cases $1, 3, 4$:** The tags follow all mentioned constraints.

**Test Case $2$:** The tag doesn't contain opening and closing symbols and also includes characters other than lower-case alpha-numeric characters in its body.

**Test Case $5$:** The tag also includes an upper-case alpha-numeric character `"A"` and a non alpha-numeric character `"/"` in its body.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
</h1>
```

**Output for this case**

```text
Success
```



#### Test case 2

**Input for this case**

```text
Clearly_Invalid
```

**Output for this case**

```text
Error
```



#### Test case 3

**Input for this case**

```text
</singlabharat>
```

**Output for this case**

```text
Success
```



#### Test case 4

**Input for this case**

```text
</5>
```

**Output for this case**

```text
Success
```



#### Test case 5

**Input for this case**

```text
<//aA>
```

**Output for this case**

```text
Error
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME97A/problems/HTMLTAGS)

[Contest Division 2](https://www.codechef.com/LTIME97B/problems/HTMLTAGS)

[Contest Division 3](https://www.codechef.com/LTIME97C/problems/HTMLTAGS)

[Practice](https://www.codechef.com/problems/HTMLTAGS)

**Setter:** [Bharat Singla](https://www.codechef.com/users/singlabharat)

**Tester:** [Felipe Mota](https://www.codechef.com/users/fmota)

**Editorialist:** [Aman Dwivedi](https://www.codechef.com/users/cherry0697)

# DIFFICULTY

Cakewalk

# PREREQUISITES

None

# PROBLEM:

You are given a string S. Your task is to find whether the given string S is a valid closing HTML tag or not.

A closing HTML tag **must**:

- Start with "</"

- End with ">"

- Have only, and at least 1, lower-case alpha-numeric characters as its body

Help Chef by printing Success if the tag is fine. If not, print Error.

# QUICK EXPLANATION:

We have a string S, and our goal is to find whether the given string is a valid HTML tag or not. Let us check the condition one by one:

**Case 1: It should Start with "</"**

-

It means that the first character of the given string should be **<** while the second character of this string should be **/**.

-

If the starting two characters of string S fulfill the requirement,  we will move to check another condition otherwise the string is not valid.

**Case 2: It should end with ">"**

-

It means that the last character of the given string should be **>**.

-

If the requirement is fulfilled we move to check the last condition left otherwise the string is not valid.

**Case 3: Have only, and at least 1, lower-case alphanumeric characters as its body**

-

It means the remaining characters of the string S should contain only lowercase English alphabets ora digit and there should be at least one such character in the body.

-

We can simply iterate on the remaining string and can check this condition.

If all the conditions are full-filled then the string S is considered to be valid otherwise not.

# TIME COMPLEXITY:

O(|S|) per test case

# SOLUTIONS:

Setter
``#include <bits/stdc++.h>
using namespace std;

void solve() {

    string s;
    cin >> s;
    int n = s.length();

    if (n < 4 or s.substr(0, 2) != "</" or s[n-1] != '>') {
        cout << "Error\n";
        return;
    }

    bool is_valid = true;
    for (int i = 2; i < n - 1; i++) {
        bool is_alpha = (s[i] >= 'a' and s[i] <= 'z');
        bool is_num = (s[i] >= '0' and s[i] <= '9');
        if (!is_alpha and !is_num) {
            is_valid = false;
            break;
        }
    }

    cout << (is_valid ? "Success" : "Error") << endl;
}

int main() {

    int tc;
    cin >> tc;
    while (tc--) solve();

    return 0;
}
``

Tester
``#include <bits/stdc++.h>
using namespace std;
template<typename T = int> vector<T> create(size_t n){ return vector<T>(n); }
template<typename T, typename... Args> auto create(size_t n, Args... args){ return vector<decltype(create<T>(args...))>(n, create<T>(args...)); }
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
			assert(l<=x && x<=r);
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
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t = readIntLn(1, 1000);
	while(t--){
		string s = readStringLn(1, 1000);
		for(auto c : s){
			assert(33 <= c && c <= 126);
		}
		if(s.size() > 3){
			bool ok = s[0] == '<' && s[1] == '/' && s[s.size() - 1] == '>';
			for(int i = 2; i + 1 < s.size(); i++)
				if(islower(s[i]) || isdigit(s[i]));
				else ok = false;
			cout << (ok ? "Success\n" : "Error\n");
		} else {
			cout << "Error\n";
		}
	}
	return 0;
}

``

Editorialist
``##include<bits/stdc++.h>
using namespace std;

#define int long long

void solve()
{
  bool ok = true;

  string s;
  cin>>s;

  int n=(int)s.size();

  if(n<4)
  {
    cout<<"Error"<<"\n";
    return;
  }

  if(s[0]!='<' || s[1]!='/' || s[n-1]!='>')
    ok=false;

  if(ok)
  {
    for(int i=2;i<n-1;i++)
    {
      if(!((s[i]>='a' && s[i]<='z') ||
        (s[i]>='0' && s[i]<='9')))
      {
        ok=false;
        break;
      }
    }
  }

  if(ok)
    cout<<"Success"<<"\n";
  else
    cout<<"Error"<<"\n";
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
