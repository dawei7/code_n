# Encoding Message

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ENCMSG |
| Difficulty Rating | 1027 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [ENCMSG](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/ENCMSG) |

---

## Problem Statement

Chef recently graduated Computer Science in university, so he was looking for a job. He applied for several job offers, but he eventually settled for a software engineering job at ShareChat. Chef was very enthusiastic about his new job and the first mission assigned to him was to implement a message encoding feature to ensure the chat is private and secure.

Chef has a message, which is a string $S$ with length $N$ containing only lowercase English letters. It should be encoded in two steps as follows:
- Swap the first and second character of the string $S$, then swap the 3rd and 4th character, then the 5th and 6th character and so on. If the length of $S$ is odd, the last character should not be swapped with any other.
- Replace each occurrence of the letter 'a' in the message obtained after the first step by the letter 'z', each occurrence of 'b' by 'y', each occurrence of 'c' by 'x', etc, and each occurrence of 'z' in the message obtained after the first step by 'a'.

The string produced in the second step is the encoded message. Help Chef and find this message.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains the message string $S$.

### Output
For each test case, print a single line containing one string — the encoded message.

### Constraints
- $1 \le T \le 1,000$
- $1 \le N \le 100$
- $|S| = N$
- $S$ contains only lowercase English letters

---

## Examples

**Example 1**

**Input**

```text
2
9
sharechat
4
chef
```

**Output**

```text
shizxvzsg
sxuv
```

**Explanation**

**Example case 1:** The original message is "sharechat". In the first step, we swap four pairs of letters (note that the last letter is not swapped), so it becomes "hsraceaht". In the second step, we replace the first letter ('h') by 's', the second letter ('s') by 'h', and so on, so the resulting encoded message is "shizxvzsg".

**Separated test cases**

#### Test case 1

**Input for this case**

```text
9
sharechat
```

**Output for this case**

```text
shizxvzsg
```



#### Test case 2

**Input for this case**

```text
4
chef
```

**Output for this case**

