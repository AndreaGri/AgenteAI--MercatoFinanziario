import streamlit as st
from agent import get_financial_agent
from langchain_core.messages import HumanMessage, AIMessage

st.set_page_config(page_title="Agente Finanziario AI", page_icon="📈")

st.title("🤖 Agente Finanziario Strategico")
st.caption("Basato su Architettura RAG & Agents - Capitolo 6 'AI Engineering'")

# 1. SIDEBAR: Profilo Utente (Costruzione del Contesto - Pag. 255)
st.sidebar.header("👤 Profilo Investitore")
risk_profile = st.sidebar.selectbox(
    "Profilo di Rischio", 
    ["Prudente", "Equilibrato", "Speculativo"]
)
budget = st.sidebar.number_input("Budget Investimento ($)", min_value=0, value=1000)
preferences = st.sidebar.text_area("Preferenze (es. Tech, Green, Crypto)", "Tech")

if st.sidebar.button("Pulisci Conversazione"):
    st.session_state.chat_history = []
    st.rerun()

# 2. INIZIALIZZAZIONE MEMORIA (Pag. 301)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "agent" not in st.session_state:
    st.session_state.agent = get_financial_agent()

# Mostra messaggi precedenti
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    else:
        st.chat_message("assistant").write(msg.content)

# 3. LOGICA DI INTERAZIONE
if prompt := st.chat_input("Chiedimi un'analisi (es: Analizza Tesla)"):
    st.chat_message("user").write(prompt)
    
    # Costruzione dell'input arricchito dal contesto del profilo
    full_input = f"""
    Profilo Utente: Rischio {risk_profile}, Budget ${budget}, Preferenze: {preferences}.
    Richiesta: {prompt}
    """
    
    with st.chat_message("assistant"):
        with st.spinner("L'agente sta analizzando i tool e pianificando la risposta..."):
            try:
                response = st.session_state.agent.invoke({
                    "input": full_input,
                    "chat_history": st.session_state.chat_history
                })
                output = response["output"]
                st.write(output)
                
                # Aggiornamento Memoria (Pag. 303)
                st.session_state.chat_history.append(HumanMessage(content=prompt))
                st.session_state.chat_history.append(AIMessage(content=output))
            except Exception as e:
                st.error(f"Errore durante l'analisi: {e}")

