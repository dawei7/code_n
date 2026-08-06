## Description

You are given a **(0-indexed)** array of positive integers `candiesCount` where `candiesCount[i]` represents the number of candies of the `i^th` type you have. You are also given a 2D array `queries` where `queries[i] = [favoriteType_i, favoriteDay_i, dailyCap_i]`.

You play a game with the following rules:

<ul>
	<li>You start eating candies on day `**0**`.</li>
	<li>You **cannot** eat **any** candy of type `i` unless you have eaten **all** candies of type `i - 1`.</li>
	<li>You must eat **at least** **one** candy per day until you have eaten all the candies.</li>
</ul>

Construct a boolean array `answer` such that `answer.length == queries.length` and `answer[i]` is `true` if you can eat a candy of type `favoriteType_i` on day `favoriteDay_i` without eating **more than** `dailyCap_i` candies on **any** day, and `false` otherwise. Note that you can eat different types of candy on the same day, provided that you follow rule 2.

Return *the constructed array *`answer`.
