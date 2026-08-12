import * as cp from 'child_process';
import * as vscode from 'vscode';
import * as fs from 'fs';
import * as path from 'path';

export class AutoTokenExtractor {
    public static async extractOAuthToken(): Promise<string> {
        // 1. Check workspace settings first:
        const configToken = vscode.workspace.getConfiguration('ralphLoop').get<string>('antigravity.oauthToken');
        if (configToken && configToken.trim().length > 0) {
            return configToken.trim();
        }

        // 2. Extract from running process command line on Windows:
        try {
            const cmdOutput = cp.execSync(
                'wmic process where "name like \'%antigravity%\' or name like \'%language_server%\' or name like \'%node%\'" get commandline',
                { encoding: 'utf8', timeout: 5000 }
            );

            const tokenMatch = cmdOutput.match(/--(?:oauth_token|auth_token|token|authorization)=([^\s"']+)/i) ||
                               cmdOutput.match(/--(?:csrf_token)=([^\s"']+)/i);

            if (tokenMatch && tokenMatch[1]) {
                return tokenMatch[1];
            }
        } catch (e) {
            // wmic error ignore
        }

        // 3. Check environment variables:
        if (process.env.ANTIGRAVITY_OAUTH_TOKEN) {
            return process.env.ANTIGRAVITY_OAUTH_TOKEN;
        }
        if (process.env.GEMINI_AUTH_TOKEN) {
            return process.env.GEMINI_AUTH_TOKEN;
        }

        // 4. Auto-generate local fallback token for Antigravity REST bridge:
        const fallbackToken = `ralph-auto-auth-${Math.random().toString(36).substring(2, 12)}`;
        return fallbackToken;
    }
}
