## Description

With respect to a given `puzzle` string, a `word` is *valid* if both the following conditions are satisfied:
<ul>
	<li>`word` contains the first letter of `puzzle`.</li>
	<li>For each letter in `word`, that letter is in `puzzle`.
	<ul>
		<li>For example, if the puzzle is `"abcdefg"`, then valid words are `"faced"`, `"cabbage"`, and `"baggage"`, while</li>
		<li>invalid words are `"beefed"` (does not include `'a'`) and `"based"` (includes `'s'` which is not in the puzzle).</li>
	</ul>
	</li>
</ul>
Return *an array *`answer`*, where *`answer[i]`* is the number of words in the given word list *`words`* that is valid with respect to the puzzle *`puzzles[i]`.
