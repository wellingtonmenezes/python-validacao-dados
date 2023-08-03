import re

class TelefoneBR:
    def __init__(self, numero) -> None:
        if self.valida_telefone(numero):
            self.numero = numero
        else:
            raise ValueError("Telefone incorreto!")

    def __str__(self) -> str:
        return self.formata_telefone()

    def valida_telefone(self, numero) -> bool:
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, numero)
        return True if resposta else False
    
    def formata_telefone(self) -> str:
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        numero = re.search(padrao, self.numero)
        numero_formatado = "+{}({}){}-{}".format(
            numero.group(1),
            numero.group(2),
            numero.group(3),
            numero.group(4)
        )
        return numero_formatado
