import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class LoginPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Layout centralizado
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        titulo = ctk.CTkLabel(self, text="💰 Login no Sistema Financeiro",
                              font=ctk.CTkFont(size=26, weight="bold"))
        titulo.grid(row=0, column=0, pady=(60, 20))

        self.entry_usuario = ctk.CTkEntry(self, placeholder_text="Usuário", width=250)
        self.entry_usuario.grid(row=1, column=0, pady=10)

        self.entry_senha = ctk.CTkEntry(self, placeholder_text="Senha", show="•", width=250)
        self.entry_senha.grid(row=2, column=0, pady=10)

        self.label_erro = ctk.CTkLabel(self, text="", text_color="red")
        self.label_erro.grid(row=3, column=0, pady=5)

        btn_login = ctk.CTkButton(self, text="Entrar", command=self.verificar_login, width=150)
        btn_login.grid(row=4, column=0, pady=20)

    def verificar_login(self):
        usuario = self.entry_usuario.get().strip()
        senha = self.entry_senha.get().strip()

        # Credenciais fixas (pode ser substituído depois por banco de dados)
        if usuario == "admin" and senha == "1234":
            self.master.abrir_sistema()
        else:
            self.label_erro.configure(text="Usuário ou senha incorretos.")
            