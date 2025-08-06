from datetime import datetime

class Aluno:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.presencas = []
        self.notas = []
        self.materiais = []
        self.atividades = []
        self.provas = []

class Funcionario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

class Responsavel:
    def __init__(self, nome, senha, id_aluno):
        self.nome = nome
        self.senha = senha
        self.id_aluno = id_aluno

class Escola:
    def __init__(self):
        self.alunos = []
        self.funcionarios = []
        self.responsaveis = []
        self.turmas = []
        self.proximo_id = 1

    def cadastrar_usuario(self, tipo, nome, senha, id_aluno=None):
        if tipo == "aluno":
            aluno = Aluno(self.proximo_id, nome, senha)
            self.alunos.append(aluno)
            print(f"🧑‍🎓 Aluno {nome} cadastrado com ID {self.proximo_id}")
            self.proximo_id += 1
        elif tipo == "funcionario":
            funcionario = Funcionario(nome, senha)
            self.funcionarios.append(funcionario)
            print(f"🧑‍🏫 Funcionário {nome} cadastrado com sucesso.")
        elif tipo == "responsavel":
            if not any(a.id == id_aluno for a in self.alunos):
                print("❌ ID de aluno inválido para o responsável.")
                return
            responsavel = Responsavel(nome, senha, id_aluno)
            self.responsaveis.append(responsavel)
            print(f"👨‍👩‍👧 Responsável {nome} cadastrado com sucesso.")
        else:
            print("❌ Tipo inválido para cadastro.")

    def login(self, nome, senha, tipo):
        if tipo == "aluno":
            for aluno in self.alunos:
                if aluno.nome == nome and aluno.senha == senha:
                    return ("aluno", aluno.id)
        elif tipo == "funcionario":
            for func in self.funcionarios:
                if func.nome == nome and func.senha == senha:
                    return ("funcionario", func.nome)
        elif tipo == "responsavel":
            for resp in self.responsaveis:
                if resp.nome == nome and resp.senha == senha:
                    return ("responsavel", resp.id_aluno)
        print("❌ Nome, senha ou tipo inválido. Tente novamente ou cadastre-se.")
        return None

    def registrar_presenca(self, id_aluno):
        aluno = self._buscar_aluno(id_aluno)
        if aluno:
            data = datetime.now()
            aluno.presencas.append(data)
            print(f"✅ Presença registrada para {aluno.nome} em {data.strftime('%d/%m/%Y')}")

    def lancar_nota(self, id_aluno, nota):
        aluno = self._buscar_aluno(id_aluno)
        if aluno:
            aluno.notas.append(nota)
            print(f"📝 Nota {nota} lançada para {aluno.nome}")

    def distribuir_material(self, id_aluno, material):
        aluno = self._buscar_aluno(id_aluno)
        if aluno:
            aluno.materiais.append(material)
            print(f"📘 Material '{material}' distribuído para {aluno.nome}")

    def agendar_prova(self, id_aluno, nome_prova, data_prova):
        aluno = self._buscar_aluno(id_aluno)
        if aluno:
            aluno.provas.append({"nome": nome_prova, "data": data_prova})
            print(f"📅 Prova '{nome_prova}' agendada para {aluno.nome} na data {data_prova}")

    def registrar_atividade(self, id_aluno, atividade):
        aluno = self._buscar_aluno(id_aluno)
        if aluno:
            aluno.atividades.append(atividade)
            print(f"🎯 Atividade '{atividade}' registrada para {aluno.nome}")

    def consultar_dados_aluno(self, id_aluno):
        aluno = self._buscar_aluno(id_aluno)
        if aluno:
            print(f"\n📋 Dados do aluno {aluno.nome}:")
            print("📚 Materiais:", aluno.materiais if aluno.materiais else "📭 Nenhum material disponível.")
            print("📈 Notas:", aluno.notas if aluno.notas else "📉 Nenhuma nota registrada.")
            print("📅 Provas:", aluno.provas if aluno.provas else "📭 Nenhuma prova agendada.")
            print("✅ Presenças:", len(aluno.presencas) if aluno.presencas else "❌ Nenhuma presença.")
            print("🎯 Atividades:", aluno.atividades if aluno.atividades else "📭 Nenhuma atividade.")

    def portal_responsaveis(self, id_aluno):
        aluno = self._buscar_aluno(id_aluno)
        if aluno:
            print(f"\n👨‍👩‍ Portal do Responsável - Acompanhamento do aluno {aluno.nome}")
            self.consultar_dados_aluno(id_aluno)
            print("\n💳 Opções de pagamento:")
            print("1. Cartão de Crédito")
            print("2. Boleto Bancário")
            print("3. PIX")
            print("4. Transferência Bancária\n")
            print("🚌 Rastreamento do transporte:")
            self.rastrear_transporte(id_aluno)
        else:
            print("Aluno não encontrado.")

    def processar_pagamento(self, id_aluno, forma_pagamento):
        aluno = self._buscar_aluno(id_aluno)
        if aluno:
            print(f"💰 Pagamento da mensalidade de {aluno.nome} realizado via {forma_pagamento}.")

    def rastrear_transporte(self, id_aluno):
        aluno = self._buscar_aluno(id_aluno)
        if aluno:
            print(f"🚌 Transporte escolar de {aluno.nome} está a caminho! Localização em tempo real disponível.")
        else:
            print("Aluno não encontrado.")

    def remover_aluno(self, id_aluno):
        aluno = self._buscar_aluno(id_aluno)
        if aluno:
            self.alunos.remove(aluno)
            print(f"❌ Aluno {aluno.nome} removido com sucesso.")

    def consultar_alunos_matriculados(self):
        if not self.alunos:
            return "Nenhum aluno matriculado."
        return [(aluno.id, aluno.nome) for aluno in self.alunos]

    def gerenciar_turmas(self, nome_turma, horario):
        self.turmas.append({"nome": nome_turma, "horario": horario})
        print(f"🏫 Turma '{nome_turma}' criada no horário {horario}")

    def _buscar_aluno(self, id_aluno):
        return next((a for a in self.alunos if a.id == id_aluno), None)
