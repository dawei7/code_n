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
      chunkSizeWarningLimit: 1200,
      rollupOptions: {
        output: {
          manualChunks(id) {
            if (id.includes('node_modules/monaco-editor') || id.includes('node_modules/@monaco-editor')) {
              return 'vendor-monaco';
            }
            if (id.includes('node_modules/mermaid') || id.includes('node_modules/cytoscape') || id.includes('node_modules/dagre-d3-es')) {
              return 'vendor-diagrams';
            }
            if (
              id.includes('node_modules/katex') ||
              id.includes('node_modules/rehype-katex') ||
              id.includes('node_modules/remark-math') ||
              id.includes('node_modules/react-markdown') ||
              id.includes('node_modules/rehype-raw') ||
              id.includes('node_modules/remark-gfm')
            ) {
              return 'vendor-content';
            }
            if (id.includes('node_modules/@fortawesome') || id.includes('node_modules/lucide-react')) {
              return 'vendor-icons';
            }
            if (id.includes('node_modules/react') || id.includes('node_modules/react-dom') || id.includes('node_modules/zustand')) {
              return 'vendor-core';
            }
          },
        },
      },
    },
  };
});
