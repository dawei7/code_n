# Releasing cOde(n) — auto-update flow

This doc covers how to cut a new release so existing installations of
cOde(n) auto-update themselves. Read this end-to-end the first time;
the second time it's a single command.

---

## 1. Architecture at a glance

```
                       YOUR MACHINE                       GITHUB
                       ────────────                       ──────
   1. python release.py                            ─────▶
      ┌─ bumps electron/package.json to v0.2.0
      ├─ git commit + push main
      ├─ git tag v0.2.0 + push tag
      ├─ builds web (Vite) + server (PyInstaller) + electron (TS)
      └─ electron-builder --publish onTagOrDraft (reads $GH_TOKEN)
         ├─ packages cOde(n)-Setup-0.2.0.exe (NSIS installer)
         ├─ packages win-unpacked/cOde(n).exe (portable)
         ├─ generates latest.yml + .blockmap
         └─ creates a published GitHub Release for v0.2.0
                                                       ────▶  Releases/v0.2.0

   2. User opens cOde(n) v0.1.0 on their machine
      ┌─ main process: autoUpdater.checkForUpdates()         ─────▶  GitHub API
      │   (one shot, on launch)
      ├─ finds v0.2.0, sees it's newer stable              ─────▶  latest.yml
      ├─ autoDownloads the new installer in the background
      └─ shows a "Restart to install" pill in the UI
   3. User clicks Restart → quitAndInstall()
      └─ NSIS applies the diff (delta update via .blockmap).
         On next launch the user is on 0.2.0.
```

The "check on launch" is a one-shot, not periodic — the spec is
"check on launch only".

---

## 2. The first time you do this (one-time setup)

### 2.1 Create a scoped GitHub PAT

Do **not** use a personal token with broad scope, and do **not** paste
your token into any chat / issue / wiki.

1. Open <https://github.com/settings/tokens?type=beta> in a browser.
2. **Generate new token → Fine-grained**.
3. **Resource owner**: just `dawei7`.
4. **Repository access**: select **only** `dawei7/code_n`.
5. **Permissions → Repository permissions**: only
   - `Contents: Read and write`  (electron-builder creates a Release
     via the GitHub Releases API, which is under Contents)
6. **Expiration**: 90 days is fine. Rotate.
7. Generate. Copy the token — you only see it once.

### 2.2 Store the token on your machine

Either:

- **Recommended (cross-machine, ephemeral)**: set it in your shell.
  ```powershell
  # PowerShell (this session only)
  $env:GH_TOKEN = "ghp_..."
  # Persist across sessions (Windows; do NOT commit the resulting
  # env-var dump)
  [Environment]::SetEnvironmentVariable("GH_TOKEN", "ghp_...", "User")
  ```
- **Or (one-machine)**: paste it into `electron/.env`:
  ```bash
  # electron/.env  (gitignored — never commit)
  GH_TOKEN=ghp_...
  ```
  A template at `electron/.env.example` shows the format.

electron-builder reads `$GH_TOKEN` from the environment at build
time. `electron/.env` is **not** auto-loaded — use `direnv` or
`dotenv-cli` if you want it. (Easiest: just set the env var in
your shell.)

### 2.3 Sanity check (no token needed)

```bash
cd electron
npm install            # one time, picks up electron-updater
npm run dist:dry       # packages the .exe WITHOUT publishing
```

This should produce both:

- `electron/release/cOde(n)-Setup-0.1.0.exe` (the NSIS installer, ~95 MB)
- `electron/release/win-unpacked/cOde(n).exe` (the portable folder, ~170 MB)

If this fails, you have a build-pipeline bug — fix that before
cutting a real release.

---

## 3. Cutting a real release (one command)

```bash
cd "c:/dawei7/code_n"

# Make sure $GH_TOKEN is set in this shell.
echo $GH_TOKEN   # sanity check; should print your token

# Cut a minor release: 0.1.0 -> 0.2.0
.venv/Scripts/python.exe release.py

# Or a patch release: 0.1.0 -> 0.1.1
.venv/Scripts/python.exe release.py --patch

# Or an explicit version: 1.0.0-rc1, etc.
.venv/Scripts/python.exe release.py --set 1.0.0

# Or a dry-run (bump + tag + build, but no push / no publish):
.venv/Scripts/python.exe release.py --dry-run
```

`release.py` does the whole pipeline:
1. Bumps `electron/package.json` (default: minor; `--patch` for
   hotfix; `--set X.Y.Z` for explicit).
2. Refuses to run on a dirty working tree or non-`main` branch.
3. Commits the version bump, pushes the branch, creates + pushes
   the `vX.Y.Z` tag.
4. Builds web + server + electron artifacts.
5. Runs `electron-builder --win --x64 --publish onTagOrDraft`,
   which uses `$GH_TOKEN` to:
   - Create a published GitHub release for the tag.
   - Attach the NSIS installer (`cOde(n)-Setup-X.Y.Z.exe`),
     its `.blockmap`, and `latest.yml`.
6. (Optional, see `--cleanup-old` below) Deletes the
   installer/blockmap of every older release to save ~95 MB
   per old release.
7. Prints the release URL at the end.

After the script finishes, every installed cOde(n) on the
previous version will auto-pull the new release on its next
launch.

### Saving space: `--cleanup-old`

