const login = document.querySelector('.login');
const checkin = document.querySelector('.checkin');
const wrapper = document.querySelector('.body__wrapper');
function loginOpen() {
  login.style.display = 'block';
  wrapper.style.opacity = '0.1';
}
function checkinOpen() {
    checkin.style.display = 'block';
    wrapper.style.opacity = '0.1';
}
function closeCheck() {
  checkin.style.display = 'none';
  wrapper.style.opacity = '1';
}
function closeLogin() {
  login.style.display = 'none';
  wrapper.style.opacity = '1';
}
