// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },

  css: [
    '@/assets/css/main.css'
  ],

  runtimeConfig: {
    public: {
      apiBase: 'http://localhost:5090'
    }
  }
})