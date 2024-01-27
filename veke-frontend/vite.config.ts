import { defineConfig } from 'vite'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [],
  build: {
    outDir: '../public/assets',
    rollupOptions: {
      input: {
        'script': 'src/main.ts',
        'styles': 'src/style.scss',
      },
      output: {
        assetFileNames: "[name].[ext]"
      }
    },
  },
})
