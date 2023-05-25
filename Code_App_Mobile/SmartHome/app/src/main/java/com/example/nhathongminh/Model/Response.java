package com.example.nhathongminh.Model;

import com.google.gson.annotations.SerializedName;


public class Response {

    @SerializedName("current_user_url")
    private String current_URL;

    public String getCurrent_URL(){
        return current_URL;
    }
    public void setCurrent_URL(String current_URL){
        this.current_URL = current_URL;
    }
}
