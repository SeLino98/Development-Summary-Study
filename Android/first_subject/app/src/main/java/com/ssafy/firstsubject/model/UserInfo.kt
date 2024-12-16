package com.ssafy.firstsubject.model

data class UserInfo(
    val name : String,
    val password : String,
    val email : String,
    val address : String,
    val addressDetail: String,
    val phone : String,
    val type : String = "none",
    val Uid : String
)
