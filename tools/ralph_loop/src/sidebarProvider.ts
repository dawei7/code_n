import * as vscode from 'vscode';

export class RalphSidebarProvider implements vscode.WebviewViewProvider {
    public static readonly viewType = 'ralph-loop-sidebar';
    private _view?: vscode.WebviewView;

    constructor(
        private readonly _extensionUri: vscode.Uri,
        private readonly _onCommand: (command: string, data?: any) => void
    ) {}

    public resolveWebviewView(
        webviewView: vscode.WebviewView,
        context: vscode.WebviewViewResolveContext,
        _token: vscode.CancellationToken
    ) {
        this._view = webviewView;

        webviewView.webview.options = {
            enableScripts: true,
            localResourceRoots: [this._extensionUri]
        };

        webviewView.webview.html = this._getHtmlForWebview(webviewView.webview);

        webviewView.webview.onDidReceiveMessage((data) => {
            switch (data.type) {
                case 'start':
                    this._onCommand('start');
                    break;
                case 'stop':
                    this._onCommand('stop');
                    break;
                case 'pause':
                    this._onCommand('pause');
                    break;
                case 'emergencyStop':
                    this._onCommand('emergencyStop');
                    break;
                case 'updateConfig':
                    this._onCommand('updateConfig', data.config);
                    break;
            }
        });
    }

    public updateState(state: any) {
        if (this._view) {
            this._view.webview.postMessage({ type: 'updateState', state });
        }
    }

    private _getHtmlForWebview(webview: vscode.Webview) {
        return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ralph Loop Control Panel</title>
    <style>
        body { font-family: var(--vscode-font-family); padding: 12px; color: var(--vscode-foreground); }
        .section { margin-bottom: 16px; border: 1px solid var(--vscode-widget-border); padding: 10px; border-radius: 4px; }
        .title { font-weight: bold; margin-bottom: 8px; font-size: 1.1em; color: var(--vscode-textLink-foreground); }
        .status-badge { display: inline-block; padding: 3px 8px; border-radius: 3px; font-weight: bold; background: var(--vscode-badge-background); color: var(--vscode-badge-foreground); }
        .btn-group { display: flex; gap: 8px; margin-top: 10px; }
        button { flex: 1; padding: 6px 10px; border: none; border-radius: 3px; background: var(--vscode-button-background); color: var(--vscode-button-foreground); cursor: pointer; }
        button:hover { background: var(--vscode-button-hoverBackground); }
        button.danger { background: var(--vscode-errorForeground); }
        .field { margin-bottom: 8px; font-size: 0.9em; }
        label { display: block; opacity: 0.8; margin-bottom: 2px; }
        input, select { width: 100%; padding: 4px; background: var(--vscode-input-background); color: var(--vscode-input-foreground); border: 1px solid var(--vscode-input-border); }
    </style>
</head>
<body>
    <div class="section">
        <div class="title">Session Status</div>
        <div class="field">State: <span id="status" class="status-badge">Stopped</span></div>
        <div class="field">Iteration: <span id="iteration">0 / 200</span></div>
        <div class="field">Elapsed Time: <span id="elapsed">0m 0s</span></div>
        <div class="btn-group">
            <button id="btnStart" onclick="vscode.postMessage({type: 'start'})">▶ Start</button>
            <button id="btnPause" onclick="vscode.postMessage({type: 'pause'})">⏸ Pause</button>
            <button id="btnStop" onclick="vscode.postMessage({type: 'stop'})">⏹ Stop</button>
        </div>
        <div style="margin-top: 6px;">
            <button class="danger" style="width: 100%;" onclick="vscode.postMessage({type: 'emergencyStop'})">⚠ Emergency Stop</button>
        </div>
    </div>

    <div class="section">
        <div class="title">Configuration</div>
        <div class="field">
            <label>Mode</label>
            <select id="mode" onchange="updateConfig()">
                <option value="Planning">Planning Mode</option>
                <option value="Fast">Fast Mode</option>
            </select>
        </div>
        <div class="field">
            <label>AI Model</label>
            <select id="model" onchange="updateConfig()">
                <option value="Claude Opus 4.6 (Thinking)">Claude Opus 4.6 (Thinking)</option>
                <option value="Claude Sonnet 4.6 (Thinking)">Claude Sonnet 4.6 (Thinking)</option>
                <option value="Gemini 3.1 Pro (High)">Gemini 3.1 Pro (High)</option>
                <option value="GPT-OSS 120B">GPT-OSS 120B</option>
            </select>
        </div>
        <div class="field">
            <label>Max Iterations</label>
            <input type="number" id="maxIter" value="200" onchange="updateConfig()">
        </div>
        <div class="field">
            <label>Task File (PRD.md)</label>
            <input type="text" id="taskFile" value="docs/tasks/PRD.md" onchange="updateConfig()">
        </div>
        <div class="field">
            <label>Progress File (progress.txt)</label>
            <input type="text" id="progressFile" value="docs/tasks/progress.txt" onchange="updateConfig()">
        </div>
    </div>

    <script>
        const vscode = acquireVsCodeApi();
        window.addEventListener('message', event => {
            const message = event.data;
            if (message.type === 'updateState') {
                const s = message.state;
                document.getElementById('status').innerText = s.state;
                document.getElementById('iteration').innerText = s.currentIter + ' / ' + s.maxIter;
                document.getElementById('elapsed').innerText = Math.floor(s.elapsedSec / 60) + 'm ' + (s.elapsedSec % 60) + 's';
            }
        });
        function updateConfig() {
            vscode.postMessage({
                type: 'updateConfig',
                config: {
                    mode: document.getElementById('mode').value,
                    model: document.getElementById('model').value,
                    maxIterations: parseInt(document.getElementById('maxIter').value),
                    taskFile: document.getElementById('taskFile').value,
                    progressFile: document.getElementById('progressFile').value
                }
            });
        }
    </script>
</body>
</html>`;
    }
}
