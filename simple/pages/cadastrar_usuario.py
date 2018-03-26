from selenium import webdriver
from simple.factories.usuario import Usuario

class CadastrarUsuario():
    def __init__(self, driver):
        self.driver = driver

    def visitar(self):
        self.driver.get('http://localhost:5000')

    def pagina_correta(self):
        return self.driver.title == 'Cadastro de Usuário'

    def preencher_usuario(self, usuario):
        campo_nome = self.driver.find_element_by_name("nome")
        campo_nome.send_keys(usuario.nome)

        campo_idade = self.driver.find_element_by_name("idade")
        campo_idade.send_keys(usuario.idade)

        botao_submit = self.driver.find_element_by_css_selector('input[type="submit"]')
        botao_submit.click()

