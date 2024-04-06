let el = document.getElementById('main')
let elCoordinates = el.getBoundingClientRect()
console.log(elCoordinates)
document.addEventListener('scroll', function() {
    const header = document.querySelector('header');
    if(window.scrollY > elCoordinates.top){
        console.log("Y :"+window.scrollY)
        console.log("EL :"+elCoordinates.top)
        header.classList.add('scrolled');
    }else{
        header.classList.remove('scrolled');
    }

})






