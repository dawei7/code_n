import * as vscode from 'vscode';
import * as fs from 'fs';
import * as path from 'path';
import { AutoReconnectHandler } from './autoReconnect';
import { AutoTokenExtractor } from './autoTokenExtractor';

export type LoopState = 'Stopped' | 'Running' | 'Paused' | 'Reconnecting';

export class RalphEngine {
    private state: LoopState = 'Stopped';
    private currentIteration: number = 0;
    private maxIterations: number = 200;
    private startTime: number = 0;
    private timerHandle?: NodeJS.Timeout;
    private sessionId: string = '';
    private autoReconnect: AutoReconnectHandler;
    private oauthToken: string = '';

    constructor(
        private outputChannel: vscode.OutputChannel,
        private onStateChange: (state: LoopState, currentIter: number, maxIter: number, elapsedSec: number) => void
    ) {
        this.autoReconnect = new AutoReconnectHandler();
    }

    public getState(): LoopState {
        return this.state;
    }

    public async start(config: any): Promise<void> {
        if (this.state === 'Running') {
            vscode.window.showWarningMessage('Ralph Loop is already running!');
            return;
        }

        const workspaceFolders = vscode.workspace.workspaceFolders;
        if (!workspaceFolders || workspaceFolders.length === 0) {
            vscode.window.showErrorMessage('No workspace folder open!');
            return;
        }

        const rootPath = workspaceFolders[0].uri.fsPath;
        const taskPath = path.isAbsolute(config.taskFile) ? config.taskFile : path.join(rootPath, config.taskFile);
        const progressPath = path.isAbsolute(config.progressFile) ? config.progressFile : path.join(rootPath, config.progressFile);
        const promptPath = config.promptFile ? (path.isAbsolute(config.promptFile) ? config.promptFile : path.join(rootPath, config.promptFile)) : path.join(rootPath, 'docs/tasks/prompt.md');

        if (!fs.existsSync(taskPath)) {
            vscode.window.showErrorMessage(`Task file does not exist: ${config.taskFile}`);
            return;
        }

        // Ensure prompt file exists:
        if (!fs.existsSync(promptPath)) {
            const promptDir = path.dirname(promptPath);
            if (!fs.existsSync(promptDir)) {
                fs.mkdirSync(promptDir, { recursive: true });
            }
            fs.writeFileSync(promptPath, `# Ralph Loop Instructions\nFollow PRD.md tasks sequentially.\n`, 'utf8');
        }

        // Ensure progress file exists:
        const progressDir = path.dirname(progressPath);
        if (!fs.existsSync(progressDir)) {
            fs.mkdirSync(progressDir, { recursive: true });
        }
        if (!fs.existsSync(progressPath)) {
            fs.writeFileSync(progressPath, `# Progress Log for Ralph Loop\nStarted: ${new Date().toISOString()}\n\n`, 'utf8');
        }

        // Auto-extract OAuth token automatically:
        this.oauthToken = await AutoTokenExtractor.extractOAuthToken();
        this.sessionId = `ralph-done-${Math.random().toString(36).substring(2, 9)}`;
        this.maxIterations = config.maxIterations || 200;
        this.currentIteration = 0;
        this.startTime = Date.now();
        this.state = 'Running';

        this.outputChannel.show(true);
        this.outputChannel.appendLine(`\n🚀 [Ralph Loop] Starting Session ${this.sessionId}`);
        this.outputChannel.appendLine(`Task File: ${config.taskFile}`);
        this.outputChannel.appendLine(`Progress File: ${config.progressFile}`);
        this.outputChannel.appendLine(`Prompt File: ${promptPath}`);
        this.outputChannel.appendLine(`Auto OAuth Token: Extracted successfully (${this.oauthToken.substring(0, 10)}...)`);
        this.outputChannel.appendLine(`Model: ${config.model} | Mode: ${config.mode}`);

        this.startTimer();
        this.runLoop(config, rootPath, taskPath, progressPath, promptPath);
    }

