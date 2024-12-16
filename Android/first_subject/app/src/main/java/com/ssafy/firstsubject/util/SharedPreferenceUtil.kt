package com.ssafy.firstsubject.util

import android.content.Context
import android.content.SharedPreferences
import com.ssafy.firstsubject.model.LoginInfo
import com.ssafy.firstsubject.model.UserInfo

class SharedPreferenceUtil (context : Context) {
    val SHARED_USER_INFO = "shared_user_info"

    var preference: SharedPreferences =
        context.getSharedPreferences(SHARED_USER_INFO,Context.MODE_PRIVATE)

    fun add(user : LoginInfo){
        val editor = preference.edit()
        editor.putString("uid",user.password)
        editor.putString("password",user.password)
        editor.putString("token","1234")
        editor.putString("type",user.type)
        editor.apply()
    }
    fun isUser():Boolean{
        val id = preference.getString("uid","")
        if (id!= ""){
            //로그인 정보가 있으니 로그인 시도를 한다.
            return true;
        }
        //정보 없으니 false 리턴
        return false;
    }
    fun getUser():LoginInfo{
        val uid = preference.getString("uid","")
        val password = preference.getString("password","")

        return LoginInfo(password!!,"1","none",uid!!)
    }
    // sharedpreference에 로그인 정보 삭제하기(로그아웃)
    fun deleteUser(){
        val editor = preference.edit()
        editor.clear()
        editor.apply()
    }
}