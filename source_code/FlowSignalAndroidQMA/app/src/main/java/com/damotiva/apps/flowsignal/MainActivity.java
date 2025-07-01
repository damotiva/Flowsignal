package com.damotiva.apps.flowsignal;

import androidx.appcompat.app.AppCompatActivity;

import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.VideoView;
import android.widget.MediaController;
import android.media.MediaPlayer;

import com.damotiva.apps.flowsignal.utils.CoolMethodat;
import com.damotiva.apps.flowsignal.utils.ExtractPostParam;
import com.damotiva.apps.flowsignal.utils.TicketCodeExtractor;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.InetSocketAddress;
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

        // Initialize views
        initializeViews();

        // Setup date display
        setupDateDisplay();

        // Initialize video player
        setupVideoPlayer();

        // Start HTTP server
        startHttpServer();
    }

    private void initializeViews() {
        ticketLeftBorderView = findViewById(R.id.ticketLeftBorderView);
        ticketRelativeLayout = findViewById(R.id.ticketRelativeLayout);
        ticketTitleTextView = findViewById(R.id.ticketTitleTextView);
        ticketCodeTextView = findViewById(R.id.ticketCodeTextView);
        ticketGoTitleTextView = findViewById(R.id.ticketGoTitleTextView);
        ticketLocationTextView = findViewById(R.id.ticketLocationTextView);
        welcomeTextview = findViewById(R.id.welcomeTextview);
        welcomeDayDateTextView = findViewById(R.id.welcomeDayDateTextView);
        videoPlayeVideoView = findViewById(R.id.videoPlayeVideoView);
    }

    private void setupDateDisplay() {
        Date date = new Date();
        SimpleDateFormat sdfDayName = new SimpleDateFormat("EEEE");
        String dayName = sdfDayName.format(date);

        SimpleDateFormat sdf = new SimpleDateFormat("dd MMMM yyyy");
        String dateTime = sdf.format(Calendar.getInstance().getTime());

        ticketCodeTextView.setText("--");
        ticketLocationTextView.setText("--");
        welcomeDayDateTextView.setText(dayName + " - " + dateTime);
    }

    private void setupVideoPlayer() {
        boolean useLiveStream = false;

        if (useLiveStream) {
            // Play M3U8 stream
            String m3u8Url = "https://live.mediacdn.ru/sr1/arhis24/playlist_hdhigh.m3u8";
            setupStreamingVideo(m3u8Url);
        } else {
            setupLocalVideo();
        }
    }

    private void setupLocalVideo() {
        String uriPath = "android.resource://" + getPackageName() + "/" + R.raw.demo_flowsignal;
        Uri uri = Uri.parse(uriPath);
        videoPlayeVideoView.setVideoURI(uri);

        videoPlayeVideoView.setOnPreparedListener(mp -> {
            mp.setLooping(true); // Enable looping
            mp.start();
        });

        videoPlayeVideoView.setOnErrorListener((mp, what, extra) -> {
            Log.e("VideoError", "Error code: " + what + " extra: " + extra);
            return true;
        });
    }

    private void setupStreamingVideo(String streamUrl) {
        Uri uri = Uri.parse(streamUrl);
        videoPlayeVideoView.setVideoURI(uri);

        // For streaming, we typically don't loop
        videoPlayeVideoView.setOnPreparedListener(MediaPlayer::start);

        videoPlayeVideoView.setOnErrorListener((mp, what, extra) -> {
            Log.e("StreamError", "Error code: " + what + " extra: " + extra);
            // Fallback to local video if stream fails
            setupLocalVideo();
            return true;
        });
    }

    private void startHttpServer() {
        coolMethodat = new CoolMethodat();
        Log.d("MATAGA", coolMethodat.getIpAddress());

        try {
            HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);
            server.createContext("/requests", new MyHandler());
            server.setExecutor(null);
            server.start();
        } catch (IOException e) {
            Log.e("HTTPServer", "Failed to start server: " + e.getMessage());
        }
    }

    class MyHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange t) throws IOException {
            // ... (keep your existing handler implementation)
        }
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (!videoPlayeVideoView.isPlaying()) {
            videoPlayeVideoView.start();
        }
    }

    @Override
    protected void onPause() {
        super.onPause();
        videoPlayeVideoView.pause();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        videoPlayeVideoView.stopPlayback();
    }
}