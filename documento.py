from pessoa_fisica import DocCpf
from pessoa_juridica import DocCnpj


class Documento:
    @staticmethod
    def criar(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Verifique a quantidade de digitos!!!!")
