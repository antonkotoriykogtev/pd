import Vue from 'vue'
import Router from 'vue-router'
import axios from 'axios'
import index from '@/components/index'
import eventdetail from '@/components/eventdetail'
import creator from '@/components/creator'
import user from '@/components/user'
import EmailActivation from "@/components/EmailActivation";
import logout from "@/components/logout"
import event_edit from "../components/event_edit";
Vue.use(Router)



export default new Router({
mode: 'history',
  routes: [
      {
        path: '/activate/:user_id/:token',
        component: EmailActivation,
      },
      {
        path:'/eventedit/:id',
        component: event_edit,

      },
      {
        path: '/',
        name: 'index',
        component: index
       },
       {
         path: '/eventdetail/:id',
         name: 'eventdetail',
         component: eventdetail,
         props: true
       },
       {
         path: '/create',
         name: 'creator',
         component: creator,
         props: true,
       },
       {
         path: '/user',
         name: 'user',
         component: user,
         props: true,
       },
        {
          path: '/logout',
          name: 'logout',
          component: logout,
          props: true,
        },



       {
         path: "/page-not-found",
         alias: '*',
         component: { render: (h) => h("div", ["404! Page Not Found!"]) },
      },
  ]
})
