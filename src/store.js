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
    },
    posts: [
        {title: 'Intertwined with the Land', 
        article: 'Native American communities have long-standing relationships with their ancestral lands, viewing them not merely as resources but as living entities. Climate change disrupts this intricate balance, altering ecosystems, diminishing biodiversity, and threatening cultural practices tied to the land...', 
        topic: 'Native living', 
        date: 'May 14th', 
        time: '15min', 
        imgUrl: ''}],
    filteredPosts: [],
    filterPosts(searchTopic) {
        filteredPosts = []
        this.posts.forEach((post) => {
            if (post.topic == searchTopic) {
                this.filteredPosts.concat(post);
            }
        })
    }
})
