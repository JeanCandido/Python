import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    M = np.hstack([A.astype(float), b.reshape(-1, 1)])
    
    for k in range(n - 1):
        if M[k, k] == 0:
            for i in range(k + 1, n):
                if M[i, k] != 0:
                    M[[k, i]] = M[[i, k]]
                    break
        for i in range(k + 1, n):
            if M[i, k] != 0:
                fator = M[i, k] / M[k, k]
                M[i, k:] -= fator * M[k, k:]
    
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (M[i, -1] - np.dot(M[i, i+1:n], x[i+1:])) / M[i, i]
    
    det = np.prod(np.diag(M[:, :n]))
    return x, det

class SistemaLinearApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resolver Sistema Linear")
        
        self.frame_top = tk.Frame(root)
        self.frame_top.pack(pady=10)
        
        tk.Label(self.frame_top, text="Dimensão:").pack(side=tk.LEFT, padx=5)
        
        self.combo_dim = ttk.Combobox(self.frame_top, values=[str(i) for i in range(2, 11)], width=5)
        self.combo_dim.set("2")
        self.combo_dim.pack(side=tk.LEFT)
        
        tk.Button(self.frame_top, text="Gerar", command=self.gerar_campos).pack(side=tk.LEFT, padx=5)
        
        self.frame_matriz = tk.Frame(root)
        self.frame_matriz.pack(pady=10)
        
        self.frame_botoes = tk.Frame(root)
        self.frame_botoes.pack(pady=10)
        
        tk.Button(self.frame_botoes, text="Resolver", command=self.resolver).pack(side=tk.LEFT, padx=5)
        tk.Button(self.frame_botoes, text="Sair", command=root.quit).pack(side=tk.LEFT, padx=5)
        
        self.frame_resultado = tk.Frame(root)
        self.frame_resultado.pack(pady=10)
        
        self.resultado_text = tk.Text(self.frame_resultado, width=50, height=10)
        self.resultado_text.pack()
        
        self.entries_A = []
        self.entries_b = []
        self.gerar_campos()

    def gerar_campos(self):
        for widget in self.frame_matriz.winfo_children():
            widget.destroy()
        
        n = int(self.combo_dim.get())
        self.entries_A = []
        self.entries_b = []
        
        for i in range(n):
            linha = []
            for j in range(n):
                e = tk.Entry(self.frame_matriz, width=5, justify="center")
                e.grid(row=i, column=j, padx=2, pady=2)
                linha.append(e)
            self.entries_A.append(linha)
            
            e_b = tk.Entry(self.frame_matriz, width=5, justify="center")
            e_b.grid(row=i, column=n, padx=10)
            self.entries_b.append(e_b)

    def resolver(self):
        n = int(self.combo_dim.get())
        
        try:
            A = np.zeros((n, n))
            b = np.zeros(n)
            
            for i in range(n):
                for j in range(n):
                    A[i, j] = float(self.entries_A[i][j].get())
                b[i] = float(self.entries_b[i].get())
            
            x, det = gauss_elimination(A, b)
            
            self.resultado_text.delete("1.0", tk.END)
            self.resultado_text.insert(tk.END, "--- Resultado ---\n")
            for i in range(n):
                self.resultado_text.insert(tk.END, f"x[{i+1}] = {x[i]:.4f}\n")
            self.resultado_text.insert(tk.END, f"\nDeterminante(A) = {det:.4f}\n")
        
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível resolver o sistema.\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaLinearApp(root)
    root.mainloop()
