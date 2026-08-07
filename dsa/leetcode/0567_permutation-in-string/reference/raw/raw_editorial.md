[TOC]

## Solution

---
### Approach 1: Brute Force

> Note: This approach is included because it is a logical first step towards building an efficient solution. However, it is a brute-force approach and is not expected to pass all test cases. Readers are still recommended to read it because it helps to understand the following approaches.

**Algorithm**

The simplest method is to generate all the permutations of the short string  and to check if the generated permutation is a substring of the longer string.

In order to generate all the possible pairings, we make use of a function `permute(string_1, string_2, current_index)`. This function creates all the possible permutations of the short string $$s1$$.

To do so, permute takes the index of the current element $$current\_index$$ as one of the arguments. Then, it swaps the current element with every other element in the array, lying towards its right, so as to generate a new ordering of the array elements. After the swapping has been done, it makes another call to permute but this time with the index of the next element in the array. While returning back, we reverse the swapping done in the current function call.

Thus, when we reach the end of the array, a new ordering of the array's elements is generated. The following animation depicts the process of generating the permutations.



![Slide 1](images/slideshow_561_Array_561_ArraySlide1.PNG)

![Slide 2](images/slideshow_561_Array_561_ArraySlide2.PNG)

![Slide 3](images/slideshow_561_Array_561_ArraySlide3.PNG)

![Slide 4](images/slideshow_561_Array_561_ArraySlide4.PNG)

![Slide 5](images/slideshow_561_Array_561_ArraySlide5.PNG)

![Slide 6](images/slideshow_561_Array_561_ArraySlide6.PNG)

![Slide 7](images/slideshow_561_Array_561_ArraySlide7.PNG)

![Slide 8](images/slideshow_561_Array_561_ArraySlide8.PNG)

![Slide 9](images/slideshow_561_Array_561_ArraySlide9.PNG)

![Slide 10](images/slideshow_561_Array_561_ArraySlide10.PNG)

![Slide 11](images/slideshow_561_Array_561_ArraySlide11.PNG)



**Implementation**


```java
public class Solution {
    boolean flag = false;

    public boolean checkInclusion(String s1, String s2) {
        permute(s1, s2, 0);
        return flag;
    }

    public String swap(String s, int i0, int i1) {
        if (i0 == i1)
            return s;
        String s1 = s.substring(0, i0);
        String s2 = s.substring(i0 + 1, i1);
        String s3 = s.substring(i1 + 1);
        return s1 + s.charAt(i1) + s2 + s.charAt(i0) + s3;
    }

    void permute(String s1, String s2, int l) {
        if (l == s1.length()) {
            if (s2.indexOf(s1) >= 0)
                flag = true;
        } else {
            for (int i = l; i < s1.length(); i++) {
                s1 = swap(s1, l, i);
                permute(s1, s2, l + 1);
                s1 = swap(s1, l, i);
            }
        }
    }
}
```


**Complexity Analysis**

Let $$n$$ be the length of $$s1$$

* Time complexity: $$O(n!)$$. The permute method generates all possible permutations of the string `s1`. In a permutation problem, the number of ways to permute a string of length $n$ is $n!$. Each recursive call swaps characters at different positions to explore every possible permutation at each level of recursion. At the first level, there are $n$ choices for which character to place in the first position. At the second level, there are $n−1$ choices for which character to place in the second position, and so on, leading to $n!$ total recursive calls.

* Space complexity: $$O(n^2)$$. The depth of the recursion tree is $$n$$($$n$$ refers to the length of the short string `s1`). Every node of the recursion tree contains a string of max. length $$n$$.

---

### Approach 2: Using sorting:

**Algorithm**

The idea behind this approach is that one string will be a permutation of another string only if both of them contain the same characters the same number of times. One string $$x$$ is a permutation of other string $$y$$ only if $$sorted(x)=sorted(y)$$.

In order to check this, we can sort the two strings and compare them.  We sort the short string $$s1$$ and all the substrings of $$s2$$, sort them and compare them with the sorted $$s1$$ string. If the two matches completely, $$s1$$'s permutation is a substring of $$s2$$, otherwise not.

**Implementation**


```java
public class Solution {
    public boolean checkInclusion(String s1, String s2) {
        s1 = sort(s1);
        for (int i = 0; i <= s2.length() - s1.length(); i++) {
            if (s1.equals(sort(s2.substring(i, i + s1.length()))))
                return true;
        }
        return false;
    }

    public String sort(String s) {
        char[] t = s.toCharArray();
        Arrays.sort(t);
        return new String(t);
    }
}
```


**Complexity Analysis**

Let $$l_1$$ be the length of string $$s_1$$ and $$l_2$$ be the length of string $$s_2$$.

