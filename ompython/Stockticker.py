from googlefinance import getQuotes
import json

stocks = ["FANG", "TDY", "TSLA"]

print(json.dumps(getQuotes(stocks), indent = 2))