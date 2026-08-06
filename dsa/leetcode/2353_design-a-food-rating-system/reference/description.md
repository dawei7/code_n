## Description

Design a food rating system that can do the following:

<ul>
	<li>**Modify** the rating of a food item listed in the system.</li>
	<li>Return the highest-rated food item for a type of cuisine in the system.</li>
</ul>

Implement the `FoodRatings` class:

<ul>
	<li>`FoodRatings(String[] foods, String[] cuisines, int[] ratings)` Initializes the system. The food items are described by `foods`, `cuisines` and `ratings`, all of which have a length of `n`.

	<ul>
		<li>`foods[i]` is the name of the `i^th` food,</li>
		<li>`cuisines[i]` is the type of cuisine of the `i^th` food, and</li>
		<li>`ratings[i]` is the initial rating of the `i^th` food.</li>
	</ul>
	</li>
	<li>`void changeRating(String food, int newRating)` Changes the rating of the food item with the name `food`.</li>
	<li>`String highestRated(String cuisine)` Returns the name of the food item that has the highest rating for the given type of `cuisine`. If there is a tie, return the item with the **lexicographically smaller** name.</li>
</ul>

Note that a string `x` is lexicographically smaller than string `y` if `x` comes before `y` in dictionary order, that is, either `x` is a prefix of `y`, or if `i` is the first position such that `x[i] != y[i]`, then `x[i]` comes before `y[i]` in alphabetic order.
