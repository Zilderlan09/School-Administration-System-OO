# 📚 Sistema de Gestão Escolar

## 📋 Sobre o Projeto

Este sistema foi desenvolvido como projeto final da disciplina de **Projeto de Software** do curso de Sistemas de Informação da **Universidade Federal de Alagoas (UFAL)**, ministrada pelo professor Dr. **Baldoino Fonseca dos Santos Neto**.

O sistema simula um ambiente escolar com suporte para três tipos de usuários:

- 👨‍🎓 Alunos  
- 👨‍🏫 Funcionários (Professores)  
- 👪 Responsáveis (Pais ou responsáveis legais)

Desenvolvido por **Zilderlan Naty dos Santos**.

---

## ✨ Funcionalidades Implementadas

- ✅ Cadastro de alunos, funcionários e responsáveis (com nome e senha)  
- 🔐 Login seguro por tipo de usuário (aluno, funcionário, responsável)  
- 📝 Menu personalizado para cada tipo de usuário  
- ⏰ Registro de presença (**restrito ao funcionário**)  
- 📊 Lançamento e consulta de notas  
- 📚 Compartilhamento e visualização de materiais didáticos  
- 🗓️ Agendamento e visualização de provas  
- 🎯 Registro de atividades extracurriculares  
- 💰 **Pagamento de mensalidade (restrito ao responsável)**  
- 🚌 Rastreio do transporte escolar (**apenas pelo responsável**)  
- 👀 Consulta de relatório completo do aluno (pelo responsável)  
- 📆 Grade de horários e gerenciamento de turmas  
- 🧠 Mensagens de erro claras para entradas inválidas ou ausentes  

---

## ⚠️ Regras e Restrições

- 📅 Datas devem ser informadas no formato `DD/MM/AAAA`  
- 🔢 **Apenas os alunos** recebem um ID exclusivo, usado por funcionários e responsáveis para vinculá-los  
- 🔒 Senhas armazenadas em texto simples (sem criptografia)  
- 🚫 Somente funcionários podem registrar presença e alterar dados acadêmicos  
- 👪 Responsáveis devem informar o **ID do aluno** ao se cadastrar  
- 💾 Todos os dados são armazenados apenas **em memória** — sem salvamento permanente  
- ❌ Caso não existam registros de materiais, notas ou provas, será exibida uma mensagem informando a ausência, junto de um símbolo visual (ASCII)

---

## 🛠️ Como Executar o Projeto

1. Instale o **Python 3.6 ou superior** ([Download aqui](https://www.python.org/downloads/))  
2. Clone ou baixe este repositório  
3. Coloque os arquivos `escola.py` e `main.py` na mesma pasta  
4. No terminal, dentro da pasta do projeto, execute:

   ```bash
   python main.py
