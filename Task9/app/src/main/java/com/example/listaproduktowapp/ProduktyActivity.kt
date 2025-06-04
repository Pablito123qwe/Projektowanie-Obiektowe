package com.example.listaproduktowapp

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class ProduktyActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_produkty)

        val produkty = intent.getParcelableArrayListExtra<Produkt>("produkty") ?: listOf()
        val recyclerView = findViewById<RecyclerView>(R.id.recyclerViewProdukty)
        recyclerView.layoutManager = LinearLayoutManager(this)
        recyclerView.adapter = ProduktyAdapter(produkty)
    }
}
