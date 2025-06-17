<template>
  <div class="back_photo">
    <div class="container-scroller">
      <div class="col-7 offset-5">
        <br/>
        <div class="row">
          
            <div class="col-4">
              <div class="card">
                <NuxtLink to="/processed_tickets">
                    <div class="card-body">
                        <div class="text-center hospital-features ticket-dash-block">
                            <i class="mdi mdi-ticket icon-md text-success"></i>
                            <h5 class="font-weight">Processed Tickets</h5>
                        </div>
                    </div>
                </NuxtLink>
              </div>
            </div>
       
            <div class="col-4">
              <div class="card">
                <NuxtLink to="/tickets_config">
                    <div class="card-body">
                        <div class="text-center hospital-features ticket-dash-block">
                            <i class="mdi mdi-cogs icon-md text-success"></i>
                            <h5 class="font-weight">Tickets Config</h5>
                        </div>
                    </div>
                </NuxtLink>
              </div>
            </div>

            <div class="col-4">
              <div class="card">
                <NuxtLink to="/tickets_reports">
                    <div class="card-body">
                        <div class="text-center hospital-features ticket-dash-block">
                            <i class="mdi mdi-chart-line icon-md text-success"></i>
                            <h5 class="font-weight">Tickets Reports</h5>
                        </div>
                    </div>
                </NuxtLink>
              </div>
            </div>
         

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TicketingIndex',
  layout: 'master',


}
</script>

<style scoped>
    .back_photo {
      background: url("../assets/images/hospital.jpg");
      background-size: 100%;
      width: 100%;
      height: 700px;
    }
    .logout-fav {
      color: red;
      margin-left: 10px;
      font-size: 20px;
    }

    .ticket-dash-block i {
        font-size: 50px;
    }

</style>