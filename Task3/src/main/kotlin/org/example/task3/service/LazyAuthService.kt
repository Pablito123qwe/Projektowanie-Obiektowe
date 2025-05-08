package org.example.task3.service

import org.springframework.context.annotation.Lazy
import org.springframework.stereotype.Service

@Lazy
@Service("lazyAuthService") // inna nazwa
class LazyAuthService {

    init {
        println("LazyAuthService initialized")
    }

    fun authenticate(username: String, password: String): Boolean {
        return username == "lazy" && password == "lazy123"
    }
}
