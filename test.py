# test.py
from yahoofinancials import YahooFinancials

ticker = 'A'
yahoo_financials = YahooFinancials(ticker)

print("yahoo financials")
print(yahoo_financials)

balance_sheet_data_qt = yahoo_financials.get_financial_stmts('quarterly', 'balance')
print("balance sheet quarterly")
print(balance_sheet_data_qt)