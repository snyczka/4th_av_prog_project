import unittest
from doctest import testfile
from operator import concat
from os.path import split

import ply.lex as lex
import ply.yacc as yacc
from Tools.scripts.find_recursionlimit import test_getitem

#from main.word_buffer import word_buffer


translator = {"SELECT": "TRAEME",
            "ANY": "TODO",
            "FROM": "DE LA TABLA",
            "WHERE": "DONDE",
            "GROUP BY": "AGRUPANDO POR",
            "JOIN": "MEZCLANDO",
            "ON": "EN",
            "DISTINCT": "LOS DISTINTOS",
            "COUNT": "CONTANDO",
            "INSERT INTO": "METE EN",
            "VALUES": "LOS VALORES",
            "UPDATE": "ACTUALIZA",
            "SET": "SETEA",
            "DELETE FROM": "BORRA DE LA TABLA",
            "ORDER BY": "ORDENA POR",
            "LIMIT": "COMO MUCHO",
            "HAVING": "WHERE DEL GROUP BY",
            "EXISTS": "EXISTE",
            "IN": "EN ESTO:",
            "BETWEEN": "ENTRE",
            "LIKE": "PARECIDO A",
            "IS NULL": "ES NULO",
            "ALTER TABLE": "CAMBIA LA TABLA",
            "ADD COLUMN": "AGREGA LA COLUMNA",
            "DROP COLUMN": "ELIMINA LA COLUMNA",
            "CREATE TABLE": "CREA LA TABLA",
            "DROP TABLE": "TIRA LA TABLA",
            "DEFAULT": "POR DEFECTO",
            "UNIQUE": "UNICO",
            "PRIMARY KEY": "CLAVE PRIMA",
            "FOREIGN KEY": "CLAVE REFERENTE",
            "NOT NULL": "NO NULO",
            "CAST": "TRANSFORMA A",
            "AND" : "Y",

              "TRAEME": "SELECT",
              "TODO": "ANY",
              "DE LA TABLA": "FROM",
              "DONDE": "WHERE",
              "AGRUPANDO POR": "GROUP BY",
              "MEZCLANDO": "JOIN",
              "EN": "ON",
              "LOS DISTINTOS": "DISTINCT",
              "CONTANDO": "COUNT",
              "METE EN": "INSERT INTO",
              "LOS VALORES": "VALUES",
              "ACTUALIZA": "UPDATE",
              "SETEA": "SET",
              "BORRA DE LA TABLA": "DELETE FROM",
              "ORDENA POR": "ORDER BY",
              "COMO MUCHO": "LIMIT",
              "WHERE DEL GROUP BY": "HAVING",
              "EXISTE": "EXISTS",
              "EN ESTO": "IN",
              "ENTRE": "BETWEEN",
              "PARECIDO A": "LIKE",
              "ES NULO": "IS NULL",
              "CAMBIA LA TABLA": "ALTER TABLE",
              "AGREGA LA COLUMNA": "ADD COLUMN",
              "ELIMINA LA COLUMNA": "DROP COLUMN",
              "CREA LA TABLA": "CREATE TABLE",
              "TIRA LA TABLA": "DROP TABLE",
              "POR DEFECTO": "DEFAULT",
              "UNICO": "UNIQUE",
              "CLAVE PRIMA": "PRIMARY KEY",
              "CLAVE REFERENTE": "FOREIGN KEY",
              "NO NULO": "NOT NULL",
              "TRANSFORMA A": "CAST",
              "Y" : "AND"
              }

tokenizer = {"SELECT",
             "ANY",
             "FROM",
             "WHERE",
             "GROUP BY",
             "JOIN",
             "ON",
             "DISTINCT",
             "COUNT",
             "INSERT INTO",
             "VALUES",
             "UPDATE",
             "SET",
             "DELETE FROM",
             "ORDER BY",
             "LIMIT",
             "HAVING",
             "EXISTS",
             "IN",
             "BETWEEN",
             "LIKE",
             "IS NULL",
             "ALTER TABLE",
             "ADD COLUMN",
             "DROP COLUMN",
             "CREATE TABLE",
             "DROP TABLE",
             "DEFAULT",
             "UNIQUE",
             "PRIMARY KEY",
             "FOREIGN KEY",
             "NOT NULL",
             "CAST"
             }

