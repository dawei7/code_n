# Practice - Music Player

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LINK02P10 |
| Difficulty Rating | 1500 |
| Difficulty Band | Linked Lists |
| Path | Data Structures and Algorithms |
| Lesson | Circular and Doubly Linked Lists |
| Official Link | [LINK02P10](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST02/problems/LINK02P10) |

---

## Problem Statement

In this problem, you need to implement the functionality of a music player using doubly linked list!

The functionality of a playlist queue needs to be implemented, i.e., adding a song to the queue, playing the next song, playing the previous song, switching to a song, etc.

You need to complete the following functions:

1. addSong(int songId): Add the songId to the end of the list
2. playNext(): Go to the next song in the list
3. playPrev(): Go to the previous song in the list
4. switchSong(int songId): Find in the list where this songId is present, go to that song and continue the playlist from there (In playlist 1<->2<->3<->4<->5 if the current song is `4` and function is called for `2`, the current song is stopped and now order is 2->3->4->5)
5. current(): Return the songId of the song currently playing

Assumptions:

1. playNext function will not be called from the last song
2. playPrev function will not be called from the first song
3. The songId provided in switchSong function is always present in the list
4. The addSong function will not be called for a songId which is already present in the list
5. The current function will not be called when the list is empty.

Note: Until the next function is called, the current song will automatically be the first songId added in the list.

The problem input is query-based:

1 : An integer `songId` will be provided with which addSong(songId) will be called
2 : playNext() is called
3 : playPrev() is called
4 : An integer `songId` will be provided with which switchSong(songId) will be called
5 : current() is called and you need to return the songId for the current song playing

**You only need to make changes in the functions mentioned. The input and calling the required functions are taken care of. Do not output anything or you may get WA verdict**

---

## Input Format

- The first line of input will contain a single integer $N$, denoting the number of queries.
- The next $N$ lines contain a single or two integers depending on the type of query.

---

## Output Format

Output a single integer songId on a new line for every time query type is 5.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ across all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
16
1 1
1 2
1 3
5
2
5
3
5
1 4
1 5
2
2
4 1
5
2
5
```

**Output**

```text
1
2
1
1
2
```

**Explanation**

The current playlist is empty.
1 1 : Add song 1 to the end of list and the current song is now 1.
Playlist: 1
1 2 : Add song 2 to the end of list.
Playlist: 1<->2
1 3 : Add song 3 to the end of list.
Playlist: 1<->2<->3
5 : Output the current song.
2 : The current song is now 2.
5 : Output the current song.
3 : The current song is now 1.
5 : Output the current song.
1 4 : Add song 4 to the end of list.
Playlist: 1<->2<->3<->4
1 5 : Add song 5 to the end of list.
Playlist: 1<->2<->3<->4<->5
2 : The current song is now 2.
2 : The current song is now 3.
4 1 : Switch from 3 to 1. The current song is now 1.
5 : Output 1.
2 : The current song is now 2.
5 : Output 2.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Practice - Music Player](https://www.codechef.com/learn/course/linked-lists/LINKEDLIST02/problems/LINK02P10)

### [](#problem-statement-1)Problem Statement:

The functionality of a playlist queue needs to be implemented, i.e., adding a song to the queue, playing the next song, playing the previous song, switching to a song, etc.

### [](#approach-2)Approach:

The key idea of this solution is to use a **doubly linked list** to manage the songs in the music player. Each song is represented by a node that contains the song ID and pointers to the previous and `next` songs. This structure allows for easy navigation between songs.

Here’s a breakdown of the approach:

-

**MusicPlayer Class**:

- head: A pointer to the first song in the list.

- currentSong: A pointer to the song currently being played.

-

**addSong(`int songId`)**:

- This function creates a new song node and adds it to the end of the list.

- If the list is empty, the new song becomes both the head and the current song.

- Otherwise, it traverses to the end of the list and links the new song.

-

**playNext()**:

- Moves the current song pointer to the next song, if available.

-

**playPrev()**:

- Moves the current song pointer to the previous song, if available.

-

**switchSong(`int songId`)**:

- This function allows switching to a specific song by traversing the list until the song ID matches.

-

**current()**:

- Returns the song ID of the song currently being played.

### [](#time-complexity-3)Time Complexity:

-

**addSong**: **O(n)** in the worst case, where n is the number of songs (traversing to the end).

-

**playNext** and **playPrev**: **O(1)** since they simply move the pointer.

-

**switchSong**: **O(n)** in the worst case, as it may need to traverse the entire list.

-

**current**: **O(1)** since it directly returns the current song’s ID.

### [](#space-complexity-4)Space Complexity:

- **O(n)** because we store n nodes in the linked list, with each node representing a song.

</details>
