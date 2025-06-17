<template>

	<div></div>

</template>


<script>

import axios from 'axios'

export default {
  name: 'Noch',
  methods: {

		//Validate Token from The API
		async validate_token(auth_user, user_id, auth_token) {
			
			//Verify Auth Username and Auth Token
			await axios({
				method: 'POST',
				url: this.$store.state.entry_api + "/verify/auth/token",
				headers: {
					"Content-Type": "application/json",
					"Auth-User": auth_user,
					"Auth-Token": auth_token
				}
			}).then( (response) => {
				var jsonData = JSON.parse(JSON.stringify(response.data))

				if (jsonData['status'] == true) {
					//Set Auth Data
					this.$store.commit('store_auth_data', { 
						auth_user : auth_user, 
						user_id: user_id, 
						auth_token : auth_token 
					})
					
					// Redirect to Index of Micro Service
					this.$router.push('/')
				}else {
					//Clear Auth Data
					this.$store.commit('clear_auth_data')

					//Redirect to /noch
					this.$router.push('/noch')
				}
			});
		}

  },

  created() {
	//If Auth Correct go to Index Page
	var auth_user = this.$route.query['auth_user']
	var auth_token = this.$route.query['auth_token']
	var user_id = this.$route.query['user_id']

	//Check for undefined in username and token
	if (auth_user == undefined) { auth_user = "" }
	if (auth_token == undefined) { auth_token = "" }
	if (user_id == undefined) { user_id = "" }


	if (auth_user !== "" && auth_token !== "") {
		
		this.validate_token(auth_user, user_id, auth_token)
		
	}
	
  }
}

</script>