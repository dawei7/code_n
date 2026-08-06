## Description

<p data-end="502" data-start="75">You are given a directed acyclic graph of `n` nodes numbered from 0 to `n − 1`. This is represented by a 2D array <code data-end="201" data-start="194">edges</code> of length<font face="monospace"> `m`</font>, where <code data-end="255" data-start="227">edges[i] = [u_i, v_i, cost_i]</code> indicates a one‑way communication from node <code data-end="304" data-start="300">u_i</code> to node <code data-end="317" data-start="313">v_i</code> with a recovery cost of <code data-end="349" data-start="342">cost_i</code>.

<p data-end="502" data-start="75">Some nodes may be offline. You are given a boolean array <code data-end="416" data-start="408">online</code> where <code data-end="441" data-start="423">online[i] = true</code> means node <code data-end="456" data-start="453">i</code> is online. Nodes 0 and `n − 1` are always online.

<p data-end="547" data-start="504">A path from 0 to `n − 1` is <strong data-end="541" data-start="532">valid</strong> if:

<ul>
	<li>All intermediate nodes on the path are online.</li>
	<li data-end="676" data-start="605">The total recovery cost of all edges on the path does not exceed `k`.</li>
</ul>

<p data-end="771" data-start="653">For each valid path, define its <strong data-end="694" data-start="685">score</strong> as the minimum edge‑cost along that path.

<p data-end="913" data-start="847">Return the **maximum** path score (i.e., the largest **minimum**-edge cost) among all valid paths. If no valid path exists, return -1.
