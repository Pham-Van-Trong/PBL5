package com.example.nhathongminh.Model;

public class ThietBi {
    private int id;
    private String name;
    private boolean status;
    private String Mess;

    public String getMess() {
        return Mess;
    }

    public void setMess(String mess) {
        Mess = mess;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public boolean getstatus() {
        return status;
    }

    public void setstatus(boolean status) {
        this.status = status;
    }
}
