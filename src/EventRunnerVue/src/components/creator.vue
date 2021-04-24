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
    <main class="creator">

      <h1 class="title is-4">Создание мероприятия</h1>
      <form v-on:submit.prevent="submitData">
        <b-field label="Название" >
          <b-input required v-model="event.name" ></b-input>
        </b-field>
        <b-field  v-on:change="handleFileUpload()" class="file is-info " :class="{'has-name': !!file}">
          <b-upload required v-model="file" class="file-label">
            <span class="file-cta">
                <b-icon class="file-icon" icon="upload"></b-icon>
                <span  class="file-label">Click to upload</span>
            </span>
            <span class="file-name" v-if="file">
                {{ file.name }}
            </span>
          </b-upload>
        </b-field>
        <!--<p class="creator_title">Фото</p>
        &lt;!&ndash;<label>Files
          <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
        </label>&ndash;&gt;-->
        <b-field label="Введите место проведения" >
          <b-input  v-model="event.address" ></b-input>
        </b-field>
        <b-field>
          <b-checkbox v-model="event.is_online"
                      type="is-info"
          >Онлайн</b-checkbox>
        </b-field>

        <p class="creator_title">Дата проведения:</p>
         <!--<input name="eventStart" type="datetime-local" v-model="event.start_date">-->
          <section>
            <b-field required label="Начало">
              <b-datetimepicker
                placeholder="Выберите дату проведения"
                icon="calendar-alt"
                :locale="locale"
                :datepicker="{ showWeekNumber }"
                :timepicker="{ enableSeconds, hourFormat }"
                horizontal-time-picker
                v-model="event.start_date"
              >
              </b-datetimepicker>
            </b-field>
          </section>

          <b-field label="Конец">
            <b-datetimepicker
              placeholder="Выберите дату проведения"
              icon="calendar-alt"
              :locale="locale"
              :datepicker="{ showWeekNumber }"
              :timepicker="{ enableSeconds, hourFormat }"
              horizontal-time-picker
              v-model="event.end_date"
            >
            </b-datetimepicker>
          </b-field>

        <!--<p>Конец: <input name="eventFinish" type="datetime-local" v-model="event.end_date"></p>-->
        <b-field label="Введите стоимость" >
          <b-input min="0" v-model="event.price" placeholder="Оставьте поле пустым для бесплатного мероприятия"></b-input>
        </b-field>
        <b-field label="Лимит количества посетителей">
          <b-slider required type="is-info" indicator :tooltip="false" :max="500"  v-model="event.max_participants_quantity"></b-slider>
        </b-field>

        <b-field label="Enter some tags">
          <b-taginput
            v-model="tags"
            :data="filteredTags"
            autocomplete
            :allow-new="allowNew"
            :open-on-focus="openOnFocus"
            field="name"
            icon="tag"
            placeholder="Add a tag"
            @typing="getFilteredTags">
          </b-taginput>
        </b-field>
        <pre style="max-height: 400px"><b>Tags:</b>{{ tags }}</pre>

        <p class="creator_title">Описание:</p>

        <vue-editor  v-model="event.description"></vue-editor>
        <p class="creator_title" >Превью вашего описания:</p>
        <div v-html="event.description"></div>

        <div class=" has-text-centered">
          <button class=" button is-info" type="submit" v-on:click="">Опубликовать</button>
        </div>

      </form>
    </main>
    <footer>
      <div class="footer_wrapper">
        <div class="info">
          <p>Подпишитесь на акции и анонсы событий</p>
          <form>
            <input name="" placeholder="example@example.com" type="text" value="">
            <button class='button is-success' name="button" type="button">Подписаться</button>
          </form>
          <div>
            <a href="#">Политика использования</a>
            <a href="#">О нас</a>
          </div>
          <p>@TimepadKillers 2020</p>
        </div>
        <div class="social">
          <div class="social_images">
            <a href=""><svg fill="none" height="40" viewBox="0 0 40 40" width="40" xmlns="http://www.w3.org/2000/svg">
              <path d="M20 0C8.95161 0 0 8.95161 0 20C0 31.0484 8.95161 40 20 40C31.0484 40 40 31.0484 40 20C40 8.95161 31.0484 0 20 0ZM29.8226 13.7016L26.5403 29.1694C26.2984 30.2661 25.6452 30.5323 24.7339 30.0161L19.7339 26.3306L17.3226 28.6532C17.0565 28.9194 16.8306 29.1452 16.3145 29.1452L16.6694 24.0564L25.9355 15.6855C26.3387 15.3306 25.8468 15.129 25.3145 15.4839L13.8629 22.6935L8.92742 21.1532C7.85484 20.8145 7.83065 20.0806 9.15323 19.5645L28.4355 12.129C29.3306 11.8065 30.1129 12.3468 29.8226 13.7016Z" fill="black"/>
            </svg>
            </a>
            <a href=""><svg fill="none" height="40" viewBox="0 0 40 40" width="40" xmlns="http://www.w3.org/2000/svg">
              <path d="M39.375 20C39.375 9.29688 30.7031 0.625 20 0.625C9.29688 0.625 0.625 9.29688 0.625 20C0.625 29.6703 7.71016 37.6859 16.9727 39.1406V25.6008H12.0508V20H16.9727V15.7312C16.9727 10.8758 19.8633 8.19375 24.2906 8.19375C26.4109 8.19375 28.6281 8.57188 28.6281 8.57188V13.3375H26.1844C23.7781 13.3375 23.0273 14.8312 23.0273 16.3633V20H28.4008L27.5414 25.6008H23.0273V39.1406C32.2898 37.6859 39.375 29.6703 39.375 20Z" fill="black"/>
            </svg>
            </a>
            <a href=""><svg fill="none" height="26" viewBox="0 0 38 26" width="38" xmlns="http://www.w3.org/2000/svg">
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
</template>
<div class="overlay">
  <div class="login">


    <h1>Вход</h1>

    <button type="button" name="button" class='close-btn is-info' v-on:click="closeCheck"><div style='transform:rotate(45deg);'>+</div></button>
    <form class="checkin_form" @submit.prevent="login">
      <input type="email"  value="" maxlength="50"  placeholder="Почта" v-model="email">
      <input type="password"  value="" password-reveal  placeholder="Пароль" v-model="password">
      <button class='form-btn button is-info overlay-btn LoginButton' native-type="submit">Войти</button>
    </form>
  </div>

  <div class="checkin">

    <h1>Регистрация</h1>
    <button type="button" name="button" class='close-btn is-info' v-on:click="closeCheck"><div style='transform:rotate(45deg);'>+</div></button>
    <form class="checkin_form" v-on:submit.prevent="RegistrationForm">
      <input type="email"   placeholder="Почта" v-model="form.email">
      <input type="password"  placeholder="Пароль" v-model="form.password">
      <button class='form-btn button is-info overlay-btn' v-on:click="alertRegistration">Зарегистрироваться</button>
    </form>

  </div>