tokens = (
        'FROM',
        'SELECT',
        'ANY',
        'WHERE',
        'GROUP_BY',
        'JOIN',
        'ON',
        'DISTINCT',
        'COUNT',
        'INSERT_INTO',
        'VALUES',
        'UPDATE',
        'SET',
        'DELETE_FROM',
        'ORDER_BY',
        'LIMIT',
        'HAVING',
        'EXISTS',
        'IN',
        'BETWEEN',
        'LIKE',
        'IS_NULL',
        'ALTER_TABLE',
        'ADD_COLUMN',
        'DROP_COLUMN',
        'CREATE_TABLE',
        'DROP_TABLE',
        'DEFAULT',
        'UNIQUE',
        'PRIMARY_KEY',
        'FOREIGN_KEY',
        'NOT_NULL',
        'CAST',
        'NAME',
        'NUMBER',
        'MINUS',
        'EQUALS',
        'LPAREN',
        'RPAREN',
        'AND',
        'GREATER_THAN',
        'LESSER_THAN',
        'END',
        'UP_COMMA',
        'COMMA',
        'DOT'
          )

t_FROM = r'DE\sLA\sTABLA'
t_SELECT = r'TRAEME'
t_ANY = r'TODO'
t_WHERE = r'DONDE'
t_GROUP_BY = r'AGRUPANDO\sPOR'
t_JOIN = r'MEZCLANDO'
t_ON = r'EN'
t_DISTINCT = r'LOS\sDISTINTOS'
t_COUNT = r'CONTANDO'
t_INSERT_INTO = r'METE\sEN'
t_VALUES = r'LOS\sVALORES'
t_UPDATE = r'ACTUALIZA'
t_SET = r'SETEA'
t_DELETE_FROM = r'BORRA\sDE\sLA\sTABLA'
t_ORDER_BY = r'ORDENA\sPOR'
t_LIMIT = r'COMO\sMUCHO'
t_HAVING = r'WHERE\sDEL\sGROUP\sBY'
t_EXISTS = r'EXISTE'
t_IN = r'EN\sESTO:'
t_BETWEEN = r'ENTRE'
t_LIKE = r'PARECIDO\sA'
t_IS_NULL = r'ES\sNULO'
t_ALTER_TABLE = r'CAMBIA\sLA\sTABLA'
t_ADD_COLUMN = r'AGREGA\sLA\sCOLUMNA'
t_DROP_COLUMN = r'ELIMINA\sLA\sCOLUMNA'
t_CREATE_TABLE = r'CREA\sLA\sTABLA'
t_DROP_TABLE = r'TIRA\sLA\sTABLA'
t_DEFAULT = r'POR\sDEFECTO'
t_UNIQUE = r'UNICO'
t_PRIMARY_KEY = r'CLAVE\sPRIMA'
t_FOREIGN_KEY = r'CLAVE\sREFERENTE'
t_NOT_NULL = r'NO\sNULO'
t_CAST = r'TRANSFORMA\sA'
t_MINUS = r'-'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_UP_COMMA = r'\''
t_AND = r'Y'
t_GREATER_THAN = r'>'
t_LESSER_THAN = r'<'
t_END = r';'
t_COMMA = r','
t_DOT = r'.'


def t_NUMBER(t):
    r'\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor numerico no valido %d", t.value)
        t.value = 0
    return t


    return t

special_words = set()
for x in list(translator.keys()):
    composite = x.split(' ')
    if len(composite) > 1:
        for y in composite:
            special_words.add(y)

#possible = word_buffer()



