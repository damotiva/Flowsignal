import sys_config from "/home/sys/config/config.json"
// import sys_config from '/Users/lexardcomputers/Desktop/UHMS/source_code/startup/sys_config/config.json'

var lan_ip = sys_config.lan_ip

var entry_api_port = sys_config.auth_api_port
var core_ui_port = sys_config.auth_front_port

var setup_config_api_port = sys_config.setupandconfig_api_port
var admission_api_port = sys_config.admission_api_port
var revenue_center_api_port = sys_config.revenue_center_api_port
var dhis2reports_api_port = sys_config.dhis2reports_api_port
var sponsor_api_port = sys_config.sponsor_api_port
var doctor_api_port = sys_config.doctor_api_port
var reception_api_port = sys_config.reception_api_port
var ticketing_api_port = sys_config.ticketing_api_port
var ticketing_smart_tv_port = sys_config.ticketing_smart_tv_port
var generalledger_api_port = sys_config.generalledger_api_port
var hr_api_port = sys_config.hr_api_port
var laboratory_api_port = sys_config.laboratory_api_port
var management_api_port = sys_config.management_api_port
var msamaha_api_port = sys_config.msamaha_api_port
var notification_api_port = sys_config.notification_api_port
var nursestation_api_port = sys_config.nursestation_api_port
var opticalunit_api_port = sys_config.opticalunit_api_port
var patientbilling_api_port = sys_config.patientbilling_api_port
var patientrecords_api_port = sys_config.patientrecords_api_port
var pharmacy_api_port = sys_config.pharmacy_api_port
var procedures_api_port = sys_config.procedures_api_port
var procurement_api_port = sys_config.procurement_api_port
var qualityassurance_api_port = sys_config.qualityassurance_api_port
var radiology_api_port = sys_config.radiology_api_port
var rch_api_port = sys_config.rch_api_port
var theater_api_port = sys_config.theater_api_port

export const state = () => ({

    // Private | LAN Installation
    entry_api: lan_ip + ':'+entry_api_port+'/api/v1',
    doctor_api: lan_ip + ':'+doctor_api_port+'/api/v1',
    core_ui: lan_ip + ':' + core_ui_port,
    reception_api: lan_ip + ':'+reception_api_port+'/api/v1',
    setup_config_api: lan_ip + ':'+setup_config_api_port+'/api/v1',
    hr_api: ':'+hr_api_port+'/api/v1',
    sponsor_api: lan_ip + ':'+sponsor_api_port+'/api/v1',
    general_ledger_api: ':'+generalledger_api_port+'/api/v1',
    admission_api : lan_ip + ':'+admission_api_port+'/api/v1',
    dhis2reports_api: lan_ip + ':'+dhis2reports_api_port+'/api/v1',
    revenue_center_api: lan_ip + ':'+revenue_center_api_port+'/api/v1',
    ticketing_api: lan_ip + ':'+ticketing_api_port+'/api/v1',
    ticketing_smart_tv: lan_ip + ':' + ticketing_smart_tv_port,
    laboratory_api: lan_ip + ':'+laboratory_api_port+'/api/v1',
    management_api : lan_ip + ':'+management_api_port+'/api/v1', 
    msamaha_api : lan_ip + ':'+msamaha_api_port+'/api/v1',
    notification_api: lan_ip + ':'+notification_api_port+'/api/v1',
    nurse_station_api: lan_ip + ':'+nursestation_api_port+'/api/v1',
    opticalunit_api: lan_ip + ':'+opticalunit_api_port+'/api/v1',
    patient_billing_api : lan_ip + ':'+patientbilling_api_port+'/api/v1',
    patients_records_api: lan_ip + ':'+patientrecords_api_port+'/api/v1',
    pharmacy_api: lan_ip + ':'+pharmacy_api_port+'/api/v1',
    procedures_api: lan_ip + ':'+procedures_api_port+'/api/v1',
    procurement_api: lan_ip + ':'+procurement_api_port+'/api/v1',
    quality_assurance_api: lan_ip + ':'+qualityassurance_api_port+'/api/v1',
    radiology_api: lan_ip + ':'+radiology_api_port+'/api/v1',
    rch_api: lan_ip + ':'+rch_api_port+'/api/v1',
    theater_api: lan_ip + ':'+theater_api_port+'/api/v1',

    auth_user: '',
    user_id: '',
    auth_token: '',
    is_authenticated: false,

})

export const mutations = {
   
    //Store Auth Data
    store_auth_data(state, auth_data) {
        state.auth_user = auth_data.auth_user
        state.user_id = auth_data.user_id
        state.auth_token = auth_data.auth_token
        state.is_authenticated = true 
    }, 
    
    //Clear Auth Data
    clear_auth_data(state) {
        state.auth_user = ''
        state.user_id = ''
        state.auth_token = ''
        state.is_authenticated = false
    },

}
