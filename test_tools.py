from tools import get_stock_price, get_financial_news

print("--- Test Prezzo Azionario ---")
print(get_stock_price.run("NVDA"))

print("\n--- Test Notizie Finanziarie ---")
print(get_financial_news.run("NVDA"))
