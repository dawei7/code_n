## Description

<p data-end="438" data-start="104">You are given an integer array <code data-end="119" data-start="113">cost</code> of size <code data-end="131" data-start="128">n</code>. You are currently at position <code data-end="166" data-start="163">n</code> (at the end of the line) in a line of <code data-end="187" data-start="180">n + 1</code> people (numbered from 0 to <code data-end="218" data-start="215">n</code>).

<p data-end="438" data-start="104">You wish to move forward in the line, but each person in front of you charges a specific amount to **swap** places. The cost to swap with person <code data-end="375" data-start="372">i</code> is given by <code data-end="397" data-start="388">cost[i]</code>.

<p data-end="487" data-start="440">You are allowed to swap places with people as follows:

<ul data-end="632" data-start="488">
	<li data-end="572" data-start="488">If they are in front of you, you **must** pay them <code data-end="546" data-start="537">cost[i]</code> to swap with them.</li>
	<li data-end="632" data-start="573">If they are behind you, they can swap with you for free.</li>
</ul>

<p data-end="755" data-start="634">Return an array `answer` of size `n`, where `answer[i]` is the <strong data-end="680" data-start="664">minimum</strong> total cost to reach each position `i` in the line<font face="monospace">.</font>
