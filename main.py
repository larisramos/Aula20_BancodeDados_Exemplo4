import sqlite3, os
nomeBD = input("Nome do Banco de Dados: ")
try:
  conector = sqlite3.connect(nomeBD)
  cursor = conector.cursor()
  id = '1'
  while id != '0':
    id = input ("Digite o índice [0 - Sair]: ")
    if id != '0':
      cursor.execute("DELETE FROM agenda WHERE id=?", (id))
      conector.commit()
      print("Okay, Contato REMOVIDO")
  cursor.close()
  conector.close()
except sqlite3.Error as error:
  print("Erro: BD não encontrado")
  print("Erro: ", error)
  os.remove(nomeBD)