def t_NAME(t):
    r'[a-zA-Z_*][a-zA-Z0-9_]*'
    t.value = t.value.replace('*', 'ANY')
    looker = t.value.upper()
    if looker in special_words:
        up_to_now = lexer.lexdata[t.lexer.lexpos +1:].split(' ')
        up_to_now.append('SAFETY')
        t.lexer.lexpos = t.lexer.lexpos + 1
        while up_to_now[0].upper().replace(';', '') in special_words:
            selection = up_to_now.pop(0).replace(';', '')
            looker = looker + ' ' + selection.upper()
            t.lexer.lexpos = t.lexer.lexpos + len(selection)
        if translator.get(looker) is not None:
            if(looker in tokenizer):
                t.type = looker
            else:
                t.type = translator.get(looker).replace(" ", "_").replace(":", '')
            t.type.replace(" ", "_").replace(":", "")
            t.value = translator.get(looker).replace('ANY', '*')
        else:
            return None
    elif translator.get(t.value) is not None:
        if(looker in tokenizer):
            t.type = looker
        else:
            t.type = translator.get(looker).replace(" ", "_").replace(":", '')
        t.type.replace(" ", "_").replace(":", "")
        t.value = translator.get(t.value).replace('ANY', '*')

    return t


t_ignore = " \t"

