from gestor_despesas.controller.usuario_controller import UsuarioController


def main():
    print("💰 Gestor de Despesas Pessoais iniciado!")
    usuario_controller = UsuarioController()
    usuario_controller.menu_principal()


if __name__ == "__main__":
    main()
