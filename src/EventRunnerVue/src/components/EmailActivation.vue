<template>
    <div>
      <h1 class="title is-1"> Подтверждение почты</h1>


    </div>
</template>

<script>
    import axios from "axios";
    import { DialogProgrammatic as Dialog } from 'buefy'

    export default {
        name: "EmailActivation",
        data(){
          return{
            form:{
              token: this.$route.params.token,
              uid: this.$route.params.user_id,
            }
          }
        },
        mounted() {
          axios.post('http://eventrunner.1gb.ru/auth/users/activation/', this.form)
            .then((res) => {
            })
            .catch((error) => {

              this.$buefy.dialog.alert({
                title: 'Error',
                message: 'Что-то пошло не так, обратитесь в поддержку.',
                type: 'is-danger',
                hasIcon: true,
                icon: 'times-circle',
                iconPack: 'fa',
                ariaRole: 'alertdialog',
                ariaModal: true
              })
            })
            .finally(() =>this.$router.push('/user'));
        }

    }
</script>

