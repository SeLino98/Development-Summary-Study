package com.ssafy.firstsubject.join

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import androidx.annotation.LayoutRes
import com.ssafy.firstsubject.databinding.ItemEmailSpinnerBinding

class EmailSpinnerAdapter(context : Context, @LayoutRes private val resId : Int,
    private val menuList : List<String>) : ArrayAdapter<String>(context, resId, menuList) {

    private var emailDomain = ""
    override fun getCount(): Int {
        return menuList.size
    }

    override fun getItem(position: Int): String? {
        return menuList[position]
    }

    override fun getView(position: Int, convertView: View?, parent: ViewGroup): View {
        val binding = ItemEmailSpinnerBinding.inflate(LayoutInflater.from(parent.context))
        val email = menuList[position]

        binding.tvSpinnerEmail.text = email
        emailDomain = email
        return binding.root
    }

    override fun getDropDownView(position: Int, convertView: View?, parent: ViewGroup): View {
        val binding = ItemEmailSpinnerBinding.inflate(LayoutInflater.from(parent.context))
        val email = menuList[position]

        binding.tvSpinnerEmail.text = email
        emailDomain = email
        return binding.root
    }
}