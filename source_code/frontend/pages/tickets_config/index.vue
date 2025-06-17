<template lang="html">
    <div class="container">
        
        <h4>Ticketing Works Main Config</h4>
        <br/><hr/>

        <form>
            <table>
                <tr>
                    <td>Reception Smart TV IP</td>
                    <td><input type="text" class="form-control"/></td>
                </tr>

                <tr>
                    <td></td>
                </tr>

                <tr>
                    <td></td>
                    <td>
                        <button class="btn btn-primary form-control">Update Config</button>
                    </td>
                </tr>
            </table>
        </form>
    </div>

</template>


<script>

import axios from 'axios'

export default {
    name: 'TicketsConfig',
    layout: 'master',

    data () {
        return {
            
        }
    }

}

</script>