* Time complexity: $O((l_2 - l_1) \cdot l_1 \log l_1)$.

  First, we sort $s_1$ which takes $O(l_1 \log l_1)$. Then, we iterate through a range of $(l_2 - l_1 + 1)$ and within the loop, we sort a substring of length $l_1$. This process takes $O((l_2 - l_1 + 1) \cdot l_1 \log l_1)$ time. Overall, we combine both time complexities: $O((l_2 - l_1 + 1 + 1) \cdot l_1 \log l_1) \rightarrow O((l_2 - l_1) \cdot l_1 \log l_1)$

* Space complexity: $O(l_1 + S)$. $t$ array is used.

    Some extra space is used when we sort an array of size $n$ in place. The space complexity of the sorting algorithm ($S$) depends on the programming language. The value of $S$ depends on the programming language and the sorting algorithm being used:
    - In Python, the sort method sorts a list using the Timsort algorithm which is a combination of Merge Sort and Insertion Sort and has a space complexity of $O(n)$
    - In C++, the `sort()` function is implemented as a hybrid of Quick Sort, Heap Sort, and Insertion Sort, with a worst-case space complexity of $O( \log n )$
    - In Java, `Arrays.sort()` is implemented using a variant of the Quick Sort algorithm which has a space complexity of $O( \log n)$

    Thus, the total space complexity of the algorithm is $O(l_1 + S)$.

---

### Approach 3: Using Hashmap

**Algorithm**

As discussed above, one string will be a permutation of another string only if both of them contain the same characters with the same frequency. We can consider every possible substring in the long string $$s2$$ of the same length as that of $$s1$$ and check the frequency of occurence of the characters appearing in the two. If the frequencies of every letter match exactly, then only $$s1$$'s permutation can be a substring of $$s2$$.

In order to implement this approach, instead of sorting and then comparing the elements for equality, we make use of a hashmap $$s1map$$ which stores the frequency of occurence of all the characters in the short string $$s1$$. We consider every possible substring of $$s2$$ of the same length as that of $$s1$$, find its corresponding hashmap as well, namely $$s2map$$. Thus, the substrings considered can be viewed as a window of length as that of $$s1$$ iterating over $$s2$$. If the two hashmaps obtained are identical for any such window, we can conclude that $$s1$$'s permutation is a substring of $$s2$$, otherwise not.

**Implementation**


```java
public class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length())
            return false;
        HashMap<Character, Integer> s1map = new HashMap<>();

        for (int i = 0; i < s1.length(); i++)
            s1map.put(s1.charAt(i), s1map.getOrDefault(s1.charAt(i), 0) + 1);

        for (int i = 0; i <= s2.length() - s1.length(); i++) {
            HashMap<Character, Integer> s2map = new HashMap<>();
            for (int j = 0; j < s1.length(); j++) {
                s2map.put(s2.charAt(i + j), s2map.getOrDefault(s2.charAt(i + j), 0) + 1);
            }
            if (matches(s1map, s2map))
                return true;
        }
        return false;
    }

    public boolean matches(HashMap<Character, Integer> s1map, HashMap<Character, Integer> s2map) {
        for (char key : s1map.keySet()) {
            if (s1map.get(key) - s2map.getOrDefault(key, -1) != 0)
                return false;
        }
        return true;
    }
}
```


**Complexity Analysis**

Let $$l_1$$ be the length of string $$s_1$$ and $$l_2$$ be the length of string $$s_2$$.

* Time complexity: $O(l_1 + (26 + l_1) \cdot (l_2 - l_1))$

  The initialization of the map `s1map` takes $O(l_1)$ since we loop through each character of $s_1$ once and store the counts.

  The outer loop runs $(l_2 - l_1 + 1)$ times, as we need to consider each possible substring of length $l_1$ within $s_2$.

  For each iteration of the outer loop, we build `s2map`, which takes $O(l_1)$ time (since we process $l_1$ characters for each substring in $s_2$).

  In the `matches` function, we iterate through `s1map` to compare it with `s2map`. This takes $O(26) = O(1)$, as the alphabet size is constant (26 characters). Thus, checking equality of the two maps involves a constant-time comparison for each character in the alphabet.

  Thus, the total time complexity becomes: $O(l_1 + (26 + l_1) \cdot (l_2 - l_1))$.

* Space complexity: $O(l_2 - l_1)$

  Each substring from $s_2$ of length $l_1$ creates a `HashMap` (`s2map`) to store the character frequencies.

  The size of this `HashMap` is $O(26)$, since there are at most 26 characters in the alphabet.

  Over $l_2 - l_1 + 1$ iterations of the outer loop, we create one such `HashMap` per iteration, resulting in $O(26 \cdot (l_2 - l_1 + 1))$ space usage.

  We also create a `HashMap` for $s_1$ (`s1map`), which similarly takes $O(26)$ space.

  Since we need to store a `HashMap` for each of the $l_2 - l_1 + 1$ substrings in the worst case, the space complexity is proportional to the number of substrings and the size of each `HashMap`.

  Therefore, the total space complexity is: $O(26 \cdot (l_2 - l_1 + 1) + 26) = O(26 \cdot (l_2 - l_1 + 1))$. In simplified terms: $O(l_2 - l_1)$

