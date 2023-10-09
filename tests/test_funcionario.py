from app.funcionario import Funcionario

colaborador = Funcionario("Sofia", "Gerente", 3000)

def test_verificarDados():
    assert colaborador.dados() == "Sofia seu cargo é Gerente e seu salário é 3000"

def test_calcularBonus():
    assert colaborador.calcularBonus() >= 300

def test_registrarPonto():
    assert colaborador.registrarPonto() == "Ponto registrado na data 2023-10-09"