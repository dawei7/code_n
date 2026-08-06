## Description

Given a binary tree and a nonempty collection of distinct nodes from that tree, find their lowest common ancestor. Every supplied node is guaranteed to occur in the tree, and every node value in the tree is unique. A node is considered its own descendant, so a target may itself be the common ancestor sought.

The answer is the deepest node whose subtree contains every supplied target. For a single target, that target is therefore the answer. Values do not impose binary-search ordering; only the parent-child structure determines ancestry. Return the ancestor node itself, not its depth or a path.
