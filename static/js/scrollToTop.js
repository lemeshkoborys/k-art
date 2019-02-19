window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
    document.getElementById("btnToTop").style.display = "block";

    document.getElementsByTagName('body')[0].classList.add("body-gallery");
    // document.getElementsByClassName('story')[0].classList.add('story-gallery');
    document.getElementsByTagName('header')[0].classList.add("header-gallery");
    document.getElementsByTagName('nav')[0].classList.add("nav-gallery");
  } else {
    document.getElementById("btnToTop").style.display = "none";

    document.getElementsByTagName('body')[0].classList.remove("body-gallery");
    // document.getElementsByClassName('story')[0].classList.remove('story-gallery');
    document.getElementsByTagName('header')[0].classList.remove("header-gallery");
    document.getElementsByTagName('nav')[0].classList.remove("nav-gallery");
  }
}

function topFunction() {
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  });
}