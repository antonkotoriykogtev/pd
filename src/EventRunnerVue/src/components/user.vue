<template>

  <div class="row">



    <div class="container is-max-desktop container_padding">

      <b-navbar v-show="NavbarNoAuth">

        <template #brand>
          <b-navbar-item tag="router-link" :to="{ path: '/' }">
            <svg width="334" height="43" viewBox="0 0 334 43" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M0 21.5001L21.5 6.11389e-05L43 21.5001L21.5 43.0001L0 21.5001Z" fill="#004ACF"/>
              <path d="M5.70107 21.5001L27.2011 6.11389e-05L48.7011 21.5001L27.2011 43.0001L5.70107 21.5001Z" fill="#0368A4"/>
              <path d="M11.4021 21.5001L32.9021 6.11389e-05L54.4021 21.5001L32.9021 43.0001L11.4021 21.5001Z" fill="#057B8A"/>
              <path d="M17.1032 21.5001L38.6032 6.11389e-05L60.1032 21.5001L38.6032 43.0001L17.1032 21.5001Z" fill="#089B5E"/>
              <path d="M22.8043 21.5001L44.3043 6.11389e-05L65.8043 21.5001L44.3043 43.0001L22.8043 21.5001Z" fill="#0CBB33"/>
              <path d="M112.651 30.076V34H93.7512V8.8H112.147V12.724H98.4312V19.276H110.599V23.128H98.4312V30.076H112.651ZM135.19 14.776L126.946 34H122.302L114.058 14.776H118.738L124.714 29.032L130.87 14.776H135.19ZM155.547 24.496C155.547 24.808 155.523 25.252 155.475 25.828H140.391C140.655 27.244 141.339 28.372 142.443 29.212C143.571 30.028 144.963 30.436 146.619 30.436C148.731 30.436 150.471 29.74 151.839 28.348L154.251 31.12C153.387 32.152 152.295 32.932 150.975 33.46C149.655 33.988 148.167 34.252 146.511 34.252C144.399 34.252 142.539 33.832 140.931 32.992C139.323 32.152 138.075 30.988 137.187 29.5C136.323 27.988 135.891 26.284 135.891 24.388C135.891 22.516 136.311 20.836 137.151 19.348C138.015 17.836 139.203 16.66 140.715 15.82C142.227 14.98 143.931 14.56 145.827 14.56C147.699 14.56 149.367 14.98 150.831 15.82C152.319 16.636 153.471 17.8 154.287 19.312C155.127 20.8 155.547 22.528 155.547 24.496ZM145.827 18.16C144.387 18.16 143.163 18.592 142.155 19.456C141.171 20.296 140.571 21.424 140.355 22.84H151.263C151.071 21.448 150.483 20.32 149.499 19.456C148.515 18.592 147.291 18.16 145.827 18.16ZM170.778 14.56C173.202 14.56 175.146 15.268 176.61 16.684C178.074 18.1 178.806 20.2 178.806 22.984V34H174.306V23.56C174.306 21.88 173.91 20.62 173.118 19.78C172.326 18.916 171.198 18.484 169.734 18.484C168.078 18.484 166.77 18.988 165.81 19.996C164.85 20.98 164.37 22.408 164.37 24.28V34H159.87V14.776H164.154V17.26C164.898 16.372 165.834 15.7 166.962 15.244C168.09 14.788 169.362 14.56 170.778 14.56ZM196.071 32.956C195.543 33.388 194.895 33.712 194.127 33.928C193.383 34.144 192.591 34.252 191.751 34.252C189.639 34.252 188.007 33.7 186.854 32.596C185.703 31.492 185.127 29.884 185.127 27.772V18.52H181.959V14.92H185.127V10.528H189.627V14.92H194.775V18.52H189.627V27.664C189.627 28.6 189.855 29.32 190.311 29.824C190.767 30.304 191.427 30.544 192.291 30.544C193.299 30.544 194.139 30.28 194.811 29.752L196.071 32.956ZM216.692 34L211.544 26.62C211.328 26.644 211.004 26.656 210.572 26.656H204.884V34H200.204V8.8H210.572C212.756 8.8 214.652 9.16 216.26 9.88C217.892 10.6 219.14 11.632 220.004 12.976C220.868 14.32 221.3 15.916 221.3 17.764C221.3 19.66 220.832 21.292 219.896 22.66C218.984 24.028 217.664 25.048 215.936 25.72L221.732 34H216.692ZM216.584 17.764C216.584 16.156 216.056 14.92 215 14.056C213.944 13.192 212.396 12.76 210.356 12.76H204.884V22.804H210.356C212.396 22.804 213.944 22.372 215 21.508C216.056 20.62 216.584 19.372 216.584 17.764ZM244.716 14.776V34H240.432V31.552C239.712 32.416 238.812 33.088 237.732 33.568C236.652 34.024 235.488 34.252 234.24 34.252C231.672 34.252 229.644 33.544 228.156 32.128C226.692 30.688 225.96 28.564 225.96 25.756V14.776H230.46V25.144C230.46 26.872 230.844 28.168 231.612 29.032C232.404 29.872 233.52 30.292 234.96 30.292C236.568 30.292 237.84 29.8 238.776 28.816C239.736 27.808 240.216 26.368 240.216 24.496V14.776H244.716ZM261.516 14.56C263.94 14.56 265.884 15.268 267.348 16.684C268.812 18.1 269.544 20.2 269.544 22.984V34H265.044V23.56C265.044 21.88 264.648 20.62 263.856 19.78C263.064 18.916 261.936 18.484 260.472 18.484C258.816 18.484 257.508 18.988 256.548 19.996C255.588 20.98 255.108 22.408 255.108 24.28V34H250.608V14.776H254.892V17.26C255.636 16.372 256.572 15.7 257.7 15.244C258.828 14.788 260.1 14.56 261.516 14.56ZM286.161 14.56C288.585 14.56 290.529 15.268 291.993 16.684C293.457 18.1 294.189 20.2 294.189 22.984V34H289.689V23.56C289.689 21.88 289.293 20.62 288.501 19.78C287.709 18.916 286.581 18.484 285.117 18.484C283.461 18.484 282.153 18.988 281.193 19.996C280.233 20.98 279.753 22.408 279.753 24.28V34H275.253V14.776H279.537V17.26C280.281 16.372 281.217 15.7 282.345 15.244C283.473 14.788 284.745 14.56 286.161 14.56ZM318.145 24.496C318.145 24.808 318.121 25.252 318.073 25.828H302.989C303.253 27.244 303.937 28.372 305.041 29.212C306.169 30.028 307.561 30.436 309.217 30.436C311.329 30.436 313.069 29.74 314.437 28.348L316.849 31.12C315.985 32.152 314.893 32.932 313.573 33.46C312.253 33.988 310.765 34.252 309.109 34.252C306.997 34.252 305.137 33.832 303.529 32.992C301.921 32.152 300.673 30.988 299.785 29.5C298.921 27.988 298.489 26.284 298.489 24.388C298.489 22.516 298.909 20.836 299.749 19.348C300.613 17.836 301.801 16.66 303.313 15.82C304.825 14.98 306.529 14.56 308.425 14.56C310.297 14.56 311.965 14.98 313.429 15.82C314.917 16.636 316.069 17.8 316.885 19.312C317.725 20.8 318.145 22.528 318.145 24.496ZM308.425 18.16C306.985 18.16 305.761 18.592 304.753 19.456C303.769 20.296 303.169 21.424 302.953 22.84H313.861C313.669 21.448 313.081 20.32 312.097 19.456C311.113 18.592 309.889 18.16 308.425 18.16ZM326.752 17.584C328.048 15.568 330.328 14.56 333.592 14.56V18.844C333.208 18.772 332.86 18.736 332.548 18.736C330.796 18.736 329.428 19.252 328.444 20.284C327.46 21.292 326.968 22.756 326.968 24.676V34H322.468V14.776H326.752V17.584Z" fill="black"/>
            </svg>


          </b-navbar-item>
        </template>
        <template #end>
          <b-navbar-item tag="div">
            <div class="buttons">
              <a class="button is-info" v-on:click="loginOpen">
                <strong>Войти</strong>
              </a>
              <a class="button is-success" v-on:click="checkinOpen">
                <strong>Зарегестрироваться</strong>
              </a>
            </div>
          </b-navbar-item>
        </template>
      </b-navbar>
    </div>
    <div class="container is-max-desktop container_padding">

      <b-navbar v-show="NavbarAuth">

        <template #brand>
          <b-navbar-item tag="router-link" :to="{ path: '/' }">
            <svg width="334" height="43" viewBox="0 0 334 43" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M0 21.5001L21.5 6.11389e-05L43 21.5001L21.5 43.0001L0 21.5001Z" fill="#004ACF"/>
              <path d="M5.70107 21.5001L27.2011 6.11389e-05L48.7011 21.5001L27.2011 43.0001L5.70107 21.5001Z" fill="#0368A4"/>
              <path d="M11.4021 21.5001L32.9021 6.11389e-05L54.4021 21.5001L32.9021 43.0001L11.4021 21.5001Z" fill="#057B8A"/>
              <path d="M17.1032 21.5001L38.6032 6.11389e-05L60.1032 21.5001L38.6032 43.0001L17.1032 21.5001Z" fill="#089B5E"/>
              <path d="M22.8043 21.5001L44.3043 6.11389e-05L65.8043 21.5001L44.3043 43.0001L22.8043 21.5001Z" fill="#0CBB33"/>
              <path d="M112.651 30.076V34H93.7512V8.8H112.147V12.724H98.4312V19.276H110.599V23.128H98.4312V30.076H112.651ZM135.19 14.776L126.946 34H122.302L114.058 14.776H118.738L124.714 29.032L130.87 14.776H135.19ZM155.547 24.496C155.547 24.808 155.523 25.252 155.475 25.828H140.391C140.655 27.244 141.339 28.372 142.443 29.212C143.571 30.028 144.963 30.436 146.619 30.436C148.731 30.436 150.471 29.74 151.839 28.348L154.251 31.12C153.387 32.152 152.295 32.932 150.975 33.46C149.655 33.988 148.167 34.252 146.511 34.252C144.399 34.252 142.539 33.832 140.931 32.992C139.323 32.152 138.075 30.988 137.187 29.5C136.323 27.988 135.891 26.284 135.891 24.388C135.891 22.516 136.311 20.836 137.151 19.348C138.015 17.836 139.203 16.66 140.715 15.82C142.227 14.98 143.931 14.56 145.827 14.56C147.699 14.56 149.367 14.98 150.831 15.82C152.319 16.636 153.471 17.8 154.287 19.312C155.127 20.8 155.547 22.528 155.547 24.496ZM145.827 18.16C144.387 18.16 143.163 18.592 142.155 19.456C141.171 20.296 140.571 21.424 140.355 22.84H151.263C151.071 21.448 150.483 20.32 149.499 19.456C148.515 18.592 147.291 18.16 145.827 18.16ZM170.778 14.56C173.202 14.56 175.146 15.268 176.61 16.684C178.074 18.1 178.806 20.2 178.806 22.984V34H174.306V23.56C174.306 21.88 173.91 20.62 173.118 19.78C172.326 18.916 171.198 18.484 169.734 18.484C168.078 18.484 166.77 18.988 165.81 19.996C164.85 20.98 164.37 22.408 164.37 24.28V34H159.87V14.776H164.154V17.26C164.898 16.372 165.834 15.7 166.962 15.244C168.09 14.788 169.362 14.56 170.778 14.56ZM196.071 32.956C195.543 33.388 194.895 33.712 194.127 33.928C193.383 34.144 192.591 34.252 191.751 34.252C189.639 34.252 188.007 33.7 186.854 32.596C185.703 31.492 185.127 29.884 185.127 27.772V18.52H181.959V14.92H185.127V10.528H189.627V14.92H194.775V18.52H189.627V27.664C189.627 28.6 189.855 29.32 190.311 29.824C190.767 30.304 191.427 30.544 192.291 30.544C193.299 30.544 194.139 30.28 194.811 29.752L196.071 32.956ZM216.692 34L211.544 26.62C211.328 26.644 211.004 26.656 210.572 26.656H204.884V34H200.204V8.8H210.572C212.756 8.8 214.652 9.16 216.26 9.88C217.892 10.6 219.14 11.632 220.004 12.976C220.868 14.32 221.3 15.916 221.3 17.764C221.3 19.66 220.832 21.292 219.896 22.66C218.984 24.028 217.664 25.048 215.936 25.72L221.732 34H216.692ZM216.584 17.764C216.584 16.156 216.056 14.92 215 14.056C213.944 13.192 212.396 12.76 210.356 12.76H204.884V22.804H210.356C212.396 22.804 213.944 22.372 215 21.508C216.056 20.62 216.584 19.372 216.584 17.764ZM244.716 14.776V34H240.432V31.552C239.712 32.416 238.812 33.088 237.732 33.568C236.652 34.024 235.488 34.252 234.24 34.252C231.672 34.252 229.644 33.544 228.156 32.128C226.692 30.688 225.96 28.564 225.96 25.756V14.776H230.46V25.144C230.46 26.872 230.844 28.168 231.612 29.032C232.404 29.872 233.52 30.292 234.96 30.292C236.568 30.292 237.84 29.8 238.776 28.816C239.736 27.808 240.216 26.368 240.216 24.496V14.776H244.716ZM261.516 14.56C263.94 14.56 265.884 15.268 267.348 16.684C268.812 18.1 269.544 20.2 269.544 22.984V34H265.044V23.56C265.044 21.88 264.648 20.62 263.856 19.78C263.064 18.916 261.936 18.484 260.472 18.484C258.816 18.484 257.508 18.988 256.548 19.996C255.588 20.98 255.108 22.408 255.108 24.28V34H250.608V14.776H254.892V17.26C255.636 16.372 256.572 15.7 257.7 15.244C258.828 14.788 260.1 14.56 261.516 14.56ZM286.161 14.56C288.585 14.56 290.529 15.268 291.993 16.684C293.457 18.1 294.189 20.2 294.189 22.984V34H289.689V23.56C289.689 21.88 289.293 20.62 288.501 19.78C287.709 18.916 286.581 18.484 285.117 18.484C283.461 18.484 282.153 18.988 281.193 19.996C280.233 20.98 279.753 22.408 279.753 24.28V34H275.253V14.776H279.537V17.26C280.281 16.372 281.217 15.7 282.345 15.244C283.473 14.788 284.745 14.56 286.161 14.56ZM318.145 24.496C318.145 24.808 318.121 25.252 318.073 25.828H302.989C303.253 27.244 303.937 28.372 305.041 29.212C306.169 30.028 307.561 30.436 309.217 30.436C311.329 30.436 313.069 29.74 314.437 28.348L316.849 31.12C315.985 32.152 314.893 32.932 313.573 33.46C312.253 33.988 310.765 34.252 309.109 34.252C306.997 34.252 305.137 33.832 303.529 32.992C301.921 32.152 300.673 30.988 299.785 29.5C298.921 27.988 298.489 26.284 298.489 24.388C298.489 22.516 298.909 20.836 299.749 19.348C300.613 17.836 301.801 16.66 303.313 15.82C304.825 14.98 306.529 14.56 308.425 14.56C310.297 14.56 311.965 14.98 313.429 15.82C314.917 16.636 316.069 17.8 316.885 19.312C317.725 20.8 318.145 22.528 318.145 24.496ZM308.425 18.16C306.985 18.16 305.761 18.592 304.753 19.456C303.769 20.296 303.169 21.424 302.953 22.84H313.861C313.669 21.448 313.081 20.32 312.097 19.456C311.113 18.592 309.889 18.16 308.425 18.16ZM326.752 17.584C328.048 15.568 330.328 14.56 333.592 14.56V18.844C333.208 18.772 332.86 18.736 332.548 18.736C330.796 18.736 329.428 19.252 328.444 20.284C327.46 21.292 326.968 22.756 326.968 24.676V34H322.468V14.776H326.752V17.584Z" fill="black"/>
            </svg>


          </b-navbar-item>
        </template>
        <template #end>
          <b-navbar-item tag="div">
            <b-dropdown :triggers="['hover']"
                        position="is-bottom-left"
                        aria-role="list"
            >
              <template #trigger>
                <a
                  class="navbar-item "
                  role="button"
                  type="is-text"
                >
                    <span>
                      <figure class="image is-24x24">
                        <img :src="profile.picture_link" class='slider-img is-rounded'   alt=" ">
                      </figure>
                    </span>
                  <h4 style="margin-left:0.5rem">{{profile.first_name}} {{profile.last_name}}</h4>
                </a>

              </template>
              <router-link :to="'/user/'" >
                <b-dropdown-item  aria-role="listitem">
                  <b-icon icon="user-alt"></b-icon>
                  Профиль
                </b-dropdown-item>
              </router-link>
              <hr class="dropdown-divider">
              <router-link :to="'/'" >
                <b-dropdown-item value="home" aria-role="listitem">

                  <b-icon icon="home"></b-icon>
                  Главная

                </b-dropdown-item>
              </router-link>
              <router-link :to="'/create'" >
                <b-dropdown-item value="products" aria-role="listitem">

                  <b-icon icon="plus-square"></b-icon>
                  Создать мероприятие

                </b-dropdown-item>
              </router-link>
              <hr class="dropdown-divider" aria-role="listitem">
              <router-link :to="'/logout'" >
                <b-dropdown-item value="settings">
                  <b-icon icon="sign-out-alt"></b-icon>
                  Выйти
                </b-dropdown-item>
              </router-link>
            </b-dropdown>

          </b-navbar-item>

        </template>


      </b-navbar>
    </div>





    <div v-show="UserNoSettings" class="container is-max-desktop EventContainerMargin" >
         <div v-if="profile.first_name">
          <div class="columns is-mobile">
            <div class="column is-half ">
              <figure class="image is-128x128">
                <img :src="profile.picture_link" class='slider-img is-rounded'  ratio="6by4" alt=" ">
              </figure>

            </div>
          </div>

          <div class="columns is-mobile">
            <div class="column is-half ">

              <h1 class="title is-3" style="display: inline;">{{profile.first_name}}</h1>
              <h1 class="title is-3"style="display: inline;">{{profile.last_name}}</h1>
              <h2 style="margin-top:10px">
                <b-icon icon="calendar"></b-icon>
                Дата рождения:
              </h2>
              <h1 style>
                {{profile.date_of_birth}}
              </h1>
              <h2 >
                <b-icon icon="envelope"></b-icon>
                Ваша почта:
              </h2>
              <h1>
                {{profile.email}}
              </h1>
              <h2>
                <b-icon icon="file-alt"></b-icon>
                О себе:
              </h2>
              <h1 >
                {{profile.about_me}}
              </h1>
              <h2>
                <b-icon icon="building"></b-icon>
                Город:
              </h2>
              <h1>
                {{profile.city}}
              </h1>
            </div>
          </div>
         </div>
          <div v-else>
             <div class="columns is-mobile">
               <div class="column is-half ">
                 <figure class="image is-128x128">
                   <b-icon
                     icon="user-circle"
                     size="is-large"
                     >
                   </b-icon>
                 </figure>
               </div>
             </div>
             <div class="columns is-mobile">
               <div class="column is-half ">
                 <h1 class="title is-3" style="display: inline;">Нету информации о вас :(</h1>
               </div>
             </div>
          </div>

        <b-button v-on:click="OpenUserSettings" class="is-success">Настройки</b-button>
    </div>

    <div v-show="UserSettings" class="container is-max-desktop " style="margin-top:20px">
      <section>
        <div class="container is-max-desktop container_padding">
          <b-tabs position="is-centered" v-model="activeTab">
            <b-tab-item label="Профиль">
              <div class="columns is-mobile">
                <div class="column is-half ">
                  <figure class="image is-128x128">
                    <img :src="profile.picture_link" class='slider-img is-rounded'  ratio="6by4" alt=" ">
                </figure>

                </div>

              </div>
              <b-button icon-left="upload" type="is-info" outlined style="margin-bottom:1rem">
                Загрузить изображение
              </b-button>
              <b-field class="file is-info "  :class="{'has-name': !!file}">
                <b-upload v-model="file" class="file-label">
                <span class="file-cta">
                    <b-icon class="file-icon" icon="upload"></b-icon>
                    <span class="file-label">Загрузить изображение</span>
                </span>
                      <span class="file-name" v-if="file">
                    {{ file.name }}
                </span>
                    </b-upload>
              </b-field>
              <form v-on:submit.prevent="SaveUserInfo">

                <b-field label="Имя" :label-position="labelPosition">
                  <b-input v-model="profileupdate.first_name" ></b-input>
                </b-field>
                <b-field label="Фамилия" :label-position="labelPosition">
                  <b-input v-model="profileupdate.last_name" ></b-input>
                </b-field>
                <b-field label="Телефон" :label-position="labelPosition">
                  <b-input  v-model="profileupdate.phone_number" ></b-input>
                </b-field>

                <b-field label="О себе"
                         :label-position="labelPosition"

                >
                  <b-input maxlength="200" type="textarea"
                           v-model="profileupdate.about_me"

                  ></b-input>
                </b-field>
                <b-field label="Город" :label-position="labelPosition">
                  <b-input
                    v-model="profileupdate.city"
                    ></b-input>
                </b-field>
                <b-field label="Select a date" :label-position="labelPosition">
                  <b-datepicker
                    v-model="profileupdate.date_of_birth"
                    placeholder="Click to select..."
                    icon="calendar-alt"
                    trap-focus>
                  </b-datepicker>
                </b-field>




                <button class=" button is-info" type="submit" v-on:click="UpdateProfile">Сохранить</button>
                <button class=" button is-info is-light" v-on:click="CloseSettings">Отменить</button>


              </form>

            </b-tab-item>

            <b-tab-item label="Настройки почты">
              <b-field label="Почта"
                       :label-position="labelPosition"
              >
                <b-input type="email"
                         :value="profile.email"
                         maxlength="45">
                </b-input>
              </b-field>
            </b-tab-item>

            <b-tab-item label="Настройки приватности">

            </b-tab-item>



          </b-tabs>
        </div>
      </section>



    </div>

    <div class="container is-max-desktop EventContainerMargin" >

      <h1 class="title is-4 MarginTextDetail" style="margin-bottom: 10px;">Мои меропрития</h1>
      <ul id='content_list'>
        <li v-for="(data,index) in info"  v-if="info[index].author==user_id" :key="id">


          <div class="card">
            <router-link :to="'/eventdetail/' + data.id" class="link-item">
              <div class="card-image">
                <div class="item_logo">
                  <figure class="image is-16by9">
                    <img :src="info[index].picture_link" style=" border-radius: 8px 8px 0 0; object-fit: cover;" alt=' '>
                  </figure>
                  <div class="item_price" v-if="info[index].price === null">
                    <b-tag type="is-info">Бесплатно</b-tag>

                  </div>
                  <div class="item_price" v-else-if="info[index].price === ''">
                    <b-tag type="is-info">Бесплатно</b-tag>

                  </div>
                  <div class="item_price" v-else-if="info[index].price === 0">
                    <b-tag type="is-info">Бесплатно</b-tag>

                  </div>
                  <div class="item_price" v-else>
                    <b-tag type="is-info"> {{info[index].price}} р.</b-tag>

                  </div>
                </div>
              </div>
              <div class="card-content">
                <div class="media">

                  <div class="media-content">
                    <p class="title is-4">{{ info[index].name }}</p>
                    <p class="subtitle is-6">

                      {{ new Date(info[index].start_date).toLocaleString('ru', {
                      year: 'numeric',
                      month: 'long',
                      day: 'numeric',
                      hour: 'numeric',
                      minute: 'numeric',
                      }) }} - {{ new Date(info[index].end_date).toLocaleString('ru', {
                      year: 'numeric',
                      month: 'long',
                      day: 'numeric',
                      hour: 'numeric',
                      minute: 'numeric',
                      }) }}
                    </p>
                  </div>
                </div>
                <div class="content">
                  <b-field>
                    <b-taglist>

                      <b-tag v-for="(data,TagsIndex) in info[index].tag" :key="id" type="is-info">{{info[index].tag[TagsIndex].name }} </b-tag>

                    </b-taglist>
                  </b-field>
                </div>
              </div>
            </router-link>
            <footer class="card-footer">

              <a class="card-footer-item editbutton"   v-on:click="EditEvent($event, info[index].id)">Редактировать</a>
              <a class="card-footer-item deletebutton" v-on:click="DeleteEvent($event, info[index].id, info[index].name)">Удалить</a>
            </footer>
          </div>


        </li>

      </ul>
    </div>

    <div class="container is-max-desktop EventContainerMargin" >
      <hr>
      <h1 class="title is-4 MarginTextDetail" style="margin-bottom: 10px;">Мои организации</h1>
      <div v-for="(data,index) in organisation" class="tile is-ancestor box" style="margin-top:10px">
        <div class="tile is-parent">
          <article class="tile is-child ">
            <figure class="image is-4by3">

            <img src="http://eventrunner.1gb.ru/media/bhVf6QaJqA4.jpg"
                 style=" border-radius: 5px; object-fit: cover;"
                 alt=' '
            >

            </figure>
          </article>
        </div>
        <div class="tile is-parent">
          <article class="tile is-child ">
            <p class="title">{{organisation[index].name}}</p>

            <p class="subtitle">Участники:</p>
            <div v-for="(data,index) in UserInOrganisation">

             <!-- <figure class="image is-64x64" >
                <img :src="profile.picture_link" style="display: inline;" class='slider-img is-rounded'  ratio="6by4" alt=" ">

              </figure>-->

            </div>

          </article>
        </div>
      </div>

    </div>



    <footer>
      <div class="footer_wrapper">
        <div class="info">
          <p>Подпишитесь на акции и анонсы событий</p>
          <form>
            <input type="text" name="" value="" placeholder="example@example.com">
            <button type="button" class='button is-success' name="button">Подписаться</button>
          </form>
          <div>
            <a href="#">Политика использования</a>
            <a href="#">О нас</a>
          </div>
          <p>@TimepadKillers 2020</p>
        </div>
        <div class="social">
          <div class="social_images">
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
    <div class="overlay">
      <div class="login">


        <h1>Вход</h1>
        <form  @submit.prevent="login">

          <b-field label="Email"
                   type="is-danger"
          >
            <b-input type="email"
                     value=""
                     maxlength="50"
                     v-model="email"
            >
            </b-input>
          </b-field>


          <b-field label="Password">
            <b-input type="password"
                     value=""
                     password-reveal
                     v-model="password">
            </b-input>
          </b-field>
          <b-button type="is-success" native-type="submit">Войти</b-button>

          <button type="button" name="button" class='close-btn is-info' v-on:click="closeCheck"><div style='transform:rotate(45deg);'>+</div></button>      </form>

      </div>





      <div class="checkin">

        <h1>Регистрация</h1>
        <button type="button" name="button" class='close-btn is-info' v-on:click="closeCheck"><div style='transform:rotate(45deg);'>+</div></button>
        <form class="checkin_form" v-on:submit.prevent="RegistrationForm">
          <input type="email"  id="name" placeholder="Почта" v-model="form.email">
          <input type="password"  id="email" placeholder="Пароль" v-model="form.password">
          <button class='form-btn button is-info overlay-btn' v-on:click="alertRegistration">Зарегистрироваться</button>
        </form>

      </div>
    </div>

  </div>
</template>

<script >
  import axios from 'axios'
  import { DialogProgrammatic as Dialog } from 'buefy'
  import VueJwtDecode from 'vue-jwt-decode'
  import store from '@/store/main.js'
  export default {

    name: 'user',
    data () {
      return {
        activeTab: 0,
        file:'',
        form:{
          email: '',
          password:'',
        },
        profile:{
          email:'',
          first_name:'',
          last_name:'',
          about_me:'',
          date_of_birth:'',
          city:'',
          picture_link:'',
          notification_type:'',
          data_visibility_type:'',
          selected_events:'',
          phone_number:'',
        },
        profileupdate:{
          email:'',
          first_name:'',
          last_name:'',
          about_me:'',
          date_of_birth: new Date(),
          city:'',
          picture_link:'',
          notification_type:'',
          data_visibility_type:'',
          selected_events:'',
          phone_number:'',
        },

        organisation:'',
        title: 'index',
        info: null,
        password: '',
        msg:'',
        msgreg:'',
        token:'',
        user_id:'',
        UserNoSettings:true,
        UserSettings:false,
        NavbarAuth:'',
        NavbarNoAuth:'',
        UserInOrganisation:'',
        labelPosition: 'on-border'
      }
    },
    methods: {
      UpdateProfile(){
        if(this.file){
          if(this.profileupdate.date_of_birth!=this.profile.date_of_birth) {
            let myDate = this.profileupdate.date_of_birth;
            let realDate =
              myDate.getFullYear() +
              "-" +
              ("0" + (myDate.getMonth() + 1)).slice(-2) +
              "-" +
              ("0" + myDate.getDate()).slice(-2);
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
            const DataCreationForm = new FormData();
            DataCreationForm.append('picture_link', this.file, this.file.name);
            DataCreationForm.append('first_name', this.profileupdate.first_name);
            DataCreationForm.append('last_name', this.profileupdate.last_name);
            DataCreationForm.append('phone_number', this.profileupdate.phone_number);
            DataCreationForm.append('about_me', this.profileupdate.about_me);
            DataCreationForm.append('city', this.profileupdate.city);
            DataCreationForm.append('date_of_birth', realDate);

            axios
              .post('http://eventrunner.1gb.ru/users/' + this.user_id,
                DataCreationForm, { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } })
              .then((res) => {
              })
              .catch((error) => {
                console.log(error.response.data);
                console.log(error.response.status);
                console.log(error.response.headers);
                this.msgreg = error.response.data;
                this.$buefy.dialog.alert({
                  title: 'Что-то пошло не так',
                  message: this.msg,
                  confirmText: 'Продолжить',
                  type: 'is-info'
                })
              })
              .finally(() => {

                  this.UserNoSettings=true;
                  this.UserSettings=false;

                  this.$buefy.dialog.alert('Информация изменена');
                  this.$router.push();

                }
              );

          }
          else{
            axios.defaults.xsrfCookieName = 'csrftoken'
            axios.defaults.xsrfHeaderName = 'X-CSRFToken'
            const DataCreationForm = new FormData();
            DataCreationForm.append('picture_link', this.file, this.file.name);
            DataCreationForm.append('first_name', this.profileupdate.first_name);
            DataCreationForm.append('last_name', this.profileupdate.last_name);
            DataCreationForm.append('phone_number', this.profileupdate.phone_number);
            DataCreationForm.append('about_me', this.profileupdate.about_me);
            DataCreationForm.append('city', this.profileupdate.city);
            DataCreationForm.append('date_of_birth', this.profileupdate.date_of_birth);

            axios
              .post('http://eventrunner.1gb.ru/users/' + this.user_id,
                DataCreationForm, { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } })
              .then((res) => {
              })
              .then((res) => {
              })
              .catch((error) => {
                console.log(error.response.data);
                console.log(error.response.status);
                console.log(error.response.headers);
                this.msgreg = error.response.data;
                this.$buefy.dialog.alert({
                  title: 'Предупреждение',
                  message: this.msg,
                  confirmText: 'Продолжить',
                  type: 'is-info'
                })
              }).finally(() => {

              this.$buefy.dialog.alert('Информация изменена');
              this.UserNoSettings=true;
              this.UserSettings=false;
              this.$router.push();
            })
            ;
          }
        }
        else{
          if(this.profileupdate.date_of_birth!=this.profile.date_of_birth) {
            let myDate = this.profileupdate.date_of_birth;
            let realDate =
              myDate.getFullYear() +
              "-" +
              ("0" + (myDate.getMonth() + 1)).slice(-2) +
              "-" +
              ("0" + myDate.getDate()).slice(-2);

            axios
              .patch('http://eventrunner.1gb.ru/users/' + this.user_id,
                {
                  first_name: this.profileupdate.first_name,
                  last_name: this.profileupdate.last_name,
                  phone_number: this.profileupdate.phone_number,
                  about_me: this.profileupdate.about_me,
                  city: this.profileupdate.city,
                  date_of_birth: realDate,
                })
              .then((res) => {
              })
              .catch((error) => {
                console.log(error.response.data);
                console.log(error.response.status);
                console.log(error.response.headers);
                this.msgreg = error.response.data;
                this.$buefy.dialog.alert({
                  title: 'Предупреждение',
                  message: this.msg,
                  confirmText: 'Продолжить',
                  type: 'is-info'
                })
              })
              .finally(() => {

                  this.UserNoSettings=true;
                  this.UserSettings=false;

                  this.$buefy.dialog.alert('Информация изменена');
                  this.$router.push();

                }
              );

          }
          else{
            axios
              .patch('http://eventrunner.1gb.ru/users/' + this.user_id,
                {
                  first_name: this.profileupdate.first_name,
                  last_name: this.profileupdate.last_name,
                  phone_number: this.profileupdate.phone_number,
                  about_me: this.profileupdate.about_me,
                  city: this.profileupdate.city,
                  date_of_birth: this.profileupdate.date_of_birth,
                })
              .then((res) => {
              })
              .catch((error) => {
                console.log(error.response.data);
                console.log(error.response.status);
                console.log(error.response.headers);
                this.msgreg = error.response.data;
                this.$buefy.dialog.alert({
                  title: 'Предупреждение',
                  message: this.msg,
                  confirmText: 'Продолжить',
                  type: 'is-info'
                })
              }).finally(() => {

              this.$buefy.dialog.alert('Информация изменена');
              this.UserNoSettings=true;
              this.UserSettings=false;
              this.$router.push();
            })
            ;
          }
        }

      },
      RegistrationForm(){ //registration form, posts new accounts to api
        axios.post('http://eventrunner.1gb.ru/auth/users/', this.form)
          .then((res) => {
          })
          .catch((error) => {
            console.log(error.response.data);
            console.log(error.response.status);
            console.log(error.response.headers);
            this.msgreg=error.response.data;
          }).finally(() => {
        });
      },
      OpenUserSettings:function(event){
        this.profileupdate.first_name=this.profile.first_name;
        this.profileupdate.last_name=this.profile.last_name;
        this.profileupdate.about_me=this.profile.about_me;
        this.profileupdate.phone_number=this.profile.phone_number;
        this.profileupdate.date_of_birth=this.profile.date_of_birth;
        this.profileupdate.city=this.profile.city;
        this.UserNoSettings=false;
        this.UserSettings=true;
      },
      DeleteEvent:function(event, event_id, event_name){
        this.$buefy.dialog.confirm({
          message: 'Вы точно хотите удалить мероприятие ' + event_name,
          cancelText: 'Не надо, пожалейте его',
          type: 'is-danger',
          confirmText: 'Да',
          onConfirm: () => axios.delete("http://eventrunner.1gb.ru/events/" + event_id).then(() => this.$router.go())
        })
      },
      EditEvent:function(event, event_id)
      {
        let id=event_id.toString();
        this.$router.push('/eventedit/' + id);
      },
      CloseSettings:function(event){
        this.UserNoSettings=true;
        this.UserSettings=false;
      },
      login: function () {
        let email = this.email
        let password = this.password
        this.$store.dispatch('login', { email, password })
          .then(() => this.$router.push('/user'))
          .catch(err => console.log(err))
      },
      loginOpen: function(event) {
        document.querySelector('.overlay').style.display = 'flex';
        document.querySelector('.login').style.display = 'block';
        document.querySelector('.navbar').style.backgroundColor = "#7f7f7f";

      },
      checkinOpen: function(event) {
        document.querySelector('.overlay').style.display = 'flex';
        document.querySelector('.checkin').style.display = 'block';
        document.querySelector('.navbar').style.backgroundColor = "#7f7f7f";

      },
      closeCheck: function(event) {
        document.querySelector('.overlay').style.display = 'none';
        document.querySelector('.checkin').style.display = 'none';
        document.querySelector('.navbar').style.backgroundColor = "white";

      },
      closeLogin: function(event) {
        document.querySelector('.overlay').style.display = 'none';
        document.querySelector('.login').style.display = 'none';
        document.querySelector('.navbar').style.backgroundColor = "white";

      },
      openBox: function(event) {
        if (document.querySelector('.profile_box ').style.display == 'none') {
          document.querySelector('.profile_box ').style.display = 'flex';
        } else {
          document.querySelector('.profile_box ').style.display = 'none';
        }
      },

      alertLogin() {
        this.$buefy.dialog.alert({
          title: 'Предупреждение',
          message: this.msg,
          confirmText: 'Продолжить',
          type: 'is-info'
        })
      },
      handleFileUpload(){
        this.file = this.$refs.file.files[0];
      },
      alertRegistration() { //this is alert for registration
        if (this.msgreg != "") {
          this.$buefy.dialog.alert({
            title: 'Ошибка',
            message: this.msgreg["email"],
            confirmText: 'Попробовать снова',
            type: 'is-danger',
          })
        }
        else{
          this.$buefy.dialog.alert('Спасибо за регистрацию, на вашу почту уже пришло письмо для подтверждения регистрации!')
        }

      }
    },
    async created() {
      if (!store.getters.isLoggedIn) {
        alert("Если вы хотите увидеть эту страницу, вам нужно войти или зарегестрироваться, сделать вы это можете на главной странице.");
        this.$router.push('/');
        this.NavbarAuth=false;
        this.NavbarNoAuth=true;
      }
      else {
        this.NavbarAuth=true;
        this.NavbarNoAuth=false;
        let decoded = VueJwtDecode.decode(localStorage.getItem('usertoken'));
        this.user_id = decoded.user_id;

        axios
          .get('http://eventrunner.1gb.ru/users/' + this.user_id)
          .then(response => (this.profile = response["data"]));
      }
    },

    mounted() {
      axios
        .get('http://eventrunner.1gb.ru/events/')
        .then(response => (this.info = response["data"]));
      axios
        .get('http://eventrunner.1gb.ru/organisation/')
        .then(response => (this.organisation = response["data"]));

      axios
        .get('http://eventrunner.1gb.ru/user_in_organisation/')
        .then(response => (this.UserInOrganisation = response["data"]));

    },

  }

</script>


