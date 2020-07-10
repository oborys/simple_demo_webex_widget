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
            <!--<v-btn-->
              <!--@click="close"-->
              <!--:disabled="!connection"-->
              <!--v-if="!progress">-->
              <!--Close connection-->
            <!--</v-btn>-->

          </v-row>
        </v-container>
      </v-form>
    <div id="my-space-widget" style="width: 500px; height: 500px;" align="right"/>
    </main>
  </div>
</template>

<script>


  //const jsxapi = require('jsxapi');
  const jwt = require('jsonwebtoken');
  //const request = require('request-promise-native');

  export default {
    data() {
      return {
        // the block where we initialize the variables for further reassignment in functions
        WEBEX_TEAMS_ISSUER_ID: 'Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi80N2MxYjAwYi1jYTg4LTQzNzEtYTdhOS1hNmE4ODliOGE0MzM',
        WEBEX_TEAMS_ISSUER_SECRET: 'emmCcE8yO+Kf6GnXPFlnGh762ArNFFrofFDaqcQjPYk=',
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
      // when users clicked on the 'submit' button function below will be called
      submit() {
        this.initConnection();
      },

      // New style API
      setname() {
        if (this.wsconnection) {
          this.wsconnection.Config.SystemUnit.Name.set(this.newSystemName);
          // xConfiguration SystemUnit Name: "Kit 006"
        }
      },
      getJWTtoken (ticketDuration) {
        // ticketDuration in hours
      const expiration = Math.floor(new Date() / 1000) + 3600 * ticketDuration
      // Create a JWT payload object
      // 'sub' (subject) will be used to create the Webex Teams user email (sub@org-uuid)
      // 'name' will be the user's display name
      const payload = {
      'sub': this.subject,
      'name': this.webex_name,
      'iss': this.WEBEX_TEAMS_ISSUER_ID,
      'exp': expiration
        };

      // Create a base64 encoded buffer from the Guest Issuer shared secret
      const encoded = Buffer.from(this.WEBEX_TEAMS_ISSUER_SECRET, 'base64');

      // Sign the JWT object using the encoded secret
      this.jwtToken = jwt.sign(payload, encoded, { algorithm: 'HS256', noTimestamp: true });

      console.log(this.jwtToken);
      },
      createWidget() {
        if (this.jwtToken === null) {
          this.getJWTtoken(1)
        }


      var widgetEl = document.getElementById('my-space-widget');
        // Init a new widget
        webex.widget(widgetEl).spaceWidget({
          guestToken: this.jwtToken,
          destinationType: 'email',
          destinationId: this.email
        });

      },
      openWidget() {
        if (this.jwtToken === null) {
          this.getJWTtoken(1)
        }
        var widgetEl = document.getElementById('my-space-widget');
        // Init a new widget
        webex.widget(widgetEl).spaceWidget({
          guestToken: this.jwtToken,
          destinationType: 'email',
          destinationId: this.email,
          startCall: true
        });
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
