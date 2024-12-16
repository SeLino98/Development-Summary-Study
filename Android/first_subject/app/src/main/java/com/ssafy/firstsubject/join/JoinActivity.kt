package com.ssafy.firstsubject.join

import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.util.Log
import android.view.View
import android.widget.AdapterView
import android.widget.Toast
import androidx.activity.viewModels
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import com.ssafy.firstsubject.R
import com.ssafy.firstsubject.constant.FAIL_JOIN
import com.ssafy.firstsubject.constant.SUCCESS_JOIN
import com.ssafy.firstsubject.databinding.ActivityJoinBinding
import com.ssafy.firstsubject.model.UserInfo

private const val TAG = "JoinActivity_싸피"
class JoinActivity : AppCompatActivity() {

    private lateinit var binding : ActivityJoinBinding
    private lateinit var emailSpinnerAdapter: EmailSpinnerAdapter
    private val joinViewModel : JoinViewModel by viewModels()
    private val emailList = ArrayList<String>()

    private var emailDomain = ""

    // 영문 및 숫자 포함 6~16자 정규식
    private val validPassword = Regex("^(?=.*[A-Za-z])(?=.*\\d)[A-Za-z\\d]{6,16}\$")
    // 영문 및 숫자 포함 15자 이내 정규식
    private val validId = Regex("^[A-Za-z\\d]{1,15}\$")

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityJoinBinding.inflate(layoutInflater)
        setContentView(binding.root)

        initSetting()
        // 회원가입 api 관련 함수
        joinUser()
        observeLiveData()
        sendEmailSecreteCode()
        // 이메일 스피너 관련 함수
        setUpSpinner()
        setUpSpinnerHandler()

