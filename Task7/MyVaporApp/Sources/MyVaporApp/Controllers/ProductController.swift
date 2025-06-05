import Vapor
import Fluent

struct ProductController: RouteCollection {
    func boot(routes: RoutesBuilder) throws {
        let products = routes.grouped("products")
        products.get(use: index)
        products.get("create", use: create)
        products.post("create", use: createPost)
        products.get(":productID", use: show)
        products.get(":productID", "edit", use: edit)
        products.post(":productID", "edit", use: editPost)
        products.post(":productID", "delete", use: delete)
    }


    func index(req: Request) throws -> EventLoopFuture<View> {
        Product.query(on: req.db).all().flatMap { products in
            let context = ["products": products]
            return req.view.render("Product/index", context)
        }
    }

    func create(req: Request) throws -> EventLoopFuture<View> {
        req.view.render("Product/create")
    }

  
    func createPost(req: Request) throws -> EventLoopFuture<Response> {
        let product = try req.content.decode(Product.self)
        return product.save(on: req.db).map {
            req.redirect(to: "/products")
        }
    }

    
    func show(req: Request) throws -> EventLoopFuture<View> {
        Product.find(req.parameters.get("productID"), on: req.db)
            .unwrap(or: Abort(.notFound)).flatMap { product in
                let context = ["product": product]
                return req.view.render("Product/show", context)
            }
    }

   
    func edit(req: Request) throws -> EventLoopFuture<View> {
        Product.find(req.parameters.get("productID"), on: req.db)
            .unwrap(or: Abort(.notFound)).flatMap { product in
                let context = ["product": product]
                return req.view.render("Product/edit", context)
            }
    }

   
    func editPost(req: Request) throws -> EventLoopFuture<Response> {
        let updatedProduct = try req.content.decode(Product.self)
        return Product.find(req.parameters.get("productID"), on: req.db)
            .unwrap(or: Abort(.notFound)).flatMap { product in
                product.name = updatedProduct.name
                product.price = updatedProduct.price
                return product.save(on: req.db).map {
                    req.redirect(to: "/products")
                }
            }
    }

    
    func delete(req: Request) throws -> EventLoopFuture<Response> {
        Product.find(req.parameters.get("productID"), on: req.db)
            .unwrap(or: Abort(.notFound)).flatMap { product in
                product.delete(on: req.db).map {
                    req.redirect(to: "/products")
                }
            }
    }
}
