"""Solution for bb_04: 8-Puzzle (Branch and Bound).


            Solve the 8-puzzle (3x3 sliding-tile puzzle with
            one empty cell) using branch and bound with the
            misplaced-tiles heuristic. Cost of a node = depth
            so far + number of tiles not in their goal position.
            Use a priority queue of live nodes; expand the
            node with the smallest cost; move the empty cell
            in the four cardinal directions to generate
            children, skipping the previous position. Stop
            when a goal state is reached. Return the number of
            moves in the shortest solution (depth of the goal
            node).
            Source: https://www.geeksforgeeks.org/dsa/8-puzzle-problem-using-branch-and-bound/
            

Inputs passed to solve():
    start: 3x3 list of lists representing the initial board (0 = blank).
    goal: 3x3 list of lists representing the target board.

Goal:
    the minimum number of moves to reach the goal from start, or -1 if unsolvable (heuristic-search bound).

Samples:
Sample 1 input:  start = [[1,2,3],[4,5,6],[7,8,0]], goal = [[1,2,3],[4,5,6],[7,8,0]]
Sample 1 output: 0

Sample 2 input:  start = [[1,2,3],[4,0,6],[7,5,8]], goal = [[1,2,3],[4,5,6],[7,8,0]]
Sample 2 output: 2 (or whatever BFS finds)


"""

def solve(start, goal):
    # Write your code here.
    return None
