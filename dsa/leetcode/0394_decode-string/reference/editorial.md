[TOC]

## Solution

---
### Overview
We are given string $s$ in a particular form $k[string]$ and we have to decode it  as `string` repeated `k` times . For example,$2[b]$ is decoded as  `bb`.

 The problem seems straightforward at first glance. But the trick here is that there can be nested encoded strings like $k[string k[string]]$. For example, string s =$3[\text{a2}[c]]$. In such cases, we must decode the innermost string and continue in an outward direction until the entire string is decoded.

 ![img](images/decode_overview.png)

If you have solved similar problem such as [Evaluate Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) or [Simplify Path](https://leetcode.com/problems/simplify-path/) , it is clear that [Stack Data Structure](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))  is best suited to implement such problems. We could implement a stack data structure or recursively build the solution by using an internal call stack. Let's understand both approaches in detail.

---
### Approach 1: Using Stack

**Intuition**

We have to decode the result in a particular pattern. We know that the input is always valid. The pattern begins with a number `k`, followed by opening braces `[`, followed by `string`. Post that, there could be one of the following cases :
1) There is another nested pattern $k[string k[string]]$
2) There is a closing bracket  $k[string]$

Since we have to start decoding the innermost pattern first, continue iterating over the string `s`, pushing each character to the stack until it is not a closing bracket `]`.  Once we encounter the closing bracket `]`, we must start decoding the pattern.

As we know that stack follows the Last In First Out (LIFO) Principle, the top of the stack would have the data we must decode.

**Algorithm**

The input can contain an alphabet `(a-z)`, digit `(0-9)`, opening braces `[` or closing braces `]`. Start traversing string `s` and process each character based on the following rules:

Case 1) Current character is not a closing bracket `]`.

Push the current character to stack.

Case 2) Current character is a closing bracket `]`.

Start decoding the last traversed string by popping the string `decodedString` and number `k` from the top of the stack.
- Pop from the stack while the next character is not an opening bracket `[` and append each character (`a-z`) to the `decodedString`.
- Pop opening bracket `[` from the stack.
- Pop from the stack while the next character is a digit `(0-9)` and build the number `k`.

Now that we have `k` and `decodedString` , decode the pattern $k[decodedString]$  by pushing the `decodedString` to stack `k` times.

Once the entire string is traversed, pop the `result` from stack and return.

![Slide 1](images/slideshow_394_LIS_slide_1.png)

![Slide 2](images/slideshow_394_LIS_slide_2.png)

![Slide 3](images/slideshow_394_LIS_slide_3.png)

![Slide 4](images/slideshow_394_LIS_slide_4.png)

![Slide 5](images/slideshow_394_LIS_slide_5.png)

![Slide 6](images/slideshow_394_LIS_slide_6.png)

![Slide 7](images/slideshow_394_LIS_slide_7.png)

![Slide 8](images/slideshow_394_LIS_slide_8.png)

![Slide 9](images/slideshow_394_LIS_slide_9.png)

![Slide 10](images/slideshow_394_LIS_slide_10.png)

![Slide 11](images/slideshow_394_LIS_slide_11.png)

![Slide 12](images/slideshow_394_LIS_slide_12.png)

![Slide 13](images/slideshow_394_LIS_slide_13.png)

![Slide 14](images/slideshow_394_LIS_slide_14.png)

![Slide 15](images/slideshow_394_LIS_slide_15.png)

![Slide 16](images/slideshow_394_LIS_slide_16.png)

![Slide 17](images/slideshow_394_LIS_slide_17.png)

**Implementation**

```cpp
class Solution {
public:
    string decodeString(string s) {
        stack<char> st;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == ']') {
                string decodedString;
                // get the encoded string (in reverse order from stack)
                while (st.top() != '[') {
                    decodedString.push_back(st.top());
                    st.pop();
                }
                // pop '[' from stack
                st.pop();

                // get the number k
                int base = 1;
                int k = 0;
                while (!st.empty() && isdigit(st.top())) {
                    k += (st.top() - '0') * base;
                    st.pop();
                    base *= 10;
                }

                // decodedString is reversed, so fix it
                reverse(decodedString.begin(), decodedString.end());

                // push decodedString k times into stack
                while (k-- > 0) {
                    for (char c : decodedString) {
                        st.push(c);
                    }
                }
            } else {
                st.push(s[i]);
            }
        }

        // build result from stack
        string result;
        result.reserve(st.size());
        while (!st.empty()) {
            result.push_back(st.top());
            st.pop();
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
```

**Complexity Analysis**

* Time Complexity: $\mathcal{O}(\text{maxK}^{\text{countK}} \cdot n)$

  where $\text{maxK}$ is the maximum value of $k$, $\text{countK}$ is the count of nested $k$ values, and $n$ is the maximum length of the encoded string.

  Example: For $s = \texttt{20[\text{a10}[bc]]}$, $\text{maxK} = 20$, $\text{countK} = 2$ (since there are 2 nested $k$ values: `20` and `10`), and there are 2 encoded strings `a` and `bc` with the maximum encoded string length $n = 2$.

  The worst case occurs when there are multiple nested patterns. Suppose all $k$ values ($\text{maxK}$) are `10` and all encoded strings ($n$) are of size `2`.

  For $s = \texttt{10[\text{ab10}[cd]]\text{10}[ef]}$, the time complexity is roughly: $10 \cdot \texttt{cd} \cdot 10 \cdot \texttt{ab} + 10 \cdot 2 =$10^{2}$\cdot 2$

  Hence, for an encoded pattern of the form $\text{maxK[\text{nmaxK}[n]]}$, the time complexity to decode is: $\mathcal{O}(\text{maxK}^{\text{countK}} \cdot n)$