GitHub Releases are independent — each release keeps its
own copy of every asset. For a project that releases
frequently, that adds up to ~95 MB × N releases. To keep
only the **latest** release's installer on the repo (old
release ENTRIES are kept, so version history stays
visible), pass `--cleanup-old`:

```bash
.venv/Scripts/python.exe release.py --cleanup-old
```

This calls `release_cleanup.py` after the publish. The
script also has a standalone mode:

```bash
# Show what would be deleted (no API writes)
.venv/Scripts/python.exe release_cleanup.py --dry-run

# Delete old release assets (keeps the latest)
.venv/Scripts/python.exe release_cleanup.py --yes

# Keep a specific tag (instead of auto-picking the latest)
.venv/Scripts/python.exe release_cleanup.py --keep v0.5.0 --yes

# Also delete the old release ENTRIES (git tags stay)
.venv/Scripts/python.exe release_cleanup.py --yes --delete-releases
```

The cleanup is **irreversible** — old installers can't be
re-downloaded from GitHub once deleted. Users who haven't
auto-updated past the latest version can still install
from the latest release directly, but anyone pinned to a
specific old version would need to upgrade.

The token needs `Contents: read and write` (the same
permission `release.py` already needs).

### Behavior matrix

| State                                 | User sees                                           |
|---------------------------------------|------------------------------------------------------|
| Idle (just launched, no auto-check yet) | Nothing. "Check for updates" button is normal.      |
| Checking (auto on launch, ~1-3s)       | "Checking…" briefly in the button label.           |
| Not available                          | Nothing changes. Button tooltip = "up to date".    |
| Available → Downloading (auto)         | Small toast: "Downloading update v0.X.Y…" + bar.   |
| Downloaded                             | Green pill: "Update ready — Restart to install".    |
| Error (network / 404 / rate-limit)    | Button tooltip = error message. No modal.           |
| Dev mode (browser / npm start)        | Hooks are no-ops. Button visible but inert.         |

---

## 4. Verifying a release

- Check <https://github.com/dawei7/code_n/releases/tag/vX.Y.Z>:
  the release should be **published** (not draft), with all three
  artifacts attached (`*.exe`, `*.exe.blockmap`, `latest.yml`).
- On a machine with the previous version installed, launch
  cOde(n). The "Check for updates" button should briefly show
  "Checking…" and then either:
  - "You are on the latest version" (if the test machine is
    already on the new version), OR
  - a green "Update v0.X.Y ready" pill in the bottom-right with a
    Restart button. Click Restart → on next launch you're on the
    new version.

---

## 5. Troubleshooting

### "FATAL: $GH_TOKEN is not set"

`release.py` checks for `$GH_TOKEN` upfront and refuses to run.
Set it in your shell (see section 2.2) and re-run.

### "FATAL: working tree is dirty"

Commit or stash your uncommitted changes, then re-run. The bump
+ tag should be the only thing in the release commit.

### "FATAL: current branch is 'X', not 'main'"

Releases are only cut from `main`. Switch to `main` and rebase
your changes if needed.

### "FATAL: tag vX.Y.Z already exists on origin"

The tag was already pushed (maybe from a previous run that
partially failed). Either:
- Cut a different version (`--set X.Y.Z+1`)
- Or delete the tag locally + remotely:
  ```bash
  git tag -d vX.Y.Z
  git push origin --delete vX.Y.Z
  ```

### "Build complains GitHub Personal Access Token is not set"

```
Error: GitHub Personal Access Token is not set, neither programmatically, nor using env variable "GH_TOKEN"
```

→ `$GH_TOKEN` is not in the environment of the shell that ran
the build. Run `echo $GH_TOKEN` in that shell — if it's
empty, your `.env` isn't being loaded, or you set it in a
different shell. Use `direnv` or set it inline:
```bash
GH_TOKEN=ghp_...  .venv/Scripts/python.exe release.py
```

### Build creates the release as a draft

→ The token doesn't have `Contents: write`. Re-create the
fine-grained PAT with that one permission checked.

### App says "Update error" on launch

- Check the dev console (or `%APPDATA%\cOde(n)\logs\`) for the
  updater log line. The most common cause is a typo in the
  `owner` / `repo` / `channel` block of `electron-builder.json`.
- The `latest.yml` file MUST be at the root of the GitHub Release
  asset list; electron-builder does this automatically, but if
  you uploaded the .exe manually, the updater will not find the
  manifest.

### "I cut a release but the running app doesn't see it"

- The `autoUpdater.channel` defaults to whatever the version was
  at install time. If you install `0.1.0` then publish `0.2.0`,
  the running `0.1.0` updater sees the `latest.yml` and knows
  `0.2.0` is newer — fine. If you install `0.1.0-beta` then
  publish `0.2.0` (stable), the `0.1.0-beta` channel is `beta`,
  NOT `latest`, so the `latest.yml` says "your channel has no
  update". This is by design.
- To force a re-check, click "↻ Check for updates" in the header.

### "I want to test the updater without shipping a real release"

Use `npm run dist:dry` from `electron/`. It builds the installer
and the portable folder, but does NOT publish. The auto-updater
will report `not-available` (correct — no GitHub release exists).
To actually test the download flow, cut a **draft** GitHub
Release manually with the artifacts from a `dist:dry` build,
install the previous version of the installer somewhere else,
and click "Check for updates". Then `dist:dry` again with the
new version. The auto-updater DOES check for updates across
`draft` releases (only `prerelease` is filtered out by
`releaseType: "release"`).
