package com.ssafy.firstsubject.util

import android.app.Application
import com.google.gson.Gson
import com.google.gson.GsonBuilder
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class ApplicationClass : Application() {

    override fun onCreate() {
        super.onCreate()

        val gson : Gson = GsonBuilder()
            .setLenient()
            .create()

        sharedPreferencesUtil = SharedPreferenceUtil(applicationContext)

        // 앱이 처음 생성되는 순간, retrofit 인스턴스를 생성
        retrofit = Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create(gson))
            .build()
    }

    companion object {
        const val BASE_URL = "http://192.168.100.178:8080"
        lateinit var retrofit : Retrofit
        lateinit var sharedPreferencesUtil: SharedPreferenceUtil

    }
}