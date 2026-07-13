import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, '.', '');
  const apiPort = env.CODEN_DEV_API_PORT || '8000';
  return {
    plugins: [react()],
    server: {
      port: 5173,
      // The fast desktop launcher supplies a free API port. A standalone
      // browser workflow keeps using the conventional localhost:8000 target.
      proxy: {
        '/api': {
          target: `http://127.0.0.1:${apiPort}`,
          changeOrigin: false,
          ws: true,
        },
      },
    },
    build: {
      outDir: 'dist',
      sourcemap: true,
    },
  };
});
