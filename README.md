# AgenteAI--MercatoFinanziario

```markdown
# 📈 Agente Finanziario Intelligente (AI Agent)

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/LLM-Groq%20Llama3-orange)
![License](https://img.shields.io/badge/License-MIT-green)

Questo repository ospita un **Agente Finanziario Agentico** avanzato, progettato per analizzare dati di mercato, fornire approfondimenti su titoli azionari e assistere nelle decisioni finanziarie. Il progetto applica i principi di **AI Engineering** per costruire un sistema robusto, capace di ragionare (ReAct) e utilizzare strumenti esterni in tempo reale.

## 🔭 Panoramica del Progetto

L'applicazione funge da consulente finanziario personale basato su AI. A differenza dei chatbot standard, questo agente non si limita a generare testo, ma **agisce**: cerca dati aggiornati, legge notizie finanziarie e analizza i trend di mercato prima di rispondere.

### ✨ Funzionalità Chiave

* **Analisi Azionaria in Tempo Reale**: Recupero istantaneo di prezzi, volumi e dati fondamentali (P/E, Market Cap) tramite `YFinance`.
* **Web Search Intelligence**: Utilizzo di `DuckDuckGo` per trovare le ultime notizie macroeconomiche e verificare i tassi di interesse attuali, riducendo le allucinazioni.
* **Profilazione Utente Dinamica**: L'agente adatta le risposte in base al profilo di rischio dell'utente e alla cronologia della conversazione.
* **Interfaccia Chat Interattiva**: UI pulita e reattiva costruita con Streamlit.
* **Compliance & Sicurezza**: Logica progettata per evitare consigli finanziari rischiosi non verificati.

## 🚀 Architettura del Sistema

Il sistema segue il pattern architetturale **ReAct (Reasoning and Acting)**:

1.  **Brain (Cervello)**: Il modello **Llama 3.3-70B** (tramite Groq Cloud) gestisce il ragionamento complesso. Decide *quale* tool usare in base alla domanda dell'utente.
2.  **Tools (Strumenti)**:
    * `Yahoo Finance Tool`: Accesso diretto ai mercati azionari.
    * `Web Search Tool`: Accesso a internet per news e verifica fattuale.
3.  **Memory (Memoria)**: Gestione dello stato della conversazione per mantenere il contesto tra una domanda e l'altra.
4.  **Frontend**: Streamlit gestisce l'input utente e il rendering delle risposte e dei grafici.

## 🛠️ Stack Tecnologico

| Componente | Tecnologia | Descrizione |
| :--- | :--- | :--- |
| **Backend** | Python 3.12 | Linguaggio core. |
| **LLM Provider** | Groq | Inferenza ultra-veloce per Llama 3. |
| **Orchestration** | LangChain / Phidata | Gestione della logica dell'agente e dei tool. |
| **Data Source** | YFinance | Dati di mercato e storici azionari. |
| **Search Engine** | DuckDuckGo | Ricerca web per dati non strutturati. |
| **Frontend** | Streamlit | Interfaccia utente web. |

## 📦 Installazione e Configurazione

Segui questi passaggi per avviare l'agente in locale o su GitHub Codespaces.

### 1. Prerequisiti
Assicurati di avere installato:
* Python 3.10 o superiore
* Git

### 2. Clona il Repository
```bash
git clone [https://github.com/AndreaGri/AgenteAI--MercatoFinanziario.git](https://github.com/AndreaGri/AgenteAI--MercatoFinanziario.git)
cd AgenteAI--MercatoFinanziario

```

### 3. Configura l'Ambiente Virtuale

È consigliato usare un ambiente virtuale per isolare le dipendenze.

```bash
# Crea l'ambiente
python -m venv venv

# Attiva l'ambiente
# Su Windows:
.\venv\Scripts\activate
# Su Mac/Linux:
source venv/bin/activate

```

### 4. Installa le Dipendenze

```bash
pip install -r requirements.txt

```

### 5. Configurazione API Key

Crea un file `.env` nella root del progetto e inserisci la tua chiave API di Groq (ottenibile su [console.groq.com](https://console.groq.com)):

```env
GROQ_API_KEY=gsk_la_tua_chiave_api_qui
# Opzionale: Se usi Phidata o Langsmith
PHI_API_KEY=la_tua_chiave_phi

```

## ▶️ Utilizzo

Per avviare l'applicazione web:

```bash
streamlit run app.py

```

*Nota: Se il file principale ha un nome diverso (es. `playground.py` o `main.py`), sostituisci `app.py` con il nome corretto.*

Il browser si aprirà automaticamente all'indirizzo `http://localhost:8501`.

### Esempi di Prompt

Prova a chiedere all'agente:

* *"Qual è il prezzo attuale delle azioni Apple e qual è il trend dell'ultima settimana?"*
* *"Confronta i fondamentali di Nvidia e AMD."*
* *"Quali sono le ultime notizie sulla BCE e i tassi di interesse?"*

## ⚠️ Disclaimer Finanziario

Questo software è fornito esclusivamente a scopo **educativo e dimostrativo**.

* **Non è un consulente finanziario certificato.**
* Le informazioni fornite dall'AI potrebbero essere incomplete o non aggiornate.
* L'autore non si assume alcuna responsabilità per eventuali decisioni finanziarie prese sulla base dell'output di questo strumento. Esegui sempre le tue ricerche (DYOR).

## 👤 Autore

**AndreaGri**

* [GitHub Profile](https://www.google.com/search?q=https://github.com/AndreaGri)

---

*Progetto sviluppato come parte del percorso di AI Engineering.*

```

```
