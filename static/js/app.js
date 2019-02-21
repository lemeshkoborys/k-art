function scrollToItem(tab, item) {
  var i;
  var x = document.getElementsByClassName("items");
  for (i = 0; i < x.length; i++) {
      x[i].style.display = "none"; 
  }
  console.log(tab, item);
  document.getElementById(tab).style.display = "block";
  
  var rect = document.getElementById(item).getBoundingClientRect();
  var w = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
  var offset;
  if(w < 768) {
    offset = rect.top - 50;
  } else {
    offset = rect.top - 99;
  }
  window.scrollBy({
    top: offset,
    behavior: "smooth"
  });
}

function toggleMenu() {
  var x = document.getElementsByClassName("menu-sm-body")[0];
  if ( x.classList.contains('expandable-sm') ) {
    x.classList.remove("expandable-sm");
    x.classList.add("expandable-sm-active");
  } else {
    x.classList.remove("expandable-sm-active");
    x.classList.add("expandable-sm");
  }
  document.getElementsByClassName("menu-sm-arrow")[0].classList.toggle('rotated');
}

function expandChild(childN) {
  var x = document.getElementsByClassName("menu-sm-item-text");
  for (i = 0; i < x.length; i++) {
    if(i == childN) {
      if (x[i].classList.contains('expandable-sm')) {
        x[i].classList.remove("expandable-sm");
        x[i].classList.add("expandable-sm-active");
      } else {
        x[i].classList.remove("expandable-sm-active");
        x[i].classList.add("expandable-sm");
      }
    } else {
      x[i].classList.remove("expandable-sm-active");
      x[i].classList.add("expandable-sm");
    }
  }
}
function openScrollToItem(tab, item) {
  localStorage.setItem('redirected', true);
  localStorage.setItem('tab', tab);
  localStorage.setItem('item', item);
  location.href='/';
}