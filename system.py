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
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha

class Responsavel:
    def __init__(self, id, nome, senha, id_aluno):
        self.id = id
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
            print(f"Aluno {nome} cadastrado com ID {self.proximo_id}")
        elif tipo == "funcionario":
            funcionario = Funcionario(self.proximo_id, nome, senha)
            self.funcionarios.append(funcionario)
            print(f"Funcionário {nome} cadastrado com ID {self.proximo_id}")
        elif tipo == "responsavel":
            if not any(a.id == id_aluno for a in self.alunos):
                print("ID de aluno inválido para o responsável.")
                return
            responsavel = Responsavel(self.proximo_id, nome, senha, id_aluno)
            self.responsaveis.append(responsavel)
            print(f"Responsável {nome} cadastrado com ID {self.proximo_id}")
        else:
            print("Tipo inválido para cadastro.")
            return
        self.proximo_id += 1

    def login(self, nome, senha, tipo):
        if tipo == "aluno":
            for aluno in self.alunos:
                if aluno.nome == nome and aluno.senha == senha:
                    return ("aluno", aluno.id)
        elif tipo == "funcionario":
            for func in self.funcionarios:
                if func.nome == nome and func.senha == senha:
                    return ("funcionario", func.id)
        elif tipo == "responsavel":
            for resp in self.responsaveis:
                if resp.nome == nome and resp.senha == senha:
                    return ("responsavel", resp.id)
        print("❌ Nome, senha ou tipo inválido. Tente novamente ou cadastre-se.")
        return None

    def registrar_presenca(self, id_aluno):
        aluno = next((a for a in self.alunos if a.id == id_aluno), None)
        if aluno:
            data = datetime.now()
            aluno.presencas.append(data)
            print(f"Presença registrada para {aluno.nome} em {data.strftime('%d/%m/%Y')}")
        else:
            print("Aluno não encontrado.")

    def lancar_nota(self, id_aluno, nota):
        aluno = next((a for a in self.alunos if a.id == id_aluno), None)
        if aluno:
            aluno.notas.append(nota)
            print(f"Nota {nota} lançada para {aluno.nome}")
        else:
            print("Aluno não encontrado.")

    def distribuir_material(self, id_aluno, material):
        aluno = next((a for a in self.alunos if a.id == id_aluno), None)
        if aluno:
            aluno.materiais.append(material)
            print(f"Material '{material}' distribuído para {aluno.nome}")
        else:
            print("Aluno não encontrado.")

    def agendar_prova(self, id_aluno, nome_prova, data_prova):
        aluno = next((a for a in self.alunos if a.id == id_aluno), None)
        if aluno:
            aluno.provas.append({"nome": nome_prova, "data": data_prova})
            print(f"Prova '{nome_prova}' agendada para {aluno.nome} na data {data_prova}")
        else:
            print("Aluno não encontrado.")

    def registrar_atividade(self, id_aluno, atividade):
        aluno = next((a for a in self.alunos if a.id == id_aluno), None)
        if aluno:
            aluno.atividades.append(atividade)
            print(f"Atividade '{atividade}' registrada para {aluno.nome}")
        else:
            print("Aluno não encontrado.")

    def consultar_dados_aluno(self, id_aluno):
        aluno = next((a for a in self.alunos if a.id == id_aluno), None)
        if aluno:
            print(f"\n📋 Dados do aluno {aluno.nome}:")
            print("📚 Materiais:", aluno.materiais if aluno.materiais else "📭 Nenhum material disponível.")
            print("📈 Notas:", aluno.notas if aluno.notas else "📉 Nenhuma nota registrada.")
            print("📅 Provas:", aluno.provas if aluno.provas else "📭 Nenhuma prova agendada.")
            print(f"✅ Presenças: {len(aluno.presencas)} dia(s)" if aluno.presencas else "❌ Nenhuma presença registrada.")
            print("🎯 Atividades:", aluno.atividades if aluno.atividades else "📭 Nenhuma atividade registrada.")
        else:
            print("Aluno não encontrado.")

    def processar_pagamento(self, id_aluno, forma_pagamento):
        aluno = next((a for a in self.alunos if a.id == id_aluno), None)
        if aluno:
            print(f"✅ Pagamento da mensalidade de {aluno.nome} realizado via {forma_pagamento}.")
        else:
            print("Aluno não encontrado.")

    def rastrear_transporte(self, id_aluno):
        aluno = next((a for a in self.alunos if a.id == id_aluno), None)
        if aluno:
            print(f"🛰️ Rastreamento do transporte escolar de {aluno.nome} em andamento...")
        else:
            print("Aluno não encontrado.")

    def remover_aluno(self, id_aluno):
        aluno = next((a for a in self.alunos if a.id == id_aluno), None)
        if aluno:
            self.alunos.remove(aluno)
            print(f"🗑️ Aluno {aluno.nome} removido com sucesso.")
        else:
            print("Aluno não encontrado.")

    def consultar_alunos_matriculados(self):
        if not self.alunos:
            return "Nenhum aluno matriculado."
        return [(aluno.id, aluno.nome) for aluno in self.alunos]

    def gerenciar_turmas(self, nome_turma, horario):
        self.turmas.append({"nome": nome_turma, "horario": horario})
        print(f"🧑‍🏫 Turma '{nome_turma}' criada no horário {horario}")
