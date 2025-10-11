import customtkinter as ctk
from tkinter import messagebox


class TelaCadastro(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cadastro de Usuário")
        self.geometry("500x600")
        self.resizable(False, False)
        self.grab_set()

        self.frame = ctk.CTkFrame(self, fg_color="#1e1e2f")
        self.frame.pack(padx=30, pady=30, fill="both", expand=True)

        self.label_titulo = ctk.CTkLabel(
            self.frame,
            text="🧾 Cadastro de Usuário",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#ffffff"
        )
        self.label_titulo.pack(pady=(15, 5))

        self.label_subtitulo = ctk.CTkLabel(
            self.frame,
            text="Preencha seus dados pessoais e financeiros",
            font=ctk.CTkFont(size=13),
            text_color="#a5a5a5"
        )
        self.label_subtitulo.pack(pady=(0, 15))

        self.entry_nome = ctk.CTkEntry(
            self.frame, placeholder_text="Nome completo",
            fg_color="#2c2c3c", text_color="#ffffff", placeholder_text_color="#aaaaaa"
        )
        self.entry_nome.pack(pady=8, padx=30, fill="x")

        self.entry_data_nasc = ctk.CTkEntry(
            self.frame, placeholder_text="Data de nascimento (DD/MM/AAAA)",
            fg_color="#2c2c3c", text_color="#ffffff", placeholder_text_color="#aaaaaa"
        )
        self.entry_data_nasc.pack(pady=8, padx=30, fill="x")

        self.entry_cpf = ctk.CTkEntry(
            self.frame, placeholder_text="CPF (somente números)",
            fg_color="#2c2c3c", text_color="#ffffff", placeholder_text_color="#aaaaaa"
        )
        self.entry_cpf.pack(pady=8, padx=30, fill="x")

        self.entry_profissao = ctk.CTkEntry(
            self.frame, placeholder_text="Profissão",
            fg_color="#2c2c3c", text_color="#ffffff", placeholder_text_color="#aaaaaa"
        )
        self.entry_profissao.pack(pady=8, padx=30, fill="x")

        self.entry_renda = ctk.CTkEntry(
            self.frame, placeholder_text="Renda mensal (R$)",
            fg_color="#2c2c3c", text_color="#ffffff", placeholder_text_color="#aaaaaa"
        )
        self.entry_renda.pack(pady=8, padx=30, fill="x")

        self.label_login = ctk.CTkLabel(
            self.frame, text="Dados de Acesso", font=ctk.CTkFont(size=14, weight="bold"), text_color="#ffffff"
        )
        self.label_login.pack(pady=(20, 5))

        self.entry_usuario = ctk.CTkEntry(
            self.frame, placeholder_text="Usuário",
            fg_color="#2c2c3c", text_color="#ffffff", placeholder_text_color="#aaaaaa"
        )
        self.entry_usuario.pack(pady=8, padx=30, fill="x")

        self.entry_senha = ctk.CTkEntry(
            self.frame, placeholder_text="Senha", show="*",
            fg_color="#2c2c3c", text_color="#ffffff", placeholder_text_color="#aaaaaa"
        )
        self.entry_senha.pack(pady=8, padx=30, fill="x")

        self.entry_confirmar = ctk.CTkEntry(
            self.frame, placeholder_text="Confirmar senha", show="*",
            fg_color="#2c2c3c", text_color="#ffffff", placeholder_text_color="#aaaaaa"
        )
        self.entry_confirmar.pack(pady=8, padx=30, fill="x")

        self.btn_cadastrar =_
