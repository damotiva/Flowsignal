package com.damotiva.apps.flowsignal;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.view.Window;
import android.view.WindowManager;
import android.widget.TextView;

import com.damotiva.apps.flowsignal.utils.CoolMethodat;

public class SplashScreenActivity extends AppCompatActivity {

    private static final int SPLASH_DURATION = 5000; // 7 seconds in milliseconds
    private CoolMethodat coolMethodat;
    private TextView ipAddrListenTextView;
    private final Handler handler = new Handler();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Make fullscreen
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                WindowManager.LayoutParams.FLAG_FULLSCREEN);

        setContentView(R.layout.activity_splash_screen);

        // Initialize views
        coolMethodat = new CoolMethodat();
        ipAddrListenTextView = findViewById(R.id.ipAddrListenTextView);
        ipAddrListenTextView.setText(coolMethodat.getIpAddress());

        // Schedule transition after 7 seconds
        handler.postDelayed(() -> {
            startMainActivity();
        }, SPLASH_DURATION);
    }

    private void startMainActivity() {
        Intent intent = new Intent(SplashScreenActivity.this, MainActivity.class);
        startActivity(intent);
        finish(); // Close splash activity so user can't go back to it
    }

    @Override
    protected void onDestroy() {
        // Remove any pending callbacks when activity is destroyed
        handler.removeCallbacksAndMessages(null);
        super.onDestroy();
    }
}