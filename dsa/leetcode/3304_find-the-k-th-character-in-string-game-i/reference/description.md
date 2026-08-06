## Description

Alice and Bob are playing a game. Initially, Alice has a string `word = "a"`.

You are given a **positive** integer `k`.

Now Bob will ask Alice to perform the following operation **forever**:

<ul>
	<li>Generate a new string by **changing** each character in `word` to its **next** character in the English alphabet, and **append** it to the *original* `word`.</li>
</ul>

For example, performing the operation on `"c"` generates `"cd"` and performing the operation on `"zb"` generates `"zbac"`.

Return the value of the `k^th` character in `word`, after enough operations have been done for `word` to have **at least** `k` characters.
