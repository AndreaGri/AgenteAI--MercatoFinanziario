import yfinance as yf
from langchain.tools import tool

@tool
def get_stock_price(symbol: str):
    """Ottiene il prezzo corrente di un'azione dato il suo ticker."""
    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period="1d")
        if hist.empty: return f"Nessun dato per {symbol}."
        return f"Il prezzo di {symbol} è {hist['Close'].iloc[-1]:.2f} USD."
    except Exception as e:
        return f"Errore prezzo: {str(e)}"

@tool
def get_financial_news(symbol: str):
    """Ottiene le ultime notizie finanziarie per un ticker."""
    try:
        ticker = yf.Ticker(symbol)
        news = ticker.news[:3]
        if not news: return f"Nessuna notizia per {symbol}."
        
        formatted = []
        for n in news:
            # Uso .get() per evitare KeyError (Senior Best Practice)
            title = n.get('title', n.get('headline', 'Titolo non disponibile'))
            publisher = n.get('publisher', 'Fonte sconosciuta')
            formatted.append(f"- {title} (Fonte: {publisher})")
        return "\n".join(formatted)
    except Exception as e:
        return f"Errore notizie: {str(e)}"

financial_tool_kit = [get_stock_price, get_financial_news]
