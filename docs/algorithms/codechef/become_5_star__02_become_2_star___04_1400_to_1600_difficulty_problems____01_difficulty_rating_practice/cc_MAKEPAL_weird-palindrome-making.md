# Weird Palindrome Making

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAKEPAL |
| Difficulty Rating | 1486 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [MAKEPAL](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/MAKEPAL) |

---

## Problem Statement

Naveej is from a tribe that speaks some weird language - their alphabet consists of $N$ distinct characters.
He has an array $A = [A_1, A_2, \dots, A_N]$, where $A_i$ denotes the number of occurrences of the $i$-th character with him.

He wants to make a [palindromic string](https://en.wikipedia.org/wiki/Palindrome) using **all** the characters he has (every character he has must be used in this string).

In order to make this possible, he can perform the following operation:
- Select an $i$ $(1 \le i \le N)$ and convert all occurrences of $i$-th alphabet to any other alphabet of his choice.

Note that Naveej just wants to be able to make any palindrome, as long as every character is used. For example, if $N = 2$ and $A = [2, 2]$ and we consider the characters to be $a$ and $b$, he can make both $abba$ and $baab$, but $aba$ is not allowed because it uses only $3$ characters.

Find the minimum number of operations required such that Naveej can make a palindromic string using all the characters he has. It can be proven that there always exists at least one sequence of operations allowing for the formation of a palindrome.

---

## Input Format

- The first line of input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$ - the size of the alphabet.
- The second line contains $N$ space-separated integers: $A_1, A_2, ..., A_N$, where $A_i$ is the number of occurrences of the $i$-th character with Naveej.

---

## Output Format

For each test case, output a single line containing one integer - the minimum number of operations required so that Naveej can make a palindromic string using all the characters he has.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 2 \cdot 10^5$
- $1 \leq A_i \leq 10^9$
- It is guaranteed that the sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
2
1
4
3
4 3 1
```

**Output**

```text
0
1
```

**Explanation**

- In the first test case, $N = 1$. Let the character be $a$. We can make the following palindromic string: $aaaa$.

- In the second test case, $N = 3$. Let the characters be $a$, $b$, $c$. It is initially not possible to make a palindrome with the given occurrences of the characters.
We perform 1 operation:
Convert all the occurrences of $b$ to $c$.
Then, we can make the following palindromic string: $acaccaca$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
4
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
3
4 3 1
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/NOV21A/problems/MAKEPAL)

[Contest Division 2](https://www.codechef.com/NOV21B/problems/MAKEPAL)

[Contest Division 3](https://www.codechef.com/NOV21C/problems/MAKEPAL)

[Practice](https://www.codechef.com/problems/MAKEPAL)

**Setter:** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

**Tester:** [Samarth Gupta](https://www.codechef.com/users/samarth2017)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Simple

#
[](#prerequisites-3)PREREQUISITES

Basic Maths

#
[](#problem-4)PROBLEM

There are N characters in a language. Neeraj has an array A of length N, where A_i denotes the number of occurrences of i-th character with him. Neeraj wants to arrange these characters in form of a palindrome.

Realizing it may not always be possible, he can perform the following operation:

- Select an i (1 \leq i \leq N) and convert **all** occurrences of i-th character to any character of his choice. All occurrences must be converted to the same character.

Find the minimum number of operations required to create a palindrome.

#
[](#quick-explanation-5)QUICK EXPLANATION

- For every character appearing at least two times, we can pair two occurrences of that character with each other, appending one at the start and one at end of the string, using up two occurrences without requiring any operation.

- This can be repeated until for each character, at most one occurrence remains.

- If there are C characters having exactly one occurrence left, then \left\lfloor \frac{C}{2}\right\rfloor is the number of operations required.

#
[](#explanation-6)EXPLANATION

Let us observe a few things about palindrome. By definition, it is a string that reads the same when reading from left to right or reading from right to left. What are the implications of this

**The i^{th} character from the left must be same as i^{th} character from the right.**

Hence, the problem is to divide the given characters into pairs, such that each pair consists of the same characters. The important thing here is that pairs do not depend on each other at all.

So, for any character, while we have at least two occurrences of that character, we can make a pair, using up two occurrences, requiring no operation.

Repeating the above process on each character one by one, at most one occurrence of each character is left.

Let’s say there are exactly C characters, for which exactly one occurrence is left. Now we need to apply operations to make pairs.

Since all C characters are different, an operation affects only one character. We can pick one character, make it the same as the second character, make a pair out of those.

This way, we needed one operation to eliminate two characters. It is easy to see that this would be repeated \lfloor C/2 \rfloor times, leading to \lfloor C/2 \rfloor operations.

If C is odd, the last character would be placed at the middle of the string. All the pairs are made and \lfloor C/2 \rfloor is the number of operations applied.

###
[](#exercise-7)Exercise

Prove that C is nothing, but the number of odd integers in the given array A. So this problem can be solved even without storing array A, only counting the number of odd integers in A.

#
[](#time-complexity-8)TIME COMPLEXITY

The time complexity is O(N) per test case.

#
[](#solutions-9)SOLUTIONS

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

long long readInt(long long l, long long r, char endd) {
    long long x=0;
    int cnt=0;
    int fi=-1;
    bool is_neg=false;
    while(true) {
        char g=getchar();
        if(g=='-') {
            assert(fi==-1);
            is_neg=true;
            continue;
        }
        if('0'<=g&&g<='9') {
            x*=10;
            x+=g-'0';
            if(cnt==0) {
                fi=g-'0';
            }
            cnt++;
            assert(fi!=0 || cnt==1);
            assert(fi!=0 || is_neg==false);

            assert(!(cnt>19 || ( cnt==19 && fi>1) ));
        } else if(g==endd) {
            if(is_neg) {
                x=-x;
            }
            assert(l<=x&&x<=r);
            return x;
        } else {
            assert(false);
        }
    }
}
string readString(int l, int r, char endd) {
    string ret="";
    int cnt=0;
    while(true) {
        char g=getchar();
        assert(g!=-1);
        if(g==endd) {
            break;
        }
        cnt++;
        ret+=g;
    }
    assert(l<=cnt&&cnt<=r);
    return ret;
}
long long readIntSp(long long l, long long r) {
    return readInt(l,r,' ');
}
long long readIntLn(long long l, long long r) {
    return readInt(l,r,'\n');
}
string readStringLn(int l, int r) {
    return readString(l,r,'\n');
}
string readStringSp(int l, int r) {
    return readString(l,r,' ');
}

void readEOF(){
    assert(getchar()==EOF);
}

int main() {
    // your code goes here
    int t;
    t = readIntLn(1, 1000);
    int sum = 0;
    while(t--){
        int n = readIntLn(1, 2e5);
        sum += n;
        assert(sum <= 2e5);
        int odd = 0;
        for(int i = 0; i < n ; i++){
            int x;
            if(i == n - 1)
                x = readIntLn(1, 1e9);
            else
                x = readIntSp(1, 1e9);
            odd += (x%2);
        }
        cout << (odd/2) << '\n';
    }
    readEOF();
    return 0;
}
``

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;

long long readInt(long long l, long long r, char endd) {
    long long x=0;
    int cnt=0;
    int fi=-1;
    bool is_neg=false;
    while(true) {
        char g=getchar();
        if(g=='-') {
            assert(fi==-1);
            is_neg=true;
            continue;
        }
        if('0'<=g&&g<='9') {
            x*=10;
            x+=g-'0';
            if(cnt==0) {
                fi=g-'0';
            }
            cnt++;
            assert(fi!=0 || cnt==1);
            assert(fi!=0 || is_neg==false);

            assert(!(cnt>19 || ( cnt==19 && fi>1) ));
        } else if(g==endd) {
            if(is_neg) {
                x=-x;
            }
            assert(l<=x&&x<=r);
            return x;
        } else {
            assert(false);
        }
    }
}
string readString(int l, int r, char endd) {
    string ret="";
    int cnt=0;
    while(true) {
        char g=getchar();
        assert(g!=-1);
        if(g==endd) {
            break;
        }
        cnt++;
        ret+=g;
    }
    assert(l<=cnt&&cnt<=r);
    return ret;
}
long long readIntSp(long long l, long long r) {
    return readInt(l,r,' ');
}
long long readIntLn(long long l, long long r) {
    return readInt(l,r,'\n');
}
string readStringLn(int l, int r) {
    return readString(l,r,'\n');
}
string readStringSp(int l, int r) {
    return readString(l,r,' ');
}

void readEOF(){
    assert(getchar()==EOF);
}

int main() {
    // your code goes here
    int t;
    t = readIntLn(1, 1000);
    int sum = 0;
    while(t--){
        int n = readIntLn(1, 2e5);
        sum += n;
        assert(sum <= 2e5);
        int odd = 0;
        for(int i = 0; i < n ; i++){
            int x;
            if(i == n - 1)
                x = readIntLn(1, 1e9);
            else
                x = readIntSp(1, 1e9);
            odd += (x%2);
        }
        cout << (odd/2) << '\n';
    }
    readEOF();
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class MAKEPAL{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni();
        int[] c = new int[2];
        for(int i = 0; i< N; i++)c[ni()%2]++;
        pn(c[1]/2);
    }
    //SOLUTION END
    void hold(boolean b)throws Exception{if(!b)throw new Exception("Hold right there, Sparky!");}
    static boolean multipleTC = true;
    FastReader in;PrintWriter out;
    void run() throws Exception{
        in = new FastReader();
        out = new PrintWriter(System.out);
        //Solution Credits: Taranpreet Singh
        int T = (multipleTC)?ni():1;
        pre();for(int t = 1; t<= T; t++)solve(t);
        out.flush();
        out.close();
    }
    public static void main(String[] args) throws Exception{
        new MAKEPAL().run();
    }
    int bit(long n){return (n==0)?0:(1+bit(n&(n-1)));}
    void p(Object o){out.print(o);}
    void pn(Object o){out.println(o);}
    void pni(Object o){out.println(o);out.flush();}
    String n()throws Exception{return in.next();}
    String nln()throws Exception{return in.nextLine();}
    int ni()throws Exception{return Integer.parseInt(in.next());}
    long nl()throws Exception{return Long.parseLong(in.next());}
    double nd()throws Exception{return Double.parseDouble(in.next());}

    class FastReader{
        BufferedReader br;
        StringTokenizer st;
        public FastReader(){
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws Exception{
            br = new BufferedReader(new FileReader(s));
        }

        String next() throws Exception{
            while (st == null || !st.hasMoreElements()){
                try{
                    st = new StringTokenizer(br.readLine());
                }catch (IOException  e){
                    throw new Exception(e.toString());
                }
            }
            return st.nextToken();
        }

        String nextLine() throws Exception{
            String str = "";
            try{
                str = br.readLine();
            }catch (IOException e){
                throw new Exception(e.toString());
            }
            return str;
        }
    }
}
``

Feel free to share your approach. Suggestions are welcomed as always.

</details>
