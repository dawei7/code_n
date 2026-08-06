## Description

<p data-end="186" data-start="43">You are given a rooted tree with <code data-end="79" data-start="76">n</code> nodes labeled from 0 to <code data-end="113" data-start="106">n - 1</code>, represented by an integer array <code data-end="164" data-start="156">parent</code> of length <code data-end="178" data-start="175">n</code>, where:

<ul>
	<li data-end="227" data-start="190"><code data-end="206" data-start="190">parent[0] = -1</code> (node 0 is the root).</li>
	<li data-end="311" data-start="230">For each <code data-end="250" data-start="239">1 <= i < n</code>, <code data-end="263" data-start="252">parent[i]</code> is the parent of node <code data-end="289" data-start="286">i</code> (<code data-end="310" data-start="291">0 <= parent[i] < i</code>).</li>
</ul>

<p data-end="439" data-start="313">You are also given an integer array <font face="monospace">nums</font> of length <code data-end="377" data-start="374">n</code>, where `<font face="monospace">nums[i]</font>` is the value of node <code data-end="418" data-start="415">i</code>, and an integer <code data-end="438" data-start="435">k</code>.

<p data-end="488" data-start="441">A non-empty subset of nodes is called **valid** if:

<ul>
	<li data-end="555" data-start="491">The **sum** of the values of the selected nodes is **divisible** by <code data-end="554" data-start="551">k</code>.</li>
	<li data-end="669" data-start="558">No **two** selected nodes are **adjacent** in the tree (no node and its direct parent are both included in the subset).</li>
</ul>

<p data-end="721" data-start="671">Return the number of valid subsets modulo `10^9 + 7`.
