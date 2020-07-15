<template>
  <div id="app">
    <header>
      <h1>Webex widget demo</h1>
    </header>
    <main>
      <v-form v-model="valid" ref="form">
        <v-container>
          <v-row>
            <v-col
              cols="12"
              md="4"
            >
              <v-text-field
                v-model="webex_name"
                :rules="nameRules"
                :counter="10"
                label="Name"
                required
              ></v-text-field>
            </v-col>

            <v-col
              cols="12"
              md="4"
            >
              <v-text-field
                v-model="subject"
                :rules="nameRules"
                :counter="10"
                label="Theme"
                required
              ></v-text-field>
            </v-col>

            <v-col
              cols="12"
              md="4"
            >
              <v-text-field
                v-model="email"
                :rules="emailRules"
                label="Email/SIP"

              ></v-text-field>
            </v-col>
            <v-btn
              @click="createWidget"
              :disabled="!fieldIsEmpty || !valid"
              v-if="!progress">
              Connect
            </v-btn>
            <div></div>
            <v-btn
              @click="openWidget"
              :disabled="!fieldIsEmpty || !valid"
              v-if="!progress">
              Call
            </v-btn>


          </v-row>
        </v-container>
      </v-form>
    <div id="my-space-widget" style="width: 500px; height: 500px;" align="right"/>
    </main>
  </div>
</template>

<script>

  const axios = require('axios')


  export default {
    data() {
      return {
        // the block where we initialize the variables for further reassignment in functions
        jwtToken: null,
        email: '',
        subject: '',
        webex_name: '',
        nameRules: [
          v => !!v || 'Login is required',
          v => v.length <= 10 || 'Name must be less than 10 characters',
        ],
        emailRules: [
          v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid'
        ],
        progress: false
      }
    },
    // the computed property where the variable 'fieldIsEmpty' can take on the value of 'true' or 'false',
    // depending on whether the fields are filled or unfilled, respectively
    computed: {
      fieldIsEmpty: function () {
        return !!(this.webex_name && this.subject)
      },
    },
    created() {

    },
    methods: {

      getJWTtoken (ticketDuration) {

      },

      // when users clicked on the 'call' or 'connect' button functions below will be called

      createWidget() {

        async function main(subject, webex_name, email) {
        try {
          console.log("subject ", subject)
          const response = await axios.post('http://localhost:5000/', {"subject": subject, "name": webex_name,"tokenTime": "2"})
          console.log(response.data)
          var widgetEl = document.getElementById('my-space-widget');
        // Init a new widget
          webex.widget(widgetEl).spaceWidget({
            guestToken: response.data,
            destinationType: 'email',
            destinationId: email
          });
        }
        catch (error) {
          console.log(error)
          }

        }
        main(this.subject, this.webex_name, this.email)
      },

      openWidget() {

        async function main(subject, webex_name, email) {
        try {
          console.log("subject ", subject)
          const response = await axios.post('http://localhost:5000/', {"subject": subject, "name": webex_name,"tokenTime": "2"})
          console.log(response.data)
          var widgetEl = document.getElementById('my-space-widget');
        // Init a new widget
          webex.widget(widgetEl).spaceWidget({
            guestToken: response.data,
            destinationType: 'email',
            destinationId: email
          });
        }
        catch (error) {
          console.log(error)
          }

        }
        main(this.subject, this.webex_name, this.email)
      },

      // You can use sip addresses below for testing (automatically enabled a call):
      // 111@bjn.vc, fireplace@ivr.vc, goldfish@selfie.vc, halloween@ivr.vc, havnen@expressway.dk

    }
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }

  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }

  .mx-auto {
    margin-left: 170px;
    margin-buttom: 100px;
  }
</style>
