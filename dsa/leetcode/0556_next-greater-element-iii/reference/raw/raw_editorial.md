[TOC]

## Solution

---
### Approach #1 Brute Force

To solve the given problem, we treat the given number as a string, $$s$$. In this approach, we find out every possible permutation of list formed by the elements of the string $$s$$ formed. We form a list of strings, $$list$$, containing all the permutations possible. Then, we sort the given $$list$$ to find out the permutation which is just larger than the given one. But this one will be a very naive approach, since it requires us to find out every possible permutation which will take really long time.

<!---iframe src="https://leetcode.com/playground/UBNhHzjo/shared" frameBorder="0" name="UBNhHzjo" width="100%" height="515"></iframe>--->


```java
public class Solution {
    public String swap(String s, int i0, int i1) {
        if (i0 == i1)
            return s;
        String s1 = s.substring(0, i0);
        String s2 = s.substring(i0 + 1, i1);
        String s3 = s.substring(i1 + 1);
        return s1 + s.charAt(i1) + s2 + s.charAt(i0) + s3;
    }
    ArrayList < String > list = new ArrayList < > ();
    void permute(String a, int l, int r) {
        int i;
        if (l == r)
            list.add(a);
        else {
            for (i = l; i <= r; i++) {
                a = swap(a, l, i);
                permute(a, l + 1, r);
                a = swap(a, l, i);
            }
        }
    }
    public int nextGreaterElement(int n) {
        String s = "" + n;
        permute(s, 0, s.length() - 1);
        Collections.sort(list);
        int i;
        for (i = list.size() - 1; i >= 0; i--) {
            if (list.get(i).equals("" + n))
                break;
        }
        return i == list.size() - 1 ? -1 : Integer.parseInt(list.get(i + 1));
    }
}
```


**Complexity Analysis**

* Time complexity : $$O(n!)$$. A total of $$n!$$ permutations are possible for a number consisting of $$n$$ digits.

* Space complexity : $$O(n!)$$. A total of $$n!$$ permutations are possible for a number consisting of $$n$$ digits, with each permutation consisting of $$n$$ digits.


---
### Approach #2 Linear Solution

**Algorithm**

In this case as well, we consider the given number $$n$$ as a character array $$a$$.
First, we observe that for any given sequence that is in descending order, no next larger permutation is possible.
 For example, no next permutation is possible for the following array:
 ```
 [9, 5, 4, 3, 1]
 ```

We need to find the first pair of two successive numbers $$a[i]$$ and $$a[i-1]$$, from the right, which satisfy
 $$a[i] > a[i-1]$$. Now, no rearrangements to the right of $$a[i-1]$$ can create a larger permutation since that subarray consists of numbers in descending order.
 Thus, we need to rearrange the numbers to the right of $$a[i-1]$$ including itself.

Now, what kind of rearrangement will produce the next larger number? We want to create the permutation just larger than the current one. Therefore, we need to replace the number $$a[i-1]$$ with the number which is just larger than itself among the numbers lying to its right section, say $$a[j]$$.

![Next Greater Element ](images/31_nums_graph.png)


We swap the numbers $$a[i-1]$$ and $$a[j]$$. We now have the correct number at index $$i-1$$. But still the current permutation isn't the permutation
    that we are looking for. We need the smallest permutation that can be formed by using the numbers only to the right of $$a[i-1]$$. Therefore, we need to place those
     numbers in ascending order to get their smallest permutation.

But, recall that while scanning the numbers from the right, we simply kept decrementing the index
      until we found the pair $$a[i]$$ and $$a[i-1]$$ where,  $$a[i] > a[i-1]$$. Thus, all numbers to the right of $$a[i-1]$$ were already sorted in descending order.
      Furthermore, swapping $$a[i-1]$$ and $$a[j]$$ didn't change that order.
      Therefore, we simply need to reverse the numbers following $$a[i-1]$$ to get the next smallest lexicographic permutation.

The following animation will make things clearer:

<!--![Next Permutation](images/31_Next_Permutation.gif)-->


![Slide 1](images/slideshow_556_Next_Greater_Element_III_556_Next_Greater_Element_IIISlide1.PNG)

![Slide 2](images/slideshow_556_Next_Greater_Element_III_556_Next_Greater_Element_IIISlide2.PNG)

![Slide 3](images/slideshow_556_Next_Greater_Element_III_556_Next_Greater_Element_IIISlide3.PNG)

![Slide 4](images/slideshow_556_Next_Greater_Element_III_556_Next_Greater_Element_IIISlide4.PNG)

![Slide 5](images/slideshow_556_Next_Greater_Element_III_556_Next_Greater_Element_IIISlide5.PNG)

![Slide 6](images/slideshow_556_Next_Greater_Element_III_556_Next_Greater_Element_IIISlide6.PNG)

![Slide 7](images/slideshow_556_Next_Greater_Element_III_556_Next_Greater_Element_IIISlide7.PNG)

![Slide 8](images/slideshow_556_Next_Greater_Element_III_556_Next_Greater_Element_IIISlide8.PNG)

![Slide 9](images/slideshow_556_Next_Greater_Element_III_556_Next_Greater_Element_IIISlide9.PNG)

![Slide 10](images/slideshow_556_Next_Greater_Element_III_556_Next_Greater_Element_IIISlide10.PNG)

![Slide 11](images/slideshow_556_Next_Greater_Element_III_556_Next_Greater_Element_IIISlide11.PNG)

![Slide 12](images/slideshow_556_Next_Greater_Element_III_556_Next_Greater_Element_IIISlide12.PNG)

![Slide 13](images/slideshow_556_Next_Greater_Element_III_556_Next_Greater_Element_IIISlide13.PNG)

![Slide 14](images/slideshow_556_Next_Greater_Element_III_556_Next_Greater_Element_IIISlide14.PNG)



<!--iframe src="https://leetcode.com/playground/uSrWDrPW/shared" frameBorder="0" name="uSrWDrPW" width="100%" height="515"></iframe>-->


```java

public class Solution {
    public int nextGreaterElement(int n) {
        char[] a = ("" + n).toCharArray();
        int i = a.length - 2;
        while (i >= 0 && a[i + 1] <= a[i]) {
            i--;
        }
        if (i < 0)
            return -1;
        int j = a.length - 1;
        while (j >= 0 && a[j] <= a[i]) {
            j--;
        }
        swap(a, i, j);
        reverse(a, i + 1);
        try {
            return Integer.parseInt(new String(a));
        } catch (Exception e) {
            return -1;
        }
    }
    private void reverse(char[] a, int start) {
        int i = start, j = a.length - 1;
        while (i < j) {
            swap(a, i, j);
            i++;
            j--;
        }
    }
    private void swap(char[] a, int i, int j) {
        char temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
}
```


**Complexity Analysis**

* Time complexity : $$O(n)$$. In worst case, only two scans of the whole array are needed. Here, $$n$$ refers to the number of digits in the given number.

* Space complexity : $$O(n)$$. An array $$a$$ of size $$n$$ is used, where $$n$$ is the number of digits in the given number.