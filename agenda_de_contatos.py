def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
  contato = {"Contato": nome_contato, "Telefone": telefone_contato, "E-mail": email_contato, "Favoritado": False}
  contatos.append(contato)
  print(f"O contato {nome_contato} foi adicionado com sucesso!") 

def ver_contatos(contatos):
  print("\nAgenda de contatos:")
  for indice, contato in enumerate(contatos, start=1):
    status = "★" if contato["Favoritado"] else " "
    nome = contato["Contato"]
    telefone = contato["Telefone"]
    email = contato["E-mail"]
    print(f"{indice}.[{status}] {nome} | {telefone} | {email}") 

def editar_contato(contatos):
  ver_contatos(contatos)
  try:
    indice = int(input("Digite o número do contato que deseja editar: "))
    indice -= 1
    contato = contatos[indice]
  except (ValueError, IndexError):
    print("Contato inválido")

  novo_nome = input("Digite o novo nome: ")
  novo_telefone = input("Digite o novo telefone: ")
  novo_email = input("Digite o novo e-mail: ")

  contato["Contato"] = novo_nome
  contato["Telefone"] = novo_telefone
  contato["E-mail"] = novo_email

  print("Contato atualizado com sucesso!")

def favoritar_contato(contatos):
  ver_contatos(contatos)
  indice = int(input("Digite o número do contato que deseja favoritar: "))
  indice -= 1

  contato = contatos[indice]

  contato["Favoritado"] = not contato["Favoritado"]
  # Truque fazendo com que False = True e True = False

  if contato["Favoritado"]:
    print("Contato marcado como favorito!")
  else:
    print("Contato removido dos favoritos!")

def ver_favoritos(contatos):
  print("\nVer favoritos:")
  
  for contato in contatos:
    if contato["Favoritado"]:

      nome = contato["Contato"]
      telefone = contato["Telefone"]
      email = contato["E-mail"]

      print(f"★  {nome} | {telefone} | {email}")

def deletar_contato(contatos):
  ver_contatos(contatos)
  indice = int(input("Digite o número do contato que deseja remover: "))
  indice -= 1

  contato_removido = contatos.pop(indice)
  print(f"O contato {contato_removido['Contato']} foi removido com sucesso!")
    
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

  escolha = input("\nEscolha uma opção: ")

  if escolha == "1":
    nome_contato = input("\nDigite o nome: ")
    telefone_contato = input("Digite o telefone: ")
    email_contato = input("Digite o e-mail: ")
    adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)

  elif escolha == "2":
    ver_contatos(contatos)

  elif escolha == "3":
    editar_contato(contatos)

  elif escolha == "4":
    favoritar_contato(contatos)

  elif escolha == "5":
    ver_favoritos(contatos)  

  elif escolha == "6":
    deletar_contato(contatos)

  elif escolha == "7":
    break

print("Programa finalizado!")