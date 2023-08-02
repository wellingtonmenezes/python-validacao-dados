class CPF(object):
    def __init__(self, cpf) -> None:
        cpf = str(cpf)
        if self.valida_cpf(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF Inválido")
    
    def __str__(self) -> str:
        return self.formata_cpf()

    def valida_cpf(self, cpf) -> bool:
        if len(cpf) == 11:
            return True
        else:
            return False
        
    def formata_cpf(self) -> str:
        cpf_formatado = "{}.{}.{}.{}".format(
            self.cpf[:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:]
        )
        return cpf_formatado