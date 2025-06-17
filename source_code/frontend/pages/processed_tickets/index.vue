<template lang="html">
    <div class="container-fluid">
        
        <br/>
        <h3>Processed Tickets ({{ tickets.length }})</h3>
        <br/><hr/>
        <table class="table table-bordered table-hover align-middle mb-0">
            <thead>
                <tr>
                    <td>S/N</td>
                    <td>Patient Name</td>
                    <td>Patient ID</td>
                    <td>Checkin ID</td>
                    <td>Ticket Code</td>
                    <td>Created</td>
                </tr>
            </thead>

            <tbody>
                <tr v-for="(ticket, id) in tickets" :key="ticket.id">
                    <td>{{ id += 1 }}</td>
                    <td>{{ ticket.patient_name }}</td>
                    <td>{{ ticket.patient_id }}</td>
                    <td>{{ ticket.checkin_id }}</td>
                    <td>{{ ticket.ticket_code }}</td>
                    <td></td>
                </tr>
            </tbody>
        </table>

   

    </div>

</template>


<script>

import axios from 'axios'

export default {
    name: 'ProcessedTickets',
    layout: 'master',

    data () {
        return {
            'tickets': []
        }
    },

    methods: {
        
        //Pull Todat Generated Tickets
        async pullTodayTickets() {
            await axios({
              method: 'GET',
              url: this.$store.state.ticketing_api + '/ticket/read_all/tickets',
              headers: {
                  "Content-Type": "application/json",
                  "Auth-User": this.$store.state.auth_user,
                  "Auth-Token": this.$store.state.auth_token,
                  "Authorization":  "Token " + this.$store.state.auth_token
              }
          }).then((response) => {
              var jsonData = JSON.parse(JSON.stringify(response.data));

              this.tickets = jsonData['tickets_data']
             
          });
        } 

    },

    created() {
        //Pull All Tickets
        this.pullTodayTickets()
    }

}

</script>