import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from simple.factories.usuario import Usuario
from simple.pages.cadastrar_usuario import CadastrarUsuario
from simple.pages.resultado_cadastro import ResultadoCadastro

class CadastroTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.usuario = Usuario(nome='Débora', idade='33')

    def test_fluxo_cadastro(self):
        wait = WebDriverWait(self.driver, 2)

        pagina_cadastro = CadastrarUsuario(self.driver)
        pagina_cadastro.visitar()

        self.assertTrue(pagina_cadastro.pagina_correta())
        pagina_cadastro.preencher_usuario(self.usuario)

        pagina_resultado = ResultadoCadastro(self.driver)
        self.assertTrue(pagina_resultado.pagina_correta())
        self.assertTrue(pagina_resultado.mensagem_sucesso())

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

'''
        wait.until(EC.title_is('Cadastro de Usuário com Sucesso'))
        self.assertIn("Cadastro de Usuário com Sucesso", self.driver.title)
'''
