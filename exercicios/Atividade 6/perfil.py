import requests

def gerar_perfil_usuario():
    """
    Gera um perfil de usuário aleatório usando a API Random User Generator.

    Retorna:
        dict: Dicionário com nome, email e país do usuário.
    """
    url = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        usuario = dados['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        return {"nome": nome, "email": email, "pais": pais}
    except Exception as e:
        print(f"Erro ao obter perfil: {e}")
        return None

if __name__ == "__main__":
    perfil = gerar_perfil_usuario()
    if perfil:
        print(f"Nome: {perfil['nome']}")
        print(f"E-mail: {perfil['email']}")
        print(f"País: {perfil['pais']}")
    else:
        print("Não foi possível gerar o perfil do usuário.")