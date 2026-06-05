"""Pygame challenge navigation hub."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional

from challenges.registry import get_challenge
from .branding import (
    BACKSTORY_PARAGRAPHS,
    GAME_TITLE,
    MAX_PLAYER_NAME_LENGTH,
    normalize_player_name,
)
from .progress import PROGRESS_FILE, load_progress, save_progress
from .samples import sample_lines
from .solutions import PROJECT_ROOT, create_solution_file as create_saved_solution_file, default_solution_path, ensure_solutions_dir
from .tree import ChallengeTree, TreeNode
from .grid import CellType, Grid
from .tracked import TrackedGrid, TrackedList
from .window import is_resize_event, mono_font, open_maximized_window, sync_window_size


def _strip_leading_docstring(source: str) -> list[str]:
    """Drop the file-header docstring so the example panel shows
    just the imports and ``def solve()`` body, not the explanatory
    paragraph above it.

    Handles the ``\\"\\"\\" ... \\"\\"\\"`` docstring at the start of
    the source and any blank lines that follow. Returns the rest
    as a list of lines (with the trailing newline trimmed).
    """
    text = source.lstrip("\n")
    if not text.startswith('"""') and not text.startswith("'''"):
        return text.splitlines()
    quote = text[:3]
    end = text.find(quote, 3)
    if end < 0:
        return text.splitlines()
    rest = text[end + 3 :]
    # Trim leading blank lines.
    return rest.lstrip("\n").splitlines()


@dataclass
class NavItem:
    node: TreeNode
    status: str
    difficulty: int
    implemented: bool

    @property
    def status_label(self) -> str:
        if self.status == "done":
            return "DONE"
        if self.status == "failed":
            return "FAILED"
        return "OPEN"