</div>




<script >
  import axios from 'axios'
  import VueJwtDecode from "vue-jwt-decode";
  import store from '@/store/main.js'
  import { VueEditor } from "vue2-editor";

  export default {
    name: 'creator',
    data () {
      return {
        title: 'creator',
        showWeekNumber: false,
        enableSeconds: false,
        hourFormat: undefined,
        locale: undefined,
        info: '',
        file: '',
        event:{
          "name": "",
          "author": "",
          "start_date": new Date(),
          "end_date": new Date(),
          "small_description": "",
          "description": "",
          "price": 0,
          "max_participants_quantity": null,
          "address": "",
          "geopoint_lat": null,
          "geopoint_long": null,
          "ics_file_link": "",
          "is_online": false,
          "tag":'',
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

        },
        token:'',
        user_id:'',
        NavbarAuth:'',
        NavbarNoAuth:'',
        content: "<h1>Some initial content</h1>",
        labelPosition: 'on-border',
        filteredTags:'',
        isSelectOnly: false,
        tags: '',
        allowNew: false,
        openOnFocus: false,
        AllTags:'',

      }
    },
    async created() {
      if (!store.getters.isLoggedIn) {
        this.NavbarAuth=false;
        this.NavbarNoAuth=true;
      }
      else if(store.getters.isLoggedIn){
        this.NavbarAuth=true;
        this.NavbarNoAuth=false
        let decoded = VueJwtDecode.decode(localStorage.getItem('usertoken'));
        this.user_id = decoded.user_id;
        axios
          .get('http://eventrunner.1gb.ru/users/' + this.user_id)
          .then(response => (this.profile = response["data"]));
        axios
          .get('http://eventrunner.1gb.ru/tag/')
          .then(response => (this.AllTags = response["data"]));
        this.filteredTags = this.AllTags
      }
    },
    methods: {


      submitData() {
        console.log(this.tags)
        let StartDateNot = this.event.start_date;
        let StartDateString=StartDateNot.toString()
        let StartTime=StartDateString.slice(16,24)
        let start_date_fin =
          StartDateNot.getFullYear() +
          "-" +
          ("0" + (StartDateNot.getMonth() + 1)).slice(-2) +
          "-" +
          ("0" + StartDateNot.getDate()).slice(-2) + "T" + StartTime + "Z";
        console.log(start_date_fin)
        let EndDateNot = this.event.end_date;
        let EndDateString=EndDateNot.toString()
        let EndTime=EndDateString.slice(16,24)
        let end_date_fin =
          EndDateNot.getFullYear() +
          "-" +
          ("0" + (EndDateNot.getMonth() + 1)).slice(-2) +
          "-" +
          ("0" + EndDateNot.getDate()).slice(-2) + "T" + EndTime + "Z";

        axios.defaults.xsrfCookieName = 'csrftoken'
        axios.defaults.xsrfHeaderName = 'X-CSRFToken'
        let TagsArray = JSON.stringify(this.tags)
        console.log(TagsArray)
        this.tags = "5"
        const DataCreationForm = new FormData();
        DataCreationForm.append('picture_link', this.file, this.file.name);
        DataCreationForm.append('author', this.user_id);
        DataCreationForm.append('name', this.event.name);
        DataCreationForm.append('start_date', start_date_fin);
        DataCreationForm.append('end_date', end_date_fin);
        DataCreationForm.append('description', this.event.description);
        DataCreationForm.append('price', this.event.price);
        DataCreationForm.append('is_online', this.event.is_online);
        DataCreationForm.append('max_participants_quantity', this.event.max_participants_quantity);
        DataCreationForm.append('tag', this.tags);


        axios.post(
          `http://eventrunner.1gb.ru/events/`,
          DataCreationForm,
          { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }
        );





      },
      getFilteredTags(text) {
        console.log(this.AllTags[0].name);
        this.filteredTags = this.AllTags.filter((option) => {
          return option.name
            .toString()
            .toLowerCase()
            .indexOf(text.toLowerCase()) >= 0
        })
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
      handleFileUpload(){
        this.file = this.$refs.file.files[0];
      },
      openBox: function(event) {
        if (document.querySelector('.profile_box ').style.display == 'none') {
          document.querySelector('.profile_box ').style.display = 'flex';
        }
        else {
          document.querySelector('.profile_box ').style.display = 'none';
        }
      },



    },
    components: {
      VueEditor
    },


  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
