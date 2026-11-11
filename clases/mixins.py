class LogMixin:
    def log(self, mensaje: str):
        clase_nombre = self.obtener_clase() if hasattr(self, 'obtener_clase') else "Sistema"
        print(f"[{clase_nombre} - {self.nombre}]: {mensaje}")

class InventarioMixin:
    def agregar_item(self, item: str):
        if not hasattr(self, 'inventario'):
            self.inventario = []
        self.inventario.append(item)
        if hasattr(self, 'log'):
            self.log(f"Item agregado al inventario: {item}")

    def usar_item(self, item: str):
        if not hasattr(self, 'inventario'):
            self.inventario = []
        if item in self.inventario:
            self.inventario.remove(item)
            if hasattr(self, 'log'):
                self.log(f"Item utilizado: {item}")
            return True
        if hasattr(self, 'log'):
            self.log(f"El item '{item}' no está en el inventario.")
        return False

    def listar_inventario(self):
        if not hasattr(self, 'inventario'):
            self.inventario = []
        return self.inventario
