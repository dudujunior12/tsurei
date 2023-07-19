const sectionHero = document.querySelector('.section-hero');

const observer = new IntersectionObserver(
    function(entries){
        const ent = entries[0];
        if(ent.isIntersecting === false){
            document.querySelector('.header').classList.add('sticky')
        }
        if(ent.isIntersecting === true){
            document.querySelector('.header').classList.remove('sticky')
        }
    }, 
    {
        root: null,
        threshold: 0,
        rootMargin: "-80px",
    }
);
observer.observe(sectionHero);