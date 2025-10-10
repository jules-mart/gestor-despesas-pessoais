from src.gestor_despesas.model.usuario import Usuario


def test_criacao_usuario():
    usuario = Usuario("Julia", "julia@email.com")
    assert usuario.nome == "Julia"
