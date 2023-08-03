from documento import Documento
from telefone_br import TelefoneBR

cpf = Documento.criar("00496558331")
cnpj = Documento.criar("94861289000187")
telefone = TelefoneBR("88992951220")

print("CPF:", cpf)
print("CNPJ:", cnpj)
print("Telefone:", telefone)
