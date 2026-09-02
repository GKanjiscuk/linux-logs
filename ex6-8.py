import subprocess

def exercicio_6():
    print("-" * 40)
    print("** Exercício 6: Última Inicialização do Sistema **")
    # Busca a data e a hora do último evento de boot no log do sistema.
    comando = "grep 'Startup finished' /var/log/syslog | tail -n 1"
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    print(resultado.stdout.strip() if resultado.stdout else "Nenhum registro encontrado.")

def exercicio_7():
    print("\n" + "-" * 40)
    print("** Exercício 7: Eventos de Desligamento e Reinicialização **")
    # Encontra e lista eventos de shutdown ou reboot.
    comando = "grep -E 'Shutting down|Rebooting' /var/log/syslog"
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    print(resultado.stdout.strip() if resultado.stdout else "Nenhum registro encontrado.")

def exercicio_8():
    print("\n" + "-" * 40)
    print("** Exercício 8: Serviços Iniciados ou Parados **")
    # Lista a data e o nome dos serviços que tiveram seu status alterado (iniciado/parado).
    comando = "grep -E 'systemd\\[1\\]: (Started|Stopped)' /var/log/syslog | awk '{print $1, $2, $3, \"-\", $6, $7, $8}'"
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    print(resultado.stdout.strip() if resultado.stdout else "Nenhum registro encontrado.")
    print("-" * 40)

# Chamada das funções
if __name__ == "__main__":
    exercicio_6()