# 📚 Sistema de Administração Escolar

## 📋 Sobre o Projeto

Este sistema foi desenvolvido como projeto da disciplina **Projeto de Software** da **Universidade Federal de Alagoas (UFAL)**, ministrada pelo professor doutor **Baldoino Fonseca dos Santos Neto**.

O sistema gerencia uma escola com funções para:

- 👨‍🎓 Alunos  
- 👨‍🏫 Funcionários (professores)  
- 👪 Responsáveis  

Desenvolvido pelo aluno **Zilderlan Naty dos Santos**.

---

## ✨ Funcionalidades Implementadas

- ✅ Cadastro de alunos, funcionários e responsáveis (com nome e senha)  
- 🔐 Login seguro por tipo de usuário (aluno, funcionário, responsável)  
- 📝 Menus personalizados para cada perfil  
- ⏰ Registro de presença **somente para funcionários**  
- 📊 Lançamento e consulta de notas  
- 📚 Distribuição e consulta de materiais  
- 🗓️ Agendamento de provas  
- 🎯 Registro de atividades extracurriculares  
- 🚌 Rastreamento simulado do transporte escolar  
- 💰 Processamento de pagamentos de mensalidades  
- 📆 Gerenciamento de turmas e horários  
- 👀 Consulta detalhada para alunos e responsáveis  
- ❌ Mensagens claras de erro e avisos para dados inválidos ou faltantes  


## ⚠️ Regras e Restrições

- 📅 Datas devem ser digitadas no formato `DD/MM/AAAA`  
- 🔢 IDs precisam ser números válidos para operações específicas  
- 🔒 Senhas simples, sem criptografia  
- 🚫 Apenas funcionários podem registrar presenças e fazer lançamentos administrativos  
- 👪 Para cadastrar um responsável, informe o ID de um aluno já cadastrado  
- 💾 Dados são armazenados **apenas na memória**, e são perdidos ao fechar o programa  
- ⚠️ Entrada inválida gera mensagem de erro e pedido para tentar novamente  


## 🛠️ Como Rodar em Outro Computador

1. Instale o **Python 3.6+** ([download aqui](https://www.python.org/downloads/))  
2. Baixe os arquivos `system.py` e `main.py` e coloque-os na mesma pasta  
3. Abra o terminal na pasta do projeto  
4. Execute o comando:  
   ```bash
   python main.py

📖 Como Usar
Primeiro, cadastre um usuário (aluno, funcionário ou responsável)
Faça login com nome, senha e tipo de usuário
Explore o menu disponível para seu perfil
Funcionários podem registrar presença, lançar notas, gerenciar turmas e muito mais
Alunos podem consultar suas notas, presenças e materiais
Responsáveis podem acessar dados do aluno vinculado a eles

- 🚀 Próximos Passos e Melhorias
- 📱 Integrar rastreamento mais visual (se possível)
- 🔧 Melhorar controle de permissões e fluxo do sistema
