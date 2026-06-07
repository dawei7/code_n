import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    // Proxy /api/* to the FastAPI server. In dev the user runs
    // `uvicorn server.app.main:app --port 8000` in a separate terminal;
    // the React app uses the same `/api` base path it would use in
    // Electron, so the API client is identical in both environments.
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: false,
      },
    },
  },
  build: {
    outDir: 'dist',
    sourcemap: true,
  },
});
