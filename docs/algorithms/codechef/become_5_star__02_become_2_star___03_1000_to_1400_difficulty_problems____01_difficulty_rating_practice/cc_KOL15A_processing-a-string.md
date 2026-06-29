# Processing a string

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KOL15A |
| Difficulty Rating | 1125 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [KOL15A](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/KOL15A) |

---

## Problem Statement

Given an alphanumeric string made up of digits and lower case Latin characters only, find the sum of all the digit characters in the string.

### Input

- The first line of the input contains an integer **T** denoting the number of test cases. Then **T** test cases follow.

- Each test case is described with a single line containing a string **S**, the alphanumeric string.

### Output

- For each test case, output a single line containing the sum of all the digit characters in that string.

### Constraints

- **1** ≤ **T** ≤ **1000**

- **1** ≤ **|S|** ≤ **1000**, where |S| is the length of the string S.

---

## Examples

**Example 1**

**Input**

```text
1
ab1231da
```

**Output**

```text
7
```

**Explanation**

The digits in this string are 1, 2, 3 and 1. Hence, the sum of all of them is 7.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Contest](http://www.codechef.com/ACMKOL15/problems/KOL15A)

[Practice](http://www.codechef.com/problems/KOL15A)

**Author:** [Pankaj Jindal](https://www.codechef.com/users/pnkjjindal)

**Tester:** [Kevin Atienza](http://www.codechef.com/users/kevinsogo)

**Editorialist:** [Kevin Atienza](http://www.codechef.com/users/kevinsogo)

### DIFFICULTY:

Simple

### PREREQUISITES:

Type conversion, strings

### PROBLEM:

Given a string of alphanumeric characters, print the sum of the digits.

### EXPLANATION:

This is the easiest problem in the contest. Straightforward solutions will likely pass.

The idea is to iterate through the input string, filter out the non-digits, convert the digit characters into actual integers, and sum them. The following are a few sample implementations.

C:

``#include <stdio.h>

char s[1111];
int main() {
    int cases, cas, i, total;
    scanf("%d", &cases);
    for (cas = 0; cas < cases; cas++) {
        scanf("%s", s);
        total = 0;
        for (i = 0; s[i]; i++) {
            if ('0' <= s[i] && s[i] <= '9') total += s[i] - '0';
        }
        printf("%d\n", total);
    }
    return 0;
}
``

C++:

``#include <iostream>
using namespace std;

int main() {
    int cases;
    cin >> cases;
    for (int cas = 0; cas < cases; cas++) {
        string s;
        cin >> s;
        int total = 0;
        for (int i = 0; s[i]; i++) {
            if ('0' <= s[i] && s[i] <= '9') total += s[i] - '0';
        }
        cout << total << endl;
    }
    return 0;
}
``

Java:

``import java.util.Scanner;
public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        for (int cas = 0; cas < cases; cas++) {
            String s = sc.next();
            int total = 0;
            for (int i = 0; i < s.length(); i++) {
                char ch = s.charAt(i);
                if ('0' <= ch && ch <= '9') {
                    total += ch - '0';
                }
            }
            System.out.println(total);
        }
    }
}
``

# Implementation details

**How to check if a character is a digit**

All the above codes use the snippet `'0' <= ch && ch <= '9'` to determine if a character `ch` is a digit. This works because the `char` type in C, C++ and Java are implemented as a single byte representing the ASCII code of the character, and the digit characters `'0'` to `'9'` are consecutive ASCII codes. In fact, you can use a similar technique to check if `ch` is a lowercase character: `'a' <= ch && ch <= 'z'`.

**How to convert a character to an integer (if it is a digit)**

Since characters are represented simply as bytes, we can perform arithmetic with them. This gives us a way to convert a digit character to a number. To convert a digit character `ch` to a number from 0 to 9, we simply use `ch - '0'`.

Note that a character being represented as a byte is not universal. In some other languages such as Python or Ruby, characters are actually represented as strings of length one, and although comparison between chars still work, you can’t necessarily perform arithmetic between chars. For example, in Python, `'l' - 'a'` would be an error. But usually there are still ways to get the ASCII value of a character. For example, in Python, you would use the `ord` and `chr` functions to convert to and from an integer, respectively.

# Common errors

This is the easiest problem in the contest. However, that doesn’t mean nothing can go wrong with your submission. Lots of things can go wrong, from major problems down to simple gaffes such as choosing the wrong language while submitting! You must be prepared to handle these mistakes, because debugging is part of a programmer’s life, and in fact usually takes more time than actual coding.

One common error is forgetting to initialize variables, as in the following:

``#include <stdio.h>

char s[1111];
int main() {
    int cases, cas, i, total = 0;
    scanf("%d", &cases);
    for (cas = 0; cas < cases; cas++) {
        scanf("%s", s);
        for (i = 0; s[i]; i++) {
            if ('0' <= s[i] && s[i] <= '9') total += s[i] - '0';
        }
        printf("%d\n", total);
    }
    return 0;
}
``

This one could be quite misleading because the line `total = 0` initializing the `total` variable is present. It’s just that it’s outside the loop, so it doesn’t reset to `0` for the following test case! Consequently, your program will most likely get wrong answers for all but the first test case.

One way to detect this is possibly to add an identical test case in your sample input. If the answers you got are different, then most likely something’s wrong. Also, to be sure, declare variables only on scopes they’re needed, as shown in the C++ and Java examples above.

Another error is allocating an array too small for the input string. Remember that when given constraints such as |S| \le 1000, judges will most likely test out extremes, so allocating an array of size 200 will not be enough. In fact, for C or C++ an array of size 1000 might not be enough too, because strings in those languages are terminated with a null character `\0`. You need at least 1001 for the null character to be accommodated. (In fact, the examples above use 1111 just to be extra cautious.)

# Readability

Another way to help you debug your code is to ensure your code is readable and clear. This includes formatting your code properly and possibly adding a few comments. In general, try to put yourself in your teammate’s shoe and see if he/she will understand the code just by reading it, without you explaining it.

Here are some things about readability related to this problem:

- When hardcoding the digits, don’t write the ASCII values. Instead, use the actual character `'0'`, `'a'`, etc. Technically, `'0'` would work the same in most cases as `48` (`'0'`'s ASCII code), but `'0'` is much clearer than a random `48` found in code.

- Simplicity is important. There’s no need for very advanced programming patterns for something as simple as this. If you check the examples above, you find that they’re simple and straight to the point, and it also has the desirable consequence of being clear and readable.

- Some submissions convert chars to ints by first converting the char to a string and then parsing it into an int. Please don’t do that. It’s harder to read than the methods above, and is actually much more inefficient.

- If possible, try to use library functions that will help you with the task if you know them. In actual real life coding work, it always pays to check whether a particular task already has a builtin function for it or has already been implemented in a library. In our case, you could use `Character.isDigit` in Java or `isdigit` in C++ to check whether a char is a digit.

# Miscellanea

Here we mention other common errors and things to remember.

- Don’t forget to print a newline at the end of each test case! To be sure, try it yourself first with a couple of test cases and see if they output as expected. Command line tools such as `diff` or `fc` are helpful for this task and guards against manual checking which is unreliable.

- Use zero-indexing. It’s idiomatic in many languages including C, C++ and Java. Even though some problems use one-indexing, it’s usually helpful to convert to zero indexing in most languages, especially if you’re gonna use some builtin functions that assume zero indexing.

- Don’t print unnecessary stuff like "Please enter the number of test cases: ". These are considered part of your output and so your solution will be marked wrong. The goal is to *exactly match* the contents of the judge’s output file.

**Language-specific things**

- When using `scanf` to take a string, use `scanf("%s",s);` instead of the incorrect `scanf("%s",&s);`.

- When copy-pasting Java code to be submitted to CodeChef, use `Main` as your public class name (as stated in [https://www.codechef.com/wiki/sample-solutions](https://www.codechef.com/wiki/sample-solutions) ). It’s because Java requires the file name and public class name to be the same, but since you copy-pasted code, CodeChef doesn’t know the public class name and could have a harder time figuring it out from code. It’s easier to just assume it’s something, say, `Main`.

**Contest-specific stuff**

These are things usually good to be done during contests but are worth keeping in mind that they are considered bad practice in industry code.

- In Java, there are times when some methods have checked exceptions, such as `IOException` for `BufferedReader.readLine()`, requiring you to handle them with bulky `try`-`catch` blocks. In these cases, you can just declare `throws Exception` in your main method. This is very much not recommended in production code, but in a contest, it’s very convenient.

- In Java, instead of importing each class separately, you can import everything from a single package using “import *”, e.g. `import java.util.*;`. Of course this is not recommended at work because it makes it harder to keep track of where each used class is defined, but during contests you don’t really need to worry about it.

- Instead of having to type `std::cin` all the time, you can add `using namespace std` in your C++ code so you can just use `cin`. It’s also considered [bad practice](http://stackoverflow.com/questions/1452721/why-is-using-namespace-std-considered-bad-practice) in real life. Nonetheless, it’s also convenient, makes code a bit clearer, and can cut down typing time. Even then, people using it must be wary, because problems such as [this](http://stackoverflow.com/questions/2712076/how-to-use-an-iterator/2712125#2712125) and [this](http://stackoverflow.com/questions/13402789/confusion-about-pointers-and-references-in-c) might occur.

### Time Complexity:

O(N)

### AUTHOR’S AND TESTER’S SOLUTIONS:

[setter](https://www.codechef.com/download/Solutions/ACMKOL15/Setter/KOL15A.cpp)

[tester](https://www.codechef.com/download/Solutions/ACMKOL15/Setter/KOL15A.cpp)

</details>
