"use strict";
/**
 * Electron main process for the cOde(n) desktop wrapper.
 *
 * Flow:
 *   1. Spawn uvicorn as a child process (server-process.ts).
 *   2. Wait for the FastAPI server to write its port file.
 *   3. Open a BrowserWindow at the server's URL.
 *   4. The renderer can request "open in VSCode" via IPC,
 *      which calls ``shell.openPath(repoRoot)``. VSCode on
 *      the user's machine handles the rest — opening the
 *      project at the repo root, with the cOde(n)-written
 *      ``solutions/.vscode-active`` file telling the launch
 *      config which challenge to default to.
 *   5. On quit, kill the uvicorn process so it doesn't outlive
 *      the app.
 *
 * The v0.9.0 pivot removed the pop-out-editor, pop-out-debug,
 * and pop-out-pane BrowserWindows (the cOde(n) app is now a
 * single window; editing + debugging happens in VSCode).
 * The detachedWindows map is gone.
 */
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
const electron_1 = require("electron");
const path = __importStar(require("node:path"));
const server_process_1 = require("./server-process");
const updater_1 = require("./updater");
let mainWindow = null;
let server = null;
/** Resolve the repo root by walking up from electron/dist/main.js. */
function resolveRepoRoot() {
    // In dev, this file is at electron/dist/main.js; the repo root
    // is three parents up.
    return path.resolve(__dirname, '..', '..', '..');
}
async function createWindow() {
    const repoRoot = resolveRepoRoot();
    // In production, progress.json + solutions/ live in the user's
    // app data dir (writable on Windows, where Program Files is not).
    // In dev, they live in the repo root.
    const codenHome = electron_1.app.isPackaged
        ? electron_1.app.getPath('userData')
        : repoRoot;
    console.log(`[coden-electron] repo root: ${repoRoot}`);
    console.log(`[coden-electron] CODEN_HOME: ${codenHome} (packaged=${electron_1.app.isPackaged})`);
    console.log(`[coden-electron] process.resourcesPath: ${process.resourcesPath}`);
    try {
        server = await (0, server_process_1.startServer)(repoRoot, codenHome);
    }
    catch (e) {
        const message = e instanceof Error ? e.message : String(e);
        console.error(`[coden-electron] failed to start server:\n${message}`);
        const webDist = path.join(process.resourcesPath, 'web-dist');
        const serverExe = path.join(process.resourcesPath, 'coden-server', process.platform === 'win32' ? 'coden-server.exe' : 'coden-server');
        const bundledExists = require('fs').existsSync(serverExe);
        const hint = bundledExists
            ? `The bundled server exists at:\n  ${serverExe}\n\n` +
                'Try running it directly from a terminal to see the actual error.'
            : `Bundled server NOT found at:\n  ${serverExe}\n\n` +
                `For dev: cd "${repoRoot}" && python -m venv .venv && .venv/Scripts/pip install -r requirements.txt`;
        void webDist; // keep referenced for diagnostic
        electron_1.dialog.showErrorBox('Failed to start cOde(n) server', `${message}\n\n${hint}`);
        electron_1.app.quit();
        return;
    }
    console.log(`[coden-electron] server up at http://127.0.0.1:${server.port} (source=${server.source})`);
    // Open the project in VSCode. Called by the renderer's
    // "Open in VSCode" button (in the transport bar + the VSCode
    // tab). Routes through ``shell.openPath`` — on Windows, that
    // invokes the OS file-association handler; VSCode (when
    // installed) registers itself for the project's folder, so
    // it opens at the repo root with the .vscode/ launch config
    // active. The renderer should have written
    // solutions/.vscode-active FIRST so the F5 launch config
    // defaults to the right challenge.
    electron_1.ipcMain.handle('open-in-vscode', () => {
        try {
            // ``shell.openPath`` returns a promise that resolves to
            // an error string (empty on success). We don't wait on it
            // here — the handler returns true immediately and logs
            // any error asynchronously.
            void electron_1.shell.openPath(repoRoot).then((errMsg) => {
                if (errMsg) {
                    console.warn(`[coden-electron] shell.openPath: ${errMsg}`);
                }
            }, (err) => {
                console.warn(`[coden-electron] shell.openPath rejected: ${err}`);
            });
            return true;
        }
        catch (e) {
            const message = e instanceof Error ? e.message : String(e);
            console.error(`[coden-electron] openInVSCode failed: ${message}`);
            return false;
        }
    });
    const mainUrl = `http://127.0.0.1:${server.port}/`;
    console.log(`[coden-electron] loading ${mainUrl}`);
    mainWindow = new electron_1.BrowserWindow({
        width: 1280,
        height: 800,
        minWidth: 800,
        minHeight: 600,
        title: 'cOde(n)',
        backgroundColor: '#020617',
        show: false,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
            contextIsolation: true,
            nodeIntegration: false,
        },
    });
    mainWindow.once('ready-to-show', () => {
        mainWindow?.show();
    });
    await mainWindow.loadURL(mainUrl);
    // Open devtools in dev builds (F12 toggles, but the console
    // is useful for the developer too).
    if (process.env.CODEN_DEVTOOLS === '1') {
        mainWindow.webContents.openDevTools({ mode: 'detach' });
    }
    mainWindow.on('closed', () => {
        mainWindow = null;
    });
}
electron_1.app.whenReady().then(() => {
    // Wire the auto-updater event listeners + IPC handlers before
    // createWindow() so the renderer can call 'update:check' as soon
    // as it boots, even before the first auto-check on launch fires.
    (0, updater_1.initAutoUpdater)();
    void createWindow();
    // One auto-check on launch, after the main window is up. In
    // dev (app.isPackaged === false) this is a no-op. The check
    // broadcasts a 'update:status' event to the renderer with the
    // result; no UI prompt unless an update is found + downloaded.
    (0, updater_1.runAutoCheckOnLaunch)();
    electron_1.app.on('activate', () => {
        // macOS: re-create the window when the dock icon is clicked.
        if (electron_1.BrowserWindow.getAllWindows().length === 0) {
            void createWindow();
        }
    });
});
electron_1.app.on('window-all-closed', () => {
    // Quit on all platforms (the macOS convention is to keep the
    // app alive, but the cOde(n) launcher is single-window; quit
    // is the right behavior for a learning app).
    if (server) {
        server.kill();
        server = null;
    }
    electron_1.app.quit();
});
electron_1.app.on('before-quit', () => {
    if (server) {
        server.kill();
        server = null;
    }
});
