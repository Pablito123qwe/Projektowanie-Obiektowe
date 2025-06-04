package com.example.listaproduktowapp

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class KategorieAdapter(
    private val kategorie: List<Kategoria>,
    private val onClick: (Kategoria) -> Unit
) : RecyclerView.Adapter<KategorieAdapter.KategoriaViewHolder>() {

    class KategoriaViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val textView: TextView = itemView.findViewById(R.id.textViewKategoria)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): KategoriaViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_kategoria, parent, false)
        return KategoriaViewHolder(view)
    }

    override fun onBindViewHolder(holder: KategoriaViewHolder, position: Int) {
        val kategoria = kategorie[position]
        holder.textView.text = kategoria.nazwa
        holder.itemView.setOnClickListener { onClick(kategoria) }
    }

    override fun getItemCount() = kategorie.size
}
