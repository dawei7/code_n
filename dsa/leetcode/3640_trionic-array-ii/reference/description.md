## Description

<p data-end="191" data-start="0">You are given an integer array <code data-end="61" data-start="55">nums</code> of length <code data-end="75" data-start="72">n</code>.

<p data-end="191" data-start="0">A <strong data-end="99" data-is-only-node="" data-start="79">trionic subarray</strong> is a contiguous subarray <code data-end="136" data-start="125">nums[l...r]</code> (with <code data-end="158" data-start="143">0 <= l < r < n</code>) for which there exist indices `l < p < q < r` such that:

<ul>
	<li data-end="267" data-start="230"><code data-end="241" data-start="230">nums[l...p]</code> is **strictly** increasing,</li>
	<li data-end="307" data-start="270"><code data-end="281" data-start="270">nums[p...q]</code> is **strictly** decreasing,</li>
	<li data-end="347" data-start="310"><code data-end="321" data-start="310">nums[q...r]</code> is **strictly** increasing.</li>
</ul>

<p data-end="609" data-is-last-node="" data-is-only-node="" data-start="349">Return the **maximum** sum of any trionic subarray in <code data-end="417" data-start="411">nums</code>.
