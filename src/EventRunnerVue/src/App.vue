<template>
  <div id="app">
  <div class="body__wrapper">
  <header>
    <div class="header-wrapper">
    <div class="logo">
      LOGO
    </div>
    <div class="profile">
      <button type="button" name="button" onclick="loginOpen()">Войти</button>
      <button type="button" name="button" onclick="checkinOpen()">Зарегистрироваться</button>
    </div>
  </div>
  </header>
  <MainPage/>
  <footer>
    <div class="footer__wrapper">
    <div class="info">
      <p>Подпишитесь на акции и анонсы событий</p>
      <form>
        <input type="text" name="" value="" placeholder="example@example.com">
        <button type="button" name="button">Подписаться</button>
      </form>
      <div>
      <a href="#">Политика использования</a>
      <a href="#">О нас</a>
    </div>
      <p>@TimepadKillers 2020</p>
    </div>
    <div class="social">
      <div class="social__images">
        <a href=""><svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M20 0C8.95161 0 0 8.95161 0 20C0 31.0484 8.95161 40 20 40C31.0484 40 40 31.0484 40 20C40 8.95161 31.0484 0 20 0ZM29.8226 13.7016L26.5403 29.1694C26.2984 30.2661 25.6452 30.5323 24.7339 30.0161L19.7339 26.3306L17.3226 28.6532C17.0565 28.9194 16.8306 29.1452 16.3145 29.1452L16.6694 24.0564L25.9355 15.6855C26.3387 15.3306 25.8468 15.129 25.3145 15.4839L13.8629 22.6935L8.92742 21.1532C7.85484 20.8145 7.83065 20.0806 9.15323 19.5645L28.4355 12.129C29.3306 11.8065 30.1129 12.3468 29.8226 13.7016Z" fill="black"/>
        </svg>
        </a>
        <a href=""><svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M39.375 20C39.375 9.29688 30.7031 0.625 20 0.625C9.29688 0.625 0.625 9.29688 0.625 20C0.625 29.6703 7.71016 37.6859 16.9727 39.1406V25.6008H12.0508V20H16.9727V15.7312C16.9727 10.8758 19.8633 8.19375 24.2906 8.19375C26.4109 8.19375 28.6281 8.57188 28.6281 8.57188V13.3375H26.1844C23.7781 13.3375 23.0273 14.8312 23.0273 16.3633V20H28.4008L27.5414 25.6008H23.0273V39.1406C32.2898 37.6859 39.375 29.6703 39.375 20Z" fill="black"/>
        </svg>
        </a>
        <a href=""><svg width="38" height="26" viewBox="0 0 38 26" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M36.8473 2.19531C37.1042 1.21875 36.8473 0.5 35.6112 0.5H31.5209C30.4792 0.5 30.0001 1.11719 29.7431 1.80469C29.7431 1.80469 27.6598 7.51562 24.7154 11.2188C23.764 12.2891 23.3265 12.6328 22.8056 12.6328C22.5487 12.6328 22.1529 12.2891 22.1529 11.3125V2.19531C22.1529 1.02344 21.8612 0.5 21.0001 0.5H14.5695C13.9167 0.5 13.5279 1.04688 13.5279 1.55469C13.5279 2.66406 15.0001 2.92188 15.1529 6.04688V12.8281C15.1529 14.3125 14.9167 14.5859 14.3959 14.5859C13.007 14.5859 9.63203 8.85156 7.63203 2.28906C7.22925 1.01563 6.83341 0.5 5.7848 0.5H1.69453C0.527859 0.5 0.291748 1.11719 0.291748 1.80469C0.291748 3.02344 1.68064 9.07813 6.75703 17.0781C10.139 22.5391 14.9029 25.5 19.2362 25.5C21.8404 25.5 22.1598 24.8438 22.1598 23.7109C22.1598 18.4922 21.9237 18 23.2292 18C23.8334 18 24.8751 18.3438 27.3056 20.9766C30.0834 24.1016 30.5417 25.5 32.0973 25.5H36.1876C37.3542 25.5 37.9445 24.8438 37.6042 23.5469C36.8265 20.8203 31.5695 15.2109 31.3334 14.8359C30.7292 13.9609 30.9029 13.5703 31.3334 12.7891C31.3404 12.7812 36.3334 4.875 36.8473 2.19531Z" fill="black"/>
        </svg>
        </a>
      </div>
      <p>
        Сотрудничество:<br>
      Example@example.example
    </p>
    </div>
  </div>
  </footer>
  </div>
  <div class="login">
  <h1>Вход</h1>
  <button type="button" name="button" class='close-btn' onclick="closeLogin()"><div style='transform:rotate(45deg);'>+</div></button>
  <form class="login__form" action="" method="">
    <input type="text" name="" value="" placeholder="Example@example.example">
    <input type="text" name="" value="" placeholder="Пароль">
  </form>
  <button type="button" name="button">Войти</button>
</div>
<div class="checkin">
  <h1>Регистрация</h1>
  <button type="button" name="button" class='close-btn' onclick="closeCheck()"><div style='transform:rotate(45deg);'>+</div></button>
  <form class="checkin__form" action="" method="">
    <input type="text" name="" value="" placeholder="Иван">
    <input type="tel" name="" value="" placeholder="+7 (999) 999 99 99 ">
    <input type="text" name="" value="" placeholder="Example@example.example">
    <input type="text" name="" value="" placeholder="Пароль">
    <input type="text" name="" value="" placeholder="Повторите пароль">
  </form>
  <button type="button" name="button">Войти</button>
</div>
  </div>
</template>
<script>
import MainPage from './components/MainPage'
export default {
  name: 'App',
  components: {
    MainPage
  }
}
</script>
