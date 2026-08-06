## Description

Two strings are considered **close** if you can attain one from the other using the following operations:

<ul>
	<li>Operation 1: Swap any two **existing** characters.

	<ul>
		<li>For example, `a<u>b</u>cd<u>e</u> -> a<u>e</u>cd<u>b</u>`</li>
	</ul>
	</li>
	<li>Operation 2: Transform **every** occurrence of one **existing** character into another **existing** character, and do the same with the other character.
	<ul>
		<li>For example, `<u>aa</u>c<u>abb</u> -> <u>bb</u>c<u>baa</u>` (all `a`'s turn into `b`'s, and all `b`'s turn into `a`'s)</li>
	</ul>
	</li>
</ul>

You can use the operations on either string as many times as necessary.

Given two strings, `word1` and `word2`, return `true`* if *`word1`* and *`word2`* are **close**, and *`false`* otherwise.*
