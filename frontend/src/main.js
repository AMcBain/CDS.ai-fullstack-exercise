import { createApp } from 'vue'
import { createI18n } from 'vue-i18n'
import enUS from './locales/en-US.json'
import App from './App.vue'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.css'

const i18n = createI18n({
    legacy: false,
    locale: 'en-US',
    messages: {
        'en-US': enUS,
    }
})

createApp(App).use(i18n).mount('#app')
