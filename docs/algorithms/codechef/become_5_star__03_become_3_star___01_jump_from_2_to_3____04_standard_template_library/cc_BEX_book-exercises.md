# Book Exercises

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BEX |
| Difficulty Rating | 1728 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Standard Template Library |
| Official Link | [BEX](https://www.codechef.com/practice/course/2to3stars/LP2TO304/problems/BEX) |

---

## Problem Statement

Harry is a bright student. To prepare thoroughly for exams, he completes all the exercises in his book! Now that the exams are approaching fast, he is doing book exercises day and night. He writes down and keeps updating the remaining number of exercises on the back cover of each book.

Harry has a lot of books messed on the floor. Therefore, he wants to pile up the books **that still have some remaining exercises** into a single pile. He will grab the books one-by-one and add the books that still have remaining exercises to the top of the pile.

Whenever he wants to do a book exercise, he will pick the book with the minimum number of remaining exercises from the pile. In order to pick the book, he has to remove all the books above it. Therefore, if there are more than one books with the minimum number of remaining exercises, he will take the one which requires the least number of books to remove. The removed books are returned to the messy floor. After he picks the book, he will do all the remaining exercises and trash the book.

Since number of books is rather large, he needs your help to tell him the number of books he must remove, for picking the book with the minimum number of exercises.

Note that more than one book can have the same name.

### Input

The first line contains a single integer **N** denoting the number of actions. Then **N** lines follow. Each line starts with an integer. If the integer is -1, that means Harry wants to do a book exercise. Otherwise, the integer is number of the remaining exercises in the book he grabs next. This is followed by a string denoting the name of the book.

### Output

For each -1 in the input, output a single line containing the number of books Harry must remove, followed by the name of the book that Harry must pick.

### Constraints

1 < **N** ≤ 1,000,000
 0 ≤ (the number of remaining exercises of each book) < 100,000
 The name of each book consists of between 1 and 15 characters 'a' - 'z'.
 Whenever he wants to do a book exercise, there is at least one book in the pile.

---

## Examples

**Example 1**

**Input**

```text
6
9 english
6 mathematics
8 geography
-1
3 graphics
-1
```

**Output**

```text
1 mathematics
0 graphics
```

**Explanation**

- For the first $-1$: Currently, there are $3$ books in the pile. The book with minimum exercises left amongst these is `mathematics`. Harry has to remove $1$ book from the top to pick `mathematics` book and solve the remaining exercises.

- For the second $-1$: The book on the top has the least number of remaining exercises. Thus, Harry has to remove $0$ books from the top pick up `graphics` book.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINKS

[Practice](http://www.codechef.com/problems/BEX)

[Contest](http://www.codechef.com/DEC12/problems/BEX)

## DIFFICULTY

EASY

## PREREQUISITES

Stack Data Structure

## PROBLEM

Harry has a lot of books messed on the floor. He keeps a pile of books. At any time, he can put a book that has some remaining exercises on top of the pile, or do a book exercise by picking a book with minimum number of remaining exercises and removing all books above it. If there are more than one such book, pick the book with the minimum number of removed books. Help him determine which book to pick whenever he wants to do a book exercise.

## QUICK EXPLANATION

Maintain a stack of books. Each book is represented by a pair of (name, number of remaining exercises, number of books above with greater number of remaining exercises). When Harry wants to do a book exercise, pop the stack and retrieve the name of the book. When Harry wants to put a book on the top of the stack, there are two possibilities. If the number of remaining exercises is greater than the number of remaining exercises of the book on the top of the stack, ignore this book and increase the “number of books above” of the book on the top of the stack. Otherwise, push a new book (name of the book, number of remaining exercises, 0) to the stack.

The time complexity of this solution is of course linear.

## EXPLANATION

This is clearly a data structure problem. The problem statement implies that we need to invent an augmented (modified) stack that supports these operations.

- Add a book on the top of the stack.

- Retrieve a book with the minimum number remaining exercises, and pop all books above it, including the book itself.

To solve this problem, we need this important lemma.

**Lemma 1**. Suppose there is a book A above a book B in the pile, and book A has greater number of remaining exercises than B. Then, book A will never get picked by Harry.

**Proof**. Because Harry always pick a book with the minimum number of remaining exercises, book B must be removed first before book A can be picked. However, removing book B will remove book A as well. Therefore, book A will never get picked.

Lemma 1 implies that we don’t have to physically put a book above another book with lower number of remaining exercises as the book can’t be picked. For each book, we can just store the number of books above it that have greater number of remaining exercises. Therefore, we have a stack in non-decreasing order of number of remaining exercises from top to bottom. All operations above can then be implemented in constant time:

- If the number of remaining exercises is greater than the number of remaining exercises of the book on the top of the stack, ignore this book (as this book can be never get picked) and increase the "number of books above" of the book on the top of the stack. Otherwise, push a new book (name of the book, number of remaining exercises, 0) to the stack.
Of course, if the stack is initially empty, we can just push the book to the stack.

- As the stack is sorted in non-decreasing order, just retrieve the book on the top of the stack (and pop it).

Because each operation is done in constant time, the whole solution runs in O(N), i.e., linear time.

**Note**. There is a tricky case in this problem! When Harry grabs a book with no remaining exercises, he does not put in to the pile.

## SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/December/Setter/BEX.cpp).

## TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/December/Tester/BEX.c).

</details>
