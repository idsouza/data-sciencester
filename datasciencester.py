''' Dicts de usuários '''
users = [
    { "id": 0, "name": "Hero"},
    { "id": 1, "name": "Dunn"},
    { "id": 2, "name": "Sue"},
    { "id": 3, "name": "Chi"},
    { "id": 4, "name": "Thor"},
    { "id": 5, "name": "Clive"},
    { "id": 6, "name": "Hicks"},
    { "id": 7, "name": "Devin"},
    { "id": 8, "name": "Kate"},
    { "id": 9, "name": "Klein"}
]

''' Tuplas com os relacionamentos entre os usuários '''
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

''' Cria lista de amigos para cada usuário'''
def criar_lista_amigos():
    for user in users:
        user['friends'] = []
    
    for i, j in friendships:
        print(users[i]['name'], "friend of", users[j]['name'])
        users[i]['friends'].append(j)
        users[j]['friends'].append(i)

''' Soma número total de conexões '''
def obter_total_conexoes():    
    return sum(len(user['friends']) for user in users)

''' Cálculo número médio de conexões '''
def calcular_media_conexoes():
    total_con = obter_total_conexoes()
    return total_con / len(users)


''' Obtem sugestoes de conexoes '''
def obter_sugest_conexoes(user_id):
    lista = (tuple(fof for fof in users[friend_id]['friends'] if fof != user_id) 
                       for friend_id in users[user_id]['friends'])
    
    return tuple(lista)

criar_lista_amigos()
print("Média de conxões: ", calcular_media_conexoes())
obter_sugest_conexoes(0)