class ChallengeNavigator:
    """Interactive Pygame menu for choosing and starting challenges."""

    BACKGROUND = (18, 21, 26)
    SURFACE = (28, 34, 43)
    SURFACE_ALT = (36, 43, 54)
    GRID_LINE = (64, 73, 89)
    SELECTED = (64, 98, 145)
    TEXT = (235, 239, 246)
    MUTED = (150, 160, 174)
    ACCENT = (86, 179, 129)
    WARNING = (238, 186, 83)
    ERROR = (231, 91, 91)

    CELL_COLORS = {
        CellType.EMPTY: (34, 39, 48),
        CellType.WALL: (10, 12, 16),
        CellType.VALUE: (66, 77, 92),
        CellType.MARKER: (141, 112, 45),
        CellType.START: (45, 126, 82),
        CellType.GOAL: (144, 58, 58),
        CellType.PATH: (39, 125, 149),
        CellType.VISITED: (48, 82, 152),
        CellType.CURRENT: (118, 77, 150),
        CellType.SORTED: (45, 126, 82),
        CellType.UNSORTED: (66, 77, 92),
        CellType.PIVOT: (158, 126, 45),
        CellType.COMPARE_A: (255, 103, 103),
        CellType.COMPARE_B: (75, 213, 190),
    }

    CATEGORIES = ["intro", "sorting", "searching", "graphs", "dynamic"]
    CATEGORY_NAMES = {
        "intro": "Introduction",
        "sorting": "Sorting",
        "searching": "Searching",
        "graphs": "Graphs",
        "dynamic": "Dynamic Programming",
    }

    def __init__(self, width: int = 1180, height: int = 760):
        self.width = width
        self.height = height
        self.tree = ChallengeTree()
        self.progress = load_progress()
        self.selected_index = 0
        self.scroll_y = 0
        self.message = "Click selects. E explores. Enter/R runs. O opens script. Reset clears run statuses."
        self.items = self._build_items()
        self._progress_mtime = self._progress_file_mtime()

    def run(self):
        import pygame

        ensure_solutions_dir()
        pygame.init()
        screen = open_maximized_window(pygame, self.width, self.height, f"{GAME_TITLE} - Challenge Navigator")
        sync_window_size(self, screen)
        clock = pygame.time.Clock()
        fonts = {
            "title": mono_font(pygame, 30, bold=True),
            "heading": mono_font(pygame, 22, bold=True),
            "body": mono_font(pygame, 18),
            "small": mono_font(pygame, 15),
        }

        if not self.progress.player_name:
            if not self._prompt_player_name(screen, clock, fonts):
                pygame.quit()
                return

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif is_resize_event(pygame, event):
                    screen = pygame.display.get_surface() or screen
                    sync_window_size(self, screen)
                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_ESCAPE, pygame.K_q):
                        running = False
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        self._move_selection(1)
                    elif event.key in (pygame.K_UP, pygame.K_w):
                        self._move_selection(-1)
                    elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        self.run_selected_challenge()
                    elif event.key == pygame.K_e:
                        self.explore_selected_challenge(screen, clock, fonts)
                    elif event.key == pygame.K_o:
                        self.open_selected_script()
                    elif event.key == pygame.K_r:
                        self.run_selected_challenge()
                    elif event.key == pygame.K_F5:
                        self.refresh()
                    elif event.key == pygame.K_n:
                        self._prompt_player_name(screen, clock, fonts, editing=True)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        self.scroll_y = max(0, self.scroll_y - 80)
                    elif event.button == 5:
                        self.scroll_y += 80
                    else:
                        action = self._button_at(event.pos)
                        if action == "explore":
                            self.explore_selected_challenge(screen, clock, fonts)
                            continue
                        if action == "run":
                            self.run_selected_challenge()
                            continue
                        if action == "open":
                            self.open_selected_script()
                            continue
                        if action == "solve":
                            self.solve_selected_challenge()
                            continue
                        if action == "reset":
                            self.reset_progress_statuses()
                            continue

                        clicked = self._item_at(event.pos)
                        if clicked is not None:
                            self.selected_index = clicked
                            self._ensure_selected_visible()

            self.refresh_if_progress_changed()

            self._draw(screen, fonts)
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

    def refresh(self):
        self.progress = load_progress()
        self.items = self._build_items()
        self.selected_index = min(self.selected_index, max(0, len(self.items) - 1))
        self._progress_mtime = self._progress_file_mtime()
        self.message = "Progress refreshed."

    def refresh_if_progress_changed(self):
        current_mtime = self._progress_file_mtime()
        if current_mtime != self._progress_mtime:
            self.progress = load_progress()
            self.items = self._build_items()
            self.selected_index = min(self.selected_index, max(0, len(self.items) - 1))
            self._progress_mtime = current_mtime

    def reset_progress_statuses(self):
        self.progress.reset_statuses()
        save_progress(self.progress)
        self.items = self._build_items()
        self._progress_mtime = self._progress_file_mtime()
        self.message = "Run statuses reset. All challenges are open."

    def _progress_file_mtime(self) -> float:
        try:
            return os.path.getmtime(PROGRESS_FILE)
        except OSError:
            return 0.0

    def player_name(self) -> str:
        return normalize_player_name(self.progress.player_name)

    def open_selected_script(self):
        item = self.current_item()
        if not item:
            return

        path = create_solution_file(item.node.challenge_id)
        opened = open_in_vscode(path)
        rel_path = os.path.relpath(path, PROJECT_ROOT)
        if opened:
            self.message = f"Opened {rel_path}. After editing, press Enter or R to run."
        else:
            self.message = f"Created {rel_path}. Could not open an editor automatically."
        self.items = self._build_items()

    def start_selected(self):
        self.open_selected_script()

    def solve_selected_challenge(self):
        """Copy the canonical optimal solution to the player's
        solutions/<id>.py, run it to capture the actual op count,
        and mark the challenge as done in progress.

        This is a pedagogical "give up and see the answer" action.
        The player can read the file in their editor, memorize the
        pattern, then click Reset to clear the completion and try
        again themselves.
        """
        item = self.current_item()
        if not item:
            return

        challenge_id = item.node.challenge_id
        optimal_path = os.path.join(
            PROJECT_ROOT, "optimal_solutions", f"{challenge_id}.py",
        )
        if not os.path.exists(optimal_path):
            self.message = (
                f"No optimal solution available for {challenge_id}."
            )
            return

        target_path = default_solution_path(challenge_id)
        rel_target = os.path.relpath(target_path, PROJECT_ROOT)
        try:
            shutil.copy2(optimal_path, target_path)
        except OSError as exc:
            self.message = f"Could not write {rel_target}: {exc}"
            return

        # Run the optimal solution to capture the real op count and
        # mark the challenge as done. We import the file via the
        # same loader the runner uses, so the solve() function is
        # available under the same module semantics.
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location(
                "_optimal_player", target_path,
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)  # type: ignore[union-attr]
            challenge = get_challenge(challenge_id)
            if challenge is None:
                self.message = (
                    f"Optimal saved to {rel_target} but no challenge is registered."
                )
                return
            result = challenge.run(
                solve_fn=module.solve,
                n=challenge.max_n,
                seed=1,
                animate=False,
                pygame=False,
            )
        except Exception as exc:  # noqa: BLE001
            self.message = (
                f"Optimal saved to {rel_target} but failed to run: "
                f"{type(exc).__name__}: {exc}"
            )
            return

        if not result.passed:
            self.message = (
                f"Optimal saved to {rel_target} but the verifier "
                f"rejected it: {result.message}"
            )
            return

        # Mark the challenge as completed with the optimal's stats.
        # Future runs by the player (if they edit and re-run) will
        # overwrite this with their own numbers via the runner's
        # existing progress.complete call.
        self.progress.complete(
            challenge_id,
            result.stats.total,
            result.actual_complexity.value,
        )
        save_progress(self.progress)
        self.items = self._build_items()
        self.message = (
            f"Optimal saved to {rel_target} and marked as done "
            f"({result.stats.total} ops, {result.actual_complexity.value}). "
            f"Open the file to study it, or press Reset to clear and try again."
        )

    def run_selected_challenge(self):
        item = self.current_item()
        if not item:
            return

        path = default_solution_path(item.node.challenge_id)
        if not os.path.exists(path):
            path = create_solution_file(item.node.challenge_id)
            open_in_vscode(path)
            self.message = f"Created {os.path.relpath(path, PROJECT_ROOT)}. Implement solve(), then press R again."
            self.items = self._build_items()
            return

        if getattr(sys, "frozen", False):
            command = [sys.executable, "--run-challenge", item.node.challenge_id, "--pygame"]
        else:
            script = os.path.join(PROJECT_ROOT, "run_challenge.py")
            command = [sys.executable, script, item.node.challenge_id, "--pygame"]
        log_path = launch_process(command)
        self.message = f"Running {item.node.challenge_id}. If nothing opens, check {os.path.relpath(log_path, PROJECT_ROOT)}"

    def explore_selected_challenge(self, screen, clock, fonts):
        import pygame

        item = self.current_item()
        if not item:
            return

        challenge = get_challenge(item.node.challenge_id)
        if not challenge:
            self.message = f"{item.node.challenge_id} is not implemented yet."
            return

        setup_data: dict[str, Any] = {}
        try:
            setup_data = challenge.setup(100, seed=7)
        except Exception:
            setup_data = {}

        buttons = self._explore_buttons()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if is_resize_event(pygame, event):
                    screen = pygame.display.get_surface() or screen
                    sync_window_size(self, screen)
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_ESCAPE, pygame.K_b):
                        return
                    if event.key in (pygame.K_RETURN, pygame.K_r):
                        self.run_selected_challenge()
                        return
                    if event.key == pygame.K_o:
                        self.open_selected_script()
                        return
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for action, rect in buttons:
                        if rect.collidepoint(event.pos):
                            if action == "back":
                                return
                            if action == "run":
                                self.run_selected_challenge()
                                return
                            if action == "open":
                                self.open_selected_script()
                                return

            buttons = self._explore_buttons()
            self._draw_explore(screen, fonts, challenge, setup_data, buttons)
            pygame.display.flip()
            clock.tick(60)

    def current_item(self) -> Optional[NavItem]:
        if not self.items:
            return None
        return self.items[self.selected_index]

    def _build_items(self) -> list[NavItem]:
        items: list[NavItem] = []
        for category in self.CATEGORIES:
            for node in self.tree.get_category_nodes(category):
                challenge = get_challenge(node.challenge_id)
                difficulty = challenge.info.difficulty if challenge else 0
                items.append(
                    NavItem(
                        node=node,
                        status=self.progress.status_for(node.challenge_id),
                        difficulty=difficulty,
                        implemented=challenge is not None,
                    )
                )
        # Only show challenges that have an implementation. The rest still
        # live in the tree (visible from the CLI tree view) but cluttering
        # the navigator with "not implemented" warnings breaks the flow.
        return [item for item in items if item.implemented]

    def _move_selection(self, delta: int):
        if not self.items:
            return
        self.selected_index = (self.selected_index + delta) % len(self.items)
        self._ensure_selected_visible()

    def _draw(self, screen, fonts):
        import pygame

        sync_window_size(self, screen)
        screen.fill(self.BACKGROUND)
        self._text(screen, fonts["title"], GAME_TITLE, 30, 24, self.TEXT)
        subtitle = f"{self.player_name()} - Data Structures and Algorithms (DSA)"
        self._text(screen, fonts["body"], subtitle, 30, 62, self.MUTED)

        margin = 30
        gap = 24
        top = 105
        bottom_h = 32
        bottom_y = max(top + 420, self.height - bottom_h - 20)
        content_h = max(360, bottom_y - top - 13)
        right_w = min(460, max(360, int(self.width * 0.34)))
        left_w = max(520, self.width - margin * 2 - gap - right_w)
        if left_w + right_w + gap > self.width - margin * 2:
            right_w = max(330, self.width - margin * 2 - gap - left_w)
        left = pygame.Rect(margin, top, left_w, content_h)
        right = pygame.Rect(left.right + gap, top, right_w, content_h)
        pygame.draw.rect(screen, self.SURFACE, left, border_radius=8)
        pygame.draw.rect(screen, self.SURFACE, right, border_radius=8)

        self._draw_list(screen, fonts, left)
        self._draw_details(screen, fonts, right)

        bottom = pygame.Rect(margin, bottom_y, self.width - margin * 2, bottom_h)
        pygame.draw.rect(screen, self.SURFACE_ALT, bottom, border_radius=6)
        self._text(screen, fonts["small"], self.message, bottom.x + 12, bottom.y + 8, self.TEXT)

    def _draw_list(self, screen, fonts, area):
        import pygame

        clip = screen.get_clip()
        screen.set_clip(area)
        y = area.y + 18 - self.scroll_y
        row_h = 38
        last_category = None
        self._row_rects: list[tuple[int, pygame.Rect]] = []

        for index, item in enumerate(self.items):
            if item.node.category != last_category:
                if last_category is not None:
                    y += 8
                if area.y <= y <= area.bottom - 26:
                    self._text(screen, fonts["heading"], self.CATEGORY_NAMES.get(item.node.category, item.node.category), area.x + 18, y, self.TEXT)
                y += 34
                last_category = item.node.category

            rect = pygame.Rect(area.x + 14, y, area.width - 28, row_h - 4)
            if rect.bottom >= area.y and rect.top <= area.bottom:
                self._row_rects.append((index, rect))
                if index == self.selected_index:
                    pygame.draw.rect(screen, self.SELECTED, rect, border_radius=6)
                else:
                    pygame.draw.rect(screen, self.SURFACE_ALT, rect, border_radius=6)

                status_color = self.MUTED
                if item.status == "done":
                    status_color = self.ACCENT
                elif item.status == "failed":
                    status_color = self.ERROR
                if not item.implemented:
                    status_color = self.WARNING
                self._text(screen, fonts["small"], item.status_label, rect.x + 12, rect.y + 10, status_color)
                self._text(screen, fonts["body"], f"{item.node.challenge_id}  {item.node.name}", rect.x + 92, rect.y + 8, self.TEXT)
                difficulty_text = f"D {item.difficulty}/10" if item.difficulty else "D --"
                difficulty_width = fonts["small"].size(difficulty_text)[0]
                self._text(screen, fonts["small"], difficulty_text, rect.right - difficulty_width - 14, rect.y + 10, self.MUTED)
            y += row_h

        screen.set_clip(clip)

    def _draw_details(self, screen, fonts, area):
        import pygame

        item = self.current_item()
        if not item:
            return

        challenge = get_challenge(item.node.challenge_id)
        padding = 18
        content_x = area.x + padding
        content_width = area.width - padding * 2
        # Layout, top to bottom in the details panel:
        #   ... description (clipped to description_bottom) ...
        #   Controls header + 1 line of shortcut text  (48 px)
        #   32 px visual gap
        #   5 action buttons in 2 rows             (96 px)
        #   16 px gap to the bottom-anchored footer
        #
        # So: controls_y = buttons_y - 32 - 48
        # And: buttons end at area.bottom - 16, so buttons_y = area.bottom - 112
        # Putting it together: controls_y = area.bottom - 192
        buttons_y = area.bottom - 112
        controls_y = buttons_y - 80
        description_bottom = controls_y - 14

        self._text(screen, fonts["heading"], item.node.name, area.x + 18, area.y + 18, self.TEXT)
        self._text(screen, fonts["body"], item.node.challenge_id, area.x + 18, area.y + 52, self.MUTED)

        y = area.y + 94
        status_color = self.MUTED
        if item.status == "done":
            status_color = self.ACCENT
        elif item.status == "failed":
            status_color = self.ERROR
        self._text(screen, fonts["body"], f"Status: {item.status_label}", content_x, y, status_color)
        y += 28
        self._text(screen, fonts["small"], f"Script: solutions/{item.node.challenge_id}.py", content_x, y, self.TEXT)
        y += 24
        self._text(screen, fonts["small"], f"Student: {self.player_name()}", content_x, y, self.TEXT)
        y += 28

        if challenge:
            info = challenge.info
            self._text(screen, fonts["small"], f"Required: {info.required_complexity.value}    Difficulty: {info.difficulty}/10", content_x, y, self.TEXT)
            y += 30
            if y + 24 < description_bottom:
                self._text(screen, fonts["body"], "Description", content_x, y, self.TEXT)
                y += 24
            previous_clip = screen.get_clip()
            screen.set_clip(pygame.Rect(content_x, y, content_width, max(0, description_bottom - y)))
            for line in self._wrap(info.description.replace("\n", " "), 42):
                if y + 18 > description_bottom:
                    self._text(screen, fonts["small"], "...", content_x, max(area.y, description_bottom - 18), self.MUTED)
                    break
                self._text(screen, fonts["small"], line, content_x, y, self.MUTED)
                y += 20
            screen.set_clip(previous_clip)
        else:
            if y < description_bottom:
                self._text(screen, fonts["body"], "Challenge exists in tree, but is not implemented yet.", content_x, y, self.WARNING)

        # Controls section comes BEFORE the action buttons, with a
        # 32 px visual gap between the two so they don't read as
        # one block. The controls are minimal: only the truly
        # global shortcuts (name, refresh, quit) live here, because
        # the per-button shortcuts are already embedded in the
        # button labels themselves.
        y = controls_y
        self._text(screen, fonts["body"], "Controls", content_x, y, self.TEXT)
        y += 28
        for line in ["N: student name | F5: refresh | Esc: quit"]:
            self._text(screen, fonts["small"], line, content_x, y, self.MUTED)
            y += 20

        self._draw_action_buttons(screen, fonts, area, buttons_y)

    def _draw_action_buttons(self, screen, fonts, area, y: int):
        import pygame

        # Two rows: regular actions on top, "give up / start over" below.
        # Row 1: Explore | Run | Open. Three buttons in one row.
        # Row 2: Solve (red, "see the answer") | Reset (warning, "start over").
        gap = 8
        row_h = 44
        inner_w = area.width - 36

        # Row 1: three equal-width buttons
        top_width = (inner_w - gap * 2) // 3
        explore_rect = pygame.Rect(area.x + 18, y, top_width, row_h)
        run_rect = pygame.Rect(explore_rect.right + gap, y, top_width, row_h)
        open_rect = pygame.Rect(run_rect.right + gap, y, top_width, row_h)

        # Row 2: two equal-width buttons
        second_y = y + row_h + 8
        bottom_width = (inner_w - gap) // 2
        solve_rect = pygame.Rect(area.x + 18, second_y, bottom_width, row_h)
        reset_rect = pygame.Rect(solve_rect.right + gap, second_y, bottom_width, row_h)

        self._button_rects = [
            ("explore", explore_rect),
            ("run", run_rect),
            ("open", open_rect),
            ("solve", solve_rect),
            ("reset", reset_rect),
        ]

        # Fill colors. Solve is RED: it's "give up and see the
        # answer", a destructive-from-learning-perspective action.
        # Reset is WARNING (yellow/orange) - "start over" is also
        # non-ideal but reversible.
        pygame.draw.rect(screen, self.SELECTED, explore_rect, border_radius=7)
        pygame.draw.rect(screen, self.ACCENT, run_rect, border_radius=7)
        pygame.draw.rect(screen, self.SURFACE_ALT, open_rect, border_radius=7)
        pygame.draw.rect(screen, self.ERROR, solve_rect, border_radius=7)
        pygame.draw.rect(screen, self.WARNING, reset_rect, border_radius=7)
        for _, r in self._button_rects:
            pygame.draw.rect(screen, self.GRID_LINE, r, width=1, border_radius=7)
        # Each label embeds the keyboard shortcut in (parentheses)
        # so the player can learn the bindings just by looking at
        # the button row. Solve and Reset deliberately have no
        # shortcut: both are destructive-from-learning-perspective
        # actions, and we don't want an accidental keypress to wipe
        # the player's progress or spoil a challenge.
        self._center_text(screen, fonts["body"], "Explore (E)", explore_rect, self.TEXT)
        self._center_text(screen, fonts["body"], "Run (R)", run_rect, self.TEXT)
        self._center_text(screen, fonts["body"], "Open (O)", open_rect, self.TEXT)
        self._center_text(screen, fonts["body"], "Solve", solve_rect, self.TEXT)
        self._center_text(screen, fonts["body"], "Reset", reset_rect, self.TEXT)

    def _explore_buttons(self):
        import pygame

        y = self.height - 70
        return [
            ("back", pygame.Rect(48, y, 130, 42)),
            ("run", pygame.Rect(194, y, 130, 42)),
            ("open", pygame.Rect(340, y, 180, 42)),
        ]

    def _draw_explore(self, screen, fonts, challenge, setup_data: dict[str, Any], buttons):
        import pygame

        sync_window_size(self, screen)
        screen.fill(self.BACKGROUND)
        info = challenge.info
        self._text(screen, fonts["title"], f"Explore: {info.name}", 36, 26, self.TEXT)
        self._text(screen, fonts["body"], f"Student: {self.player_name()}    Required: {info.required_complexity.value}", 36, 66, self.MUTED)

        # Two columns below the title strip. The left pane is the
        # Description (kept wide on purpose so it can grow long in
        # the future without overflowing the right column). The
        # right pane is split vertically: Function signature on
        # top, Input / Output samples below it.
        panel_gap = 28
        panel_top = 100
        panel_bottom_pad = 100
        panel_height = max(220, self.height - panel_top - panel_bottom_pad)
        left_width = max(420, int((self.width - 72 - panel_gap) * 0.55))
        right_width = self.width - 72 - panel_gap - left_width

        desc_rect = pygame.Rect(36, panel_top, left_width, panel_height)
        right_rect = pygame.Rect(desc_rect.right + panel_gap, panel_top, right_width, panel_height)

        right_inner_gap = 20
        sig_height = (right_rect.height - right_inner_gap) // 2
        sig_rect = pygame.Rect(right_rect.x, right_rect.y, right_rect.width, sig_height)
        samples_rect = pygame.Rect(
            right_rect.x,
            sig_rect.bottom + right_inner_gap,
            right_rect.width,
            right_rect.height - sig_height - right_inner_gap,
        )

        pygame.draw.rect(screen, self.SURFACE, desc_rect, border_radius=8)
        pygame.draw.rect(screen, self.SURFACE, sig_rect, border_radius=8)
        pygame.draw.rect(screen, self.SURFACE, samples_rect, border_radius=8)

        # Description fills the entire left panel. Wrap to a width
        # that fits the panel and stop drawing when we run out of
        # room - description text is short in practice, so truncation
        # only happens for unusually long ones.
        self._text(screen, fonts["body"], "Description", desc_rect.x + 16, desc_rect.y + 14, self.TEXT)
        desc_y = desc_rect.y + 42
        desc_wrap = self._chars_for_width(fonts["small"], desc_rect.width - 32)
        for line in self._wrap(info.description.replace("\n", " "), desc_wrap):
            if desc_y + 20 > desc_rect.bottom - 16:
                break
            self._text(screen, fonts["small"], line, desc_rect.x + 16, desc_y, self.MUTED)
            desc_y += 20

        # Right column: Function signature (top), Input / Output samples (bottom).
        self._text(screen, fonts["body"], "Function signature", sig_rect.x + 16, sig_rect.y + 14, self.TEXT)
        self._draw_function_signature(screen, fonts, challenge, setup_data, sig_rect)
        self._text(screen, fonts["body"], "Input / Output samples", samples_rect.x + 16, samples_rect.y + 14, self.TEXT)
        self._draw_sample_lines(screen, fonts, info.id, samples_rect)

        for action, rect in buttons:
            fill = self.SURFACE_ALT
            if action == "run":
                fill = self.ACCENT
            elif action == "back":
                fill = self.SELECTED
            pygame.draw.rect(screen, fill, rect, border_radius=7)
            pygame.draw.rect(screen, self.GRID_LINE, rect, width=1, border_radius=7)
            label = {"back": "Back", "run": "Run", "open": "Open Script"}[action]
            self._center_text(screen, fonts["body"], label, rect, self.TEXT)

        self._text(screen, fonts["small"], "Esc/B: back   Enter/R: run   O: open script", 540, self.height - 58, self.MUTED)

    def _draw_function_signature(self, screen, fonts, challenge, setup_data, area):
        """Render the function signature, input descriptions, and return
        description inside ``area`` (a panel rect with 16 px padding)."""
        import pygame

        sig_y = area.y + 50
        # Build the call signature: def solve(arg1, arg2, ...):
        args = ", ".join(setup_data.keys()) if setup_data else ""
        sig_text = f"def solve({args}):"
        self._text(screen, fonts["body"], sig_text, area.x + 16, sig_y, self.TEXT)
        sig_y += 28

        # Per-argument hint: for each input, show the name and a
        # short description taken from the challenge's ChallengeInfo.
        # Indent the label by 2 spaces and the description by 4
        # spaces - that visual hierarchy matches the return block
        # below and keeps the column readable.
        wrap_width = self._chars_for_width(fonts["small"], area.width - 32)
        arg_hints = self._arg_hints_for(challenge)
        if arg_hints:
            for arg_name, hint_text in arg_hints.items():
                if arg_name not in setup_data:
                    continue
                self._text(screen, fonts["small"], f"  {arg_name}:", area.x + 16, sig_y, self.MUTED)
                sig_y += 18
                for line in self._wrap(hint_text, wrap_width):
                    self._text(screen, fonts["small"], f"    {line}", area.x + 16, sig_y, self.MUTED)
                    sig_y += 18
                sig_y += 4

        # Return description - prefer an explicit hint from the
        # challenge, else say "see the sample I/O on the right".
        # Indentation mirrors the per-arg block: label at 2 spaces,
        # description at 4 spaces so the two columns line up.
        return_text = self._return_hint_for(challenge)
        self._text(screen, fonts["small"], "  return:", area.x + 16, sig_y, self.MUTED)
        sig_y += 18
        for line in self._wrap(return_text, wrap_width):
            self._text(screen, fonts["small"], f"    {line}", area.x + 16, sig_y, self.MUTED)
            sig_y += 18

    def _draw_sample_lines(self, screen, fonts, challenge_id, area):
        """Render the input/output sample lines inside ``area``."""
        sample_y = area.y + 50
        for line in sample_lines(challenge_id):
            if sample_y + 18 > area.bottom - 16:
                # Truncate with an ellipsis if we run out of room.
                self._text(screen, fonts["small"], "...", area.x + 16, area.bottom - 22, self.MUTED)
                break
            self._text(screen, fonts["small"], line, area.x + 16, sample_y, self.MUTED)
            sample_y += 20

    def _arg_hints_for(self, challenge) -> dict[str, str]:
        """Per-challenge map of input-name -> human-readable description.

        Sourced from the challenge's :class:`AlgorithmSpec`. Adding
        a new challenge is one entry in the spec - no edit here.
        """
        spec = getattr(challenge, "_spec", None)
        if spec is not None:
            return dict(spec.inputs)
        return {}

    def _return_hint_for(self, challenge) -> str:
        """Per-challenge return-value description.

        Sourced from the challenge's :class:`AlgorithmSpec`.
        """
        spec = getattr(challenge, "_spec", None)
        if spec is not None:
            return spec.returns
        return "see the sample I/O on the right."

    def _draw_sample_grid(self, screen, fonts, grid: Optional[Grid], area):
        import pygame

        if not grid:
            self._text(screen, fonts["small"], "No visual sample is available for this challenge.", area.x, area.y, self.MUTED)
            return

        cell_size = max(22, min(48, area.width // max(1, grid.width), area.height // max(1, grid.height)))
        grid_width = cell_size * grid.width
        grid_height = cell_size * grid.height
        start_x = area.x + max(0, (area.width - grid_width) // 2)
        start_y = area.y + max(0, (area.height - grid_height) // 2)
        for y in range(grid.height):
            for x in range(grid.width):
                cell = grid.get(x, y)
                rect = pygame.Rect(start_x + x * cell_size, start_y + y * cell_size, cell_size - 2, cell_size - 2)
                color = self.CELL_COLORS.get(cell.cell_type, self.SURFACE_ALT)
                pygame.draw.rect(screen, color, rect, border_radius=4)
                pygame.draw.rect(screen, self.GRID_LINE, rect, width=1, border_radius=4)
                label = str(cell.value) if cell.value is not None else cell.label
                if label:
                    self._center_text(screen, fonts["small"], label[:5], rect, self.TEXT)

    def _draw_setup_summary(self, screen, fonts, setup_data: dict[str, Any], x: int, y: int, width: int):
        lines = self._setup_summary_lines(setup_data)
        for line in lines[:4]:
            self._text(screen, fonts["small"], line[:58], x, y, self.MUTED)
            y += 18

    def _setup_summary_lines(self, setup_data: dict[str, Any]) -> list[str]:
        if not setup_data:
            return ["Sample setup could not be generated."]
        lines: list[str] = []
        for name, value in setup_data.items():
            if isinstance(value, TrackedList):
                lines.append(f"{name}: {value.raw[:10]}")
            elif isinstance(value, TrackedGrid):
                lines.append(f"{name}: {value.width}x{value.height} tracked grid")
            else:
                lines.append(f"{name}: {value}")
        return lines

    def _draw_example_solution(self, screen, fonts, challenge_id: str, area):
        previous_clip = screen.get_clip()
        import pygame

        code_area = pygame.Rect(area.x + 16, area.y + 48, area.width - 32, area.height - 64)
        screen.set_clip(code_area)
        y = code_area.y
        for line in self._example_solution_lines(challenge_id):
            self._text(screen, fonts["small"], line, code_area.x, y, self.MUTED if line.strip().startswith("#") else self.TEXT)
            y += 18
            if y > code_area.bottom:
                break
        screen.set_clip(previous_clip)

    def _example_solution_lines(self, challenge_id: str) -> list[str]:
        # Prefer the registered AlgorithmSpec's source so the example
        # is always in sync with the actual canonical solution.
        from challenges.registry import get_challenge
        challenge = get_challenge(challenge_id)
        spec = getattr(challenge, "_spec", None) if challenge is not None else None
        if spec is not None:
            return _strip_leading_docstring(spec.source)

        # Fall back to a generic stub for unknown ids.
        return [
            "# Study the input names shown on the left.",
            "# Keep the operation limit in mind.",
            "def solve():",
            "    # Build a small correct version first.",
            "    return None",
        ]

    def _item_at(self, pos) -> Optional[int]:
        for index, rect in getattr(self, "_row_rects", []):
            if rect.collidepoint(pos):
                return index
        return None

    def _button_at(self, pos) -> Optional[str]:
        for action, rect in getattr(self, "_button_rects", []):
            if rect.collidepoint(pos):
                return action
        return None

    def _ensure_selected_visible(self):
        top, bottom = self._selected_row_bounds()
        visible_top = 0
        visible_bottom = 560
        if top - self.scroll_y < visible_top:
            self.scroll_y = max(0, top - 8)
        elif bottom - self.scroll_y > visible_bottom:
            self.scroll_y = max(0, bottom - visible_bottom + 8)

    def _selected_row_bounds(self) -> tuple[int, int]:
        y = 18
        row_h = 38
        last_category = None
        for index, item in enumerate(self.items):
            if item.node.category != last_category:
                if last_category is not None:
                    y += 8
                y += 34
                last_category = item.node.category
            if index == self.selected_index:
                return y, y + row_h
            y += row_h
        return 0, row_h

    def _text(self, screen, font, text, x, y, color):
        screen.blit(font.render(text, True, color), (x, y))

    def _center_text(self, screen, font, text, rect, color):
        surface = font.render(text, True, color)
        screen.blit(surface, surface.get_rect(center=rect.center))

    def _prompt_player_name(self, screen, clock, fonts, editing: bool = False) -> bool:
        import pygame

        typed = "" if not editing else self.player_name()
        cursor_visible = True
        last_cursor_toggle = datetime.now()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if is_resize_event(pygame, event):
                    screen = pygame.display.get_surface() or screen
                    sync_window_size(self, screen)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return editing
                    if event.key == pygame.K_RETURN:
                        self.progress.player_name = normalize_player_name(typed)
                        save_progress(self.progress)
                        self.message = f"Student profile set to {self.player_name()}."
                        return True
                    if event.key == pygame.K_BACKSPACE:
                        typed = typed[:-1]
                    elif event.unicode and len(typed) < MAX_PLAYER_NAME_LENGTH:
                        char = event.unicode
                        if 32 <= ord(char) <= 126:
                            typed += char

            if (datetime.now() - last_cursor_toggle).total_seconds() > 0.5:
                cursor_visible = not cursor_visible
                last_cursor_toggle = datetime.now()

            screen.fill(self.BACKGROUND)
            self._text(screen, fonts["title"], GAME_TITLE, 48, 42, self.TEXT)
            self._text(screen, fonts["body"], "Choose the name of the student you will play.", 48, 84, self.MUTED)

            story_y = 138
            for paragraph in BACKSTORY_PARAGRAPHS:
                for line in self._wrap(paragraph, 82)[:4]:
                    self._text(screen, fonts["small"], line, 48, story_y, self.TEXT)
                    story_y += 20
                story_y += 14

            box = pygame.Rect(48, self.height - 178, 520, 48)
            pygame.draw.rect(screen, self.SURFACE, box, border_radius=7)
            pygame.draw.rect(screen, self.GRID_LINE, box, width=2, border_radius=7)
            display_name = typed + ("_" if cursor_visible else "")
            self._text(screen, fonts["body"], display_name or "Type a name", box.x + 14, box.y + 13, self.TEXT if typed else self.MUTED)
            self._text(screen, fonts["small"], "Enter: continue   Backspace: edit   Esc: cancel", 48, self.height - 106, self.MUTED)
            self._text(screen, fonts["small"], "Names are stored locally in progress.json.", 48, self.height - 80, self.MUTED)

            pygame.display.flip()
            clock.tick(60)

    def _wrap(self, text: str, width: int) -> list[str]:
        words = text.split()
        lines: list[str] = []
        current = ""
        for word in words:
            if len(current) + len(word) + 1 > width:
                if current:
                    lines.append(current)
                current = word
            else:
                current = f"{current} {word}".strip()
        if current:
            lines.append(current)
        return lines or [""]

    @staticmethod
    def _chars_for_width(font, pixel_width: int) -> int:
        """Approximate how many characters of ``font`` fit in ``pixel_width``.

        Used when we know a panel's width in pixels but ``_wrap``
        wants a char count. Falls back to a conservative estimate
        of 8 px per char when the font size is unknown.
        """
        if pixel_width <= 0:
            return 20
        char_w = 8
        try:
            char_w, _ = font.size("M")
        except (AttributeError, Exception):
            pass
        if not char_w or char_w <= 0:
            char_w = 8
        return max(20, pixel_width // char_w)


def create_solution_file(challenge_id: str) -> str:
    """Create a challenge solution script if it does not exist yet."""
    challenge = get_challenge(challenge_id)
    if challenge:
        info = challenge.info
        return create_saved_solution_file(challenge_id, info.name, info.description)
    return create_saved_solution_file(challenge_id)


def open_in_vscode(path: str) -> bool:
    """Open a file in VS Code using the command line if it is available."""
    normalized = os.path.normpath(path)
    command = _find_code_command()
    if command:
        subprocess.Popen([command, "-g", normalized], cwd=PROJECT_ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True

    notepad = shutil.which("notepad.exe") or "notepad.exe"
    try:
        subprocess.Popen([notepad, normalized], cwd=PROJECT_ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except OSError:
        return False


def launch_process(command: list[str]) -> str:
    log_dir = os.path.join(PROJECT_ROOT, "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, "last_challenge_run.log")
    with open(log_path, "w", encoding="utf-8") as log_file:
        log_file.write(f"Started: {datetime.now().isoformat(timespec='seconds')}\n")
        log_file.write(f"Command: {' '.join(command)}\n\n")
        subprocess.Popen(command, cwd=PROJECT_ROOT, stdout=log_file, stderr=log_file)
    return log_path


def _find_code_command() -> Optional[str]:
    command = shutil.which("code") or shutil.which("code.cmd")
    if command:
        return command

    local_app_data = os.environ.get("LOCALAPPDATA")
    if local_app_data:
        candidate = os.path.join(local_app_data, "Programs", "Microsoft VS Code", "bin", "code.cmd")
        if os.path.exists(candidate):
            return candidate
    return None


def launch_navigation():
    ChallengeNavigator().run()
