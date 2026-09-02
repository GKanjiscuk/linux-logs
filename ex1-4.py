import subprocess

def exercicio_1():
    print("-" * 40)
    print("** Exercício 1: Tentativas de Senha Incorreta **")
    # Filtra falhas de login, extrai usuários e conta ocorrências
    comando = "grep -E 'Failed password|authentication failure' /var/log/auth.log | awk '{print $9}' | sort | uniq -c"
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    print(resultado.stdout.strip() if resultado.stdout else "Nenhum registro encontrado.")

def exercicio_2():
    print("\n" + "-" * 40)
    print("** Exercício 2: Logins Bem-Sucedidos **")
    # Filtra logins com sucesso e extrai data, hora e usuário
    comando = "grep 'session opened for user' /var/log/auth.log | awk '{print $1, $2, $3, \"Usuário:\", $11}'"
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    print(resultado.stdout.strip() if resultado.stdout else "Nenhum registro encontrado.")

def exercicio_3():
    print("\n" + "-" * 40)
    print("** Exercício 3: Auditoria do Sudo **")
    # Filtra uso do sudo e extrai data, hora e usuário
    comando = "grep 'sudo:' /var/log/auth.log | awk '{print $1, $2, $3, \"Usuário:\", $6}'"
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    print(resultado.stdout.strip() if resultado.stdout else "Nenhum registro encontrado.")

def exercicio_4():
    print("\n" + "-" * 40)
    print("** Exercício 4: Logins Rejeitados (Usuários Inexistentes) **")
    # Busca tentativas de login de usuários que não existem no sistema
    comando = "grep 'Invalid user' /var/log/auth.log"
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    print(resultado.stdout.strip() if resultado.stdout else "Nenhum registro encontrado.")
    print("-" * 40)

# Chamada das funções
if __name__ == "__main__":
    exercicio_1()
    exercicio_2()
    exercicio_3()
    exercicio_4()