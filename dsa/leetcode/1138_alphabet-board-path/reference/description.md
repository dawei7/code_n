## Description

On an alphabet board, we start at position `(0, 0)`, corresponding to character `board[0][0]`.



Here, `board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]`, as shown in the diagram below.



<img alt="" src="https://assets.leetcode.com/uploads/2019/07/28/azboard.png" style="width: 250px; height: 317px;" />



We may make the following moves:



<ul>
	<li>`'U'` moves our position up one row, if the position exists on the board;</li>
	<li>`'D'` moves our position down one row, if the position exists on the board;</li>
	<li>`'L'` moves our position left one column, if the position exists on the board;</li>
	<li>`'R'` moves our position right one column, if the position exists on the board;</li>
	<li>`'!'` adds the character `board[r][c]` at our current position `(r, c)` to the answer.</li>
</ul>

(Here, the only positions that exist on the board are positions with letters on them.)



Return a sequence of moves that makes our answer equal to `target` in the minimum number of moves.  You may return any path that does so.
