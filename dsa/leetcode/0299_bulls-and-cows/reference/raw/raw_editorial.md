[TOC]

## Solution

---

### Overview

At first glance, this popular Google question seems to be easy. The only difficulty here is to define how to count.

- To count bulls, one could parse both strings and count the matches, and that's the correct way to do things.

![img](images/bulls2.png)
*Figure 1. Count bulls.*


- To count cows, one could parse `guess` string and count the characters which are present in the string `secret` but located in the wrong positions. Though the cows are more complicated creatures than bulls. For some test cases, it might work.

![img](images/bulls2.png)
*Figure 2. Count cows.*


- Although, in general, one has to count the characters as well. For example, if `secret` contains just one digit "4" then the maximum number of 4-cows is 1. Even if `guess` contains many "4"s. In the following example, only one of two "4"s should be counted as a cow. 

![img](images/cows.png)
*Figure 3. Only one of two "4"s should be counted as "4-cow".*

 
To figure out these three points is enough to solve the problem. 
   
In this article, we start from a straightforward two-pass solution that already has the best time ($$\mathcal{O}(N)$$) and space complexity ($$\mathcal{O}(1)$$).

As a follow-up, we implement a one-pass solution and discuss some Java-related optimizations in approach 2. 

### Approach 1: HashMap: Two Passes

**Algorithm**

- Initialize the number of bulls and cows to zero.

- Initialize the hashmap `character -> its frequency` for the string `secret`. This hashmap could be later used during the iteration over the string `guess` to keep the available characters. 

- It's time to iterate over the string `guess`.

    - If the current character `ch` of the string `guess` is in the string `secret`: `if ch in h`, then there could be two situations.
        
        - The corresponding characters of two strings match: `ch == secret[idx]`.
        
            - Then it's time to update the bulls: `bulls += 1`. 
            
            - The update of the cows is needed if the count for the current character in the hashmap is negative or equal to zero. That means that before it was already used for cows, and the cows counter should be decreased: `cows -= int(h[ch] <= 0)`.
        
        - The corresponding characters of two strings don't match: `ch != secret[idx]`. Then increase the cows counter: `cows += int(h[ch] > 0)`.
        
        - In both cases, one has to update the hashmap, marking the current character as used: `h[ch] -= 1`.

- Return the number of bulls and cows.



![Slide 1](images/slideshow_299_LIS_299_slide_1.png)

![Slide 2](images/slideshow_299_LIS_299_slide_2.png)

![Slide 3](images/slideshow_299_LIS_299_slide_3.png)

![Slide 4](images/slideshow_299_LIS_299_slide_4.png)

![Slide 5](images/slideshow_299_LIS_299_slide_5.png)

![Slide 6](images/slideshow_299_LIS_299_slide_6.png)

![Slide 7](images/slideshow_299_LIS_299_slide_7.png)

![Slide 8](images/slideshow_299_LIS_299_slide_8.png)

![Slide 9](images/slideshow_299_LIS_299_slide_9.png)

![Slide 10](images/slideshow_299_LIS_299_slide_10.png)



**Implementation**


```python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        h = Counter(secret)
            
        bulls = cows = 0
        for idx, ch in enumerate(guess):
            if ch in h:
                # corresponding characters match
                if ch == secret[idx]:
                    # update the bulls
                    bulls += 1
                    # update the cows 
                    # if all ch characters from secret 
                    # were used up
                    cows -= int(h[ch] <= 0)
                # corresponding characters don't match
                else:
                    # update the cows
                    cows += int(h[ch] > 0)
                # ch character was used
                h[ch] -= 1
                
        return "{}A{}B".format(bulls, cows)
```


**Complexity Analysis**

* Time complexity: $$\mathcal{O}(N)$$, we pass over the strings two times.

* Space complexity: $$\mathcal{O}(1)$$ to keep hashmap `h` which contains at most 10 elements.

<br />
<br />


---
### Approach 2: One Pass

**Intuition**

Let's optimize approach 1 by building the hashmap during the strings' parsing. That would allow us to reduce the number of passes to one.

**Algorithm**

- Initialize the number of bulls and cows to zero.

- Initialize the hashmap to count characters. During the iteration, `secret` string gives a positive contribution, and `guess` - negative contribution. 

- Iterate over the strings: `s` is the current character in the string `secret` and `g` - the current character in the string `guess`.

    - If `s == g`, update bulls counter: `bulls += 1`.
    
    - Otherwise, if `s != g`:
    
        - Update `cows` by adding 1 if so far `guess` contains more `s` characters than `secret`: `h[s] < 0`.
        
        - Update `cows` by adding 1 if so far `secret` contains more `g` characters than `guess`: `h[g] > 0`.
        
        - Update the hashmap by marking the presence of `s` character in the string `secret`: `h[s] += 1`.
        
        - Update the hashmap by marking the presence of `g` character in the string `guess`: `h[g] -= 1`.

- Return the number of bulls and cows.

**Implementation**


```python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        h = defaultdict(int)
        bulls = cows = 0

        for idx, s in enumerate(secret):
            g = guess[idx]
            if s == g: 
                bulls += 1
            else:
                cows += int(h[s] < 0) + int(h[g] > 0)
                h[s] += 1
                h[g] -= 1
                
        return "{}A{}B".format(bulls, cows)
```


To further optimize the Java solution, one could use an array instead of a hashmap because there are known problems with [Java HashMap performance](https://github.com/vavr-io/vavr/issues/571). Another small improvement is to replace string concatenation with a StringBuilder.


```java
class Solution {
    public String getHint(String secret, String guess) {
        int[] h = new int[10];
            
        int bulls = 0, cows = 0;
        int n = guess.length();
        for (int idx = 0; idx < n; ++idx) {
            char s = secret.charAt(idx);
            char g = guess.charAt(idx);
            if (s == g) {
                bulls++;    
            } else {
                if (h[s - '0'] < 0) 
                    cows++;
                if (h[g - '0'] > 0)
                    cows++;
                h[s - '0']++;
                h[g - '0']--;
            }
        } 
                
        StringBuilder sb = new StringBuilder();
        sb.append(bulls); 
        sb.append("A"); 
        sb.append(cows); 
        sb.append("B");
        return sb.toString();
    }
}
```


**Complexity Analysis**

* Time complexity: $$\mathcal{O}(N)$$, we do one pass over the strings.

* Space complexity: $$\mathcal{O}(1)$$ to keep hashmap (or array) `h` which contains at most 10 elements.

<br />
<br />


---