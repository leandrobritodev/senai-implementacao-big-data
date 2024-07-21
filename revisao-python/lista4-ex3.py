### Lista 4 - Exercício 3  ###

import time
print("=" * 5 + "Speak" + "=" * 5)
time.sleep(1)
texto = input("Habla mona: ")

def speak(texto):
  substitutos = {"A":"4", "B":"8", "E":"3", "I":"1", "O":"0", "T":"7"}
  for letra, substitutos in substitutos.items():
    texto = texto.replace(letra.upper(), substitutos)
    texto = texto.replace(letra.lower(), substitutos)
  return texto

print(speak(texto))
