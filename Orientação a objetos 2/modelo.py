class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'


class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
anc = Filme('A Noiva Cadáver', 2005, 74)

supernatural = Serie('supernatural', 2005, 15)
house = Serie('Dr. House', 2004, 8)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

anc.dar_likes()
anc.dar_likes()

supernatural.dar_likes()
supernatural.dar_likes()

house.dar_likes()


listaFS = [vingadores, supernatural, anc, house]

PlaylistFS = Playlist('Filminhos', listaFS)

print(f'tamanho da playlist: {len(PlaylistFS)}')

for Programa in PlaylistFS:
    print(Programa)
