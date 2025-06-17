<template>
  <div>
    <div class="horizontal-menu">
     <nav class="navbar top-navbar p-0" style="border-bottom: 2px solid #0881cc;">
       <div class="container-fluid">
         <div class="text-center navbar-brand-wrapper d-flex align-items-center justify-content-center">
            <NuxtLink class="brand-logo mt-3" to="/" style="color: #0881cc; text-decoration: none;">
             <h4 class="font-20 d-block font-weight-light text-center"><strong>TICKETING WORKS</strong></h4>
             </NuxtLink>
         </div>
         <div class="navbar-menu-wrapper d-flex align-items-center justify-content-end">
         
           <ul class="navbar-nav navbar-nav-right">
              <li class="nav-item nav-profile dropdown">
                <a class="nav-link" id="profileDropdown" href="#" data-toggle="dropdown" aria-expanded="false">
                  <div class="nav-profile-img">
                    <img src="../assets/images/hospital.jpg" alt="image">
                  </div>
                  <div class="nav-profile-text">
                    <p class="text-black font-weight-semibold m-0">User : {{ user }}</p>
                  </div>

                  &nbsp;&nbsp;&nbsp;&nbsp;

                  <button class="btn btn-success" @click="goToMicroServicesDashboard()">Micro-Services</button>

                  &nbsp;&nbsp;

                  <button class="btn btn-danger" @click="logout()"><i class="fa fa-share" aria-hidden="true"></i>&nbsp;Logout</button>
                  
                </a>
              </li>
          </ul>

         </div>
       </div>
     </nav>
   </div>
<Nuxt />
  </div>
</template>

<script>

import axios from 'axios'

export default {
  name: 'LayoutMaster',

  data() {
    return {
      user: this.$store.state.auth_user
    }
  },

  methods: {
      // Go To Micro Services Dashboard
      goToMicroServicesDashboard() {
        const usernameQuery = this.$store.state.auth_user
        const tokenQuery = this.$store.state.auth_token
        const user_id = this.$store.state.user_id

        window.location.assign(this.$store.state.core_ui + "/prepare/welcome?username=" + usernameQuery + "&user_id=" + user_id + "&token=" + tokenQuery , "_blank");
      },

      async logout() {
        //Send Logout Request
        await axios({
            method: 'POST',
            url: this.$store.state.entry_api + '/logout',
            headers: {
                "Content-Type": "application/json",
                "Auth-User": this.$store.state.auth_user,
                "Auth-Token": this.$store.state.auth_token
            }
        }).then((response) => {
            var jsonData = JSON.parse(JSON.stringify(response.data));

            if (jsonData['status'] == true) {
              //Show Notification
              this.$toast.success('You have been Logged Out Successfully');

              //Clear Auth Data
              this.$store.commit('clear_auth_data')
        
              //Go to Core UI
              window.location.assign(this.$store.state.core_ui)
            }else {
              //Show Error on Logout
              this.$toast.error('Failed to Logout. Please Try Again...');
            }
            
        });

      }
  }

}

</script>


<style scoped>

  .container-fluid {
    padding: 10px;
  }

</style>