var carousels = document.getElementsByClassName('carousel');
for (let i = 0; i < carousels.length; i++) {
  createSliderStore(i);
}

function createSliderStore(carouselId) {
  var i = 0;

  var carousel = document.getElementsByClassName('carousel')[carouselId];
  var slides = carousel.getElementsByClassName('slide');
  var n = slides.length;

  var leftBtn = carousel.getElementsByClassName('leftButton')[0];
  var rightBtn = carousel.getElementsByClassName('rightButton')[0];
  
  leftBtn.addEventListener('click', showPrev);
  rightBtn.addEventListener('click', showNext);

  function manageClasses() {
    for (let j = 0; j < n; j++) {
      if(j !== i) {
        slides[j].classList.remove('active');
      } else {
        slides[j].classList.add('active');
      }
    }
  }

  function showPrev(){
    if(--i < 0) i = n - 1;
    manageClasses();
  }

  function showNext(){
    if(++i >= n) i = 0;
    manageClasses();
  }

  manageClasses();
}