```text
sxuv
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Div1](https://www.codechef.com/COOK96A/problems/ENCMSG)

[Div2](https://www.codechef.com/COOK96B/problems/ENCMSG)

[Practice](https://www.codechef.com/problems/ENCMSG)

**Setter-** [Hasan Jaddouh](https://www.codechef.com/users/kingofnumbers)

**Tester-** [Ivan Safonov](https://www.codechef.com/users/isaf27)

**Editorialist-** [Abhishek Pandey](https://www.codechef.com/users/vijju123)

### DIFFICULTY:

CAKEWALK

### PRE-REQUISITES:

[Strings](https://www.geeksforgeeks.org/string-data-structure/), [Arrays](https://www.geeksforgeeks.org/arrays-in-c-language-set-1-introduction/), [ASCII system for characters](http://ee.hawaii.edu/~tep/EE160/Book/chap4/subsection2.1.1.1.html)

### PROBLEM:

Given a string S on N characters, we have to perform the following operations-

- swap adjacent characters. Eg- Swap 1 with 2, 3 with 4 and so on.

- swap every alphabet OF THE ORIGINAL STRING with its mirror reverse, i.e. if ASCII value of the character is K , swap it with character of ASCII value 'a'+('z'-K). Hence, 'a' is replaced by 'z', 'b' with 'y' and so on.

### QUICK EXPLANATION:

**Key to AC-** This is a majorly implementation question. Proper practice in these topics is the key to quick AC.

Swapping of the adjacent characters is trivial. The replacement of alphabets can be easily done by realizing that every alphabet is replaced by 'a'+('z'-K) counterpart, where K is ASCII value of the character.

### EXPLANATION:

This editorial will have only a single section, as its majorly an easy implementation problem. We will be discussing setter’s solution owing to its neat implementation.

**1.Setter’s solution-**

The first thing to carry out is the swap operation. Remember the kind of swapping. Let me denote character at index i with c_i. We have to swap c_0 with c_1, c_2 with c_3  and so on. Familiarity with arrays and strings is needed. You can use a temporary variable for swapping, or perhaps put [std::swap](https://en.cppreference.com/w/cpp/algorithm/swap) function from C++ STL. Both the ways are given in tab below-

Click to view

**1. Using std::swap-**

``for(int i=0;i< n-1;i+=2){
		    swap(s[i],s[i+1]);
		}
``

**2. Using temporary variable-**

``for(int i=0;i< n-1;i+=2){
			char c=s[i];
			s[i] = s[i+1];
			s[i+1] = c;
		}
``

Now all that remains is to do the alphabet replacing. We can do that trivially using the formula given above. An example is given under tab. We will replace s[i] with s[i]='a'+('z'-s[i]);

Click to view
``for(int i=0;i< n;i++){
			s[i]  = 'z' + 'a'- s[i];
		}
``

### SOLUTION:

The codes of setter and tester are pasted below in tabs for you guys to refer if the links dont work. [@admin](/u/admin) needs some time for linking solutions, hence code was pasted for your convenience.

[Setter](https://www.codechef.com/download/Solutions/COOK96/setter/ENCMSG.cpp)

Click to view
``#include <iostream>
#include <algorithm>
#include <string>
#include <assert.h>
using namespace std;

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
			assert(cnt>0);
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

int T;
int n;
string s;
int main(){
	T=readIntLn(1,1000);
	while(T--){
		n=readIntLn(1,100);
		s=readStringLn(n,n);
		for(int i=0;i<n;i++){
			assert('a'<=s[i] && s[i]<='z');
		}
		for(int i=0;i<n-1;i+=2){
			char c=s[i];
			s[i] = s[i+1];
			s[i+1] = c;
		}
		for(int i=0;i<n;i++){
			s[i]  = 'z' + 'a'- s[i];
		}
		cout<<s<<endl;
	}
	assert(getchar()==-1);
}
``

[Tester](https://www.codechef.com/download/Solutions/COOK96/tester/ENCMSG.cpp)

Click to view
``#include <bits/stdc++.h>
#include <cassert>

using namespace std;

typedef long long ll;
typedef long double ld;

// read template
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
			assert(cnt>0);
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
// end

void solve()
{
	int n;// = readIntLn(1, 100);
	cin >> n;
	string s;// = readStringLn(n, n);
	cin >> s;
	assert((int)s.size() == n);
	bool ch = true;
	for (int i = 0; i < n; i++) ch &= ('a' <= s[i] && s[i] <= 'z');
	assert(ch);
	for (int i = 0; i < n - 1; i += 2) swap(s[i], s[i + 1]);
	for (int i = 0; i < n; i++) s[i] = (char)((int)'a' + (int)'z' - (int)s[i]);
	cout << s << "\n";
}

int main()
{
	int T;// = readIntLn(1, 1000);
	cin >> T;
	while (T--) solve();
	//assert(getchar() == -1);
	return 0;
}
``

Time Complexity= O(N)

### CHEF VIJJU’S CORNER

**1.** Some contestants wrote a logic similar to below while coding for swapping part-

``for(int i=0;i< n-1;i++){
			char c=s[i];
			s[i] = s[i+1];
			s[i+1] = c;
		}
``

Is something wrong there? :o

**2.** This time, we were able to derive a formula. What if, this wouldnt be possible? What if mapping would had been random, eg - Replace ‘a’ with ‘g’, ‘h’ with ‘i’, ‘b’ with also ‘g’ , or perhaps what if mapping would be given in input? Its easy still! Just make an array of size 26 and store which alphabet is i'th one mapped to. Meaning, table[i] would store the character to which alphabet with ASCII 'a'+i gets mapped to. Now, another version, what if I say that the characters are upto {10}^{9}, but only {10}^{5} are used and need to be mapped? I want to bring [std::map](https://www.google.com/search?q=std+map&rlz=1C1DIMA_enIN688IN688&oq=std+map&aqs=chrome..69i57j0l5.1335j0j4&sourceid=chrome&ie=UTF-8) data structure to your attention.

</details>
