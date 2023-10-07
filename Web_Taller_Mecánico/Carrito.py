class Carrito:
    def __init__(self, request) -> None:
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"] 
        else:
            self.carrito = carrito

    def agregar(self, producto): 
        id = str(producto.idProducto)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "idProducto":producto.idProducto, 
                
                "nombre":producto.nombre,
                "precio":producto.precio,
                "total":producto.precio,
                "cantidad":1
            }
        else:
            self.carrito[id]["cantidad"]+=1
            self.carrito[id]["total"]+=producto.precio
        self.actualizar()

    def actualizar(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def restar(self,producto):
        id = str(producto.idProducto)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"]-=1
            self.carrito[id]["total"]-=producto.precio
            if self.carrito[id] == 0:
                self.eliminar(producto)
            self.actualizar()

    def eliminar(self, producto):
        id = str(producto.idProducto)
        del self.carrito[id]
        self.actualizar()

    def vaciar(self):
        self.session["carrito"] = {}
        self.session.modified = True