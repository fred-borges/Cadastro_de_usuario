import tkinter as tk
import psycopg2

def adicionar():
    nome = text_nome.get()
    apelido = text_apelido.get()
    passs = text_password.get()

    conn = psycopg2.connect(
        dbname='postgres', 
        user='postgres', 
        password='sua_password', 
        host='localhost'
    )

    cur = conn.cursor()

    cur.execute("INSERT INTO cadastro_de_usuarios (nome, apelido, passs) VALUES (%s, %s, %s)", (nome, apelido, passs))
    
    # Confirma a transação
    conn.commit()
    
    # Fecha o cursor e a conexão
    cur.close()
    conn.close()
    
    # Limpa os campos de entrada após a inserção
    text_nome.delete(0, tk.END)
    text_apelido.delete(0, tk.END)
    text_password.delete(0, tk.END)



root = tk.Tk()
root.geometry('400x300')
root.title("Cadastro de usuários")
root.resizable(False, False)
root.config(cursor="watch")


label = tk.Label(root)
label = tk.Label(
    root,
    text='Cadastro de usuário',
    font=("Helvetica", 14))
label.pack(ipadx=10, ipady=10)

label_nome = tk.Label(root, text='Nome: ')
label_nome.pack(ipadx=10, ipady=0)
text_nome = tk.Entry(root)
text_nome.pack(padx=10, pady=10)


label_apelido = tk.Label(root, text='Apelido: ')
label_apelido.pack(ipadx=10, ipady=0)

text_apelido = tk.Entry(root)
text_apelido.pack(padx=10, pady=10)

label_password = tk.Label(root, text='Password: ')
label_password.pack(ipadx=10, ipady=0)

text_password = tk.Entry(root, show="*")
text_password.pack(padx=10, pady=10)

botao = tk.Button(root, text="Cadstrar", command=adicionar)
botao.pack(padx=10, pady=10)


root.mainloop()
