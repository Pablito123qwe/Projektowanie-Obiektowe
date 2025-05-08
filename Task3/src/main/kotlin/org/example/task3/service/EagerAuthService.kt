package org.example.task3.service

import org.springframework.stereotype.Service

@Service("eagerAuthService") // nazwany bean
class EagerAuthService {

    init {
        println("EagerAuthService initialized")
    }

    fun authenticate(username: String, password: String): Boolean {
        return username == "admin" && password == "admin123"
    }
}
