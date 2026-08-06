## Description

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

<ul>
	<li>`'a'` maps to `".-"`,</li>
	<li>`'b'` maps to `"-..."`,</li>
	<li>`'c'` maps to `"-.-."`, and so on.</li>
</ul>

For convenience, the full table for the `26` letters of the English alphabet is given below:

```

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
```

Given an array of strings `words` where each word can be written as a concatenation of the Morse code of each letter.

<ul>
	<li>For example, `"cab"` can be written as `"-.-..--..."`, which is the concatenation of `"-.-."`, `".-"`, and `"-..."`. We will call such a concatenation the **transformation** of a word.</li>
</ul>

Return *the number of different **transformations** among all words we have*.
