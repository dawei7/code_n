## Description

<p data-end="128" data-start="0">You are given an integer array <code data-end="37" data-start="31">nums</code> of length <code data-end="51" data-start="48">n</code>.

<p data-end="128" data-start="0">An array is <strong data-end="76" data-start="65">trionic</strong> if there exist indices <code data-end="117" data-start="100">0 < p < q < n − 1</code> such that:

<ul>
	<li data-end="170" data-start="132"><code data-end="144" data-start="132">nums[0...p]</code> is **strictly** increasing,</li>
	<li data-end="211" data-start="173"><code data-end="185" data-start="173">nums[p...q]</code> is **strictly** decreasing,</li>
	<li data-end="252" data-start="214"><code data-end="228" data-start="214">nums[q...n − 1]</code> is **strictly** increasing.</li>
</ul>

<p data-end="315" data-is-last-node="" data-is-only-node="" data-start="254">Return <code data-end="267" data-start="261">true</code> if <code data-end="277" data-start="271">nums</code> is trionic, otherwise return <code data-end="314" data-start="307">false</code>.
