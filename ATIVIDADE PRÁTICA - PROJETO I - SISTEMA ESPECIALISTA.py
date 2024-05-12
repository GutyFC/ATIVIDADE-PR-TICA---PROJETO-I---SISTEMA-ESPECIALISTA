import tkinter as tk
from tkinter import messagebox

# FUNÇAO PRA AVANÇAR PARA PROXIMA TELA 
def avancar_tela():
    tela_inicial.pack_forget()
    tela_principal.pack()

# FUNÇAO PARA VERIFICAR SE O VALOR ESTA NO INTERVALO DE 0 A 10
def verificar_intervalo(valor):
    if valor < 0 or valor > 10:
        raise ValueError("Valor fora do intervalo permitido (0 a 10)")

# FUNÇAO PARA CALCULAR E EXIBIR RESULTADOS
def calcular_resultados():
    try:
        parametro1 = int(entry_parametro1.get())
        verificar_intervalo(parametro1)
        parametro2 = int(entry_parametro2.get())
        verificar_intervalo(parametro2)
        parametro3 = int(entry_parametro3.get())
        verificar_intervalo(parametro3)
        parametro4 = int(entry_parametro4.get())
        verificar_intervalo(parametro4)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))
        return

    # ZERAR PONTUAÇÕES E PERCENTUAIS
    for i in BD:
        i["PONTUACAO_TOTAL"] = 0
        i["PERCENTUAL"] = 0

    # CALCULAR PONTUAÇÕES BASEADO NOS PARÂMETROS INFORMADOS
    for pos, campeonato in enumerate(BD):
        caracteristicas = campeonato["CARACTERISTICAS"]
        campeonato["PONTUACAO_TOTAL"] += caracteristicas.get("DISPUTA", 0) * parametro1
        campeonato["PONTUACAO_TOTAL"] += caracteristicas.get("QUALIDADE FUTEBOL", 0) * parametro2
        campeonato["PONTUACAO_TOTAL"] += caracteristicas.get("MÉDIA DE GOLS", 0) * parametro3
        campeonato["PONTUACAO_TOTAL"] += caracteristicas.get("TRANSMISSÃO PARA O BRASIL", 0) * parametro4

    # CALCULAR PERCENTUAIS
    total_pontuacao = sum(campeonato["PONTUACAO_TOTAL"] for campeonato in BD)

    # Verificar se total_pontuacao é zero para evitar divisão por zero
    if total_pontuacao == 0:
    # Lidar com essa situação, talvez exibir uma mensagem ou retornar
        messagebox.showerror("Erro", "A pontuação total é zero. Não é possível calcular os percentuais.")
    else:
        for pos, campeonato in enumerate(BD):
            BD[pos]["PERCENTUAL"] = float(campeonato["PONTUACAO_TOTAL"]) / total_pontuacao * 100

    # ORDENAR A LISTA
    BD_ordenado = sorted(BD, key=lambda x: x["PERCENTUAL"], reverse=True)

    # EXIBIR TODOS OS PERCENTUAIS
    resultado_texto.set("\nRESULTADOS PARA OS PARÂMETROS (ordenados):\n")
    for campeonato in BD_ordenado:
        resultado_texto.set(resultado_texto.get() + f"{campeonato['CAMPEONATO']}: {campeonato['PERCENTUAL']:.2f}%\n")

    # ENCONTRAR CAMPEONATO COM MAIOR PERCENTUAL
    campeonato_mais_provavel = max(BD, key=lambda x: x["PERCENTUAL"])
    resultado_texto.set(resultado_texto.get() + f"\nVOCÊ VAI ASSISTIR AO CAMPEONATO: {campeonato_mais_provavel['CAMPEONATO']} com {campeonato_mais_provavel['PERCENTUAL']:.2f}% de probabilidade de atender aos parâmetros especificados.")

# CRIAR JANELA PRINCIPAL
root = tk.Tk()
root.title("Escolha de Campeonato")

# CONFIGURAÇOES DO TKINTER
root.configure(bg='black')

# TELA INICIAL
tela_inicial = tk.Frame(root, bg='black')
tela_inicial.pack(expand=True, fill="both")

