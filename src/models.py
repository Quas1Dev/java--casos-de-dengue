class Municipality:
    def __init__ (self, cod_municipality, name):
        self.cod_municipality = cod_municipality
        self.name = name

class Populacao:
    def __init__(self, cod_municipality, year, amount):
        self.cod_municipality = cod_municipality
        self.year = year
        self.amount = amount

class Dengue:
    def __init__(self, cod_municipality, year, cases):
        self.cod_municipality = cod_municipality
        self.year = year
        self.cases = cases
