package com.damotiva.apps.uwatahospital_qma;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.Window;
import android.view.WindowManager;
import android.widget.TextView;

import com.damotiva.apps.uwatahospital_qma.utils.CoolMethodat;

public class SplashScreenActivity extends AppCompatActivity {

    private Thread delayThread;
    private CoolMethodat coolMethodat;
    private TextView ipAddrListenTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // Remove the title bar
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN, WindowManager.LayoutParams.FLAG_FULLSCREEN);

        setContentView(R.layout.activity_splash_screen);

        //Inits
        coolMethodat = new CoolMethodat();

        //Casting Views
        ipAddrListenTextView = (TextView) findViewById(R.id.ipAddrListenTextView);
        ipAddrListenTextView.setText(coolMethodat.getIpAddress());

        //Delay Thread
        delayThread = new Thread() {
            @Override
            public synchronized void start() {
                try {
                    //Sleep for Three Seconds
                    sleep(3000);

                }catch (InterruptedException exc) {
                    //Catch Error with Sentry
                    exc.printStackTrace();
                }finally {
                    Intent mainActivityIntent = new Intent(getBaseContext(), MainActivity.class);
                    startActivity(mainActivityIntent);
                }
            }
        };

        //Start Delay Thread
        delayThread.start();
    }
}