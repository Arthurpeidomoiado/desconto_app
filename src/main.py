from src.models.desconto import DescontoVIP,DescontoNormal,DescontoPremium
from src.models.pedido import Pedido
from src.services.PedidoService import PedidoService
if __name__ == '__main__':
    service = PedidoService();
    pedido1 = Pedido('Leonardo',DescontoNormal())
    pedido1.valor_original = 100;

    pedido2 = Pedido('Artur', DescontoPremium())
    pedido2.valor_original= 100;

    pedido3 = Pedido('Jorge', DescontoVIP())
    pedido3.valor_original = 100;

service.adicionar_pedidos(pedido1)
service.adicionar_pedidos(pedido2)
service.adicionar_pedidos(pedido3)
service.processar_pedidos()