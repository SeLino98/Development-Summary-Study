package com.ssafy.firstsubject

import android.content.Context
import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import com.ssafy.firstsubject.constant.FAIL_JOIN
import com.ssafy.firstsubject.constant.FAIL_LOGIN
import com.ssafy.firstsubject.constant.SUCCESS_JOIN
import com.ssafy.firstsubject.constant.SUCCESS_LOGIN
import com.ssafy.firstsubject.databinding.FragmentLoginBinding
import com.ssafy.firstsubject.model.LoginInfo
import com.ssafy.firstsubject.util.ApplicationClass

// TODO: Rename parameter arguments, choose names that match
// the fragment initialization parameters, e.g. ARG_ITEM_NUMBER
private const val ARG_PARAM1 = "param1"
private const val ARG_PARAM2 = "param2"

class LoginFragment : Fragment() {

    private var _binding : FragmentLoginBinding? = null
    private val binding get() = _binding!!
    private lateinit var mainActivity: MainActivity

    override fun onAttach(context: Context) {
        super.onAttach(context)
        mainActivity = context as MainActivity

    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        arguments?.let {
        }
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        // Inflate the layout for this fragment
        _binding = FragmentLoginBinding.inflate(inflater, container, false)
        return binding.root
    }
    private var isImage = true

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        observeLiveData()

        binding.btnJoin.setOnClickListener {
            mainActivity.openJoinActivity()
        }//회원가입

        binding.imgAutologin.setOnClickListener {//자동로그인 활성 체크 부분
            if (isImage){
                binding.imgAutologin.setImageResource(R.drawable.ico_check_on)
                isImage = false;
            }else{
                binding.imgAutologin.setImageResource(R.drawable.ico_check_off)
                isImage = true;
            }
        }
        binding.btnLogin.setOnClickListener {
            // 1. 필수 입력된 것들을 체크를 한다. // 유효성 체크
            if (binding.editId.text.isNullOrEmpty()||binding.editPasswd.text.isNullOrEmpty()){
                Toast.makeText(mainActivity, FAIL_LOGIN,Toast.LENGTH_SHORT).show()
            }else{
                //2. 코루틴으로 로그인 실행한다.
                //viewmodel로 이동
                val id = binding.editId.text.toString()
                val password = binding.editPasswd.text.toString()
                mainActivity.loginViewModel.getIsUser(id,password)
            }
        }
    }
    private fun observeLiveData() {
        mainActivity.loginViewModel.isLogin.observe(mainActivity){
            if(it.output==1){
                Toast.makeText(mainActivity, SUCCESS_LOGIN, Toast.LENGTH_SHORT).show()
                // 로그인이 성공하면 화면전환을 실행하는데,

                // Shared 이용해서 자동 로그인 체킹돼 있음 shared에 저장한다.
                ApplicationClass.sharedPreferencesUtil.add(
                    LoginInfo(binding.editPasswd.toString(),"1","none",binding.editId.toString())
                )
                // 아이디랑 비번을 저장한다.
                // 엑티비티 이동


            } else if (it.output == 2) { //실패한 경우
                Toast.makeText(mainActivity, FAIL_LOGIN, Toast.LENGTH_SHORT).show()
            }
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }

    companion object {
//        @JvmStatic
//        fun newInstance(param1: String, param2: String) =
//            loginFragment().apply {
//                arguments = Bundle().apply {
//                    putString(ARG_PARAM1, param1)
//                    putString(ARG_PARAM2, param2)
//                }
//            }
    }
}