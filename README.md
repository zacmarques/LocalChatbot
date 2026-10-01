# 🤖 LocalChatbot - Chatbot de IA Local com Openai e Ollama

Uma interface sólida com chatbot de IA desenvolvido em Python que permite interagir com modelos de linguagem (LLM) rodando 100% localmente no computador utilizando o **Ollama**. Como parte de um portifólio que estou buscando criar, conta com a personalização do criador, porém pode ser facilmente retirado via código, inibido clicando na "setinha" e utilizado sem essas informações.

> 📌 **Projeto de Portfólio:** Desenvolvido para praticar manipulação de APIs de IA, execução de modelos locais e previsão com Machine Learning em Python e estruturação de código.

---

## 🚀 Funcionalidades

- Interface simples para troca de mensagens com a IA.
- Processamento 100% local (sem necessidade de chaves de API pagas ou conexão com a nuvem, mas você deve substituir a IA por um modelo que você tenha instalado).
- Respostas em tempo real integradas com o modelo configurado no Ollama.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **Execução de IA Local:** [Ollama](https://ollama.com/)
- **Bibliotecas Python:** `openai` / `ollama` / `streamlit`

---

## 📋 Pré-requisitos

Antes de rodar o projeto, você precisará ter instalado em sua máquina:

1. **Python 3.10+** instalado.
2. **Ollama** baixado e em execução.
3. Um modelo de IA baixado no Ollama (exemplo: `ollama run llama3` ou `ollama run mistral`). No código foi utilizado o Qwen 2.5:7b que eu gosto de usar por ser leve, rápido e entregar resultados legais para meus projetos pessoais.

---

## 🔧 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/zacmarques/LocalChatbot.git](https://github.com/zacmarques/LocalChatbot.git)