# Button Pairs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | UWCOI20B |
| Difficulty Rating | 1309 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [UWCOI20B](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/UWCOI20B) |

---

## Problem Statement

Using his tip-top physique, Kim has now climbed up the mountain where the base is located. Kim has found the door to the (supposedly) super secret base. Well, it is super secret, but obviously no match for Kim's talents.

The door is guarded by a row of $N$ buttons. Every button has a single number $A_i$ written on it. Surprisingly, more than one button can have the same number on it. Kim recognises this as Soum's VerySafe door, for which you need to press two buttons to enter the password. More importantly, the sum of the two numbers on the buttons you press must be odd. Kim can obviously break through this door easily, but he also wants to know how many different pairs of buttons he can pick in order to break through the door.

Can you help Kim find the number of different pairs of buttons he can press to break through the door?

Note: Two pairs are considered different if any of the buttons pressed in the pair is different (by position of the button pressed). Two pairs are not considered different if they're the same position of buttons, pressed in a different order.

Please refer to the samples for more details.

###Input:

- The first line contains a single integer $T$, representing the number of testcases. $2T$ lines follow, 2 for each testcase.
- For each testcase, the first line contains a single integer $N$, the number of buttons.
- The second line of each testcase contains $N$ space-separated integers, $A_1, A_2, \ldots, A_N$, representing the numbers written on each button.

###Output:

Print a single number, $K$, representing the number of pairs of buttons in $A$ which have an odd sum.

###Subtasks

For all subtasks,  $1 \leq T \leq 10$, $1 \leq N \leq 100000$, and $1 \leq A_i \leq 100000$ for all $A_i$.

Subtask 1 [15 points] : $N \leq 2$, There are at most 2 buttons

Subtask 2 [45 points] : $N \leq 1000$, There are at most 1000 buttons

Subtask 3 [40 points] : No additional constraints.

---

## Examples

**Example 1**

**Input**

```text
3
4
3 5 3 4
2
5 7
1
4
```

**Output**

```text
3
0
0
```

**Explanation**

This section uses 1-indexing.

In the first sample, the buttons are: $[3, 5, 3, 4]$

$A[1] +  A[4] = 3 + 4 = 7$ which is odd.
$A[2] +  A[4] = 5 + 4 = 9$ which is odd.
$A[3] +  A[4] = 3 + 4 = 7$ which is odd.

In total, there are 3 pairs with an odd sum, so the answer is 3.

In the second sample, the buttons are: $[5, 7]$. There are no odd pairs, so the answer is $0$.

In the third sample, the buttons are: $[4]$. There are no pairs at all, so the answer is $0$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
3 5 3 4
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
2
5 7
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
1
4
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# B. Button Pairs:

[Link to Practice](https://www.codechef.com/problems/UWCOI20B)

[Link to Contest](https://www.codechef.com/UWCOI20/problems/UWCOI20B)

***Author:***  [Soumyaditya Choudhuri (socho)](https://www.codechef.com/users/socho)

***Tester:***  [Taranpreet Singh (taran_1407)](https://www.codechef.com/users/taran_1407)

***Editorialist:***  [Soumyaditya Choudhuri (socho)](https://www.codechef.com/users/socho)

# DIFFICULTY:

SIMPLE

# PREREQUISITES:

Casework, Math

# PROBLEM:

Given an array A of length N, find the number of pairs of numbers with an odd sum.

Subtask 1 [15 points]: N \leq 2

Subtask 2 [45 points]: N \leq 1000

Subtask 3 [40 points]: N \leq 100000

# QUICK EXPLANATION:

Each pair must have an odd number and an even number, so output the product of the number of odd numbers and the number of even numbers.

# EXPLANATION:

## *Subtask 1*

For this subtask, we note that N \leq 2. This means that the array has size 1 or 2. Let’s consider the two cases:

If the array has size 1, then there are no pairs we can select. As a result, the answer must be 0.

Otherwise, if the array has size 2, then there is only one possible pair. We check if the sum of the two numbers in the array is odd. If it is, we output 1. If it is not, we output 0.

## *Subtask 2*

For this subtask, we note that N \leq 1000. This means that the array has size at most 1000, and a solution running in O(N^2) should pass. To solve this subtask, we use a naive solution. We maintain a counter of the number of pairs with an odd sum, initialised at 0.

We loop through every possible pair in the input, using two nested for loops. If the pair has an odd sum, we add one to our counter. At the end, we output the value of our counter.

## *Subtask 3*

In the final subtask, we note that N \leq 100000. Our O(N^2) solution will probably not pass for the subtask. For this, we attempt to do a little bit of casework.

We consider the different possibilities for the pair of numbers. Specifically, we note the parities of every combination:

- If we add an even number to an even number, we get an even number.

- If we add an odd number to an odd number, we get an even number.

- If we add an odd number to an even number, we get an odd number.

In particular, we notice that only the third case is important, when we add one odd number and one even number. We must find the number of occurrences of the third case.

We see that the pairs must contain one even and one odd number. In particular, if there are E even numbers in the array, and O odd numbers in the array, then the number of valid pairs will be E * O (there are E possible values of the even number in the pair and O possible values of the odd number). This solution obtains a perfect score for this task.

# SOLUTIONS:

Setter's Solution
``#include "bits/stdc++.h"
using namespace std;

void solve() {

	long long n;
	cin >> n;
	long long odd = 0;
	long long even = 0;
	for (long long i=0; i<n; i++) {
		long long x;
		cin >> x;
		if (x % 2 == 0) even++;
		else odd++;
	}

	cout << odd * even << endl;

}

int main() {

	int t;
	cin >> t;
	while (t--) solve();

}
``

Tester's Solution
``    import java.math.BigInteger;
    import java.util.*;
    import java.io.*;
    import java.text.*;
    public class Main{
        //SOLUTION BEGIN
        //Into the Hardware Mode
        void pre() throws Exception{}
        void solve(int TC)throws Exception {
            int n = ni();
            int[] c = new int[2];
            for(int i = 0; i< n; i++)c[ni()%2]++;
            pn(c[0]*(long)c[1]);
        }
        //SOLUTION END
        void hold(boolean b)throws Exception{if(!b)throw new Exception("Hold right there, Sparky!");}
        void exit(boolean b){if(!b)System.exit(0);}
        long IINF = (long)1e15;
        final int INF = (int)1e9+2, MX = (int)2e6+5;
        DecimalFormat df = new DecimalFormat("0.00000000000");
        double PI = 3.141592653589793238462643383279502884197169399, eps = 1e-7;
        static boolean multipleTC = true, memory = true, fileIO = false;
        FastReader in;PrintWriter out;
        void run() throws Exception{
            if(fileIO){
                in = new FastReader("");
                out = new PrintWriter("");
            }else {
                in = new FastReader();
                out = new PrintWriter(System.out);
            }
            //Solution Credits: Taranpreet Singh
            int T = (multipleTC)?ni():1;
            pre();
            for(int t = 1; t<= T; t++)solve(t);
            out.flush();
            out.close();
        }
        public static void main(String[] args) throws Exception{
            if(memory)new Thread(null, new Runnable() {public void run(){try{new Main().run();}catch(Exception e){e.printStackTrace();}}}, "1", 1 << 28).start();
            else new Main().run();
        }
        int find(int[] set, int u){return set[u] = (set[u] == u?u:find(set, set[u]));}
        int digit(long s){int ans = 0;while(s>0){s/=10;ans++;}return ans;}
        long gcd(long a, long b){return (b==0)?a:gcd(b,a%b);}
        int gcd(int a, int b){return (b==0)?a:gcd(b,a%b);}
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

</details>
