package com.ssafy.firstsubject

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.activity.viewModels
import com.ssafy.firstsubject.databinding.ActivityMainBinding
import com.ssafy.firstsubject.join.JoinActivity
import com.ssafy.firstsubject.main.TestMainBoardActivity
import com.ssafy.firstsubject.util.ApplicationClass

class MainActivity : AppCompatActivity() {

    private lateinit var binding : ActivityMainBinding
    val loginViewModel : LoginViewModel by viewModels()



    //처음 실행할 때 shared에 아디 비번을 통신요청보낸다.

    // 프래그먼트 시작할 때 쉐어드의 데이터 값이 있으면 바로 이페이지 말고 로그인된 페이지로 넘어간다.
    //
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        openLoginFragment()
        observeView()
    }
    private fun observeView(){
        val isLogin = ApplicationClass.sharedPreferencesUtil.isUser()
        if (isLogin){
            //로그인 진행
            val loginInfo = ApplicationClass.sharedPreferencesUtil.getUser()
            loginViewModel.getIsUser(loginInfo.uid,loginInfo.password)
            //성공이면 화면 전환
            //아니면 x
        }
        loginViewModel.isLogin.observe(this){
            if (it.output == 1){
                openTestMainBoardActivity()
            }
        }
    }
    private fun openLoginFragment() {
        supportFragmentManager.beginTransaction()
            .replace(R.id.fragment_container, LoginFragment())
            .commit()
    }

    fun openJoinActivity() {
        val intent = Intent(this, JoinActivity::class.java)
        startActivity(intent)
    }
    fun openTestMainBoardActivity(){
        val intent = Intent(this, TestMainBoardActivity::class.java)
        startActivity(intent)
    }
}