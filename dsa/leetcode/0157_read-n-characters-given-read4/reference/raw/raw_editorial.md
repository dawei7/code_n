[TOC]

## Solution

---

### Overview

**Interview Tendencies: Google and Facebook**

A long time ago, long ago, so long ago that no one can remember, algorithm interview questions were less popular. Ten years ago big companies mainly filtered the candidates by the university ranks, and the interview questions were like [please describe how DDR memory works](https://hexus.net/tech/tech-explained/ram/702-ddr-ii-how-it-works/).

Nowadays there are some tendencies to merge this "old-style interview" with the modern algorithm questions interview. The idea is to ask a question that 
sounds like algorithmic but checks your knowledge of how computers work: [Round-robin CPU scheduling](https://en.wikipedia.org/wiki/Round-robin_scheduling), [C10k problem first solved by nginx](https://en.wikipedia.org/wiki/C10k_problem), etc. 

> Is it good or bad? That's a reality to deal with, especially if we speak about Google or Facebook interviews.

**Read N Characters Given Read4**

Back to the problem, the question is "How does the memory work":

- Because of the physical implementation, loading 4 bytes in DDR is faster than loading 1 byte 4 times.

- On the majority of computers today, a collection of 4 bytes, or 32 bits, is called a _word_. Most modern CPUs are optimized for the operations with _words_. 

To sum up, the problem is a practical low-level question. The standard approach (Approach 1) to solve it using the _internal_ buffer of 4 characters:

File -> Internal Buffer of 4 Characters -> Buffer of N Characters.

![img](images/internal.png)
*Figure 1. Approach 1: solution with an internal buffer.*


Once it's done, and you show your understanding of memory operations, the follow-up question is how to speed up. The answer (Approach 2) is quite straightforward. If it's possible, do not use the internal buffer of 4 characters to avoid the double copy:

File -> Buffer of N Characters.

![img](images/no_internal2.png)
*Figure 2. Approach 2: solution without internal buffer.*


<br />
<br />


---
### Approach 1: Use Internal Buffer of 4 Characters

![img](images/internal.png)
*Figure 3. Solution with internal buffer.*


**Algorithm**

Let's use an internal buffer of 4 characters to solve this problem:

File -> Internal Buffer of 4 Characters -> Buffer of N Characters.

- Initialize the number of copied characters `copiedChars = 0`, and the number of read characters: `readChars = 4`. It's convenient to initialize `readChars` to `4` and then use `readChars != 4` as EOF marker. 

- Initialize an internal buffer of 4 characters: `buf4`.

- While the number of copied characters is less than N: `copiedChars < n` and there are still characters in the file: `readChars == 4`:

    - Read from the file into the internal buffer: `readChars = read4(buf4)`.
    
    - Copy the characters from internal buffer `buf4` into main buffer `buf` one by one. Increase `copiedChars` after each character. If the number of copied characters is equal to N: `copiedChars == n`, interrupt the copy process and return `copiedChars`.

**Implementation**


```python
class Solution:
    def read(self, buf: List[str], n: int) -> int:
        copied_chars = 0
        read_chars = 4
        buf4 = [""] * 4

        while copied_chars < n and read_chars == 4:
            read_chars = read4(buf4)

            for i in range(read_chars):
                if copied_chars == n:
                    return copied_chars
                buf[copied_chars] = buf4[i]
                copied_chars += 1

        return copied_chars
```


**Complexity Analysis**

* Time complexity: $$O(N)$$ to copy N characters.

* Space complexity: $$O(1)$$ to keep `buf4` of 4 elements.

<br />
<br />


---
### Approach 2: Speed Up: No Internal Buffer

![img](images/one_buf.png)
*Figure 4. Solution without internal buffer.*


This solution is mainly suitable for the languages (C, C++, Golang) where pointers allow to append directly to the primary buffer `buf`. 

**Algorithm**

1. Initialize: 
   - The number of copied characters `copiedChars` as `0`.
   - The number of read characters `readChars` as `4`.
   - The number of remaining characters that we want to read `remainingChars` as `n`. 
2. While number of remaining characters that we want to read is greater than or equal to 4 and the number of read characters equals 4:
   - Read from the file directly into the buffer (`read4(buf + copiedChars)`). 
   - Increase the count of `copiedChars` by the number of characters read.
3. We break from the while loop either when we run out of characters to read (`readChars != 4`) or when there are less than `4` characters left that we want to read. Why break when `remainingChars` is less than `4`? Because if we only want to read say `2` more characters, and there are `3` or more characters remaining in the given file, then we will end up writing more than `n` characters to `buf`.
4. So when there are less than 4 characters that we want to read, we will use an internal buffer **only once** and read exactly `remainingChars` from that buffer into `buf`. 
5. Finally, `buf` will either contain **exactly** `n` characters, or there were less than `n` characters in the file and we read all of the characters. So we will return the minimum value of `n` and `copiedChars` since this represents exactly how many characters were stored in `buf`. 

**Implementation**


```python
class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        copiedChars = 0
        readChars = 4
        remainingChars = n

        # While there are at least 4 characters remaining to be read and the last
        # call to readChars returned 4 characters, write directly to buf.
        while remainingChars >= 4 and readChars == 4:
            buf4 = [""] * 4
            readChars = read4(buf4)
            for i in range(readChars):
                buf[copiedChars + i] = buf4[i]
            copiedChars += readChars

        # If there are between 1 and 3 characters that we still want to read and
        # readChars was not 0 last time we called read4, then create a buffer
        # for just this one call so we can ensure buf does not overflow.
        if remainingChars > 0 and readChars != 0:
            buf4 = [""] * 4
            readChars = read4(buf4)

            for i in range(min(remainingChars, readChars)):
                buf[copiedChars + i] = buf4[i]
            copiedChars += readChars

        return min(n, copiedChars)
```


**Complexity Analysis**

* Time complexity: $$O(N)$$ to copy N characters.

* Space complexity: $$O(1)$$.