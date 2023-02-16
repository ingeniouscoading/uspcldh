// owl-carousel customisations
var owl = $('.owl-carousel');
owl.owlCarousel({
    items: 4,
    loop: true,
    margin: 10,
    autoplay: true,
    autoplayTimeout: 1000,
    autoplayHoverPause: true
});
$('.play').on('click', function () {
    owl.trigger('play.owl.autoplay', [1000])
})
$('.stop').on('click', function () {
    owl.trigger('stop.owl.autoplay')
})

// navbar behavior on scroll

window.onscroll = function () { myFunction() };

function myFunction() {
    if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
        document.getElementById("myNavbar").classList.add("fixed-top");
    } else {
        document.getElementById("myNavbar").classList.remove("fixed-top");
    }
}


// sweet alert //

// Swal.fire({
//     imageUrl: 'https://unsplash.it/400/200',
//     imageAlt: 'Custom image',
// })

