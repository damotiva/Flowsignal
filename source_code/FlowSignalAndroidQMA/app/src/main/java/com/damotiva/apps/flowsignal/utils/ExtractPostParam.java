package com.damotiva.apps.flowsignal.utils;

import java.util.HashMap;
import java.util.Map;

public class ExtractPostParam {

    public Map<String, String> extractPostQuery(String postQuery) {
        Map<String, String> queryParams = new HashMap<>();
        String[] queryPairs = postQuery.split("&");
        for (String queryPair : queryPairs) {
            String[] keyValue = queryPair.split("=");
            queryParams.put(keyValue[0], keyValue[1]);
        }
        return queryParams;
    }

    public String extractParam(String postQuery, String keyRequired) {
        Map<String, String> queryParams = extractPostQuery(postQuery);

        String keyValue = queryParams.get(keyRequired);

        return keyValue;
    }
}