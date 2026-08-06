## Description

You are given the strings `key` and `message`, which represent a cipher key and a secret message, respectively. The steps to decode `message` are as follows:

<ol>
	<li>Use the **first** appearance of all 26 lowercase English letters in `key` as the **order** of the substitution table.</li>
	<li>Align the substitution table with the regular English alphabet.</li>
	<li>Each letter in `message` is then **substituted** using the table.</li>
	<li>Spaces `' '` are transformed to themselves.</li>
</ol>

<ul>
	<li>For example, given `key = "<u>**hap**</u>p<u>**y**</u> <u>**bo**</u>y"` (actual key would have **at least one** instance of each letter in the alphabet), we have the partial substitution table of (`'h' -> 'a'`, `'a' -> 'b'`, `'p' -> 'c'`, `'y' -> 'd'`, `'b' -> 'e'`, `'o' -> 'f'`).</li>
</ul>

Return *the decoded message*.
