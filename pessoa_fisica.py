from validate_docbr import CPF

class DocCpf:
    def __init__(self, cpf) -> None:
        cpf = str(cpf)
        if self.valida_cpf(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF Inválido")
    
    def __str__(self) -> str:
        return self.formata_cpf()

    def valida_cpf(self, cpf) -> bool:
        valida_cpf = CPF()
        return valida_cpf.validate(cpf)
  
    def formata_cpf(self) -> str:
        mascara_cpf = CPF()
        return mascara_cpf.mask(self.cpf)