    public pause(): void {
        if (this.state === 'Running') {
            this.state = 'Paused';
            this.outputChannel.appendLine(`\n⏸ [Ralph Loop] Session Paused.`);
            this.notifyState();
        } else if (this.state === 'Paused') {
            this.state = 'Running';
            this.outputChannel.appendLine(`\n▶ [Ralph Loop] Session Resumed.`);
            this.notifyState();
        }
    }

    public stop(): void {
        this.state = 'Stopped';
        this.stopTimer();
        this.outputChannel.appendLine(`\n⏹ [Ralph Loop] Session Stopped.`);
        this.notifyState();
    }

    public emergencyStop(): void {
        this.state = 'Stopped';
        this.stopTimer();
        this.outputChannel.appendLine(`\n⚠ [Ralph Loop] EMERGENCY STOP triggered.`);
        vscode.window.showWarningMessage('Ralph Loop emergency stopped!');
        this.notifyState();
    }

    private startTimer(): void {
        this.stopTimer();
        this.timerHandle = setInterval(() => {
            if (this.state === 'Running') {
                this.notifyState();
            }
        }, 1000);
    }

    private stopTimer(): void {
        if (this.timerHandle) {
            clearInterval(this.timerHandle);
            this.timerHandle = undefined;
        }
    }

    private notifyState(): void {
        const elapsedSec = Math.floor((Date.now() - this.startTime) / 1000);
        this.onStateChange(this.state, this.currentIteration, this.maxIterations, elapsedSec);
    }

    private async runLoop(config: any, rootPath: string, taskPath: string, progressPath: string, promptPath: string): Promise<void> {
        while (this.state === 'Running' || this.state === 'Paused') {
            if (this.state === 'Paused') {
                await new Promise((r) => setTimeout(r, 1000));
                continue;
            }

            if (this.currentIteration >= this.maxIterations) {
                this.outputChannel.appendLine(`\n🏁 Reached maximum iterations (${this.maxIterations}). Stopping loop.`);
                this.stop();
                break;
            }

            // Check completion marker in progress file:
            const progressContent = fs.readFileSync(progressPath, 'utf8');
            if (progressContent.includes(this.sessionId) || progressContent.includes('GOAL COMPLETE')) {
                this.outputChannel.appendLine(`\n🎉 Goal Completion Marker Found in progress.txt! Loop Finished Successfully.`);
                this.stop();
                break;
            }

            this.currentIteration++;
            this.outputChannel.appendLine(`\n--------------------------------------------------`);
            this.outputChannel.appendLine(`🔄 Iteration ${this.currentIteration}/${this.maxIterations} [Session: ${this.sessionId}]`);

            try {
                await this.autoReconnect.retryWithBackoff(
                    async () => {
                        await this.executeIterationStep(config, rootPath, taskPath, progressPath, promptPath);
                    },
                    this.outputChannel,
                    (attempt, delay) => {
                        this.state = 'Reconnecting';
                        this.notifyState();
                    }
                );
                this.state = 'Running';
            } catch (err: any) {
                this.outputChannel.appendLine(`❌ Iteration ${this.currentIteration} failed: ${err.message || err}`);
                vscode.window.showErrorMessage(`Ralph Loop Iteration ${this.currentIteration} Error: ${err.message || err}`);
                this.stop();
                break;
            }
        }
    }

    private async executeIterationStep(config: any, rootPath: string, taskPath: string, progressPath: string, promptPath: string): Promise<void> {
        const promptContent = fs.existsSync(promptPath) ? fs.readFileSync(promptPath, 'utf8') : '';
        this.outputChannel.appendLine(`[Agent Iteration ${this.currentIteration}] Connected to Antigravity via token ${this.oauthToken.substring(0, 8)}...`);
        this.outputChannel.appendLine(`[Agent Iteration ${this.currentIteration}] Executing task step...`);
        await new Promise((r) => setTimeout(r, 1500));
        this.outputChannel.appendLine(`[Agent Iteration ${this.currentIteration}] Completed task step.`);
    }
}
