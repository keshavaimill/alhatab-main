// vite.config.ts
import { defineConfig } from "file:///C:/Users/Aditi%20singh/Downloads/al-hatab-insights-main-main(keshav)/al-hatab-insights-main-main/al-hatab-insights-main/node_modules/vite/dist/node/index.js";
import react from "file:///C:/Users/Aditi%20singh/Downloads/al-hatab-insights-main-main(keshav)/al-hatab-insights-main-main/al-hatab-insights-main/node_modules/@vitejs/plugin-react-swc/index.js";
import path from "path";
import { componentTagger } from "file:///C:/Users/Aditi%20singh/Downloads/al-hatab-insights-main-main(keshav)/al-hatab-insights-main-main/al-hatab-insights-main/node_modules/lovable-tagger/dist/index.js";
var __vite_injected_original_dirname = "C:\\Users\\Aditi singh\\Downloads\\al-hatab-insights-main-main(keshav)\\al-hatab-insights-main-main\\al-hatab-insights-main";
var vite_config_default = defineConfig(({ mode }) => ({
  server: {
    host: "::",
    port: 8080,
    proxy: {
      "/api/text2sql": {
        // Proxy to backend URL from environment variable
        // Set VITE_TEXT2SQL_API_URL in .env file (e.g., https://alhatab-main-merged.onrender.com)
        // Defaults to deployed backend if not set
        target: process.env.VITE_TEXT2SQL_API_URL || "https://alhatab-main-merged.onrender.com",
        changeOrigin: true,
        rewrite: (path2) => path2.replace(/^\/api\/text2sql/, "")
      }
    }
  },
  plugins: [react(), mode === "development" && componentTagger()].filter(Boolean),
  resolve: {
    alias: {
      "@": path.resolve(__vite_injected_original_dirname, "./src")
    }
  }
}));
export {
  vite_config_default as default
};
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsidml0ZS5jb25maWcudHMiXSwKICAic291cmNlc0NvbnRlbnQiOiBbImNvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9kaXJuYW1lID0gXCJDOlxcXFxVc2Vyc1xcXFxBZGl0aSBzaW5naFxcXFxEb3dubG9hZHNcXFxcYWwtaGF0YWItaW5zaWdodHMtbWFpbi1tYWluKGtlc2hhdilcXFxcYWwtaGF0YWItaW5zaWdodHMtbWFpbi1tYWluXFxcXGFsLWhhdGFiLWluc2lnaHRzLW1haW5cIjtjb25zdCBfX3ZpdGVfaW5qZWN0ZWRfb3JpZ2luYWxfZmlsZW5hbWUgPSBcIkM6XFxcXFVzZXJzXFxcXEFkaXRpIHNpbmdoXFxcXERvd25sb2Fkc1xcXFxhbC1oYXRhYi1pbnNpZ2h0cy1tYWluLW1haW4oa2VzaGF2KVxcXFxhbC1oYXRhYi1pbnNpZ2h0cy1tYWluLW1haW5cXFxcYWwtaGF0YWItaW5zaWdodHMtbWFpblxcXFx2aXRlLmNvbmZpZy50c1wiO2NvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9pbXBvcnRfbWV0YV91cmwgPSBcImZpbGU6Ly8vQzovVXNlcnMvQWRpdGklMjBzaW5naC9Eb3dubG9hZHMvYWwtaGF0YWItaW5zaWdodHMtbWFpbi1tYWluKGtlc2hhdikvYWwtaGF0YWItaW5zaWdodHMtbWFpbi1tYWluL2FsLWhhdGFiLWluc2lnaHRzLW1haW4vdml0ZS5jb25maWcudHNcIjtpbXBvcnQgeyBkZWZpbmVDb25maWcgfSBmcm9tIFwidml0ZVwiO1xuaW1wb3J0IHJlYWN0IGZyb20gXCJAdml0ZWpzL3BsdWdpbi1yZWFjdC1zd2NcIjtcbmltcG9ydCBwYXRoIGZyb20gXCJwYXRoXCI7XG5pbXBvcnQgeyBjb21wb25lbnRUYWdnZXIgfSBmcm9tIFwibG92YWJsZS10YWdnZXJcIjtcblxuLy8gaHR0cHM6Ly92aXRlanMuZGV2L2NvbmZpZy9cbmV4cG9ydCBkZWZhdWx0IGRlZmluZUNvbmZpZygoeyBtb2RlIH0pID0+ICh7XG4gIHNlcnZlcjoge1xuICAgIGhvc3Q6IFwiOjpcIixcbiAgICBwb3J0OiA4MDgwLFxuICAgIHByb3h5OiB7XG4gICAgICBcIi9hcGkvdGV4dDJzcWxcIjoge1xuICAgICAgICAvLyBQcm94eSB0byBiYWNrZW5kIFVSTCBmcm9tIGVudmlyb25tZW50IHZhcmlhYmxlXG4gICAgICAgIC8vIFNldCBWSVRFX1RFWFQyU1FMX0FQSV9VUkwgaW4gLmVudiBmaWxlIChlLmcuLCBodHRwczovL2FsaGF0YWItbWFpbi1tZXJnZWQub25yZW5kZXIuY29tKVxuICAgICAgICAvLyBEZWZhdWx0cyB0byBkZXBsb3llZCBiYWNrZW5kIGlmIG5vdCBzZXRcbiAgICAgICAgdGFyZ2V0OiBwcm9jZXNzLmVudi5WSVRFX1RFWFQyU1FMX0FQSV9VUkwgfHwgXCJodHRwczovL2FsaGF0YWItbWFpbi1tZXJnZWQub25yZW5kZXIuY29tXCIsXG4gICAgICAgIGNoYW5nZU9yaWdpbjogdHJ1ZSxcbiAgICAgICAgcmV3cml0ZTogKHBhdGgpID0+IHBhdGgucmVwbGFjZSgvXlxcL2FwaVxcL3RleHQyc3FsLywgXCJcIiksXG4gICAgICB9LFxuICAgIH0sXG4gIH0sXG4gIHBsdWdpbnM6IFtyZWFjdCgpLCBtb2RlID09PSBcImRldmVsb3BtZW50XCIgJiYgY29tcG9uZW50VGFnZ2VyKCldLmZpbHRlcihCb29sZWFuKSxcbiAgcmVzb2x2ZToge1xuICAgIGFsaWFzOiB7XG4gICAgICBcIkBcIjogcGF0aC5yZXNvbHZlKF9fZGlybmFtZSwgXCIuL3NyY1wiKSxcbiAgICB9LFxuICB9LFxufSkpO1xuIl0sCiAgIm1hcHBpbmdzIjogIjtBQUFpaUIsU0FBUyxvQkFBb0I7QUFDOWpCLE9BQU8sV0FBVztBQUNsQixPQUFPLFVBQVU7QUFDakIsU0FBUyx1QkFBdUI7QUFIaEMsSUFBTSxtQ0FBbUM7QUFNekMsSUFBTyxzQkFBUSxhQUFhLENBQUMsRUFBRSxLQUFLLE9BQU87QUFBQSxFQUN6QyxRQUFRO0FBQUEsSUFDTixNQUFNO0FBQUEsSUFDTixNQUFNO0FBQUEsSUFDTixPQUFPO0FBQUEsTUFDTCxpQkFBaUI7QUFBQTtBQUFBO0FBQUE7QUFBQSxRQUlmLFFBQVEsUUFBUSxJQUFJLHlCQUF5QjtBQUFBLFFBQzdDLGNBQWM7QUFBQSxRQUNkLFNBQVMsQ0FBQ0EsVUFBU0EsTUFBSyxRQUFRLG9CQUFvQixFQUFFO0FBQUEsTUFDeEQ7QUFBQSxJQUNGO0FBQUEsRUFDRjtBQUFBLEVBQ0EsU0FBUyxDQUFDLE1BQU0sR0FBRyxTQUFTLGlCQUFpQixnQkFBZ0IsQ0FBQyxFQUFFLE9BQU8sT0FBTztBQUFBLEVBQzlFLFNBQVM7QUFBQSxJQUNQLE9BQU87QUFBQSxNQUNMLEtBQUssS0FBSyxRQUFRLGtDQUFXLE9BQU87QUFBQSxJQUN0QztBQUFBLEVBQ0Y7QUFDRixFQUFFOyIsCiAgIm5hbWVzIjogWyJwYXRoIl0KfQo=
