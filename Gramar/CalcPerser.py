from sly import Parser, Lexer
from Gramar import CalcLexer
from Gramar import GF1234577
from Errors_custom import PerserError

class CalcParser(Parser):
    tokens = CalcLexer.tokens

    precedence = (
        ('left', PLUS, MINUS),
        ('left', TIMES, DIVIDE)
    )

    # Program główny
    @_('PROGRAM IS declarations BEGIN statements END')
    def program(self, p):

        return {'type': 'program', 'declarations': p.declarations, 'statements': p.statements}

    # Deklaracje zmiennych (IDENTIFIER)
    @_('declarations COMMA IDENTIFIER')
    def declarations(self, p):
        return p.declarations + [p.IDENTIFIER]  # Dodajemy nową zmienną do listy deklaracji

    @_('IDENTIFIER')
    def declarations(self, p):
        return [p.IDENTIFIER]  # Tylko jedna zmienna

    # Instrukcje
    @_('statements statement')
    def statements(self, p):
        return p.statements + [p.statement]

    @_('statement')
    def statements(self, p):
        return [p.statement]

    # Przypisanie zmiennej
    @_('IDENTIFIER ASSIGN expression SEMICOLON')
    def statement(self, p):

        return {'type': 'assignment', 'variable': p.IDENTIFIER, 'value': p.expression}

    # Instrukcja odczytu
    @_('READ IDENTIFIER SEMICOLON')
    def statement(self, p):

        return {'type': 'read', 'variable': p.IDENTIFIER}

    # Instrukcja wypisania
    @_('WRITE expression SEMICOLON')
    def statement(self, p):

        return {'type': 'write', 'value': p.expression}

    # Wyrażenie arytmetyczne
    @_('expression PLUS term')
    def expression(self, p):
        return {'type': 'expression', 'left': p.expression, 'operator': '+', 'right': p.term}

    @_('term')
    def expression(self, p):
        return p.term

    # Termin (operacje takie jak mnożenie, dzielenie, etc.)
    @_('term TIMES factor')
    def term(self, p):
        return {'type': 'term', 'left': p.term, 'operator': '*', 'right': p.factor}

    @_('factor')
    def term(self, p):
        return p.factor

    # Czynnik - może to być liczba lub zmienna
    @_('NUMBER')
    def factor(self, p):
        return {'type': 'number', 'value': int(p.NUMBER)}

    @_('IDENTIFIER')
    def factor(self, p):
        return {'type': 'identifier', 'name': p.IDENTIFIER}

    # Obsługa nawiasów
    @_('LPAREN expression RPAREN')
    def factor(self, p):
        return p.expression

    # Obsługa błędów składniowych
    def error(self, p):
        raise PerserError(p.lineno, f"cant proces {p.type} in this context")

