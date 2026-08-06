## Description

You are given a **0-indexed** binary string `s` and two integers `minJump` and `maxJump`. In the beginning, you are standing at index `0`, which is equal to `'0'`. You can move from index `i` to index `j` if the following conditions are fulfilled:

<ul>
	<li>`i + minJump <= j <= min(i + maxJump, s.length - 1)`, and</li>
	<li>`s[j] == '0'`.</li>
</ul>

Return `true`* if you can reach index *`s.length - 1`* in *`s`*, or *`false`* otherwise.*
