[TOC]

## Solution

--- 

### Overview

In this problem, we have been given strings (i.e. a word) in an array `words`.   
We need to check: when all these words are written in a matrix with each row having one word, does the $k^{th}$ row of the matrix match the $k^{th}$ column?

![show_using_image](images/Slide1.PNG)

---

### Approach 1: Storing New Words

#### Intuition

We can start this problem by thinking of generating and storing the new words, (i.e. words represented by each column) and then matching them with the respective row's words.

We will take an empty strings array `newWords` and fill it by generating new words by iterating on the matrix column-wise.   
In the end, we will check if both the array's words at the same index match or not. 

Get a brief idea through this slideshow:

!?!../Documents/422/slideshow1.json:1024,768!?!

<br />

Also we can make note of two facts:  

**First, to form a valid square the number of rows and columns must be equal.**   
Let's say we have two words with 3 and 2 characters respectively. Thus, columns will represent 3 words but rows will represent only 2 words so we can't make a valid square in this case.

**Second, in a valid square, the first row must have the most characters**   
Let's say the second row has $6$ characters and the first row has only $5$ characters.    
Thus, the word represented by the $5^{th}$ index column has the first character empty but not the next character(s), so to match the $5^{th}$ index column with the $5^{th}$ index row, the word represented by the row should also have the first character empty (a whitespace), but this is not possible, as given the constraints the row characters will only have alphabetic characters from `'a'` to `'z'`.

![show_using_image_2](images/Slide25.PNG)

Thus, the first row will denote the number of columns in our matrix and if the first row has less characters than any other row, the matrix won't be a valid square. 



#### Algorithm

1. Initialize variables:
    - `cols` to `0`, used to store the maximum number of characters of any word in the matrix.
    - `rows` to `words.size()`, used to store the number of rows in the matrix.
    - `newWords`, an empty string array to store new words represented by each column of the matrix.
2. Iterate over all elements in the `words` array and store the length of the maximum length word in `cols` which will be the number of columns in the matrix. 
3. If the first row doesn't have the maximum number of characters or the number of rows is not equal to the number of columns, we can't form a valid square thus we can return `false`.
4. For each column `col` from `0` to `cols - 1`:
    - We initialize an empty string variable `newWord`.
    - Then, we iterate over each row `row`, and if a character exists at the current position `(row, col)` in the matrix we append it in `newWord`.
    - After generating the word `newWord` represented by the current column `col`, we store it in `newWords` array.
5. At the end, if `newWords` and `words` have the same elements at the same index we return `true`, otherwise return `false`.

#### Implementation



```python
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        cols = 0
        rows = len(words)
        new_words = []
        
        for word in words:
            cols = max(cols, len(word))

        # If the first row doesn't have maximum number of characters, or
        # the number of rows is not equal to columns it can't form a square.
        if cols != len(words[0]) or rows != cols:
            return False

        for col in range(cols):
            new_word = []
            # Iterate on each character of column 'col'.
            for row in range(rows):
                # If the current row's word's size is less than the column number it means this column is empty,
                # or, if there is a character present then use it to make the new word.
                if col < len(words[row]):
                    new_word.append(words[row][col])
            # Push the new word of column 'col' in the list.
            new_words.append(''.join(new_word))

        # Check if all row's words match with the respective column's words.
        return words == new_words
```



#### Complexity Analysis

Here, $n$ is the number of strings in the `words` array and $m$ is the maximum length of a string.

* Time complexity: $O(n \cdot m)$          
  - We iterate on the `words` array to find the maximum number of characters in a word in $O(n)$ time.
  - Then we iterate over each element of a column to form a word which will take $O(n)$ time, so for $m$ columns, it will take $O(n \cdot m)$ time.
  - At the end, we compare strings at same index in `words` and `newWords` arrays which will take $O(m)$ time for each index, so for $n$ strings, we will take $O(n \cdot m)$ time.
  - Thus, overall we take $O(n \cdot m)$ time.
                    
* Space complexity: $O(n \cdot m)$   
  - We are storing $n$ strings of length $m$ in an additional array. 
  - Thus, we use $O(n \cdot m)$ space.         

---

### Approach 2: Iterate on the Matrix

#### Intuition

The previous approach is fairly efficient in terms of run-time and will be accepted, but we can still optimize it further.  
We were generating and storing the words represented by each column and then we were comparing them with words represented by rows. Instead, we can directly iterate over the $k^{th}$ row and column characters simultaneously and check if all positions have the same characters or not without storing them. 

This will help in saving computation time like generating new words and comparing them at the end, and the space used to store them.

We will keep a variable `wordNum` to represent the index of the row and column and a variable `currPos` to point to the current index of the word of the current row and column. Then we will increment `currPos` to match all characters of the current row and column.
If all characters match we move to the next word, thus incrementing `wordNum` and checking again.


You can get a brief idea of it with this slideshow:

!?!../Documents/422/slideshow2.json:1024,768!?!

<br />

#### Algorithm

1. Initialize variables, 
    - `wordNum`, representing the number of the row and column of the current word.  
    - `charPos`, representing the index of the current character of the `wordNum` word.
2. Iterate over each `wordNum` from `0` to `words.size() - 1`, representing the number of each word:
    - Then we iterate over each character `charPos` from `0` to `words[wordNum].size() - 1`:
        - If `currPos` is greater than or equal to `words.size()`, that is, the word represented by the `wordNum`-th row is larger than the respective column's word, or
        - if `wordNum` is greater than or equal to `words[charPos].size()`, that is, the word represented by the `wordNum`-th column is larger than the respective row's word, or
        - if the character at index `(wordNum, charPos)` does not match character at index `(charPos, wordNum)` in matrix, then we return `false`.
3. At the end all words represented by each row would have matched with words represented by respective columns, thus we will return `true`.

#### Implementation



```python
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for word_num in range(len(words)):
            for char_pos in range(len(words[word_num])):
                # char_pos (curr 'row' word) is bigger than column word, or
                # word_num (curr 'column' word) is bigger than row word, or 
                # characters at index (word_num,char_pos) and (char_pos,word_num) are not equal.
                if char_pos >= len(words) or \
                    word_num >= len(words[char_pos]) or \
                    words[word_num][char_pos] != words[char_pos][word_num]:
                    return False
        return True
```



#### Complexity Analysis

Here, $n$ is the number of strings in the $words$ array and $m$ is the maximum length of a string.

* Time complexity: $O(n \cdot m)$          
  - We iterate over all characters of a word represented by a row and column which will take $O(m)$ time, thus for $n$ rows we will take $O(n \cdot m)$ time.
                    
* Space complexity: $O(1)$   
  - We are not using any auxiliary space.