* Space Complexity: $\mathcal{O}\left(\sum (\text{maxK}^{\text{countK}} \cdot n)\right)$

  where $\text{maxK}$ is the maximum value of $k$, $\text{countK}$ is the count of nested $k$ values, and $n$ is the maximum length of the encoded string.

  The maximum stack size would be equivalent to the sum of all decoded strings of the form $\text{maxK[\text{nmaxK}[n]]}$.

---

### Approach 2: Using 2 Stack

**Intuition**

In the previous approach, we used a single character stack to store the digits`(0-9)` as well as letters `(a-z)`.
 We could instead maintain 2 separate stacks.
- `countStack`: The stack would store all the integer `k`.
- `stringStack`: The stack would store all the decoded strings.

Also, instead of pushing the decoded string to the stack character by character, we could improve our algorithm by appending all the characters into the string first and then push the entire string into the `stringStack`. Let's look at the algorithm in detail.

**Algorithm**

Iterate over the string `s` and process each character as follows:

Case 1) If the current character is a digit `(0-9)`, append it to the number `k`.

Case 2) If the current character is a letter `(a-z)`,  append it to the `currentString`.

Case 3) If current character is a opening bracket `[`, push `k` and `currentString` into` countStack` and `stringStack` respectively.

Case 4) Closing bracket `]`: We must begin the decoding process,
- We must decode the `currentString`. Pop `currentK` from the `countStack` and decode the pattern $\text{currentK}[currentString]$

- As the `stringStack` contains the previously decoded string, pop the `decodedString` from the `stringStack`.
Update the `decodedString` = `decodedString` + $\text{currentK}[currentString]$

![img](images/twoStack_diagram.png)

**Implementation**

```cpp

class Solution {
public:
    string decodeString(string s) {
        stack<int> countStack;
        stack<string> stringStack;
        string currentString;
        int k = 0;
        for (auto ch : s) {
            if (isdigit(ch)) {
                k = k * 10 + ch - '0';
            } else if (ch == '[') {
                // push the number k to countStack
                countStack.push(k);
                // push the currentString to stringStack
                stringStack.push(currentString);
                // reset currentString and k
                currentString = "";
                k = 0;
            } else if (ch == ']') {
                string decodedString = stringStack.top();
                stringStack.pop();
                // decode currentK[currentString] by appending currentString k times
                for (int currentK = countStack.top(); currentK > 0; currentK--) {
                    decodedString = decodedString + currentString;
                }
                countStack.pop();
                currentString = decodedString;
            } else {
                currentString = currentString + ch;
            }
        }
        return currentString;
    }
};

```

**Complexity Analysis**

Assume, $n$ is the length of the string $s$.
* Time Complexity: $\mathcal{O}(\text{maxK} \cdot n)$,  where $\text{maxK}$ is the maximum value of $k$ and $n$ is the length of a given string $s$. We traverse a string of size $n$ and iterate $k$ times to decode each pattern of form $\text{k[string]}$. This gives us worst case time complexity as $\mathcal{O}(\text{maxK} \cdot n)$.

* Space Complexity: $\mathcal{O}(m+n)$, where $m$ is the number of `letters(a-z)` and $n$ is the number of `digits(0-9)` in string $s$. In worst case, the maximum size of $\text{stringStack}$ and  $\text{countStack}$ could be $m$ and $n$ respectively.

---

### Approach 3: Using Recursion

**Intuition**

In the previous approach, we implemented an external stack to keep the track of each character traversed. Ideally, a stack is required when we have nested encoded string in the form $k[string k[string]]$.

Using this intuition, we could start by building `k` and `string` and recursively decode for each nested substring. The recursion uses an internal call stack to store the previous state. Let's understand the algorithm in detail.

**Algorithm**

-  Build `result` while next character is letter `(a-z)` and build the number k while next character is a digit `(0-9)` by iterating over string `s`.
- Ignore the next `[` character and recursively find the nested `decodedString`.
- Decode the current pattern $k[decodedString]$ and append it to the result.
- Return the current `result`.

The above steps are repeated recursively for each pattern until the entire string `s` is traversed.

Base Condition: We must define a base condition that must be satisfied to backtrack from the recursive call.
In this case, we would backtrack and return the `result` when we have traversed the string `s` or the next character is `]` and there is no nested substring.

Thanks to [@bluedawnstar](https://leetcode.com/bluedawnstar/) for suggesting the solution.

**Implementation**

```cpp
class Solution {
public:
    string decodeString(string s) {
        int index = 0;
        return decodeString(s, index);
    }
    string decodeString(const string& s, int& index) {
        string result;
        while (index < s.length() && s[index] != ']') {
            if (!isdigit(s[index]))
                result += s[index++];
            else {
                int k = 0;
                // build k while next character is a digit
                while (index < s.length() && isdigit(s[index]))
                    k = k * 10 + s[index++] - '0';
                // ignore the opening bracket '['
                index++;
                string decodedString = decodeString(s, index);
                // ignore the closing bracket ']'
                index++;
                while (k-- > 0)
                    result += decodedString;
            }
        }
        return result;
    }
};
```

**Complexity Analysis**

Assume, $n$ is the length of the string $s$.
* Time Complexity: $\mathcal{O}(\text{maxK} \cdot n)$ as in _Approach 2_

* Space Complexity: $\mathcal{O}(n)$. This is the space used to store the internal call stack used for recursion. As we are recursively decoding each nested pattern, the maximum depth of recursive call stack would not be more than $n$