import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tools import financial_tool_kit

load_dotenv()

def get_financial_agent():
    # LLM Aggiornato: Llama 3.3 70B Versatile (Modello di punta Gennaio 2026)
    llm = ChatGroq(
        model="llama-3.3-70b-versatile", 
        temperature=0, 
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    # Prompt ottimizzato (Pag. 293)
    prompt = ChatPromptTemplate.from_messages([
        ("system", """Sei un Agente Finanziario Senior esperto in analisi di mercato.
        Analizza i mercati usando i tool forniti.
        
        REGOLE:
        1. Recupera sempre prezzo e notizie per un'analisi completa.
        2. Adatta il consiglio al profilo di rischio dell'utente.
        3. Se il profilo non è specificato, chiedilo.
        """),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    agent = create_tool_calling_agent(llm, financial_tool_kit, prompt)

    return AgentExecutor(
        agent=agent, 
        tools=financial_tool_kit, 
        verbose=True,
        handle_parsing_errors=True
    )

if __name__ == "__main__":
    try:
        agent = get_financial_agent()
        print("--- AVVIO AGENTE (MODELLO 3.3 VERSATILE) ---")
        res = agent.invoke({
            "input": "Analizza NVIDIA (NVDA). Sono un investitore con profilo Speculativo.",
            "chat_history": []
        })
        print("\nCONSULENZA FINALE:\n", res["output"])
    except Exception as e:
        print(f"\nERRORE: {e}")
