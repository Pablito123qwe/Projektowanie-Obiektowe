package org.example.task3

import jakarta.annotation.PostConstruct
import org.example.task3.service.EagerAuthService
import org.example.task3.service.LazyAuthService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class Task3Application {

    @Autowired
    lateinit var eagerAuthService: EagerAuthService

    @Autowired
    lateinit var lazyAuthService: LazyAuthService

    @PostConstruct
    fun init() {
        println("EagerAuthService test: ${eagerAuthService.authenticate("admin", "admin123")}")
        // LazyAuthService nie jest jeszcze użyty — nie zainicjalizuje się na starcie
    }
}

fun main(args: Array<String>) {
    runApplication<Task3Application>(*args)
}
