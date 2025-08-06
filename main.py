from system import Escola

def menu_aluno(escola, user_id):
    aluno = next((a for a in escola.alunos if a.id == user_id), None)
    if not aluno:
        print("❌ Aluno não encontrado.")
        return
    print(f"\n🎓 Bem-vindo(a), {aluno.nome}!")
    while True:
        print("\n--- Menu do Aluno ---")
        print("1. Ver materiais")
        print("2. Ver notas")
        print("3. Ver provas agendadas")
        print("4. Ver presenças")
        print("5. Ver atividades extracurriculares")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            if aluno.materiais:
                print(f"📚 Materiais: {aluno.materiais}")
            else:
                print("📭 Nenhum material disponível no momento.")
        elif opcao == "2":
            if aluno.notas:
                print(f"📊 Notas: {aluno.notas}")
            else:
                print("📉 Nenhuma nota registrada ainda.")
        elif opcao == "3":
            if aluno.provas:
                print(f"📝 Provas agendadas: {aluno.provas}")
            else:
                print("📭 Nenhuma prova agendada no momento.")
        elif opcao == "4":
            if aluno.presencas:
                print(f"✅ Presenças registradas: {len(aluno.presencas)} dia(s)")
            else:
                print("❌ Nenhuma presença registrada ainda.")
        elif opcao == "5":
            if aluno.atividades:
                print(f"🎯 Atividades: {aluno.atividades}")
            else:
                print("📭 Nenhuma atividade registrada.")
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def menu_funcionario(escola, user_id):
    funcionario = next((f for f in escola.funcionarios if f.id == user_id), None)
    if not funcionario:
        print("❌ Funcionário não encontrado.")
        return
    print(f"\n👨‍🏫 Bem-vindo(a), {funcionario.nome}!")
    while True:
        print("\n--- Menu do Funcionário ---")
        print("1. Registrar presença do aluno")
        print("2. Lançar nota do aluno")
        print("3. Distribuir material")
        print("4. Gerenciar turmas")
        print("5. Agendar prova")
        print("6. Registrar atividade extracurricular")
        print("7. Remover aluno")
        print("8. Consultar alunos matriculados")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            try:
                id_aluno = int(input("ID do aluno para registrar presença: "))
                escola.registrar_presenca(id_aluno)
            except ValueError:
                print("ID inválido.")
        elif opcao == "2":
            try:
                id_aluno = int(input("ID do aluno: "))
                nota = float(input("Nota a lançar: "))
                escola.lancar_nota(id_aluno, nota)
            except ValueError:
                print("Valor inválido.")
        elif opcao == "3":
            try:
                id_aluno = int(input("ID do aluno: "))
                material = input("Material a distribuir: ")
                escola.distribuir_material(id_aluno, material)
            except ValueError:
                print("ID inválido.")
        elif opcao == "4":
            turma = input("Nome da turma: ")
            horario = input("Horário da turma: ")
            escola.gerenciar_turmas(turma, horario)
        elif opcao == "5":
            try:
                id_aluno = int(input("ID do aluno: "))
                nome_prova = input("Nome da prova: ")
                data_prova = input("Data da prova (DD/MM/AAAA): ")
                escola.agendar_prova(id_aluno, nome_prova, data_prova)
            except ValueError:
                print("Valor inválido.")
        elif opcao == "6":
            try:
                id_aluno = int(input("ID do aluno: "))
                atividade = input("Atividade extracurricular: ")
                escola.registrar_atividade(id_aluno, atividade)
            except ValueError:
                print("ID inválido.")
        elif opcao == "7":
            try:
                id_aluno = int(input("ID do aluno para remoção: "))
                escola.remover_aluno(id_aluno)
            except ValueError:
                print("ID inválido.")
        elif opcao == "8":
            alunos = escola.consultar_alunos_matriculados()
            if isinstance(alunos, str):
                print(alunos)
            else:
                print("Alunos matriculados:")
                for id_aluno, nome in alunos:
                    print(f"ID: {id_aluno} | Nome: {nome}")
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def menu_responsavel(escola, user_id):
    responsavel = next((r for r in escola.responsaveis if r.id == user_id), None)
    if not responsavel:
        print("❌ Responsável não encontrado.")
        return
    print(f"\n👪 Bem-vindo, {responsavel.nome}!")
    while True:
        print("\n--- Menu do Responsável ---")
        print("1. Consultar dados do aluno")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            escola.consultar_dados_aluno(responsavel.id_aluno)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def main():
    escola = Escola()
    print("=== Sistema de Administração Escolar ===")
    while True:
        print("\n1 - Login")
        print("2 - Cadastrar usuário")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            tipo = input("Tipo de usuário (aluno/funcionario/responsavel): ").strip().lower()
            nome = input("Nome: ")
            senha = input("Senha: ")
            login_result = escola.login(nome, senha, tipo)
            if login_result is None:
                print("Falha no login. Tente novamente ou cadastre-se.")
                continue
            tipo_logado, user_id = login_result
            if tipo_logado == "aluno":
                menu_aluno(escola, user_id)
            elif tipo_logado == "funcionario":
                menu_funcionario(escola, user_id)
            elif tipo_logado == "responsavel":
                menu_responsavel(escola, user_id)
        elif opcao == "2":
            tipo = input("Tipo de usuário para cadastro (aluno/funcionario/responsavel): ").strip().lower()
            nome = input("Nome: ")
            senha = input("Senha: ")
            if tipo == "responsavel":
                try:
                    id_aluno = int(input("ID do aluno que o responsável irá acompanhar: "))
                except ValueError:
                    print("ID inválido.")
                    continue
                escola.cadastrar_usuario(tipo, nome, senha, id_aluno)
            else:
                escola.cadastrar_usuario(tipo, nome, senha)
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
