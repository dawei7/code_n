# Mutated Minions

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHN15A |
| Difficulty Rating | 777 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [CHN15A](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHN15A) |

---

## Problem Statement

Gru has not been in the limelight for a long time and is, therefore, planning something particularly nefarious. Frustrated by his minions' incapability which has kept him away from the limelight, he has built a transmogrifier — a machine which mutates minions.

Each minion has an intrinsic characteristic value (similar to our DNA), which is an integer. The transmogrifier adds an integer **K** to each of the minions' characteristic value.

Gru knows that if the new characteristic value of a minion is divisible by 7, then it will have Wolverine-like mutations.

Given the initial characteristic integers of **N** minions, all of which are then transmogrified, find out how many of them become Wolverine-like.

---

## Input Format

The first line contains one integer, **T**, which is the number of test cases. \
Each test case contains of $2$ lines of input.
- The first line contains two integers **N** and **K**, as described in the statement
- The next line contains **N** integers, which denote the initial characteristic values for the minions

---

## Output Format

For each testcase, output one integer in a new line, which is the number of Wolverine-like minions after the transmogrification.

---

## Constraints

- **1 ≤ T ≤ 100**

- **1 ≤ N ≤ 100**

- **1 ≤ K ≤ 100**

- All initial characteristic values lie between 1 and 105, both inclusive.

---

## Examples

**Example 1**

**Input**

```text
1
5 10
2 4 1 35 1
```

**Output**

```text
1
```

**Explanation**

After transmogrification, the characteristic values become {12,14,11,45,11}, out of which only 14 is divisible by 7. So only the second minion becomes Wolverine-like.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Contest](http://www.codechef.com/ACMCHN15/problems/CHN15A)

[Practice](https://www.codechef.com/problems/CHN15A)

**Author:** [Arjun Arul](http://www.codechef..com/users/arjunarul)

**Tester:** [Kevin Atienza](http://www.codechef.com/users/kevinsogo)

**Editorialist:** [Kevin Atienza](http://www.codechef.com/users/kevinsogo)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

Modulo operation

### PROBLEM:

There are N minions, each having a characteristic value. Each minion is transmogrified. The transmogrifier adds an integer K to the minion’s characteristic value. If a minion’s new characteristic value is divisible by 7, then it will have Wolverine-like mutations.

How many of them become Wolverine-like after all of them are transmogrified?

### EXPLANATION:

This is the easiest problem in the contest, so straightforward solutions will likely pass.

Simply loop through all N characteristic values, counting the numbers which when increased by K becomes divisible by 7. Checking whether a number is divisible by another number can be done with the [modulo operation], written as `a % b` in most programming languages (including C++ and Java). Here are a few implementations:

C++:

``#include <iostream>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    while (cases--) {
        int n, k, ans = 0;
        cin >> n >> k;
        while (n--) {
            int a;
            cin >> a;
            if ((a + k) % 7 == 0) ans++;
        }
        cout << ans << endl;
    }
    return 0;
}
``

Java:

``import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        for (int cas = 0; cas < cases; cas++) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            int ans = 0;
            for (int i = 0; i < n; i++) {
                int a = sc.nextInt();
                if ((a + k) % 7 == 0) ans++;
            }
            System.out.println(ans);
        }
    }
}
``

# Common errors

This is the easiest problem in the contest. However, that doesn’t mean nothing can go wrong with your submission. Lots of things can go wrong, from major problems down to simple gaffes such as choosing the wrong language while submitting! You must be prepared to handle these mistakes, because debugging is part of a programmer’s life, and in fact usually takes more time than actual coding.

One common error is forgetting to initialize variables, as in the following:

``#include <iostream>
using namespace std;

int main() {
    int cases, n, k, a, ans = 0;
    cin >> cases;
    while (cases--) {
        cin >> n >> k;
        while (n--) {
            cin >> a;
            if ((a + k) % 7 == 0) ans++;
        }
        cout << ans << endl;
    }
    return 0;
}
``

This one is also quite misleading because the line `ans = 0` makes you think that the `ans` variable is being initialized properly. However, it’s outside the loop, so it doesn’t reset to `0` for the following test case! Consequently, your program will most likely get wrong answers for all but the first test case. Quite a few participants made this mistake!

One way to detect this is possibly to add an identical test case in your sample input. If the answers you got are different, then most likely something’s wrong. Also, to be sure, declare variables only on scopes they’re needed, as shown in the examples above.

