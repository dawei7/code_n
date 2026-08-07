[TOC]

## Solution

---

### Approach 1: Hashmap

**Intuition**

The naive approach would be to construct as many `"zero"`s as it's possible from letters available in the input string, then as many `"one"`s as it's possible, etc. The problem is that the letters `"o"`, `"n"`, `"e"` could be present as well in the other numbers which mean that the straightforward approach could be misleading.

![compute](images/misleading.png)

Hence the idea is to look for something unique. One could notice all even numbers contain a unique letter :

* The letter "z" is present only in "zero".
* The letter "w" is present only in "two".
* The letter "u" is present only in "four".
* The letter "x" is present only in "six".
* The letter "g" is present only in "eight".

> Hence there is a good way to count even numbers.

That is actually the key to how to count `3`s, `5`s, and `7`s since some letters are present only in one odd and one even number (and all even numbers have already been counted) :

* The letter "h" is present only in "three" and "eight".
* The letter "f" is present only in "five" and "four".
* The letter "s" is present only in "seven" and "six".

Now one needs to count `9`s and `1`s only, and the logic is basically the same :

* Letter "i" is present in "nine", "five", "six", and "eight".
* Letter "n" is present in "one", "seven", and "nine".

**Implementation**



![Slide 1](images/slideshow_423_LIS_423_slide_2.png)

![Slide 2](images/slideshow_423_LIS_423_slide_3.png)

![Slide 3](images/slideshow_423_LIS_423_slide_4.png)

![Slide 4](images/slideshow_423_LIS_423_slide_5.png)

![Slide 5](images/slideshow_423_LIS_423_slide_6.png)

![Slide 6](images/slideshow_423_LIS_423_slide_7.png)

![Slide 7](images/slideshow_423_LIS_423_slide_8.png)

![Slide 8](images/slideshow_423_LIS_423_slide_9.png)

![Slide 9](images/slideshow_423_LIS_423_slide_10.png)

![Slide 10](images/slideshow_423_LIS_423_slide_11.png)

![Slide 11](images/slideshow_423_LIS_423_slide_12.png)

![Slide 12](images/slideshow_423_LIS_423_slide_13.png)




```python
class Solution:
    def originalDigits(self, s: 'str') -> 'str':
        # building hashmap letter -> its frequency
        count = collections.Counter(s)
        
        # building hashmap digit -> its frequency 
        out = {}
        # letter "z" is present only in "zero"
        out["0"] = count["z"]
        # letter "w" is present only in "two"
        out["2"] = count["w"]
        # letter "u" is present only in "four"
        out["4"] = count["u"]
        # letter "x" is present only in "six"
        out["6"] = count["x"]
        # letter "g" is present only in "eight"
        out["8"] = count["g"]
        # letter "h" is present only in "three" and "eight"
        out["3"] = count["h"] - out["8"]
        # letter "f" is present only in "five" and "four"
        out["5"] = count["f"] - out["4"]
        # letter "s" is present only in "seven" and "six"
        out["7"] = count["s"] - out["6"]
        # letter "i" is present in "nine", "five", "six", and "eight"
        out["9"] = count["i"] - out["5"] - out["6"] - out["8"]
        # letter "n" is present in "one", "nine", and "seven"
        out["1"] = count["n"] - out["7"] - 2 * out["9"]

        # building output string
        output = [key * out[key] for key in sorted(out.keys())]
        return "".join(output)
```


**Complexity Analysis**

* Time complexity: $$\mathcal{O}(N)$$ where `N` is the number of characters in the input string. $$\mathcal{O}(N)$$ time is needed to compute hashmap `count`
"letter -> its frequency in the input string". Then we deal with a data structure `out` which contains `10` elements only and all operations are done in a constant time.
 
* Space complexity: $$\mathcal{O}(1)$$. `count` contains a constant number of elements since the input string contains only lowercase English letters, and `out` contains not more than `10` elements.