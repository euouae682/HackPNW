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
    searchQuery: '',
    setSearchQuery(query) {
        searchQuery = query;
    },
    posts: [
        {title: 'Intertwined with the Land', 
        article: 'Native American communities have long-standing relationships with their ancestral lands, viewing them not merely as resources but as living entities. Climate change disrupts this intricate balance, altering ecosystems, diminishing biodiversity, and threatening cultural practices tied to the land...', 
        topic: 'Native living', 
        date: 'May 14th', 
        time: '15min', 
        inset: false,
        imgUrl: 'placeholder-hero.jpg'},
        {title: 'Disproportionate Impacts and Environmental Injustice', 
        article: "Native American communities in the United States have long faced socio-economic disparities and limited access to resources. Unfortunately, these challenges are further exacerbated by the impacts of climate change...", 
        fulltxt1: "Native American communities in the United States have long faced socio-economic disparities and limited access to resources. Unfortunately, these challenges are further exacerbated by the impacts of climate change. With many of these communities residing in geographically vulnerable areas, such as coastal regions and fire-prone areas, they are particularly susceptible to the physical and economic consequences of climate-related events. As a result, environmental justice concerns arise as these communities bear a disproportionate burden of the environmental degradation caused by climate change. Historically, Native American communities have experienced systemic socio-economic disparities, including poverty, limited job opportunities, inadequate healthcare, and substandard education. These challenges, rooted in a long history of marginalization and oppression, have contributed to a lack of resources and resilience in the face of climate change. Native American communities are disproportionately affected by climate change due to their geographical locations. Coastal tribes, such as those in Alaska and the Gulf Coast, face rising sea levels, increasing storm intensity, and erosion. These impacts threaten their traditional ways of life, including subsistence hunting and fishing, and can lead to displacement and loss of cultural heritage. Moreover, many Native American communities reside in areas prone to wildfires, such as those in the western United States. As climate change intensifies droughts and heatwaves, the frequency and severity of wildfires increase. These fires pose a significant threat to tribal lands, homes, and sacred sites, undermining the cultural and spiritual fabric of these communities. Environmental degradation resulting from climate change further compounds the challenges faced by Native American communities. Industrial activities, including mining, fossil fuel extraction, and energy development, often occur near or on tribal lands, leading to pollution and habitat destruction. These activities can contaminate water sources, disrupt ecosystems, and threaten the health and well-being of community members. Additionally, inadequate waste management and environmental regulations in some regions exacerbate the environmental burdens faced by Native American communities. Limited access to clean water and sanitation facilities can result in health issues, including higher rates of waterborne diseases.",
        fulltxt2: "The disproportionate impacts of climate change on Native American communities highlight the need for environmental justice. Environmental justice advocates argue that marginalized communities should not bear a disproportionate burden of environmental harm and should have equal access to environmental benefits. Efforts to address environmental injustice include advocacy for stronger environmental regulations, meaningful consultation with tribal communities in decision-making processes, and increased support for sustainable and culturally appropriate solutions. Furthermore, partnerships between tribal governments, non-governmental organizations, and governmental agencies can help amplify the voices of Native American communities and advocate for policy changes that prioritize environmental justice. Native American communities face unique challenges stemming from a history of socio-economic disparities and limited access to resources. Climate change compounds these challenges by disproportionately impacting these communities through the destruction of coastal regions and the increasing frequency of wildfires. Additionally, environmental degradation resulting from industrial activities exacerbates the burdens faced by Native American communities. To address these issues, a comprehensive approach is necessary, one that emphasizes environmental justice, community engagement, and sustainable solutions. By prioritizing the voices and needs of Native American communities, society can work towards a more equitable and sustainable future, where the impacts of climate change are shared more equitably among all communities.",
        topic: 'Climate change', 
        date: 'May 5th', 
        time: '15min', 
        inset: false,
        imgUrl: 'placeholder-hero.jpg'},
        {title: 'Cultural Heritage at Risk', 
        article: 'Climate change also poses risks to Native American cultural heritage. Sacred sites, traditional ceremonies, and medicinal plant knowledge face significant challenges due to the loss of ecosystems, erosion of cultural landscapes...', 
        topic: 'Adaptation', 
        date: 'May 1st', 
        time: '10min', 
        inset: false,
        imgUrl: 'placeholder-hero.jpg'},
        {title: 'Native Lead Solutions', 
        article: 'Native American communities are actively engaging in climate change mitigation and adaptation efforts. They are at the forefront of renewable energy initiatives, promoting clean energy projects that respect cultural values and create economic opportunities. Indigenous leaders and organizations..', 
        topic: 'Leadership and advocacy', 
        date: 'May 14th', 
        time: '15min', 
        inset: false,
        imgUrl: 'placeholder-hero.jpg'},
        {title: 'Traditional Knowledge as a Resilience Tool', 
        article: 'Native American communities possess a wealth of traditional ecological knowledge that has been passed down through generations. This knowledge offers invaluable insights into the interconnectedness of ecosystems, sustainable resource management, and adaptation strategies...', 
        topic: 'Climate change', 
        date: 'May 5th', 
        time: '15min', 
        inset: false,
        imgUrl: 'placeholder-hero.jpg'},
        {title: 'Cultural Heritage at Risk', 
        article: 'Climate change also poses risks to Native American cultural heritage. Sacred sites, traditional ceremonies, and medicinal plant knowledge face significant challenges due to the loss of ecosystems, erosion of cultural landscapes...', 
        topic: 'Native living', 
        date: 'May 14th', 
        time: '15min', 
        inset: false,
        imgUrl: 'placeholder-hero.jpg'},
    ],
    filteredPosts: [],
    filterPosts(searchTopic) {
        if (searchTopic == '') {
            this.filteredPosts = this.posts;
        }
        else {
            this.filteredPosts = []
            this.posts.forEach((post) => {
                if (post.topic == searchTopic) {
                    this.filteredPosts.push(post);
                }
            })
        }
    },
    toggleDetail(post) {
        post.inset = !post.inset;
    }
})
