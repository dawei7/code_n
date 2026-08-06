## Description

You are playing the **<a href="https://en.wikipedia.org/wiki/Bulls_and_Cows" target="_blank">Bulls and Cows</a>** game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

<ul>
	<li>The number of "bulls", which are digits in the guess that are in the correct position.</li>
	<li>The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.</li>
</ul>

Given the secret number `secret` and your friend's guess `guess`, return *the hint for your friend's guess*.

The hint should be formatted as `"xAyB"`, where `x` is the number of bulls and `y` is the number of cows. Note that both `secret` and `guess` may contain duplicate digits.
