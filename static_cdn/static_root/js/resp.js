burger = document.querySelector('.burger')
navList = document.querySelector('.nav_list')

burger.addEventListener('click', () => {
  navList.classList.toggle('.nav_list');
})