---

### Approach 4: Using Array [Accepted]

**Algorithm**

Instead of making use of a special HashMap datastructure just to store the frequency of occurence of characters, we can use a simpler array data structure to store the frequencies. Given strings contains only lowercase alphabets ('a' to 'z'). So we need to take an array of size 26.The rest of the process remains the same as the last approach.

**Implementation**


```java
public class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length())
            return false;
        int[] s1arr = new int[26];
        for (int i = 0; i < s1.length(); i++)
            s1arr[s1.charAt(i) - 'a']++;
        for (int i = 0; i <= s2.length() - s1.length(); i++) {
            int[] s2arr = new int[26];
            for (int j = 0; j < s1.length(); j++) {
                s2arr[s2.charAt(i + j) - 'a']++;
            }
            if (matches(s1arr, s2arr))
                return true;
        }
        return false;
    }

    public boolean matches(int[] s1arr, int[] s2arr) {
        for (int i = 0; i < 26; i++) {
            if (s1arr[i] != s2arr[i])
                return false;
        }
        return true;
    }
}
```


**Complexity Analysis**

Let $$l_1$$ be the length of string $$s_1$$ and $$l_2$$ be the length of string $$s_2$$.

* Time complexity: $O(l_1 + (26 + l_1) \cdot (l_2 - l_1))$

  The initialization of the array `s1arr` takes $O(l_1)$ since we loop through each character of $s_1$ once and store the counts.

  The outer loop runs $(l_2 - l_1 + 1)$ times, as we need to consider each possible substring of length $l_1$ within $s_2$.

  For each iteration of the outer loop, we build `s2arr`, which takes $O(l_1)$ time (since we process $l_1$ characters for each substring in $s_2$).

  In the `matches` function, we iterate through `s1arr` to compare it with `s2arr`. This takes $O(26) = O(1)$, as the alphabet size is constant (26 characters). Thus, checking equality of the two maps involves a constant-time comparison for each character in the alphabet.

  Thus, the total time complexity becomes: $O(l_1 + (26 + l_1) \cdot (l_2 - l_1))$.

* Space complexity: $O(l_2 - l_1)$

  Each substring from $s_2$ of length $l_1$ creates a array (`s2arr`) to store the character frequencies.

  The size of this array is $O(26)$, since there are at most 26 characters in the alphabet.

  Over $l_2 - l_1 + 1$ iterations of the outer loop, we create one such array per iteration, resulting in $O(26 \cdot (l_2 - l_1 + 1))$ space usage.

  We also create a array for $s_1$ (`s1arr`), which similarly takes $O(26)$ space.

  Since we need to store a array for each of the $l_2 - l_1 + 1$ substrings in the worst case, the space complexity is proportional to the number of substrings and the size of each array.

  Therefore, the total space complexity is: $O(26 \cdot (l_2 - l_1 + 1) + 26) = O(26 \cdot (l_2 - l_1 + 1))$. In simplified terms: $O(l_2 - l_1)$

---
### Approach 5: Sliding Window  [Accepted]:

**Algorithm**

Instead of building a new hashmap from scratch for every window we check in $$s2$$, we can just set up a fixed-size array of length 26 once for the first window in $$s2$$. Then, as we slide the window over, we can simply update it. Basically, we’ll remove the character that's no longer in the window and add the new one that’s now part of it. So, the array gets tweaked only at the two spots related to those two characters. Each time we update the array, we just compare all the elements to check if everything matches up for the result we want.

**Implementation**


```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s2_len, s1_len = len(s2), len(s1)

        if s1_len > s2_len:
            return False

        s1_char_freq_arr = [0] * 26
        s2_window_char_freq_arr = [0] * 26

        for index in range(s1_len):
            s1_char_freq_arr[ord(s1[index]) - ord('a')] += 1
            s2_window_char_freq_arr[ord(s2[index]) - ord('a')] += 1

        if s1_char_freq_arr == s2_window_char_freq_arr:
            return True

        for index in range(s2_len - s1_len):
            s2_window_char_freq_arr[ord(s2[index]) - ord('a')] -= 1
            s2_window_char_freq_arr[ord(s2[index + s1_len]) - ord('a')] += 1

            if s1_char_freq_arr == s2_window_char_freq_arr:
                return True

        return False
```


**Complexity Analysis**

