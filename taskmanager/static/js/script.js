
document.addEventListener('DOMContentLoaded', function() {
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
  });

  // Or with jQuery

  $(document).ready(function(){
    $('.sidenav').sidenav();
  });