def t_newline(t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")


def t_error(t):
        print("Digito invalido '%s'" % t.value[0])
        t.lexer.skip(1)


lexer = lex.lex()

precedence = (
    ('right', 'GREATER_THAN', 'LESSER_THAN'),
    ('right', 'MINUS')
)

def p_querry(p):
    '''statement : query END'''
    p[0] = p[1] + ';'
    return p[0]

def p_empty(p):
    '''empty :'''
    pass

def p_query_selection(p):
    '''query : SELECT attributes FROM grouping
             | SELECT COUNT LPAREN attributes RPAREN FROM grouping
             | SELECT attributes FROM grouping JOIN NAME ON joiner condition
             | SELECT attributes FROM grouping GROUP_BY NAME
             | SELECT COUNT LPAREN attributes RPAREN FROM grouping GROUP_BY NAME
             | SELECT COUNT LPAREN attributes RPAREN FROM grouping GROUP_BY NAME HAVING bool
             | SELECT attributes FROM grouping GROUP_BY NAME ORDER_BY attributes
             | SELECT attributes FROM grouping GROUP_BY NAME HAVING bool'''
    p[0] = p[1]
    openPare = False
    for x in p[2:]:
        if x is not None:
            if x == '(' or openPare:
                openPare = True
                if x == ')':
                    openPare = False
                p[0] = p[0] + x
            else:
                p[0] = p[0] + ' ' + x



def p_grouping_name(p):
    '''grouping : NAME condition'''
    if p[2] is not None:
        p[0] = p[1] + ' ' + p[2]
    else:
        p[0] = p[1]

def p_attributes_any(p):
    '''attributes : ANY'''
    p[0] = p[1]

def p_attributes_distinct(p):
    '''attributes : DISTINCT NAME'''
    p[0] = p[1] + ' ' + p[2]

def p_attributes_values(p):
    '''attributes : LPAREN values RPAREN
                  | values'''
    p[0] = p[1]
    for x in p[2:]:
        p[0] = p[0] + x

def p_values_completion(p):
    '''values : NAME
              | NAME COMMA values
              | UP_COMMA NAME UP_COMMA
              | UP_COMMA NAME UP_COMMA COMMA values
              | NUMBER
              | ANY'''
    up_comma_open = p[1] == '\''
    if p[1] == 'ANY' or p[1] == 'TODO':
        if language_eng(lexer):
            p[0] = '*'
        else:
            p[0] = 'TODO'
    else:
        p[0] = p[1]
    for x in p[2:]:
        if x == ',':
            p[0] = p[0] + x
        elif x == '\'':
            if not up_comma_open:
                p[0] = p[0] + ' ' + x
                up_comma_open = True
            else:
                p[0] = p[0] + x
                up_comma_open = False
        elif up_comma_open:
            p[0] = p[0] + x
        else:
            p[0] = p[0] + ' ' + str(x)



def p_joiner_complete(p):
    '''joiner : NAME DOT NAME EQUALS NAME DOT NAME'''
    p[0] = p[1] + p[2] + p[3] + ' ' + p[4] + ' ' + p[5] + p[6] + p[7]

def p_condition_bool(p):
    '''condition : WHERE bool
                 | empty'''
    if p[1] is not None:
        p[0] = p[1] + ' ' + p[2]

def language_eng(lexer) -> bool:
    test_word = lexer.lexdata.split(' ')[0]
    return test_word == 'TRAEME' or test_word == 'METE' or test_word == 'ACTUALIZA' or test_word == 'BORRA' or test_word == 'CAMBIA'

def p_bool_complete(p):
    '''bool : NAME EQUALS NUMBER
            | NAME LESSER_THAN NUMBER
            | NAME GREATER_THAN NUMBER
            | bool AND bool
            | NAME EQUALS UP_COMMA NAME UP_COMMA
            | NAME DOT NAME EQUALS UP_COMMA NAME UP_COMMA
            | NAME DOT NAME EQUALS NUMBER
            | NAME DOT NAME LESSER_THAN NUMBER
            | NAME DOT NAME GREATER_THAN NUMBER
            | COUNT LPAREN values RPAREN GREATER_THAN NUMBER
            | COUNT LPAREN values RPAREN LESSER_THAN NUMBER
            | COUNT LPAREN values RPAREN EQUALS NUMBER
            | NAME BETWEEN NUMBER AND NUMBER'''
    open_par = False
    up_comma_open = False
    dot_used = False
    if p[1] == 'CONTANDO' or p[1] == 'COUNT':
        if language_eng(lexer):
            p[0] = 'COUNT'
        else:
            p[0] = 'CONTANDO'
    else:
        p[0] = p[1]
    for x in p[2:]:
        if x == '\'':
            if not up_comma_open:
                p[0] = p[0] + ' ' + x
                up_comma_open = True
            else:
                p[0] = p[0] + x
                up_comma_open = False
        elif up_comma_open:
            p[0] = p[0] + x
        else:
            if x == '.':
                dot_used = True
                p[0] = p[0] + x
            elif x == '(' or open_par:
                open_par = x != ')'
                p[0] = p[0] + x

            else:
                if dot_used:
                    dot_used = False
                    p[0] = p[0] + x
                else:
                    p[0] = p[0] + ' ' + str(x)




def p_query_insertion(p):
    '''query : INSERT_INTO NAME attributes insertion'''
    p[0] = p[1]
    for x in p[2:]:
        p[0] = p[0] + ' ' + x


def p_insertion(p):
    '''insertion : VALUES LPAREN values RPAREN'''
    p[0] = p[1] + ' ' + p[2] + p[3] + p[4]

def p_query_update(p):
    '''query : UPDATE NAME SET editions condition'''
    p[0] = p[1]
    for x in p[2:]:
        p[0] = p[0] + ' ' + x

def p_editions_complete(p):
    '''editions : NAME EQUALS NUMBER
                | NAME EQUALS UP_COMMA NAME UP_COMMA
                | editions COMMA editions'''
    up_comma_open = False
    p[0] = p[1]
    for x in p[2:]:
        if x == '\'':
            if not up_comma_open:
                p[0] = p[0] + ' ' + x
                up_comma_open = True
            else:
                p[0] = p[0] + x
                up_comma_open = False
        elif not up_comma_open:
            p[0] = p[0] + ' ' + str(x)
        else:
            p[0] = p[0] + x

def p_query_alter(p):
    '''query : ALTER_TABLE NAME alteration'''
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3]

def p_alteration_completion(p):
    '''alteration : DROP_COLUMN NAME
                  | ADD_COLUMN addition'''
    p[0] = p[1]
    for x in p[2:]:
        p[0] = p[0] + ' ' + x

def p_addition_template(p):
    '''addition : NAME typing setting'''
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3]

def p_typing_completion(p):
    '''typing   :   NAME LPAREN NUMBER RPAREN
                |   NAME'''
    p[0] = p[1]
    for x in p[2:]:
        p[0] = p[0] + str(x)

def p_setting(p):
    '''setting : NOT_NULL'''
    if p[1] is not None:
        p[0] = p[1]

def p_query_deletion(p):
    '''query : DELETE_FROM NAME condition'''
    p[0] = p[1] + ' ' + p[2] + ' ' + p[3]

def p_error(t):
    if t is not None:
        print(f"Error de sintaxis {t.value} en {t} de {lexer.lexdata}")
    else:
        print(f"Null value in {lexer.lexdata}")

def setup_parser():
    return yacc.yacc()


    


if __name__ == '__main__':
   
    pass

