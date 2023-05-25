package com.example.nhathongminh;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.Toast;

import com.example.nhathongminh.API.APIService;
import com.example.nhathongminh.Model.CheckCua;
import com.example.nhathongminh.Model.Response;
import com.example.nhathongminh.Model.ThietBi;

import retrofit2.Call;
import retrofit2.Callback;

public class MainActivity2 extends AppCompatActivity {
    ImageView DenPhongNgu;
    ImageView DenPhongNguBat;
    ImageView DenPhongKhach;
    ImageView DenPhongKhachBat;
    ImageView DongCua;
    ImageView MoCua;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        DenPhongNgu = (ImageView) findViewById(R.id.DenPhongNgu);
        DenPhongNguBat = (ImageView) findViewById(R.id.DenPhongNguBat);
        DenPhongKhach = (ImageView) findViewById(R.id.DenPhongKhach);
        DenPhongKhachBat = (ImageView) findViewById(R.id.DenPhongKhachBat);
        DongCua = (ImageView) findViewById(R.id.CuaDong);
        MoCua = (ImageView) findViewById(R.id.CuaMo);

        APIService.apiService.CHECKCUA().enqueue(new Callback<CheckCua>() {
            @Override
            public void onResponse(Call<CheckCua> call, retrofit2.Response<CheckCua> response) {
                CheckCua checkCua = response.body();
                boolean Check = checkCua.getstatus();
                if(Check)
                {
                    MoCua.setVisibility(View.VISIBLE);
                    DongCua.setVisibility(View.INVISIBLE);
                }
                else {
                    MoCua.setVisibility(View.INVISIBLE);
                    DongCua.setVisibility(View.VISIBLE);
                }
            }
            @Override
            public void onFailure(Call<CheckCua> call, Throwable t) {
                Toast.makeText(MainActivity2.this,"Loi",Toast.LENGTH_SHORT).show();
            }
        });

        DenPhongNgu.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                BatDenPN();
            }
        });
        DenPhongNguBat.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                TatDenPN();
            }
        });
        DenPhongKhach.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                BatDenPK();
            }
        });
        DenPhongKhachBat.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                TatDenPK();
            }
        });
        DongCua.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                MoCua();
            }
        });
        MoCua.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                DongCua();
            }
        });
    }
    private void BatDenPN() {
        APIService.apiService.BatDenPN().enqueue(new Callback<ThietBi>() {
            retrofit2.Response<ThietBi> ChuoiAPI ;
            @Override
            public void onResponse(Call<ThietBi> call, retrofit2.Response<ThietBi> response) {
                ThietBi batdenPN = response.body();
                String Mess = batdenPN.getMess();
                if(Mess.equals("PN ON")){
                    Toast.makeText(MainActivity2.this,"Bật đèn phòng ngủ thành công!",Toast.LENGTH_SHORT).show();
                    DenPhongNguBat.setVisibility(View.VISIBLE);
                    DenPhongNgu.setVisibility(View.INVISIBLE);}
            }
            @Override
            public void onFailure(Call<ThietBi> call, Throwable t) {
            }
        });
    }

    private void TatDenPN() {
        APIService.apiService.TatDenPN().enqueue(new Callback<ThietBi>() {
            @Override
            public void onResponse(Call<ThietBi> call, retrofit2.Response<ThietBi> response) {
                ThietBi tatdenPN = response.body();
                String Mess = tatdenPN.getMess();
                if(Mess.equals("PN OFF")) {
                    Toast.makeText(MainActivity2.this, "Tắt đèn phòng ngủ thành công!", Toast.LENGTH_SHORT).show();
                    DenPhongNguBat.setVisibility(View.INVISIBLE);
                    DenPhongNgu.setVisibility(View.VISIBLE);
                }
            }
            @Override
            public void onFailure(Call<ThietBi> call, Throwable t) {}
        });
    }
    private void BatDenPK() {
        APIService.apiService.BatDenPK().enqueue(new Callback<ThietBi>() {
            @Override
            public void onResponse(Call<ThietBi> call, retrofit2.Response<ThietBi> response) {
                ThietBi batdenPK = response.body();
                String Mess = batdenPK.getMess();
                if(Mess.equals("PK ON")) {
                    Toast.makeText(MainActivity2.this, "Bật đèn phòng khách thành công!", Toast.LENGTH_SHORT).show();
                    DenPhongKhachBat.setVisibility(View.VISIBLE);
                    DenPhongKhach.setVisibility(View.INVISIBLE);
                }
            }
            @Override
            public void onFailure(Call<ThietBi> call, Throwable t) {}
        });
    }
    private void TatDenPK() {
        APIService.apiService.TatDenPK().enqueue(new Callback<ThietBi>() {
            @Override
            public void onResponse(Call<ThietBi> call, retrofit2.Response<ThietBi> response) {
                ThietBi tatdenPK = response.body();
                String Mess = tatdenPK.getMess();
                if(Mess.equals("PK OFF")) {
                    Toast.makeText(MainActivity2.this, "Tắt đèn phòng khách thành công!", Toast.LENGTH_SHORT).show();
                    DenPhongKhachBat.setVisibility(View.INVISIBLE);
                    DenPhongKhach.setVisibility(View.VISIBLE);
                }
            }
            @Override
            public void onFailure(Call<ThietBi> call, Throwable t) {}
        });
    }
    private void MoCua() {
        APIService.apiService.MoCua().enqueue(new Callback<ThietBi>() {
            @Override
            public void onResponse(Call<ThietBi> call, retrofit2.Response<ThietBi> response) {
                ThietBi mocua = response.body();
                String Mess = mocua.getMess();
                if(Mess.equals("DOOR ON")) {
                    Toast.makeText(MainActivity2.this, "Mở cửa thành công!", Toast.LENGTH_SHORT).show();
                    MoCua.setVisibility(View.VISIBLE);
                    DongCua.setVisibility(View.INVISIBLE);
                }
            }
            @Override
            public void onFailure(Call<ThietBi> call, Throwable t) {}
        });
    }
    private void DongCua() {
        APIService.apiService.DongCua().enqueue(new Callback<ThietBi>() {
            @Override
            public void onResponse(Call<ThietBi> call, retrofit2.Response<ThietBi> response) {
                ThietBi dongcua = response.body();
                String Mess = dongcua.getMess();
                if(Mess.equals("DOOR OFF")) {
                    Toast.makeText(MainActivity2.this, "Đóng cửa thành công!", Toast.LENGTH_SHORT).show();
                    MoCua.setVisibility(View.INVISIBLE);
                    DongCua.setVisibility(View.VISIBLE);
                }
            }
            @Override
            public void onFailure(Call<ThietBi> call, Throwable t) {}
        });
    }
}





