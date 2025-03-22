import PrimeVue from 'primevue/config';
import Aura from '@primeuix/themes/aura';
import { createApp } from 'vue';
import App from './App.vue';
import Button from "primevue/button";

const app = createApp(App);
app.use(PrimeVue, {
    theme: {
        preset: Aura
    }
});
app.component('Button', Button);
app.mount('#app');