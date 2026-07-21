N, T = map(int, input().split())

alunos = []

for _ in range(N):
    nome, habilidade = input().split()
    alunos.append((int(habilidade), nome))

alunos.sort(reverse=True)

times = [[] for _ in range(T)]

for indice, (_, nome) in enumerate(alunos):
    times[indice % T].append(nome)

for indice, time in enumerate(times, start=1):
    time.sort()

    print(f"Time {indice}")

    for nome in time:
        print(nome)

    print()