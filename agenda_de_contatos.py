def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
  contato = {"Contato": nome_contato, "Telefone": telefone_contato, "E-mail": email_contato, "Favoritado": False}
  contatos.append(contato)
  print(f"O contato {nome_contato} foi adicionado com sucesso!") 

def ver_contatos(contatos):
  print("\nAgenda de contatos:")
  

contatos = []

while True:
  print("\nAgenda de Contatos")
  print("1. Adicionar contato")
  print("2. Visualizar contatos")
  print("3. Editar contato")
  print("4. Marcar / desmarcar favorito")
  print("5. Visualizar contatos favoritos")
  print("6. Apagar contato")
  print("7. Sair")

  escolha = input("Escolha uma opção: ")

  if escolha == "1":
    nome_contato = input("Digite o nome: ")
    telefone_contato = input("Digite o telefone: ")
    email_contato = input("Digite o e-mail: ")
    adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)

  elif escolha == "2":
    ver_contatos(contatos)