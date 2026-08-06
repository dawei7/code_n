## Description

You are given an **undirected weighted** tree with <code data-end="51" data-start="48">n</code> nodes, numbered from <code data-end="75" data-start="72">0</code> to <code data-end="86" data-start="79">n - 1</code>. It is represented by a 2D integer array <code data-end="129" data-start="122">edges</code> of length <code data-end="147" data-start="140">n - 1</code>, where <code data-end="185" data-start="160">edges[i] = [u_i, v_i, w_i]</code> indicates that there is an edge between nodes <code data-end="236" data-start="232">u_i</code> and <code data-end="245" data-start="241">v_i</code> with weight <code data-end="262" data-start="258">w_i</code>.​

Additionally, you are given a 2D integer array <code data-end="56" data-start="47">queries</code>, where <code data-end="105" data-start="69">queries[j] = [src1_j, src2_j, dest_j]</code>.

Return an array <code data-end="24" data-start="16">answer</code> of length equal to <code data-end="60" data-start="44">queries.length</code>, where <code data-end="79" data-start="68">answer[j]</code> is the **minimum total weight** of a subtree such that it is possible to reach <code data-end="174" data-start="167">dest_j</code> from both <code data-end="192" data-start="185">src1_j</code> and <code data-end="204" data-start="197">src2_j</code> using edges in this subtree.

A <strong data-end="2287" data-start="2276">subtree</strong> here is any connected subset of nodes and edges of the original tree forming a valid tree.
