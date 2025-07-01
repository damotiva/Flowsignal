package com.damotiva.apps.flowsignal.utils;


import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class TicketCodeExtractor {

    public static String extractKey(String input, String keyTitle) {

        String keyValue = "";

        //String pattern = "name=\""+keyTitle+"\"(.*?)----------------------------";
        String pattern = "name=\""+keyTitle+"\"(.*?)------";

        // Creating a Pattern object
        Pattern regex = Pattern.compile(pattern, Pattern.DOTALL);

        // Matching the pattern on the input string
        Matcher matcher = regex.matcher(input);

        // Extracting the value if a match is found
        // Finding the ticket code value
        if (matcher.find()) {
            keyValue = matcher.group(1).trim();
        } else {
            keyValue = "404";
        }

        return keyValue;
    }
}