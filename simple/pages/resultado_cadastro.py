class ResultadoCadastro():
    def __init__(self, driver):
        self.driver = driver

    def pagina_correta(self):
        return self.driver.title == 'Cadastro de Usuário com Sucesso'

    def mensagem_sucesso(self):
        mensagem = self.driver.find_element_by_id("mensagem")
        return mensagem.text == 'Usuário cadastrado com sucesso!'
