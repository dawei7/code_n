# Releasing cOde(n) — auto-update flow

This doc covers how to cut a new release so existing
installations of cOde(n) auto-update themselves. Read this end-to-end
the first time; the second time it's a 5-minute checklist.

---

## 1. Architecture at a glance

```
                       YOUR MACHINE                       GITHUB
                       ────────────                       ──────
   1. git tag v0.2.0 && git push --tags        ─────▶
   2. python build_app.py (or npm run dist)
      ┌─ electron-builder reads $GH_TOKEN
      ├─ packages win-unpacked/ + a portable .exe
      ├─ creates a draft GitHub Release for v0.2.0
      └─ uploads .exe + .blockmap + latest.yml         ────▶  Releases/v0.2.0

   3. User opens cOde(n) v0.1.0 on their machine
      ┌─ main process: autoUpdater.checkForUpdates()         ────▶  GitHub API
      │   (one shot, on launch)
      ├─ finds v0.2.0, sees it's newer stable              ────▶  latest.yml
      ├─ autoDownloads the new .exe in the background
      └─ shows a "Restart to install" pill in the UI
   4. User clicks Restart → quitAndInstall()
      └─ On next launch, the user is on v0.2.0.
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

This should produce `electron/release/win-unpacked/cOde(n).exe` and
NOT touch GitHub. If this fails, you have a build-pipeline bug —
fix that before cutting a real release.

---

## 3. Cutting a real release (5 minutes)

### 3.1 Bump the version

`electron/package.json` is the source of truth. Bump it:

```json
{
  "name": "coden-electron",
  "version": "0.2.0",
  ...
}
```

(`0.1.0` → `0.2.0` for new features, `0.1.0` → `0.1.1` for patches.
`0.1.0` → `1.0.0` is your call when you decide it's "stable".)

### 3.2 Commit + tag

```bash
cd <repo-root>
# Stage and commit the version bump.
git add electron/package.json
git commit -m "chore: bump version to v0.2.0"
# Create the matching tag.
git tag v0.2.0
git push origin main --tags
```

The `v` prefix is conventional; electron-builder will strip it for
the GitHub Release name (`Release v0.2.0` or `0.2.0`).

### 3.3 Build + publish

```bash
cd <repo-root>
# Make sure $GH_TOKEN is set in this shell.
echo $GH_TOKEN   # sanity check; should print your token

# Build + publish. This is the step that talks to GitHub.
.venv/Scripts/python.exe build_app.py
# or, if you've already built web+server:
cd electron && npm run dist
```

What electron-builder does under the hood:
1. Runs `electron-builder --win --x64` with `publish: { provider: "github", owner: "dawei7", repo: "code_n", releaseType: "release", channel: "latest" }`.
2. Builds the unpacked `electron/release/win-unpacked/`.
3. Calls the GitHub Releases API to create a draft release for
   the tag, uploads `cOde(n) 0.X.Y.exe` + the `.blockmap` +
   `latest.yml` to it, then publishes (un-drafts) the release.
4. **Stable only**: `releaseType: "release"` + `channel: "latest"`
   ensures pre-releases (`-rc`, `-beta`) are NEVER picked up by
   `autoUpdater.channel = 'latest'` in `electron/src/updater.ts`.

### 3.4 Verify

- Check <https://github.com/dawei7/code_n/releases/tag/v0.2.0>:
  the release should be **published** (not draft), with all three
  artifacts attached (`*.exe`, `*.exe.blockmap`, `latest.yml`).
- On a machine with the previous version installed, launch
  cOde(n). The "Check for updates" button should briefly show
  "Checking…" and then either:
  - "You are on the latest version" (if the test machine is
    already on the new version), OR
  - a green "Update v0.2.0 ready" pill in the bottom-right with a
    Restart button. Click Restart → on next launch you're on 0.2.0.

---

## 4. Behavior matrix

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

## 5. Troubleshooting

### Build complains "GitHub Personal Access Token is not set"

```
Error: GitHub Personal Access Token is not set, neither programmatically, nor using env variable "GH_TOKEN"
```

→ `$GH_TOKEN` is not in the environment of the shell that ran
`npm run dist`. Run `echo $GH_TOKEN` in that shell — if it's
empty, your `.env` isn't being loaded, or you set it in a
different shell. Use `direnv` or set it inline:

```bash
GH_TOKEN=ghp_...  npm run dist
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

Use `npm run dist:dry` from `electron/`. It builds the unpacked
app, but does NOT publish. The auto-updater will report
`not-available` (correct — no GitHub release exists). To actually
test the download flow, cut a **draft** GitHub Release manually
with the artifacts from a `dist:dry` build, install the previous
version of the .exe somewhere else, and click "Check for updates".
Then `dist:dry` again with the new version. The auto-updater
DOES check for updates across `draft` releases (only `prerelease`
is filtered out by `releaseType: "release"`).
