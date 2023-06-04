import { reactive } from "vue";

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
  searchQuery: "",
  setSearchQuery(query) {
    searchQuery = query;
  },
  thumbnails: [
    {
      imgUrl: "education/tn1.png",
      title: "Indigenous Women Keep Going Missing in Montana",
      description:
        "Indigenous women in Montana continue to go missing at an alarming rate, exposing a deeply troubling issue of vulnerability and lack of protection. ",
    },
    {
      imgUrl: "education/tn2.png",
      title:
        "Indigenous groups fight climate change by getting their 'land back’",
      description:
        "By regaining control over their traditional territories, Indigenous groups are able to implement sustainable land management practices and preserve their cultural heritage while combating the impacts of climate change.",
    },
    {
      imgUrl: "education/tn3.png",
      title: "Climate change forces First Nations people to move village",
      description:
        "The effects of climate change are compelling First Nations people to relocate their villages, disrupting centuries-old traditions and livelihoods.",
    },
  ],
  posts: [
    {
      title: "Intertwined with the Land",
      article:
        "Native American communities have long-standing relationships with their ancestral lands, viewing them not merely as resources but as living entities. Climate change disrupts this intricate balance, altering ecosystems, diminishing biodiversity, and threatening cultural practices tied to the land...",
      topic: "Native living",
      date: "May 14th",
      time: "15min",
      imgUrl: "blog/blog1.png",
    },
    {
      title: "Disproportionate Impacts and Environmental Injustice",
      article:
        "Native American communities often face socio-economic disparities and limited access to resources, which exacerbate the impacts of climate change. Many communities reside in geographically vulnerable areas...",
      topic: "Climate change",
      date: "May 5th",
      time: "15min",
      imgUrl: "blog/blog2.png",
    },
    {
      title: "Cultural Heritage at Risk",
      article:
        "Climate change also poses risks to Native American cultural heritage. Sacred sites, traditional ceremonies, and medicinal plant knowledge face significant challenges due to the loss of ecosystems, erosion of cultural landscapes...",
      topic: "Adaptation",
      date: "May 1st",
      time: "10min",
      imgUrl: "blog/blog3.png",
    },
    {
      title: "Native Lead Solutions",
      article:
        "Native American communities are actively engaging in climate change mitigation and adaptation efforts. They are at the forefront of renewable energy initiatives, promoting clean energy projects that respect cultural values and create economic opportunities. Indigenous leaders and organizations..",
      topic: "Leadership and advocacy",
      date: "May 14th",
      time: "15min",
      imgUrl: "blog/blog4.png",
    },
    {
      title: "Traditional Knowledge as a Resilience Tool",
      article:
        "Native American communities possess a wealth of traditional ecological knowledge that has been passed down through generations. This knowledge offers invaluable insights into the interconnectedness of ecosystems, sustainable resource management, and adaptation strategies...",
      topic: "Climate change",
      date: "May 5th",
      time: "15min",
      imgUrl: "blog/blog2.png",
    },
    {
      title: "Cultural Heritage at Risk",
      article:
        "Climate change also poses risks to Native American cultural heritage. Sacred sites, traditional ceremonies, and medicinal plant knowledge face significant challenges due to the loss of ecosystems, erosion of cultural landscapes...",
      topic: "Native living",
      date: "May 14th",
      time: "15min",
      imgUrl: "blog/blog1.png",
    },
  ],
  filteredPosts: [],
  filterPosts(searchTopic) {
    if (searchTopic == "") {
      this.filteredPosts = this.posts;
    } else {
      this.filteredPosts = [];
      this.posts.forEach((post) => {
        if (post.topic == searchTopic) {
          this.filteredPosts.push(post);
        }
      });
    }
  },
});
