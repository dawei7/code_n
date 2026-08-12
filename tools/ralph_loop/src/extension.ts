import * as vscode from 'vscode';
import { RalphEngine, LoopState } from './ralphEngine';
import { RalphSidebarProvider } from './sidebarProvider';
import { RalphStatusBar } from './statusBar';
import { FileDetector } from './fileDetector';

export function activate(context: vscode.ExtensionContext) {
    const outputChannel = vscode.window.createOutputChannel('Ralph Loop');
    const statusBar = new RalphStatusBar();
    const fileDetector = new FileDetector();

    const getStoredConfig = () => {
        const config = vscode.workspace.getConfiguration('ralphLoop');
        return {
            maxIterations: context.workspaceState.get<number>('maxIterations', config.get<number>('maxIterations', 200)),
            mode: context.workspaceState.get<string>('mode', config.get<string>('defaultMode', 'Planning')),
            model: context.workspaceState.get<string>('model', config.get<string>('defaultModel', 'Claude Opus 4.6 (Thinking)')),
            taskFile: context.workspaceState.get<string>('taskFile', config.get<string>('taskFile', 'docs/tasks/PRD.md')),
            progressFile: context.workspaceState.get<string>('progressFile', config.get<string>('progressFile', 'docs/tasks/progress.txt')),
            promptFile: context.workspaceState.get<string>('promptFile', config.get<string>('promptFile', ''))
        };
    };

    let activeConfig = getStoredConfig();

    const engine = new RalphEngine(outputChannel, (state: LoopState, currentIter: number, maxIter: number, elapsedSec: number) => {
        statusBar.updateState(state, currentIter, maxIter, elapsedSec);
        if (sidebarProvider) {
            sidebarProvider.updateState({ state, currentIter, maxIter, elapsedSec });
        }
    });

    const sidebarProvider = new RalphSidebarProvider(context.extensionUri, async (command: string, data?: any) => {
        switch (command) {
            case 'start':
                await engine.start(activeConfig);
                break;
            case 'stop':
                engine.stop();
                break;
            case 'pause':
                engine.pause();
                break;
            case 'emergencyStop':
                engine.emergencyStop();
                break;
            case 'updateConfig':
                if (data) {
                    activeConfig = { ...activeConfig, ...data };
                    for (const key of Object.keys(data)) {
                        await context.workspaceState.update(key, data[key]);
                    }
                }
                break;
        }
    });

    context.subscriptions.push(
        vscode.window.registerWebviewViewProvider(RalphSidebarProvider.viewType, sidebarProvider)
    );

    context.subscriptions.push(
        vscode.commands.registerCommand('ralph.start', async () => {
            await engine.start(activeConfig);
        }),
        vscode.commands.registerCommand('ralph.stop', () => {
            engine.stop();
        }),
        vscode.commands.registerCommand('ralph.pause', () => {
            engine.pause();
        }),
        vscode.commands.registerCommand('ralph.emergencyStop', () => {
            engine.emergencyStop();
        }),
        statusBar
    );

    outputChannel.appendLine('Ralph Loop Extension Activated successfully.');
}

export function deactivate() {}
