import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class CadastroTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:5000")

    def test_fluxo_cadastro(self):
        wait = WebDriverWait(self.driver, 2)

        self.assertIn("Cadastro de Usuário", self.driver.title)

        campo_nome = self.driver.find_element_by_name("nome")
        campo_nome.send_keys("Celso")

        campo_idade = self.driver.find_element_by_name("idade")
        campo_idade.send_keys("33")

        botao_submit = self.driver.find_element_by_css_selector('input[type="submit"]')
        botao_submit.click()

        self.assertIn("Cadastro de Usuário com Sucesso", self.driver.title)

        mensagem = self.driver.find_element_by_id("mensagem")
        self.assertEqual('Usuário cadastrado com sucesso!', mensagem.text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

'''
        wait.until(EC.title_is('Cadastro de Usuário com Sucesso'))
        self.assertIn("Cadastro de Usuário com Sucesso", self.driver.title)
'''
