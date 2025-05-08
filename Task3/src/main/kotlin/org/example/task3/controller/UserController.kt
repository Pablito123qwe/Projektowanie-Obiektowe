package org.example.task3.controller

import org.example.task3.model.LoginRequest
import org.example.task3.model.User
import org.example.task3.service.EagerAuthService
import org.example.task3.service.LazyAuthService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/api/users")
class UserController @Autowired constructor(
    private val eagerAuthService: EagerAuthService,
    private val lazyAuthService: LazyAuthService
) {

    private val users = listOf(
        User(1, "alice"),
        User(2, "bob"),
        User(3, "charlie")
    )

    @GetMapping
    fun getAllUsers(): List<User> = users

    @PostMapping("/login")
    fun login(
        @RequestBody request: LoginRequest,
        @RequestParam(defaultValue = "eager") strategy: String
    ): String {
        val success = when (strategy) {
            "eager" -> eagerAuthService.authenticate(request.username, request.password)
            "lazy" -> lazyAuthService.authenticate(request.username, request.password)
            else -> false
        }

        return if (success) {
            "Access granted (${strategy}) for user: ${request.username}"
        } else {
            "Access denied"
        }
    }
}
