package com.ssafy.firstsubject.service

import com.ssafy.firstsubject.model.JoinResponse
import com.ssafy.firstsubject.model.LoginInfo
import com.ssafy.firstsubject.model.LoginResponse
import com.ssafy.firstsubject.model.SocialInfo
import com.ssafy.firstsubject.model.SocialResponse
import com.ssafy.firstsubject.model.UserInfo
import retrofit2.Response
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST

interface JoinService {
   @POST("/api/sign/regProfile") // 회원가입 api
   suspend fun joinUser(@Body userInfo: UserInfo) : Response<JoinResponse>

   @POST("/api/sign/login") //일반 로그인
   suspend fun loginUser(@Body loginInfo: LoginInfo) : Response<LoginResponse>

   @POST("/api/sign/exists/social")
   suspend fun existsUser(@Body existUser: SocialInfo) :Response<SocialResponse>

   @POST("/api/auth/send/email") // 이메일 인증코드 발송 api
   suspend fun sendSecretCode() : Response<JoinResponse>

   @GET("/api/auth/check/email") // 이메일 인증코드 확인 api
   suspend fun getSecretCode() : Response<JoinResponse>
}