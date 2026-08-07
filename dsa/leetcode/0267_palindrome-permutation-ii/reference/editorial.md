[TOC]

## Solution

---
### Approach #1 Brute Force [Time Limit Exceeded]

The simplest solution is generate every possible permutation of the given string $s$ and check if the generated permutation is a palindrome. After this, the palindromic permuations can be added to a $set$ in order to eliminate the duplicates. At the end, we can return an array comprised of the elements of this $set$ as the resultant array.

Let's look at the way these permutations are generated. We make use of a recursive function `permute` which  takes the index of the current element $current_{index}$ as one of the arguments. Then, it swaps the current element with every other element in the array, lying towards its right, so as to generate a new ordering of the array elements. After the swapping has been done, it makes another call to `permute` but this time with the index of the next element in the array. While returning back, we reverse the swapping done in the current function call. Thus, when we reach the end of the array, a new ordering of the array's elements is generated.

The animation below depicts the ways the permutations are generated.

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

```java
class Solution {
    Set<String> set = new HashSet<>();

    public List<String> generatePalindromes(String s) {
        permute(s.toCharArray(), 0);
        return new ArrayList<String>(set);
    }

    public boolean isPalindrome(char[] s) {
        for (int i = 0; i < s.length; i++) {
            if (s[i] != s[s.length - 1 - i]) return false;
        }
        return true;
    }

    public void swap(char[] s, int i, int j) {
        char temp = s[i];
        s[i] = s[j];
        s[j] = temp;
    }

    void permute(char[] s, int l) {
        if (l == s.length) {
            if (isPalindrome(s)) set.add(new String(s));
        } else {
            for (int i = l; i < s.length; i++) {
                swap(s, l, i);
                permute(s, l + 1);
                swap(s, l, i);
            }
        }
    }
}
```

**Complexity Analysis**

* Time complexity : $O((n+1)!)$. A total of $n!$ permutations are possible. For every permutation generated, we need to check if it is a palindrome, each of which requires $O(n)$ time.

* Space complexity : $O(n)$. The depth of the recursion tree can go upto $n$.

---
### Approach #2 Backtracking [Accepted]

**Algorithm**

It might be possible that no palindromic permutation could be possible for the given string $s$. Thus, it is useless to generate the permutations in such a case. Taking this idea, firstly we check if a palindromic permutation is possible for $s$. If yes, then only we proceed further with generating the permutations. To check this, we make use of a hashmap $map$ which stores the number of occurences of each character(out of 128 ASCII characters possible). If the number of characters with odd number of occurences exceeds 1, it indicates that no palindromic permutation is possible for $s$. To look at this checking process in detail, look at Approach 4 of the [article](https://leetcode.com/articles/palindrome-permutation) for Palindrome Permutation.

Once we are sure that a palindromic permutation is possible for $s$, we go for the generation of the required permutations. But, instead of wildly generating all the permutations, we can include some smartness in the generation of permutations i.e. we can generate only those permutations which are already palindromes.

One idea to to do so is to generate only the first half of the palindromic string and to append its reverse string to itself to generate the full length palindromic string.

Based on this idea, by making use of the number of occurences of the characters in $s$ stored in $map$, we create a string $st$  which contains all the characters of $s$ but with the number of occurences of these characters in $st$ reduced to half their original number of occurences in $s$.

Thus, now we can generate all the permutations of this string $st$ and append the reverse of this permuted string to itself to create the palindromic permutations of $s$.

In case of a string $s$ with odd length, whose palindromic permutations are possible, one of the characters in $s$ must be occuring an odd number of times. We keep a track of this character, $ch$, and it is kept separte from the string $st$. We again generate the permutations for $st$ similarly and append the reverse of the generated permutation to itself, but we also place the character $ch$ at the middle of the generated string.

In this way, only the required palindromic permutations will be generated. Even if we go with the above idea, a lot of duplicate strings will be generated.

In order to avoid generating duplicate palindromic permutations in the first place itself, as much as possible, we can make use of this idea. As discussed in the last approach, we swap the current element with all the elements lying towards its right to generate the permutations. Before swapping, we can check if the elements being swapped are equal. If so, the permutations generated even after swapping the two will be duplicates(redundant). Thus, we need not proceed further in such a case.

See this animation for a clearer understanding.

![Slide 1](images/slideshow_267_Palindrome_Permutation_II_267_Palindrome_Permutation_IISlide1.PNG)

![Slide 2](images/slideshow_267_Palindrome_Permutation_II_267_Palindrome_Permutation_IISlide2.PNG)

![Slide 3](images/slideshow_267_Palindrome_Permutation_II_267_Palindrome_Permutation_IISlide3.PNG)

![Slide 4](images/slideshow_267_Palindrome_Permutation_II_267_Palindrome_Permutation_IISlide4.PNG)

![Slide 5](images/slideshow_267_Palindrome_Permutation_II_267_Palindrome_Permutation_IISlide5.PNG)

![Slide 6](images/slideshow_267_Palindrome_Permutation_II_267_Palindrome_Permutation_IISlide6.PNG)

![Slide 7](images/slideshow_267_Palindrome_Permutation_II_267_Palindrome_Permutation_IISlide7.PNG)

![Slide 8](images/slideshow_267_Palindrome_Permutation_II_267_Palindrome_Permutation_IISlide8.PNG)

![Slide 9](images/slideshow_267_Palindrome_Permutation_II_267_Palindrome_Permutation_IISlide9.PNG)

```java
class Solution {
    Set<String> set = new HashSet<>();

    public List<String> generatePalindromes(String s) {
        int[] map = new int[128];
        char[] st = new char[s.length() / 2];
        if (!canPermutePalindrome(s, map)) return new ArrayList<>();
        char ch = 0;
        int k = 0;
        for (int i = 0; i < map.length; i++) {
            if (map[i] % 2 == 1) ch = (char) i;
            for (int j = 0; j < map[i] / 2; j++) {
                st[k++] = (char) i;
            }
        }
        permute(st, 0, ch);
        return new ArrayList<String>(set);
    }

    public boolean canPermutePalindrome(String s, int[] map) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            map[s.charAt(i)]++;
            if (map[s.charAt(i)] % 2 == 0) count--;
            else count++;
        }
        return count <= 1;
    }

    public void swap(char[] s, int i, int j) {
        char temp = s[i];
        s[i] = s[j];
        s[j] = temp;
    }

    void permute(char[] s, int l, char ch) {
        if (l == s.length) {
            set.add(
                new String(s) +
                (ch == 0 ? "" : ch) +
                new StringBuffer(new String(s)).reverse()
            );
        } else {
            for (int i = l; i < s.length; i++) {
                if (s[l] != s[i] || l == i) {
                    swap(s, l, i);
                    permute(s, l + 1, ch);
                    swap(s, l, i);
                }
            }
        }
    }
}
```

**Complexity Analysis**

* Time complexity : $O\big((\frac{n}{2}+1)!\big)$. At most $\frac{n}{2}!$ permutations need to be generated in the worst case. Further, for each permutation generated, `string.reverse()` function will take $n/4$ time.

* Space complexity : $O(n)$. The depth of recursion tree can go upto $n/2$ in the worst case.