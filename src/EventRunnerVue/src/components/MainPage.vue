<template>
<div>
    <nav>
      <input type="text" class="searcing nav__items" placeholder="Хакатоны, Stand-up, Ленинград">
      <div class="buttons nav__items">
        <button class="buttons__items">Вебинары</button>
        <button class="buttons__items">Фильмы</button>
        <button class="buttons__items">Конференции</button>
      </div>
    </nav>
    <div class="content__settings">
        <div class="choosing">
          <h1>Мероприятия Москвы <span class="arrow">&#8250;</span></h1>
        </div>
        <button type="button" name="button">Дата <span class="arrow">&#8250;</span></button>
    </div>
      <h3 class="greeting">Наша подборка</h3>
      <div class="slider">
      </div>
      <div id='content__list'><content-list :items="items"></content-list></div>
      </div>
</template>
<script type='text/javascript'>
export default {
  name: 'MainPage',
  data () {
    return {
      message: 'MainPage'
    }
  }
}
var Vue = require('Vue')
Vue.component('content-list', {
  props: ['items'],
  template: '<ul><li><div class="item__logo"><div class="item__price">{{item.price}}</div></div><h4 class="title">{{item.title}}</h4><p class="date">{{item.date}}</p><p class="msg">{{item.message}}</p></li></ul>'
})
var contentList = new Vue()
contentList({
  el: '#content__list',
  data: {
    items:
    [{
      title: 'Название мероприятия',
      message: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In in massa eget pharetra turpis molestie rutrum volutpat. Aliquet duis aliquet leo, libero enim, quis.',
      price: '1200 р',
      date: '01 - 01 декабря 2020'
    }, {
      title: 'Название мероприятия',
      message: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In in massa eget pharetra turpis molestie rutrum volutpat. Aliquet duis aliquet leo, libero enim, quis.',
      price: '1200 р',
      date: '01 - 01 декабря 2020'
    }, {
      title: 'Название мероприятия',
      message: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In in massa eget pharetra turpis molestie rutrum volutpat. Aliquet duis aliquet leo, libero enim, quis.',
      price: '1200 р',
      date: '01 - 01 декабря 2020'
    }, {
      title: 'Название мероприятия',
      message: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In in massa eget pharetra turpis molestie rutrum volutpat. Aliquet duis aliquet leo, libero enim, quis.',
      price: '1200 р',
      date: '01 - 01 декабря 2020'
    }, {
      title: 'Название мероприятия',
      message: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In in massa eget pharetra turpis molestie rutrum volutpat. Aliquet duis aliquet leo, libero enim, quis.',
      price: '1200 р',
      date: '01 - 01 декабря 2020'
    }, {
      title: 'Название мероприятия',
      message: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In in massa eget pharetra turpis molestie rutrum volutpat. Aliquet duis aliquet leo, libero enim, quis.',
      price: '1200 р',
      date: '01 - 01 декабря 2020'
    }
    ]
  }
})
</script>
