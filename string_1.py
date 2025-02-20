nome = "RaFaEl"
saldo = 1000.56789

print(nome.lower())
print(nome.upper())
print(nome.title())

texto = "    Olá, mundo!    "
print(texto.strip())
print(texto.lstrip())
print(texto.rstrip())
print(texto.replace("mundo", "Python").strip())
print(texto.strip().center(20, "#"))
print(texto.strip().ljust(20, "#"))
print(texto.strip().rjust(20, "#"))
print(texto.strip().zfill(20))

print(f"Me chamo Rafael e meu saldo é de R${saldo:20.2f}")



