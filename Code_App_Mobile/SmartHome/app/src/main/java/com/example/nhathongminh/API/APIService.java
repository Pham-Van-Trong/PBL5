package com.example.nhathongminh.API;

import com.example.nhathongminh.Model.CheckCua;
import com.example.nhathongminh.Model.Response;
import com.example.nhathongminh.Model.ThietBi;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.util.List;

import retrofit2.Call;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.GET;
import retrofit2.http.Query;

public interface APIService {
    Gson gson = new GsonBuilder().setDateFormat("dd-MM-yyyy HH:mm:ss").create();
    APIService apiService = new Retrofit.Builder()
            .baseUrl("https://7ac7-113-185-53-16.ngrok-free.app/")
            .addConverterFactory(GsonConverterFactory.create(gson))
            .build()
            .create(APIService.class);
    @GET("ledpn_off/")
    Call<ThietBi> TatDenPN();
    @GET("ledpn_on/")
    Call<ThietBi> BatDenPN();
    @GET("ledpk_off/")
    Call<ThietBi> TatDenPK();
    @GET("ledpk_on/")
    Call<ThietBi> BatDenPK();
    @GET("door_off/")
    Call<ThietBi> DongCua();
    @GET("door_on/")
    Call<ThietBi> MoCua();
    @GET("items/3/")
    Call<CheckCua> CHECKCUA();
}





