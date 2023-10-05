from datetime import date
class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def dados(self):
        return f"{self.nome} seu cargo é {self.cargo} e seu salário é {self.salario}"
    
    def registrarPonto(self):
        return f"Ponto registrado na data {date.today()}"
    
    def descontarSalario(self, valor):
        if valor <= 0:
            return f"Operação inválida"
        else:
            self.salario -= valor

    def promover(self, novoCargo, novoSalario):
        self.cargo = novoCargo
        self.salario = novoSalario

        return f"promovido para {self.cargo} com salário de R${self.salario}"
    
    def calcularBonus(self):
        bonus = self.salario * 0.1 #fazendo calculo de 10% do salário
        return bonus