#Gerador de senhas com ou sem caracteres do tip letras 
import random
import string 
print('Bem Vindo ao Gerador de senhas automatico:') 
escolha = int(input('Escolha 1 se deseja uma senha com apenas caracteres, ou escolha 2 se deseja alfanuméricos:'))
if escolha == 1:
  senha_numerico= random.randint(1000, 9999)
  print(f'Senha com apenas números:{senha_numerico}')

elif escolha == 2:
 def senha_alfanumericos(tamanho=4, caracteres=string.ascii_letters + string.digits):
    return ''.join(random.choice(caracteres) for _ in range(tamanho)) 
 print('Senha com alfanumericos:')
 print(senha_alfanumericos()) 

else: 
    print('Isso não é uma opção valida. Por favor, escolha novamente.')