import subprocess

def exercicio_11():
    print("-" * 40)
    print("** Exercício 11: Pacotes Instalados **")
    # Filtra o log de pacotes e lista instalações com a data
    comando = "grep ' install ' /var/log/dpkg.log | awk '{print $1, $2, \"Pacote:\", $4}'"
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    print(resultado.stdout.strip() if resultado.stdout else "Nenhum registro encontrado.")

def exercicio_12():
    print("\n" + "-" * 40)
    print("** Exercício 12: Pacotes Removidos **")
    # Identifica todos os pacotes que foram removidos do sistema
    comando = "grep ' remove ' /var/log/dpkg.log | awk '{print $1, $2, \"Pacote:\", $4}'"
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    print(resultado.stdout.strip() if resultado.stdout else "Nenhum registro encontrado.")

def exercicio_13():
    print("\n" + "-" * 40)
    print("** Exercício 13: Rastreio de Comandos de Pacotes **")
    # Rastreia quem executou comandos de pacotes (apt, dpkg) e qual ação foi realizada
    comando = "grep 'sudo:' /var/log/auth.log | grep -E 'apt|apt-get|dpkg' | awk '{print $1, $2, $3, \"Usuário:\", $6, \"Comando:\", $9, $10, $11, $12}'"
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    print(resultado.stdout.strip() if resultado.stdout else "Nenhum registro encontrado.")
    print("-" * 40)

# Chamada das funções
if __name__ == "__main__":
    exercicio_11()
    exercicio_12()
    exercicio_13()