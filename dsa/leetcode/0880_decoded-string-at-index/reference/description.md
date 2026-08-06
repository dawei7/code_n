## Description

You are given an encoded string `s`. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

<ul>
	<li>If the character read is a letter, that letter is written onto the tape.</li>
	<li>If the character read is a digit `d`, the entire current tape is repeatedly written `d - 1` more times in total.</li>
</ul>

Given an integer `k`, return *the *`k^th`* letter (**1-indexed)** in the decoded string*.
