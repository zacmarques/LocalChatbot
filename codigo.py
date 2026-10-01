# -*- coding: utf-8 -*-
# =============================================================================
# ChatBot de IA que fiz como portifólio de Python, Streamlit e conexão com Ollama. Servirá para compor Github e currículo de pesquisador de Humanidades Digitais.
# Desenvolvido por: Isaac Marques de Souza Garcia
# Paleta de cores: olive-leaf, black-forest, cornsilk, sunlit-clay, copperwood
# =============================================================================

import streamlit as st
from openai import OpenAI
import time

# ━━ PALETA DE CORES ━━
OLIVE_LEAF = "#606C38"
BLACK_FOREST = "#283618"
CORNSILK = "#FEFAE0"
SUNLIT_CLAY = "#DDA15E"
COPPERWOOD = "#BC6C25"

# ━━ CONFIGURAÇÃO ━━
st.set_page_config(
    page_title="ChatBot Humanidades & Tecnologia",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ━━ CSS PERSONALIZADO ━━
st.markdown(f"""
<style>
    /* Fundo e tema */
    :root {{
        --olive-leaf: {OLIVE_LEAF};
        --black-forest: {BLACK_FOREST};
        --cornsilk: {CORNSILK};
        --sunlit-clay: {SUNLIT_CLAY};
        --copperwood: {COPPERWOOD};
    }}

    /* Fundo do chat */
    #st-chat-container {{
        background-color: {CORNSILK} !important;
    }}

    /* Cabeçalho */
    .stMarkdown {{
        color: {BLACK_FOREST};
    }}

    /* Título */
    h1, h2, h3 {{
        color: {BLACK_FOREST};
        border-bottom: 2px solid {SUNLIT_CLAY};
        padding-bottom: 10px;
    }}

    /* Mensagem do usuário */
    .stChatMessage[data-testid="stChatMessageUser"] {{
        background-color: {OLIVE_LEAF} !important;
        color: {CORNSILK} !important;
        border-radius: 15px !important;
        padding: 15px !important;
        border: 1px solid {SUNLIT_CLAY} !important;
    }}

    /* Mensagem da IA */
    .stChatMessage[data-testid="stChatMessageAssistant"] {{
        background-color: {BLACK_FOREST} !important;
        color: {CORNSILK} !important;
        border-radius: 15px !important;
        padding: 15px !important;
        border: 1px solid {SUNLIT_CLAY} !important;
    }}

    /* Barra de digitação */
    .stTextInput[data-testid="stChatInput"] {{
        background-color: {CORNSILK} !important;
        border: 2px solid {SUNLIT_CLAY} !important;
        border-radius: 15px !important;
        padding: 10px !important;
    }}

    /* Botão de enviar */
    .stButton>button {{
        background-color: {OLIVE_LEAF} !important;
        color: {CORNSILK} !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 10px 25px !important;
        font-weight: bold !important;
    }}

    .stButton>button:hover {{
        background-color: {COPPERWOOD} !important;
        color: {BLACK_FOREST} !important;
    }}

    /* Barra lateral */
    #stSidebar {{
        background-color: {BLACK_FOREST} !important;
        color: {CORNSILK} !important;
        border-right: 1px solid {SUNLIT_CLAY} !important;
    }}

    /* Títulos da barra lateral */
    .css-1d391kg {{
        color: {SUNLIT_CLAY} !important;
        border-bottom: 2px solid {SUNLIT_CLAY} !important;
        padding-bottom: 10px !important;
    }}

    /* Texto de placeholder */
    .placeholder-text {{
        color: {SUNLIT_CLAY} !important;
    }}

    /* Fonte */
    body {{
        font-family: 'Georgia', 'Times New Roman', serif;
    }}
</style>
""", unsafe_allow_html=True)

# ━━ INICIALIZAÇÃO ━━
modelo_ia = OpenAI(
    base_url="http://127.0.0.1:11434/v1",
    api_key="ollama"  # Ollama não requer API key
)

# ━━ LADO ESQUERDO (Informações) ━━
with st.sidebar:
    st.markdown(f"""
    ### 📚 Informações sobre o criador
    
    **Isaac Marques de Souza Garcia**

   *Pesquisador interdisciplinar que atua nas frentes de História da África, Ensino de História, Humanidades Digitais e Análise de Dados em Python*
    """
    )
    
    st.markdown("---")
    st.markdown("### 🎨 Paleta de Cores")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.color_picker("Olive Leaf", OLIVE_LEAF, disabled=True)
    with col2:
        st.color_picker("Black Forest", BLACK_FOREST, disabled=True)
    with col3:
        st.color_picker("Corn Silk", CORNSILK, disabled=True)
    
    st.markdown("---")
    st.markdown("### 📖 Sobre")
    st.markdown("""
    *Esse trabalho conta como uma peça isolada de teste e portifolio para consolidar minha habilidade em criação de chatbots de IA via bibliotecas do Python e apresentá-los ao usuário no navegador*
    """)

    st.markdown("---")
    st.markdown("""
    ### 🚀 Opções
    """)
    
    if st.button("Limpar Conversa", type="primary"):
        st.session_state["lista_mensagens"] = []
        st.rerun()

# ━━ TÍTULO E BEM-VINDO ━━
st.markdown(f"""
<div style="text-align: center; padding: 30px;">
    <h1 style="color: {OLIVE_LEAF}; border: none; text-shadow: 2px 2px {SUNLIT_CLAY};">
        📚 ChatBot de IA
    </h1>
    <p style="color: {SUNLIT_CLAY}; font-size: 1.2rem;">
        Conectando Python, IA e Humanidades Digitais.
    </p>
    <p style="color: {BLACK_FOREST}; font-size: 0.9rem;">
        Use este chatbot para explorar buscar por conteúdos históricos.
    </p>
</div>
""", unsafe_allow_html=True)

# ━━ HISTÓRICO DE CONVERSA ━━
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

for mensagem in st.session_state["lista_mensagens"]:
    if mensagem["role"] == "user":
        st.chat_message("user").write(mensagem["content"])
    else:
        st.chat_message("assistant").write(mensagem["content"])

# ━━ CAMPO DE MENSAGEM ━━
mensagem_usuario = st.chat_input("Digite sua mensagem aqui...")

# ━━ PROCESSAMENTO ━━
if mensagem_usuario:
    # Adiciona mensagem do usuário
    st.chat_message("user").write(mensagem_usuario)
    st.session_state["lista_mensagens"].append({"role": "user", "content": mensagem_usuario})
    
    # Mensagem de "digitando..."
    with st.chat_message("assistant"):
        st.markdown("📝 *Digitando...*")
    
    # Integração com Ollama
    try:
        resposta_ia = modelo_ia.chat.completions.create(
            model="qwen2.5:7b",
            messages=st.session_state["lista_mensagens"],
            max_tokens=4080,
            extra_body={
                "temperature": 0.5,
                "options": {
                    "num_ctx": 8192,
                    "seed": 42
                }
            }
        )
        resposta_ia = resposta_ia.choices[0].message.content
    except Exception as e:
        resposta_ia = f"*Erro na conexão com Ollama:* {str(e)}"
        st.error("⚠️ Verifique se o Ollama está rodando em http://127.0.0.1:11434")
    
    # Adiciona mensagem da IA
    st.session_state["lista_mensagens"].append({"role": "assistant", "content": resposta_ia})
    
    # Remove mensagem temporária
    st.chat_message("assistant").markdown(resposta_ia)

st.markdown("---")
with st.sidebar:
    st.markdown(
        """
        <p style="font-style: italic; text-align: justify; margin-top: 15px;">
            Ressalto que o Ollama deve estar rodando localmente para que o chatbot funcione corretamente, mas para melhorar a experiência do usuário será necessária a integração com a internet. Como a memória e a capacidade foram reduzidas para fins de teste, sem o acesso à internet ele não entrega nem metade de sua capacidade.
        </p>
    """,
        unsafe_allow_html=True,
    )
