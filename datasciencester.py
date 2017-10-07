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

for user in users:
    user['friends'] = []

''' Cria lista de amigos para cada usuário'''
for i, j in friendships:
    print(users[i]['name'], "friend of", users[j]['name'])
    users[i]['friends'].append(j)
    users[j]['friends'].append(i)

''' Soma número total de conexões '''
total_con = 0
total_con = sum(len(user['friends']) for user in users)

''' Cálculo número médio de conexões '''
media_con = total_con / len(users)
print(media_con)

print('Testando commit...')







