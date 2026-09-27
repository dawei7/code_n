"""Tests for the Guided Example render-risk checks.

The checks in ``tools/audit_guided_examples.py`` exist because structural
counters accepted constructs that the renderers reject: a star superscript
written as ``^\\*`` reached ten spans in the corpus, and an unquoted Mermaid edge
label containing brackets broke a whole diagram. Both shipped past every
existing counter and were caught only by the slower render gates.

These tests exist because the first two drafts of the check were themselves
wrong: one matched the valid ``^*`` instead of the broken ``^\\*``, and the other
flagged quoted Mermaid *node* labels that legitimately contain pipes and
brackets. A check that is silently too strict or too loose is worse than none.
"""
from __future__ import annotations

import unittest

from tools.audit_guided_examples import count_tables, render_risks


class KatexHostileConstructTest(unittest.TestCase):
    def test_star_superscript_with_backslash_is_flagged(self) -> None:
        risks = render_risks("Let $I^\\*$ be an optimal selection.")
        self.assertTrue(any("undefined control sequence" in risk for risk in risks))

    def test_braced_star_superscript_is_accepted(self) -> None:
        self.assertEqual(render_risks("Let $I^{*}$ be an optimal selection."), [])

    def test_bare_star_superscript_is_accepted(self) -> None:
        # `^*` parses in KaTeX, so it must not be reported.
        self.assertEqual(render_risks("Let $I^*$ be an optimal selection."), [])

    def test_undefined_outer_join_is_flagged(self) -> None:
        risks = render_risks("The join $A \\leftouterjoin B$ is not defined.")
        self.assertTrue(any("leftouterjoin" in risk for risk in risks))

    def test_pipe_inside_text_is_flagged(self) -> None:
        risks = render_risks("The size $\\text{a \\| b}$ is invalid.")
        self.assertTrue(any("textbar" in risk for risk in risks))

    def test_textbar_inside_text_is_accepted(self) -> None:
        self.assertEqual(render_risks("The size $\\text{a \\textbar b}$ is fine."), [])


class MermaidRenderRiskTest(unittest.TestCase):
    ACCESSIBLE = "```mermaid\nflowchart TD\n  accTitle: T\n  accDescr: D\n  A --> B\n```"

    def test_diagram_without_acc_title_is_flagged(self) -> None:
        content = "```mermaid\nflowchart TD\n  accDescr: D\n  A --> B\n```"
        self.assertIn("Mermaid diagram without accTitle", render_risks(content))

    def test_diagram_without_acc_descr_is_flagged(self) -> None:
        content = "```mermaid\nflowchart TD\n  accTitle: T\n  A --> B\n```"
        self.assertIn("Mermaid diagram without accDescr", render_risks(content))

    def test_accessible_diagram_is_accepted(self) -> None:
        self.assertEqual(render_risks(self.ACCESSIBLE), [])

    def test_unquoted_edge_label_with_bracket_is_flagged(self) -> None:
        content = (
            "```mermaid\nflowchart TD\n  accTitle: T\n  accDescr: D\n"
            '  A -->|nums1[i] smaller| C["advance"]\n```'
        )
        risks = render_risks(content)
        self.assertTrue(any("unquoted bracket" in risk for risk in risks), risks)

    def test_quoted_edge_label_with_bracket_is_accepted(self) -> None:
        content = (
            "```mermaid\nflowchart TD\n  accTitle: T\n  accDescr: D\n"
            '  A -->|"nums1[i] smaller"| C["advance"]\n```'
        )
        self.assertEqual(render_risks(content), [])

    def test_quoted_node_label_may_contain_pipes_and_brackets(self) -> None:
        # A node label is not an edge label; this draft of the check flagged it.
        content = (
            "```mermaid\nflowchart TD\n  accTitle: T\n  accDescr: D\n"
            '  C{"Is |arr[i] - arr[j]| small?"} --> D["advance"]\n```'
        )
        self.assertEqual(render_risks(content), [])


class TableCountingRegressionTest(unittest.TestCase):
    def test_alignment_colon_delimiter_row_is_a_table(self) -> None:
        content = "| a | b |\n|:---:|:---:|\n| 1 | 2 |\n"
        self.assertEqual(count_tables(content), 1)

    def test_table_inside_a_fence_is_not_counted(self) -> None:
        content = "```text\n| a | b |\n|---|---|\n| 1 | 2 |\n```\n"
        self.assertEqual(count_tables(content), 0)

    def test_pipe_line_without_delimiter_row_is_not_a_table(self) -> None:
        self.assertEqual(count_tables("| a | b |\n| 1 | 2 |\n"), 0)


if __name__ == "__main__":
    unittest.main()