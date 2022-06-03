from peewee import *

database = MySQLDatabase('chinaa94_pedidos', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'br654.hostgator.com.br', 'port': 3306, 'user': 'chinaa94_teste', 'password': '197200197200'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class TbProdutos(BaseModel):
    cod_produto = CharField(column_name='cod_produto', primary_key=True)
    medicamento = CharField(column_name='medicamento', null=True)
    tipo = CharField(column_name='tipo', null=True)
    ultimo_fornecedor = IntegerField(column_name='ultimo fornecedor', null=True)
    venda = FloatField(column_name='venda', null=True)
    ultima_compra = FloatField(column_name='ultima compra', null=True)

    class Meta:
        table_name = 'tb_produtos'

class TbBarras(BaseModel):
    barra_generico = CharField(column_name='barraGenerico', constraints=[SQL("DEFAULT ''")], primary_key=True)
    barra_produto = ForeignKeyField(column_name='barraProduto', constraints=[SQL("DEFAULT ''")], field='cod_produto', model=TbProdutos)

    class Meta:
        table_name = 'tb_barras'

class TbCompras(BaseModel):
    valor_total = FloatField(column_name='valor total', null=True)
    data = DateField(primary_key=True)

    class Meta:
        table_name = 'tb_compras'

class TbFornecedores(BaseModel):
    codigo = AutoField(column_name='codigo')
    nome_do_fornecedor = CharField(column_name='nome do fornecedor', null=True)

    class Meta:
        table_name = 'tb_fornecedores'

class TbComprasItem(BaseModel):
    cod_produto = ForeignKeyField(column_name='cod_produto', field='barra_generico', model=TbBarras)
    fornecedor = ForeignKeyField(column_name='fornecedor', field='codigo', model=TbFornecedores)
    quantidade = IntegerField(column_name='quantidade')
    data = ForeignKeyField(column_name='data', field='data', model=TbCompras)
    valor = FloatField()
    venda = FloatField()

    class Meta:
        table_name = 'tb_compras_item'
        indexes = (
            (('data', 'cod_produto'), True),
        )
        primary_key = CompositeKey('cod_produto', 'data')

class TbPedidos(BaseModel):
    cod_produto = ForeignKeyField(column_name='cod_produto', field='barra_generico', model=TbBarras, unique=True)
    quantidade = IntegerField(column_name='quantidade')
    ativo = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    contador = AutoField()

    class Meta:
        table_name = 'tb_pedidos'

