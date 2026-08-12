import * as vscode from 'vscode';

export class AutoReconnectHandler {
    private maxRetries: number = 5;
    private backoffDelaysMs: number[] = [15000, 30000, 60000, 120000, 120000];

    public isConnectionError(error: any): boolean {
        if (!error) return false;
        const msg = (typeof error === 'string' ? error : error.message || '').toLowerCase();
        return (
            msg.includes('econnrefused') ||
            msg.includes('http/2 session destroyed') ||
            msg.includes('socket hang up') ||
            msg.includes('network error') ||
            msg.includes('connection reset') ||
            msg.includes('timeout')
        );
    }

    public async retryWithBackoff<T>(
        action: () => Promise<T>,
        outputChannel: vscode.OutputChannel,
        onRetryAttempt?: (retryCount: number, delayMs: number) => void
    ): Promise<T> {
        let attempt = 0;
        while (true) {
            try {
                return await action();
            } catch (err: any) {
                if (!this.isConnectionError(err) || attempt >= this.maxRetries) {
                    throw err;
                }
                const delay = this.backoffDelaysMs[attempt] || 120000;
                attempt++;
                outputChannel.appendLine(`\n═══ 断点续跑 ═══ Network issue detected: ${err.message || err}. Retry attempt ${attempt}/${this.maxRetries} in ${delay / 1000}s...`);
                
                if (onRetryAttempt) {
                    onRetryAttempt(attempt, delay);
                }

                await new Promise((resolve) => setTimeout(resolve, delay));
            }
        }
    }
}
