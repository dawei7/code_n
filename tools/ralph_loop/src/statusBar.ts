import * as vscode from 'vscode';

export class RalphStatusBar {
    private statusBarItem: vscode.StatusBarItem;

    constructor() {
        this.statusBarItem = vscode.window.createStatusBarItem(vscode.StatusBarAlignment.Left, 100);
        this.statusBarItem.command = 'ralph.pause';
        this.updateState('Stopped', 0, 0, 0);
        this.statusBarItem.show();
    }

    public updateState(state: 'Running' | 'Paused' | 'Stopped' | 'Reconnecting', currentIter: number, maxIter: number, elapsedSec: number): void {
        const icon = state === 'Running' ? '$(sync~spin)' : state === 'Paused' ? '$(debug-pause)' : state === 'Reconnecting' ? '$(warning)' : '$(stop)';
        const minutes = Math.floor(elapsedSec / 60);
        const seconds = elapsedSec % 60;
        const timeStr = `${minutes}m ${seconds}s`;

        if (state === 'Stopped') {
            this.statusBarItem.text = `$(play) Ralph Loop: Stopped`;
            this.statusBarItem.tooltip = 'Click to manage Ralph Loop session';
        } else {
            this.statusBarItem.text = `${icon} Ralph: ${state} (${currentIter}/${maxIter}) [${timeStr}]`;
            this.statusBarItem.tooltip = `Ralph Loop ${state} - Iteration ${currentIter} of ${maxIter}. Click to Pause/Resume.`;
        }
    }

    public dispose(): void {
        this.statusBarItem.dispose();
    }
}
