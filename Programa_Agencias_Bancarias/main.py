from ContasBancos import ContaCorrente, CartaoCredito
from Agencia import Agencia, AgenciaVirtual, AgenciaComum, AgenciaPremium

#Teste Programa ContasBancos:
'''Criando uma conta corrente'''
conta_wanderson = ContaCorrente('Wanderson', '140.008.867-46', 225, 12145)

'''Criando um cartão de crédito'''
cartao_wanderson = CartaoCredito('Wanderson', conta_wanderson)

'''Alterando a senha do cartão'''
cartao_wanderson.senha = '4567'
print(cartao_wanderson.senha)

'''Análisando todos os atributos da conta criada'''
for atributo in conta_wanderson.__dict__:
    print(f'{atributo}: {conta_wanderson.__dict__[atributo]}')

print('-'*50)

#Teste Programa Agencias:
'''Criar agencias:'''
agencia1 = Agencia(11998453833, 1345432342542, 2354)
agencia_virtual = AgenciaVirtual('www.minhaagenciavirtual.com', 22998234789, 1234456232334)
agencia_comum = AgenciaComum(229989237432, 22738883334982)
agencia_premium = AgenciaPremium(119982344583, 11344452345823)

'''Depositar valor no caixa paypal da agencia virtual'''
agencia_virtual.depositar_paypal(2000)
print(agencia_virtual.caixa)
print(agencia_virtual.caixa_paypal)

'''Adicionando Cliente na Agencia Premium'''
agencia_premium.adicionar_cliente('Jessica', 14088293412, 5000)
agencia_premium.adicionar_cliente('Wanderson', 14088293412, 5000000)
print(agencia_premium.clientes)