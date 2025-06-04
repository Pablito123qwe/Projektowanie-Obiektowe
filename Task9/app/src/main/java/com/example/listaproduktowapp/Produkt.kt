package com.example.listaproduktowapp

import android.os.Parcelable
import kotlinx.parcelize.Parcelize

@Parcelize
data class Produkt(
    val nazwa: String,
    val cena: Double
) : Parcelable
