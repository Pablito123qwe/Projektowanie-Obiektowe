package com.example.listaproduktowapp

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val kategorie = listOf(
            Kategoria("Elektronika", listOf(
                Produkt("Laptop", 3999.99),
                Produkt("Smartfon", 2299.50),
                Produkt("Tablet", 1199.00)
            )),
            Kategoria("Książki", listOf(
                Produkt("Wiedźmin", 45.99),
                Produkt("Hobbit", 39.90)
            )),
            Kategoria("Ubrania", listOf(
                Produkt("Koszulka", 59.99),
                Produkt("Spodnie", 119.99)
            ))
        )

        val recyclerView = findViewById<RecyclerView>(R.id.recyclerViewKategorie)
        recyclerView.layoutManager = LinearLayoutManager(this)
        recyclerView.adapter = KategorieAdapter(kategorie) { kategoria ->
            val intent = Intent(this, ProduktyActivity::class.java)
            intent.putParcelableArrayListExtra("produkty", ArrayList(kategoria.produkty))
            startActivity(intent)
        }
    }
}
