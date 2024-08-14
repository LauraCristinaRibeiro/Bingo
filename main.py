import tkinter as tk
import random

class BingoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Bingo')


        #lista de números sorteados
        self.ls_num_sorteados = []

        #Label para exibir números sorteados
        self.lbl_result = tk.Label(root, text='', font=('Arial', 14))
        self.lbl_result.pack(pady=20)


        #Botão para sortear números
        self.btn_sortear = tk.Button(root, text="Sortear", command=self.sortear_numeros, font=('Arial', 14))
        self.btn_sortear.pack(pady=10)

        #Botão para reiniciar o jogo
        self.btn_reset = tk.Button(root, text="Reiniciar o jogo", command=self.reset_jogo, font=('Arial', 14))
        self.btn_reset.pack(pady=10)

        #Função de sortear um número de 1 a 75 e adiciona a lista
    def sortear_numeros(self):
        if len(self.ls_num_sorteados) < 75:
            numeroSorteado = random.randint(1, 75)
            while numeroSorteado in self.ls_num_sorteados:
                numeroSorteado = random.randint(1, 75)
            self.ls_num_sorteados.append(numeroSorteado)
            self.lbl_result.config(text=', '.join(map(str, self.ls_num_sorteados)))
        else:
            self.lbl_result.config(text="Bingo encerrado!")


    def reset_jogo(self):
        self.ls_num_sorteados.clear()
        self.lbl_result.config(text='')


if __name__ == "__main__":
    root = tk.Tk()
    app = BingoApp(root)
    root.mainloop()