        // 비밀번호 유효성 검사
        checkValidPassword()
    }
    private fun initSetting() {
        binding.ivJoinBack.setOnClickListener {
            finish()
        }
    }

    // 비밀번호 유효성 검사 watcher
    private fun checkValidPassword() {
        val id = binding.etJoinId
        val password = binding.etJoinPassword
        val checkPassword = binding.etJoinCheckPassword

        // 아이디 확인 입력을 관찰하는 watcher
        id.addTextChangedListener(object: TextWatcher {
            override fun beforeTextChanged(p0: CharSequence?, p1: Int, p2: Int, p3: Int) {

            }

            override fun onTextChanged(s: CharSequence?, p1: Int, p2: Int, p3: Int) {
                val inputId = s.toString()

                if (inputId.matches(validId)) {
                    val defaultBackground = ContextCompat.getDrawable(this@JoinActivity, R.drawable.background_edittext)
                    id.background = defaultBackground
                } else {
                    val purpleBackground = ContextCompat.getDrawable(this@JoinActivity, R.drawable.background_red)
                    id.background = purpleBackground
                }
            }

            override fun afterTextChanged(p0: Editable?) {

            }

        })

        // 비밀번호 입력을 관찰하는 watcher
        password.addTextChangedListener(object: TextWatcher {
            override fun beforeTextChanged(p0: CharSequence?, p1: Int, p2: Int, p3: Int) {

            }

            override fun onTextChanged(s: CharSequence?, p1: Int, p2: Int, p3: Int) {
                val inputPassword = s.toString()

                if (inputPassword.matches(validPassword)) {
                    val defaultBackground = ContextCompat.getDrawable(this@JoinActivity, R.drawable.background_edittext)
                    password.background = defaultBackground
                } else {
                    val purpleBackground = ContextCompat.getDrawable(this@JoinActivity, R.drawable.background_red)
                    password.background = purpleBackground
                }
            }

            override fun afterTextChanged(p0: Editable?) {

            }
        })
        // 비밀번호 확인 입력을 관찰하는 watcher
        checkPassword.addTextChangedListener(object: TextWatcher {
            override fun beforeTextChanged(p0: CharSequence?, p1: Int, p2: Int, p3: Int) {

            }

            override fun onTextChanged(s: CharSequence?, p1: Int, p2: Int, p3: Int) {
                val inputCheckPassword = s.toString()

                if (inputCheckPassword.matches(validPassword)) {
                    val defaultBackground = ContextCompat.getDrawable(this@JoinActivity, R.drawable.background_edittext)
                    checkPassword.background = defaultBackground
                } else {
                    val purpleBackground = ContextCompat.getDrawable(this@JoinActivity, R.drawable.background_red)
                    checkPassword.background = purpleBackground
                }
            }

            override fun afterTextChanged(p0: Editable?) {

            }

        })
    }


    // 이메일 인증번호 요청
    private fun sendEmailSecreteCode() {
        binding.btnSendCode.setOnClickListener {
            joinViewModel.requestEmailSecretCode()
        }
    }

    private fun joinUser() {
        binding.btnApplyJoin.setOnClickListener {

            val id = binding.etJoinId.text.toString()
            val password = binding.etJoinPassword.text.toString()
            val checkPassword = binding.etJoinCheckPassword.text.toString()
            val name = binding.etJoinName.text.toString()
            val email = binding.etJoinEmail.text.toString()  + "@" + emailDomain
            val phoneNumber = binding.etJoinPhoneNumber.text.toString()

            if (id.isEmpty() || password.isEmpty() || checkPassword.isEmpty() || name.isEmpty() || email.isEmpty() || phoneNumber.isEmpty()) {
                Toast.makeText(this, "필수항목을 입력해주세요.", Toast.LENGTH_SHORT).show()
            } else {
                val userInfo = UserInfo(
                    binding.etJoinName.text.toString(),
                    binding.etJoinPassword.text.toString(),
                    email,
                    binding.etAddress.text.toString(),
                    binding.etAddressDetail.text.toString(),
                    binding.etJoinPhoneNumber.text.toString(),
                    "none",
                    binding.etJoinId.text.toString()
                )
                Log.d(TAG, "email: $email")

                if (emailDomain == "직접입력") {
                    Toast.makeText(this, "이메일을 입력해주세요.", Toast.LENGTH_SHORT).show()
                } else {
                    joinViewModel.getIsJoin(userInfo)
                }
            }
        }
    }

    private fun observeLiveData() {
        joinViewModel.isJoin.observe(this) { joinResponse ->
            if (joinResponse.output == 1) {
                Toast.makeText(this, SUCCESS_JOIN, Toast.LENGTH_SHORT).show()
            } else if (joinResponse.output == 2) {
                Toast.makeText(this, FAIL_JOIN, Toast.LENGTH_SHORT).show()
            }
        }

        joinViewModel.isSendSecretCode.observe(this) { joinResponse ->
            if (joinResponse.output == 1) {
                Toast.makeText(this, "인증번호가 발송되었습니다.", Toast.LENGTH_SHORT).show()
                joinViewModel.getEmailSecretCode()
            } else {
                Toast.makeText(this, "인증번호가 발송이 실패하였습니다.", Toast.LENGTH_SHORT).show()
            }
        }

        joinViewModel.isGetSecretCode.observe(this) { joinResponse ->
            if (joinResponse.output == 1) {
                Toast.makeText(this, "인증번호를 받았습니다.", Toast.LENGTH_SHORT).show()
            } else {
                Toast.makeText(this, "인증번호 받기를 실패하였습니다.", Toast.LENGTH_SHORT).show()
            }
        }
    }

    private fun setUpSpinner() {
        val emails = resources.getStringArray(R.array.spinner_email)

        for (email in emails.indices) {
            emailList.add(emails[email])
        }

        emailSpinnerAdapter = EmailSpinnerAdapter(this, R.layout.item_email_spinner, emailList)
        binding.emailSpinner.adapter = emailSpinnerAdapter
    }

    // spinner 선택 함수
    private fun setUpSpinnerHandler() {
        binding.emailSpinner.onItemSelectedListener = object: AdapterView.OnItemSelectedListener {
            // spinner 선택 시 String으로 저장
            override fun onItemSelected(p0: AdapterView<*>?, p1: View?, position: Int, p3: Long) {
                emailDomain = binding.emailSpinner.getItemAtPosition(position) as String
            }

            override fun onNothingSelected(p0: AdapterView<*>?) {

            }

        }

    }
}