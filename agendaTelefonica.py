agenda = {}

def incluirNovoNome(nome, telefones):
    nome = str(input('nome '))
    if nome not in agenda:
        agenda[nome] = telefones
        print(f"{nome} adicionado com os telefones: {telefones}")
    else:
        print(f"{nome} já existe na agenda.")

def incluirTelefone(nome, telefone):
    if nome in agenda:
        agenda[nome].append(telefone)
        print(f"Telefone {telefone} adicionado a {nome}.")
    else:
        resposta = input(f"{nome} não está na agenda. Deseja incluí-lo? (s/n): ")
        if resposta.lower() == 's':
            incluirNovoNome(nome, [telefone])
        else:
            print("Operação cancelada.")

def excluirTelefone(nome, telefone):
    if nome in agenda:
        if telefone in agenda[nome]:
            agenda[nome].remove(telefone)
            print(f"Telefone {telefone} removido de {nome}.")
            if not agenda[nome]:  # Se a lista de telefones estiver vazia
                del agenda[nome]
                print(f"{nome} removido da agenda, pois não há mais telefones.")
        else:
            print(f"Telefone {telefone} não encontrado para {nome}.")
    else:
        print(f"{nome} não encontrado na agenda.")

def excluirNome(nome):
    if nome in agenda:
        del agenda[nome]
        print(f"{nome} removido da agenda.")
    else:
        print(f"{nome} não encontrado na agenda.")

def consultarTelefone(nome):
    if nome in agenda:
        return agenda[nome]
    else:
        print(f"{nome} não encontrado na agenda.")
        return None

# Exemplos de uso
incluirNovoNome("Alice", ["1234-5678", "8765-4321"])
incluirTelefone("Alice", "5555-5555")
incluirTelefone("Bob", "1111-1111")
excluirTelefone("Alice", "1234-5678")
excluirNome("Bob")
telefones = consultarTelefone("Alice")
print(f"Telefones de Alice: {telefones}")