Another error is allocating an array too small for the input sequence. Remember that when given constraints such as N \le 100, judges will most likely test out extremes, so allocating an array of size 10 will not be enough. Some participants also made this mistake and got a “Runtime error” verdict.

If you want to be extra cautious, you could allocate a larger array, say 111 or even 300. But in this particular problem, you can forgo allocating any array altogether and simply calculate the answer on the fly (throwing away each input value after using it), as is shown in the examples above. Note however that you can’t do that in most problems.

# Readability

Another way to help you debug your code is to ensure your code is readable and clear. This includes formatting your code properly and possibly adding a few comments. In general, try to put yourself in your teammate’s shoe and see if he/she will understand the code just by reading it, without you explaining it.

Also, remember, simplicity is important. There’s no need for very advanced programming patterns for something as simple as this. If you check the examples above, you find that they’re simple and straight to the point, and it also has the desirable consequence of being clear and readable.

# Miscellanea

Here we mention other common errors and things to remember.

- Don’t forget to print a newline at the end of each test case! To be sure, try it yourself first with a couple of test cases and see if they output as expected. Command line tools such as `diff` or `fc` are helpful for this task and guards against manual checking which is unreliable.

- Use zero-indexing. It’s idiomatic in many languages including C, C++ and Java. Even though some problems use one-indexing, it’s usually helpful to convert to zero indexing in most languages, especially if you’re gonna use some builtin functions that assume zero indexing.

- Don’t print unnecessary stuff like "Please enter the number of test cases: ". These are considered part of your output and so your solution will be marked wrong. The goal is to *exactly match* the contents of the judge’s output file. Note that this includes extra lines and spaces, etc.!

- You don’t need to check whether `1 <= n && n <= 100`, etc. because *these constraints are guaranteed*. You just assume that they are true and try to solve the given problem.

- Some submissions read the input as “k n” instead of the correct “n k”. This would most likely mean that you’re reading the input incorrectly and you won’t get a correct answer. In general, pay careful attention to the problem statement and input format.

- Make sure that your program works as expected by trying out a couple of test cases. In particular, don’t submit code that doesn’t compile. It will cost you penalty points if you eventually solve the problem (not to mention real time lost).

- Submit the source code, not the compiled output!

**Language-specific things**

- When copy-pasting Java code to be submitted to CodeChef, use `Main` as your public class name (as stated in [https://www.codechef.com/wiki/sample-solutions](https://www.codechef.com/wiki/sample-solutions) ). It’s because Java requires the file name and public class name to be the same, but since you copy-pasted code, CodeChef doesn’t know the public class name and could have a harder time figuring it out from code. It’s easier to just assume it’s something, say, `Main`.

- In C++, always return 0 in the `main` function, because returning something else means you’re signalling an error, and even if your code outputs correctly, you might receive a “Runtime error” verdict.

**Contest-specific stuff**

These are things usually good to be done during contests but are worth keeping in mind that they are considered bad practice in industry code.

- In Java, there are times when some methods have checked exceptions, such as `IOException` for `BufferedReader.readLine()`, requiring you to handle them with bulky `try`-`catch` blocks. In these cases, you can just declare `throws Exception` in your main method. This is very much not recommended in production code, but in a contest, it’s very convenient.

- In Java, instead of importing each class separately, you can import everything from a single package using “import *”, e.g. `import java.util.*;`. Of course this is not recommended at work because it makes it harder to keep track of where each used class is defined, but during contests you don’t really need to worry about it.

- Instead of having to type `std::cin` all the time, you can add `using namespace std` in your C++ code so you can just use `cin`. It’s also considered [bad practice](http://stackoverflow.com/questions/1452721/why-is-using-namespace-std-considered-bad-practice) in real life. Nonetheless, it’s also convenient, makes code a bit clearer, and can cut down typing time. Even then, people using it must be wary, because problems such as [this](http://stackoverflow.com/questions/2712076/how-to-use-an-iterator/2712125#2712125) and [this](http://stackoverflow.com/questions/13402789/confusion-about-pointers-and-references-in-c) might occur.

### Time Complexity:

O(N)

### AUTHOR’S AND TESTER’S SOLUTIONS:

[setter](http://www.codechef.com/download/Solutions/ACMCHN15/Setter/CHN15A.cpp)

[tester](http://www.codechef.com/download/Solutions/ACMCHN15/Tester/CHN15A.cpp)

</details>
