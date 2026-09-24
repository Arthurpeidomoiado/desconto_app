from src.models.pedido import Pedido

class PedidoRepository:
    def __init__(self):
        self.pedidos = []
    def adicionar_pedidos(self,pedido: Pedido):
        self.pedidos.append(pedido)
    def listar_pedidos(self):
        return self.pedidos