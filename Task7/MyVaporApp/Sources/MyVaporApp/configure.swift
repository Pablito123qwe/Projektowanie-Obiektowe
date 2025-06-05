import Vapor
import Fluent
import FluentSQLiteDriver
import Leaf

public func configure(_ app: Application) throws {
    app.databases.use(.sqlite(.file("db.sqlite")), as: .sqlite)
    app.migrations.add(CreateProduct())
    app.views.use(.leaf)
    try routes(app)
}

