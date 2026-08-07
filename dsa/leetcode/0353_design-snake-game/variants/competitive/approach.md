## General
Given Design a <a href="https://en.wikipedia.org/wiki/Snake_(video_game)" target="_blank">Snake game</a> that is played on a device with screen size `height x width`. <a href="http://patorjk.com/games/snake/" target="_blank..., the algorithm executes breadth-first search (BFS) level-order traversal using a queue. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, a double-ended queue (`deque`) to support dynamic $O(1)$ push and pop operations at both ends. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(q)$ — Operation count bound.
- **Space Complexity**: $O(f)$ — Auxiliary memory allocation bound.
