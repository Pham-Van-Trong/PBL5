package com.example.nhathongminh;

import androidx.appcompat.app.AppCompatActivity;
import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;
import com.google.firebase.FirebaseApp;

public class MainActivity extends AppCompatActivity {
    TextView txtTaiKhoan;
    TextView txtMatKhau;
    Button btnDangNhap;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        FirebaseApp.initializeApp(this);

        txtTaiKhoan = (TextView) findViewById(R.id.txtTaiKhoan);
        txtMatKhau = (TextView) findViewById(R.id.txtMatKhau);
        btnDangNhap = (Button) findViewById(R.id.btnDangNhap);

        btnDangNhap.setOnClickListener(new View.OnClickListener() {
        @Override
        public void onClick(View view) {
//            Intent intent = new Intent(MainActivity.this,MainActivity2.class);
//            startActivity(intent);
            if (txtTaiKhoan.getText().length() == 0 && txtMatKhau.getText().length() == 0)
                Toast.makeText(MainActivity.this,"Vui lòng nhập Tài khoản và Mật khẩu",Toast.LENGTH_SHORT).show();
            else {
                if (txtTaiKhoan.getText().toString().equals("admin")  && txtMatKhau.getText().toString().equals("123") ) {
                    Toast.makeText(MainActivity.this,"Đăng nhập thành công!",Toast.LENGTH_SHORT).show();
                    Intent intent = new Intent(MainActivity.this,MainActivity2.class);
                    startActivity(intent);
                }
                else
                Toast.makeText(MainActivity.this,"Tài khoản hoặc Mật khẩu chưa đúng",Toast.LENGTH_SHORT).show();
            }
        }
        });
    }

}



