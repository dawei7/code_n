## Description

<p data-end="331" data-start="85">You are given an undirected connected graph with <code data-end="137" data-start="134">n</code> nodes labeled from 0 to <code data-end="171" data-start="164">n - 1</code> and a 2D integer array <code data-end="202" data-start="195">edges</code> where <code data-end="234" data-start="209">edges[i] = [u_i, v_i, w_i]</code> denotes an undirected edge between node <code data-end="279" data-start="275">u_i</code> and node <code data-end="293" data-start="289">v_i</code> with weight <code data-end="310" data-start="306">w_i</code>, and an integer <code data-end="330" data-start="327">k</code>.

<p data-end="461" data-start="333">You are allowed to remove any number of edges from the graph such that the resulting graph has **at most** <code data-end="439" data-start="436">k</code> connected components.

<p data-end="589" data-start="463">The **cost** of a component is defined as the **maximum** edge weight in that component. If a component has no edges, its cost is 0.

<p data-end="760" data-start="661">Return the **minimum** possible value of the **maximum** cost among all components <strong data-end="759" data-start="736">after such removals</strong>.
