## Description

You have a movie renting company consisting of `n` shops. You want to implement a renting system that supports searching for, booking, and returning movies. The system should also support generating a report of the currently rented movies.

Each movie is given as a 2D integer array `entries` where `entries[i] = [shop_i, movie_i, price_i]` indicates that there is a copy of movie `movie_i` at shop `shop_i` with a rental price of `price_i`. Each shop carries **at most one** copy of a movie `movie_i`.

The system should support the following functions:

<ul>
	<li>**Search**: Finds the **cheapest 5 shops** that have an **unrented copy** of a given movie. The shops should be sorted by **price** in ascending order, and in case of a tie, the one with the **smaller **`shop_i` should appear first. If there are less than 5 matching shops, then all of them should be returned. If no shop has an unrented copy, then an empty list should be returned.</li>
	<li>**Rent**: Rents an **unrented copy** of a given movie from a given shop.</li>
	<li>**Drop**: Drops off a **previously rented copy** of a given movie at a given shop.</li>
	<li>**Report**: Returns the **cheapest 5 rented movies** (possibly of the same movie ID) as a 2D list `res` where `res[j] = [shop_j, movie_j]` describes that the `j^th` cheapest rented movie `movie_j` was rented from the shop `shop_j`. The movies in `res` should be sorted by **price **in ascending order, and in case of a tie, the one with the **smaller **`shop_j` should appear first, and if there is still tie, the one with the **smaller **`movie_j` should appear first. If there are fewer than 5 rented movies, then all of them should be returned. If no movies are currently being rented, then an empty list should be returned.</li>
</ul>

Implement the `MovieRentingSystem` class:

<ul>
	<li>`MovieRentingSystem(int n, int[][] entries)` Initializes the `MovieRentingSystem` object with `n` shops and the movies in `entries`.</li>
	<li>`List<Integer> search(int movie)` Returns a list of shops that have an **unrented copy** of the given `movie` as described above.</li>
	<li>`void rent(int shop, int movie)` Rents the given `movie` from the given `shop`.</li>
	<li>`void drop(int shop, int movie)` Drops off a previously rented `movie` at the given `shop`.</li>
	<li>`List<List<Integer>> report()` Returns a list of cheapest **rented** movies as described above.</li>
</ul>

**Note:** The test cases will be generated such that `rent` will only be called if the shop has an **unrented** copy of the movie, and `drop` will only be called if the shop had **previously rented** out the movie.
