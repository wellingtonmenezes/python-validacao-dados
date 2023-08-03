from validate_docbr import CNPJ

class DocCnpj:
    def __init__(self, cnpj) -> None:
        cnpj = str(cnpj)
        if self.valida_cnpj(cnpj):
            self.cnpj = cnpj
        else:
            raise ValueError("CNPJ Inválido")
        
    def __str__(self) -> str:
        return self.formata_cnpj()

    def valida_cnpj(self, cnpj) -> bool:
        valida_cnpj = CNPJ()
        return valida_cnpj.validate(cnpj)
        
    def formata_cnpj(self) -> str:
        mascara_cnpj = CNPJ()
        return mascara_cnpj.mask(self.cnpj)
