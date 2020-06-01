import Vue from 'vue'
import vueCustomElement from 'vue-custom-element';

// import UglyFilm from './UglyFilm.vue';
import UglyFilm from './components/UglyFilm.vue';

// Configure Vue to ignore the element name when defined outside of Vue.
Vue.config.ignoredElements = [
    'ugly-film'
];

// Enable the plugin
Vue.use(vueCustomElement);

// Register your component
Vue.customElement('ugly-film', UglyFilm, {
    // shadow: true
    // Additional Options: https://github.com/karol-f/vue-custom-element#options
});