import { reactive } from 'vue';

export const store = reactive({
    showNav: false,
    toggleNav() {
        this.showNav = !this.showNav;
    }
})
