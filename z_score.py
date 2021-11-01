from reuterspy import Reuters
reuters = Reuters()
import pandas as pd
pd.set_option('display.max_rows', None)
from yahoofinancials import YahooFinancials

ticker_reuters = input("Enter ticker for Reuters: ")
ticker_yahoo = input("Enter ticker for yahoo: ")

def reshape_reuters_statements(df):
    return df.pivot(index="metric", columns="year", values="value").reset_index()

def get_metric_latest_bs(df, metric_name):
    return int(float(df[2020][df['metric'] == metric_name].iloc[0]))

ticker_list = [ticker_reuters]

# Different statements
# df_cf = reuters.get_cash_flow(ticker_list)
# print("df_cf: ", df_cf)

# df_cf = reshape_reuters_statements(df_cf)

df_bs = reuters.get_balance_sheet(ticker_list)
df_bs = reshape_reuters_statements(df_bs)

df_is = reuters.get_income_statement(ticker_list)
df_is = reshape_reuters_statements(df_is)

df_key_metrics = reuters.get_key_metrics(ticker_list)

# Calculate A

total_current_assets = int(float(df_bs[2020][df_bs['metric'] == 'Total Current Assets'].iloc[0]))
total_current_liabilities = get_metric_latest_bs(df_bs, 'Total Current Liabilities')
print(int(total_current_assets))
print(type(total_current_liabilities))
# Working capital = total_current_assets - total_current_liabilities
working_capital = total_current_assets - total_current_liabilities
print(working_capital)

total_assets = get_metric_latest_bs(df_bs, 'Total Assets')
print(total_assets)

A = working_capital/(float(total_assets))
print(A)

# B
retained_earnings = get_metric_latest_bs(df_bs, 'Retained Earnings (Accumulated Deficit)')
retained_earnings
B = retained_earnings/(float(total_assets))

# C

ebit = get_metric_latest_bs(df_is, 'Revenue') - get_metric_latest_bs(df_is, 'Total Operating Expense')
C = ebit / float(total_assets)
print(C)

## D = Market Value of Equity / Total Liabilities

import yfinance as yf
pd.set_option('display.float_format', str)
ticker = yf.Ticker(ticker_yahoo)

yahoo_financials = YahooFinancials(ticker_yahoo)

# Hakee hinnan
yahoo_financials.get_prev_close_price()

# prev close 22.9.2021
price = yahoo_financials.get_prev_close_price()

ticker_yfinance = yf.Ticker(ticker_yahoo)
shares = ticker_yfinance.info['sharesOutstanding']

# Kaikki muut arvot ilmoitettu miljoonissa
market_value_of_equity = (price*shares)/(1000000)

liabilities = get_metric_latest_bs(df_bs,'Total Liabilities')
print(liabilities)

D = market_value_of_equity/float(liabilities)
print("D: ", D)

E = get_metric_latest_bs(df_is, 'Revenue') / float(get_metric_latest_bs(df_bs, 'Total Debt'))
print("E: ", E)

Z = (1.2*A)+(1.4*B)+(3.3*C)+(0.6*D)+(1.0*E)
print("Z: ", Z)