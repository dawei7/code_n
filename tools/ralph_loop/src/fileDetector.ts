import * as vscode from 'vscode';
import * as path from 'path';

export class FileDetector {
    private taskFilePatterns: string[] = [
        'PRD.md', 'TASKS.md', 'TODO.md', 'SPEC.md', 'REQUIREMENTS.md',
        'BACKLOG.md', 'ROADMAP.md', 'PLAN.md', 'ISSUES.md',
        'prd.md', 'tasks.md', 'todo.md', 'spec.md',
        'PRD.txt', 'TASKS.txt', 'TODO.txt', 'SPEC.txt'
    ];

    private promptFilePatterns: string[] = [
        'PROMPT.md', 'INSTRUCTIONS.md', 'SYSTEM_PROMPT.md', 'AGENT_PROMPT.md', 'CONTEXT.md',
        'prompt.md', 'instructions.md', 'system_prompt.md',
        'PROMPT.txt', 'INSTRUCTIONS.txt'
    ];

    public async detectTaskFiles(): Promise<string[]> {
        return this.findMatchingWorkspaceFiles(this.taskFilePatterns);
    }

    public async detectPromptFiles(): Promise<string[]> {
        return this.findMatchingWorkspaceFiles(this.promptFilePatterns);
    }

    private async findMatchingWorkspaceFiles(patterns: string[]): Promise<string[]> {
        const workspaceFolders = vscode.workspace.workspaceFolders;
        if (!workspaceFolders || workspaceFolders.length === 0) {
            return [];
        }

        const results: Set<string> = new Set();
        for (const pattern of patterns) {
            const files = await vscode.workspace.findFiles(`**/${pattern}`, '**/node_modules/**', 20);
            for (const file of files) {
                results.add(vscode.workspace.asRelativePath(file));
            }
        }

        return Array.from(results);
    }

    public async selectTaskFileWithQuickPick(currentPath: string): Promise<string | undefined> {
        const detected = await this.detectTaskFiles();
        const items: vscode.QuickPickItem[] = detected.map(file => ({
            label: file,
            description: '$(file) Auto-detected task file'
        }));

        items.push({
            label: '$(edit) Enter custom relative path...',
            description: 'Provide relative filepath manually'
        });

        const picked = await vscode.window.showQuickPick(items, {
            placeHolder: 'Select Task Specification File (PRD.md)'
        });

        if (!picked) return undefined;

        if (picked.label.includes('custom relative path')) {
            return await vscode.window.showInputBox({
                value: currentPath || 'docs/tasks/PRD.md',
                prompt: 'Enter relative path to task file'
            });
        }

        return picked.label;
    }
}
