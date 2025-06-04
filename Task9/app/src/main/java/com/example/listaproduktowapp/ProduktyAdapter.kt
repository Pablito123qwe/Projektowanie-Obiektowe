package com.example.listaproduktowapp

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class ProduktyAdapter(
    private val produkty: List<Produkt>
) : RecyclerView.Adapter<ProduktyAdapter.ProduktViewHolder>() {

    class ProduktViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val nazwa: TextView = itemView.findViewById(R.id.textViewProduktNazwa)
        val cena: TextView = itemView.findViewById(R.id.textViewProduktCena)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ProduktViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_produkt, parent, false)
        return ProduktViewHolder(view)
    }

    override fun onBindViewHolder(holder: ProduktViewHolder, position: Int) {
        val produkt = produkty[position]
        holder.nazwa.text = produkt.nazwa
        holder.cena.text = String.format("%.2f zł", produkt.cena)
    }

    override fun getItemCount() = produkty.size
}
