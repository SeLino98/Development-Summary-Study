package com.ssafy.firstsubject

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ssafy.firstsubject.model.LoginInfo
import com.ssafy.firstsubject.model.LoginResponse
import com.ssafy.firstsubject.util.RetrofitUtil
import kotlinx.coroutines.launch

class LoginViewModel :ViewModel() {
    private val _isLogin = MutableLiveData<LoginResponse>()
    val isLogin : LiveData<LoginResponse> = _isLogin

    fun getIsUser(userId:String,password:String){
        val type : String = "none"
        val loginInfo = LoginInfo(
            password,"1",type,userId
        )
        viewModelScope.launch {
            val response = RetrofitUtil.joinService.loginUser(loginInfo)
            if (response.isSuccessful){
                _isLogin.value = response.body()
            }
        }
    }

}