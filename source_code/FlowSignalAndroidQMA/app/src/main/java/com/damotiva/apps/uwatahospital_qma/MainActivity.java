package com.damotiva.apps.uwatahospital_qma;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.media.AudioManager;
import android.net.Uri;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.util.Log;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.VideoView;

import com.damotiva.apps.uwatahospital_qma.utils.CoolMethodat;
import com.damotiva.apps.uwatahospital_qma.utils.ExtractPostParam;
import com.damotiva.apps.uwatahospital_qma.utils.HttpServerThread;
import com.damotiva.apps.uwatahospital_qma.utils.TicketCodeExtractor;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.UnknownHostException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class MainActivity extends AppCompatActivity {

    private CoolMethodat coolMethodat;

    private ExtractPostParam extractPostParam;

    private View ticketLeftBorderView;
    private RelativeLayout ticketRelativeLayout;

    private TextView ticketTitleTextView;
    private TextView ticketCodeTextView;
    private TextView ticketGoTitleTextView;
    private TextView ticketLocationTextView;

    private TextView welcomeTextview;
    private TextView welcomeDayDateTextView;

    private VideoView videoPlayeVideoView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Remove the title bar
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
        getWindow().setFlags(
                WindowManager.LayoutParams.FLAG_FULLSCREEN,
                WindowManager.LayoutParams.FLAG_FULLSCREEN);

        setContentView(R.layout.activity_main);

        //Casting Views
        ticketLeftBorderView = (View) findViewById(R.id.ticketLeftBorderView);
        ticketRelativeLayout = (RelativeLayout) findViewById(R.id.ticketRelativeLayout);

        ticketTitleTextView = (TextView) findViewById(R.id.ticketTitleTextView);
        ticketCodeTextView = (TextView) findViewById(R.id.ticketCodeTextView);
        ticketGoTitleTextView = (TextView) findViewById(R.id.ticketGoTitleTextView);
        ticketLocationTextView = (TextView) findViewById(R.id.ticketLocationTextView);

        welcomeTextview = (TextView) findViewById(R.id.welcomeTextview);
        welcomeDayDateTextView = (TextView) findViewById(R.id.welcomeDayDateTextView);

        videoPlayeVideoView = (VideoView) findViewById(R.id.videoPlayeVideoView);

        //String videoUrl = "http://192.168.1.102/videos/victoria.mp4";
        //Uri uri = Uri.parse(videoUrl);

        extractPostParam = new ExtractPostParam();

        String uriPath = "android.resource://"+getPackageName()+"/"+R.raw.victoria;
        Uri uri = Uri.parse(uriPath);
        videoPlayeVideoView.setVideoURI(uri);
        videoPlayeVideoView.start();

        Calendar calendar = Calendar.getInstance();

        // Set the year, month, and day of month
        calendar.get(Calendar.YEAR);
        calendar.get(Calendar.MONTH);
        calendar.get(Calendar.DAY_OF_MONTH);


        Date date = new Date();
        SimpleDateFormat sdfDayName = new SimpleDateFormat("EEEE");
        String dayName = sdfDayName.format(date);

        System.out.println(dayName);

        // Get the date and time in the desired format
        SimpleDateFormat sdf = new SimpleDateFormat("dd MMMM yyyy");
        String dateTime = sdf.format(calendar.getTime());

        //Initial Views Values
        ticketCodeTextView.setText("--");
        ticketLocationTextView.setText("--");
        welcomeDayDateTextView.setText(dayName + " - " + dateTime);

        //Initiate Cool Methodat
        coolMethodat = new CoolMethodat();
        //ticketCodeTextView.setText(coolMethodat.getIpAddress());
        Log.d("MATAGA", coolMethodat.getIpAddress());

        HttpServer server = null;
        try {
            server = HttpServer.create(new InetSocketAddress(8080), 0);
        } catch (IOException e) {
            Log.d("MATAGA", "Exception : " + e.getMessage());
            e.printStackTrace();
        }

        server.createContext("/requests", new MyHandler());
        server.setExecutor(null); // creates a default executor
        server.start();

    }


    class MyHandler implements HttpHandler {
        public void handle(HttpExchange t) throws IOException {

            String ticketId = "";
            String ticketCode = "";
            String ticketLocation = "";

            //Add Cors
            t.getResponseHeaders().add("Access-Control-Allow-Origin", "*");

            if (t.getRequestMethod().equalsIgnoreCase("OPTIONS")) {
                t.getResponseHeaders().add("Access-Control-Allow-Methods", "GET, OPTIONS");
                t.getResponseHeaders().add("Access-Control-Allow-Headers", "Content-Type,Authorization");
                t.sendResponseHeaders(204, -1);
                return;
            }

            //Receive the line from the POST
            InputStream in = t.getRequestBody();

            String line;
            StringBuilder postData = new StringBuilder();
            BufferedReader br = new BufferedReader(new InputStreamReader(in));

            while ((line = br.readLine()) != null) {
                postData.append(line);
            }

            ticketId = TicketCodeExtractor.extractKey(postData.toString(), "ticketId");
            ticketCode = TicketCodeExtractor.extractKey(postData.toString(), "ticketCode");
            ticketLocation = TicketCodeExtractor.extractKey(postData.toString(), "ticketLocation");

            //ticketId = extractPostParam.extractParam(postData.toString(), "ticketId");
            //ticketCode = extractPostParam.extractParam(postData.toString(), "ticketCode");
            //ticketLocation = extractPostParam.extractParam(postData.toString(), "ticketLocation");

            String finalTicketCode = ticketCode;
            String finalTicketLocation = ticketLocation;

            //Set Data on Screen for 60 Seconds
            ticketCodeTextView.setText(finalTicketCode);
            ticketLocationTextView.setText(finalTicketLocation);

            in.close();

            //acknowledge the post request
            String response = "Ack  -  " + postData.toString();
            t.sendResponseHeaders(200, response.length());
            OutputStream os = t.getResponseBody();
            os.write(response.getBytes());
            os.close();

        }
    }

}