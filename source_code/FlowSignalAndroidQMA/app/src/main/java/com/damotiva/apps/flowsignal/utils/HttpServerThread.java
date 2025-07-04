package com.damotiva.apps.flowsignal.utils;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class HttpServerThread extends Thread {

    private ServerSocket httpServerSocket;
    private     String gets = "";

    static final int HttpServerPORT = 8888;

    @Override
    public void run() {
        Socket socket = null;

        try {
            httpServerSocket = new ServerSocket(HttpServerPORT);

            while(true){
                socket = httpServerSocket.accept();

                HttpResponseThread httpResponseThread = new HttpResponseThread(socket, "RCV_QMA");
                httpResponseThread.start();

            }
    } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

    }


}