label_bem_vindo = tk.Label(tela_inicial, text="Bem-vindo ao programa onde você vai definir qual campeonato deseja assistir!", font=("Arial", 14), bg='black', fg='white')
label_bem_vindo.pack(pady=10)

label_instrucoes = tk.Label(tela_inicial, text="Este programa serve para ajudá-lo a escolher entre os seguintes campeonatos: BRASILEIRÃO, PREMIER LEAGUE, BUNDESLIGA e LALIGA.\nVocê poderá escolher com base nos seguintes parâmetros: DISPUTA, QUALIDADE DO FUTEBOL, MÉDIA DE GOLS e TRANSMISSÃO PARA O BRASIL.", bg='black', fg='white')
label_instrucoes.pack(pady=10)

button_avancar = tk.Button(tela_inicial, text="Avançar", command=avancar_tela, bg='#4CAF50', fg='white', bd=0)
button_avancar.pack(pady=10)

# TELA PRINCIPAL
tela_principal = tk.Frame(root, bg='black')

# LISTA DE CAMPEONATOS E SEUS PARAMETROS
BD=[
    {"CAMPEONATO":"BRASILEIRÃO", "CARACTERISTICAS": {"DISPUTA":10,"QUALIDADE FUTEBOL":2,"MÉDIA DE GOLS":3,"TRANSMISSÃO PARA O BRASIL":10}, "PONTUACAO_TOTAL":0,"PERCENTUAL":0},
    {"CAMPEONATO":"PREMIER LEAGUE", "CARACTERISTICAS": {"DISPUTA":7,"QUALIDADE FUTEBOL":10,"MÉDIA DE GOLS":5,"TRANSMISSÃO PARA O BRASIL":7}, "PONTUACAO_TOTAL":0,"PERCENTUAL":0},
    {"CAMPEONATO":"BUNDESLIGA", "CARACTERISTICAS": {"DISPUTA":3,"QUALIDADE FUTEBOL":7,"MÉDIA DE GOLS":10,"TRANSMISSÃO PARA O BRASIL":6}, "PONTUACAO_TOTAL":0,"PERCENTUAL":0},
    {"CAMPEONATO":"LALIGA", "CARACTERISTICAS": {"DISPUTA":4,"QUALIDADE FUTEBOL":10,"MÉDIA DE GOLS":7,"TRANSMISSÃO PARA O BRASIL":7}, "PONTUACAO_TOTAL":0,"PERCENTUAL":0}
]

# CONFIGURAÇAO DO TKINTER
label_style = {'font': ('Arial', 12), 'bg': 'black', 'fg': 'white'}

# TELA PRINCIPAL
tk.Label(tela_principal, text="Quanto você deseja que o campeonato seja disputado? (de 0 a 10):", **label_style).pack()
entry_parametro1 = tk.Entry(tela_principal, bg='#F2F2F2', bd=2)
entry_parametro1.pack()

tk.Label(tela_principal, text="Quanto você deseja que seja o nível da qualidade do futebol jogado? (de 0 a 10):", **label_style).pack()
entry_parametro2 = tk.Entry(tela_principal, bg='#F2F2F2', bd=2)
entry_parametro2.pack()

tk.Label(tela_principal, text="Para você, o quanto a média de gols é importante? (de 0 a 10):", **label_style).pack()
entry_parametro3 = tk.Entry(tela_principal, bg='#F2F2F2', bd=2)
entry_parametro3.pack()

tk.Label(tela_principal, text="Quanto a transmissão para o Brasil importa para você? (de 0 a 10):", **label_style).pack()
entry_parametro4 = tk.Entry(tela_principal, bg='#F2F2F2', bd=2)
entry_parametro4.pack()

button_calcular = tk.Button(tela_principal, text="Calcular", command=calcular_resultados, bg='#4CAF50', fg='white', bd=0)
button_calcular.pack(pady=10)

resultado_texto = tk.StringVar()
resultado_label = tk.Label(tela_principal, textvariable=resultado_texto, **label_style)
resultado_label.pack()

# Executar o loop de eventos
root.mainloop()
