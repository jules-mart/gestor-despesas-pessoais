# TelaPrincipal.py (Versão Atualizada com a aba "Meu Perfil")

import customtkinter as ctk
from Resumo import AbaResumo

class TelaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Painel Financeiro Principal")
        self.geometry("800x600")
        self.resizable(True, True)

        # Configura o grid para que o TabView ocupe todo o espaço
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # --- Cria o sistema de Abas (TabView) ---
        self.tab_view = ctk.CTkTabview(self, fg_color="#1e1e2f")
        self.tab_view.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # --- Adiciona as abas ---
        self.tab_view.add("Resumo")
        self.tab_view.add("Despesas")
        self.tab_view.add("Limites")
        self.tab_view.add("Metas")
        self.tab_view.add("Meu Perfil")  # <-- NOVA ABA ADICIONADA AQUI

        # Define a aba inicial que será exibida
        self.tab_view.set("Resumo")

        # --- Adiciona conteúdo em cada aba ---
        self.criar_conteudo_abas()

    def criar_conteudo_abas(self):
        # Aba de Resumo
        # Cria uma instância da nossa classe importada e a coloca na aba "Resumo"
        aba_resumo = AbaResumo(master=self.tab_view.tab("Resumo"))
        aba_resumo.pack(fill="both", expand=True)

        # Aba de Despesas
        frame_despesas = self.tab_view.tab("Despesas")
        label_despesas = ctk.CTkLabel(
            frame_despesas, text="Aqui será o local para lançamento de despesas.", font=ctk.CTkFont(size=20)
        )
        label_despesas.pack(padx=20, pady=20, expand=True)

        # Aba de Limites
        frame_limites = self.tab_view.tab("Limites")
        label_limites = ctk.CTkLabel(
            frame_limites, text="Aqui ficarão os controles de limites de gastos.", font=ctk.CTkFont(size=20)
        )
        label_limites.pack(padx=20, pady=20, expand=True)

        # Aba de Metas
        frame_metas = self.tab_view.tab("Metas")
        label_metas = ctk.CTkLabel(
            frame_metas, text="Aqui ficará o acompanhamento de metas.", font=ctk.CTkFont(size=20)
        )
        label_metas.pack(padx=20, pady=20, expand=True)

        # --- ABA MEU PERFIL (NOVO CONTEÚDO) ---
        frame_perfil = self.tab_view.tab("Meu Perfil")
        
        # Cria um frame interno para centralizar o conteúdo do perfil
        inner_frame = ctk.CTkFrame(frame_perfil, fg_color="transparent")
        inner_frame.pack(padx=100, pady=50, fill="both", expand=True)
        
        label_perfil_titulo = ctk.CTkLabel(
            inner_frame, text="Alterar Informações do Usuário", font=ctk.CTkFont(size=22, weight="bold")
        )
        label_perfil_titulo.pack(pady=(10, 25))

        entry_nome = ctk.CTkEntry(
            inner_frame, placeholder_text="Nome Completo", height=35
        )
        entry_nome.pack(pady=8, fill="x")

        entry_cpf = ctk.CTkEntry(
            inner_frame, placeholder_text="CPF (somente números)", height=35
        )
        entry_cpf.pack(pady=8, fill="x")
        
        entry_profissao = ctk.CTkEntry(
            inner_frame, placeholder_text="Profissão", height=35
        )
        entry_profissao.pack(pady=8, fill="x")

        entry_nova_senha = ctk.CTkEntry(
            inner_frame, placeholder_text="Nova Senha", show="*", height=35
        )
        entry_nova_senha.pack(pady=8, fill="x")

        entry_confirmar_senha = ctk.CTkEntry(
            inner_frame, placeholder_text="Confirmar Nova Senha", show="*", height=35
        )
        entry_confirmar_senha.pack(pady=8, fill="x")

        btn_salvar = ctk.CTkButton(
            inner_frame,
            text="Salvar Alterações",
            height=40,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#3b82f6",
            hover_color="#2563eb"
        )
        btn_salvar.pack(pady=25, fill="x")


