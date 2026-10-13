import customtkinter as ctk

# Configuração inicial do tema e aparência
ctk.set_appearance_mode("dark")  # Opções: "dark", "light", "system"
ctk.set_default_color_theme("blue")  # Opções: "blue", "green", "dark-blue"

class Calculadora(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da janela
        self.title("Calculadora CTK")
        self.geometry("520x520")
        self.resizable(False, False)

        # Variável para armazenar a expressão matemática
        self.expressao = ""

        # Tela de exibição (Display)
        self.display = ctk.CTkEntry(
            self, 
            width=340, 
            height=70, 
            font=("Arial", 28, "bold"), 
            justify="right",
            state="readonly"
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20)
        self.atualizar_display("0")

        # Configuração dos botões
        self.criar_botoes()

    def criar_botoes(self):
        # Grade de botões: (Texto, Linha, Coluna, Cor do botão)
        botoes = [
            ('C', 1, 0, "#d9534f"), ('(', 1, 1, "#5bde92"), (')', 1, 2, "#5bc0de"), ('/', 1, 3, "#f0ad4e"),
            ('7', 2, 0, None),      ('8', 2, 1, None),      ('9', 2, 2, None),      ('*', 2, 3, "#f0ad4e"),
            ('4', 3, 0, None),      ('5', 3, 1, None),      ('6', 3, 2, None),      ('-', 3, 3, "#f0ad4e"),
            ('1', 4, 0, None),      ('2', 4, 1, None),      ('3', 4, 2, None),      ('+', 4, 3, "#f0ad4e"),
            ('0', 5, 0, None),      ('.', 5, 1, None),      ('=', 5, 2, "#5cb85c")
        ]

        for texto, linha, coluna, cor in botoes:
            # Define o tamanho de colunas extras para o botão de igual '=' que ocupa 2 colunas
            colspan = 2 if texto == '=' else 1
            
            # Cores padrão do CustomTkinter se nenhuma for especificada
            cor_botao = cor if cor else ctk.ThemeManager.theme["CTkButton"]["fg_color"]
            cor_hover = "#333333" if not cor else None

            btn = ctk.CTkButton(
                self, 
                text=texto, 
                width=75 if texto != '=' else 160,
                height=60, 
                font=("Arial", 20, "bold"),
                fg_color=cor_botao,
                hover_color=cor_hover,
                command=lambda t=texto: self.ao_clicar(t)
            )
            btn.grid(row=linha, column=coluna, columnspan=colspan, padx=5, pady=5, sticky="nsew")

    def ao_clicar(self, valor):
        if valor == 'C':
            self.expressao = ""
            self.atualizar_display("0")
        elif valor == '=':
            try:
                # Calcula o resultado de forma segura
                resultado = str(eval(self.expressao))
                # Formata para tirar o .0 se for um número inteiro
                if resultado.endswith('.0'):
                    resultado = resultado[:-2]
                self.atualizar_display(resultado)
                self.expressao = resultado
            except Exception:
                self.atualizar_display("Erro")
                self.expressao = ""
        else:
            # Evita acumular caracteres se a tela mostrar erro ou zero inicial
            if self.expressao == "" and valor in "+-*/.)":
                if valor != '.': 
                    return
            
            self.expressao += str(valor)
            self.atualizar_display(self.expressao)

    def atualizar_display(self, texto):
        self.display.configure(state="normal")
        self.display.delete(0, ctk.END)
        self.display.insert(0, texto)
        self.display.configure(state="readonly")

# Executa o aplicativo
if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
