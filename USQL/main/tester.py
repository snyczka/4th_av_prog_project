import unittest
from __init__ import *


class USQL_tester(unittest.TestCase):

    def test_sentence_10(self):
        parser = setup_parser()
        self.assertEqual(parser.parse('TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;'), 'SELECT * FROM usuarios WHERE edad > 18.0;')
    def test_sentence_1(self):
        parser = setup_parser() 
        self.assertEqual(parser.parse('TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad =\'Madrid\';'), 'SELECT DISTINCT nombre FROM clientes WHERE ciudad = \'Madrid\';')
    def test_sentence_2(self):
        parser = setup_parser()
        self.assertEqual(parser.parse('METE EN usuarios (nombre, edad) LOS VALORES (\'Juan\', 25);'), 'INSERT INTO usuarios (nombre, edad) VALUES (\'Juan\', 25.0);')
    def test_sentence_3(self):
        parser = setup_parser()
        self.assertEqual(parser.parse('ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = \'ingeniero\';'), 'UPDATE empleados SET salario = 3000.0 WHERE puesto = \'ingeniero\';')
    def test_sentence_4(self):
        parser = setup_parser()
        self.assertEqual(parser.parse('TRAEME TODO DE LA TABLA pedidos MEZCLANDO clientes EN pedidos.cliente_id= clientes.id DONDE clientes.ciudad = \'Barcelona\';'), 'SELECT * FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id WHERE clientes.ciudad = \'Barcelona\';')
    def test_sentence_5(self):
        parser = setup_parser()
        self.assertEqual(parser.parse('TRAEME CONTANDO(TODO) DE LA TABLA ventas AGRUPANDO POR producto WHERE DEL GROUP BY COUNT(*) > 5;'), 'SELECT COUNT(*) FROM ventas GROUP BY producto HAVING COUNT(*) > 5.0;')
    def test_sentence_6(self):
        parser = setup_parser()
        self.assertEqual(parser.parse('BORRA DE LA tabla clientes DONDE edad ENTRE 18 Y 25;'), 'DELETE FROM clientes WHERE edad BETWEEN 18.0 AND 25.0;')
    def test_sentence_7(self):
        parser = setup_parser()
        self.assertEqual(parser.parse('CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO;'), 'ALTER TABLE empleados ADD COLUMN direccion VARCHAR(255.0) NOT NULL;')
    def test_sentence_8(self):
        parser = setup_parser()
        self.assertEqual(parser.parse('CAMBIA LA TABLA empleados ELIMINA LA COLUMNA direccion;'), 'ALTER TABLE empleados DROP COLUMN direccion;')
    def test_sentence_9(self):
        parser = setup_parser()
        self.assertEqual(parser.parse('SELECT clause FROM contract;'), 'TRAEME clause DE LA TABLA contract;')



if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
