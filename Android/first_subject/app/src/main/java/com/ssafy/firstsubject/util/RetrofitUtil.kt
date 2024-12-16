package com.ssafy.firstsubject.util

import com.ssafy.firstsubject.service.JoinService

class RetrofitUtil {
    companion object {
        val joinService = ApplicationClass.retrofit.create(JoinService::class.java)
    }
}