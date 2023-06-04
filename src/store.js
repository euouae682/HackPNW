import { reactive } from 'vue';

export const store = reactive({
    showNav: false,
    toggleNav() {
        this.showNav = !this.showNav;
    },
    tradExpand: true,
    toggleTrad() {
        this.tradExpand = true;
        this.womenExpand = false;
        this.warmingExpand = false;
    },
    womenExpand: false,
    toggleWomen() {
        this.tradExpand = false;
        this.womenExpand = true;
        this.warmingExpand = false;
    },
    warmingExpand: false,
    toggleWarming() {
        this.tradExpand = false;
        this.womenExpand = false;
        this.warmingExpand = true;
    }
})
