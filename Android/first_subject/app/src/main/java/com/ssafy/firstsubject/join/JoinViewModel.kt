package com.ssafy.firstsubject.join

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.ssafy.firstsubject.model.JoinResponse
import com.ssafy.firstsubject.model.UserInfo
import com.ssafy.firstsubject.util.RetrofitUtil
import kotlinx.coroutines.launch
import retrofit2.Response

class JoinViewModel : ViewModel() {
    private val _isJoin = MutableLiveData<JoinResponse>()
    val isJoin : LiveData<JoinResponse> = _isJoin

    private val _isSendSecretCode = MutableLiveData<JoinResponse>()
    val isSendSecretCode : LiveData<JoinResponse> = _isSendSecretCode

    private val _isGetSecretCode = MutableLiveData<JoinResponse>()
    val isGetSecretCode : LiveData<JoinResponse> = _isGetSecretCode

    fun getIsJoin(userInfo : UserInfo) {
        viewModelScope.launch {
            val response = RetrofitUtil.joinService.joinUser(userInfo)

            if (response.isSuccessful) {
                _isJoin.value = response.body()
            }
        }
    }

    fun requestEmailSecretCode() {
        viewModelScope.launch {
            val response = RetrofitUtil.joinService.sendSecretCode()

            if (response.isSuccessful) {
                _isSendSecretCode.value = response.body()
            }
        }
    }

    fun getEmailSecretCode() {
        viewModelScope.launch {
            val response = RetrofitUtil.joinService.getSecretCode()

            if (response.isSuccessful) {
                _isGetSecretCode.value = response.body()
            }
        }
    }
}