Let $$l_1$$ be the length of string $$s_1$$ and $$l_2$$ be the length of string $$s_2$$.

* Time complexity: $O(l_1 + 26 \cdot (l_2 - l_1)) = O(l_1 + (l_2 - l_1)) = O(l_2)$

  The loop that populates two frequency arrays runs for $l_1$ iterations, as it processes all characters in $s_1$ and the first $l_1$ characters in $s_2$. This step takes $O(l_1)$ time.

  The outer loop runs $l_2 - l_1$ times, sliding the window of size $l_1$ across $s_2$. For each iteration, two operations are performed:
     - Increment the count of the new character added to the window (`s2arr[s2.charAt(i + l_1) - 'a']++`).
     - Decrement the count of the character leaving the window (`s2arr[s2.charAt(i) - 'a']--`).
  Both of these operations are constant-time, $O(1)$, for each iteration since the arrays are of fixed size (26). Thus, the time complexity for this part is $O(l_2 - l_1)$.

  The `matches` function compares the two arrays element by element, which takes $O(26) = O(1)$ time because the arrays have a fixed size of 26.

  Combining the preprocessing and sliding window steps, the total time complexity is: $O(l_1 + 26 \cdot (l_2 - l_1))$

  Since $26$ is a constant, this simplifies to: $O(l_1 + (l_2 - l_1)) = O(l_2)$

* Space complexity: $O(26 + 26) = O(1)$

  Two arrays, `s1arr` and `s2arr`, are used to store character frequencies. Each array has a fixed size of 26, regardless of the lengths of $s_1$ and $s_2$. Therefore, the space used for these arrays is $O(26 + 26) = O(52) = O(1)$.

  No other data structures that depend on the size of $s_1$ or $s_2$ are used. The space required is constant, independent of the input size.

  Thus, the total space complexity is: $O(1)$

---
### Approach 6: Optimized Sliding Window [Accepted]:

**Algorithm**

The last approach can be optimized, if instead of comparing all the elements of the `s1arr` for every updated `s2arr` corresponding to every window of $$s2$$ considered, we keep a track of the number of elements which were already matching in the `s1arr` and update just the count of matching elements when we shift the window towards the right.

To do so, we maintain a `count` variable, which stores the number of characters(out of the 26 alphabets), which have the same frequency of occurence in $$s1$$ and the current window in $$s2$$. When we slide the window, if the deduction of the last element and the addition of the new element leads to a new frequency match of any of the characters, we increment the `count` by 1. If not, we keep the `count` intact. But, if a character whose frequency was the same earlier(prior to addition and removal) is added, it now leads to a frequency mismatch which is taken into account by decrementing the same `count` variable. If, after the shifting of the window, the `count` evaluates to 26, it means all the characters match in frequency totally. So, we return a True in that case immediately.

**Implementation**


```java
public class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length())
            return false;
        int[] s1arr = new int[26];
        int[] s2arr = new int[26];
        for (int i = 0; i < s1.length(); i++) {
            s1arr[s1.charAt(i) - 'a']++;
            s2arr[s2.charAt(i) - 'a']++;
        }

        int count = 0;
        for (int i = 0; i < 26; i++) {
            if (s1arr[i] == s2arr[i])
                count++;
        }

        for (int i = 0; i < s2.length() - s1.length(); i++) {
            int r = s2.charAt(i + s1.length()) - 'a', l = s2.charAt(i) - 'a';
            if (count == 26)
                return true;
            s2arr[r]++;
            if (s2arr[r] == s1arr[r]) {
                count++;
            } else if (s2arr[r] == s1arr[r] + 1) {
                count--;
            }
            s2arr[l]--;
            if (s2arr[l] == s1arr[l]) {
                count++;
            } else if (s2arr[l] == s1arr[l] - 1) {
                count--;
            }
        }
        return count == 26;
    }
}
```


**Complexity Analysis**

Let $$l_1$$ be the length of string $$s_1$$ and $$l_2$$ be the length of string $$s_2$$.

* Time complexity: $O(l_1 + (l_2 - l_1)) \approx O(l_2)$

  Populating `s1arr` and `s2arr` takes $O(l_1)$ time since we iterate over the first $l_1$ characters of both strings.

  The outer loop runs $l_2 - l_1$ times. In each iteration, we update two characters (one entering and one leaving the window) in constant time $O(1)$, and we maintain a count of matches. This step takes $O(l_2 - l_1)$.

  Checking if `count == 26` also happens in $O(1)$, since it's a constant comparison.

  Thus, the total time complexity is: $O(l_1 + (l_2 - l_1)) \approx O(l_2)$

* Space complexity: $$O(1)$$

  Two fixed-size arrays (`s1arr` and `s2arr`) of size 26 are used for counting character frequencies. No additional space that grows with the input size is used.