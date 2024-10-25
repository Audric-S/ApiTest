# Install necessary packages before running
# !pip install yfinance streamlit matplotlib

import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Define a list of ticker symbols for selection
ticker_symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NFLX", "NVDA", "BRK-B", "JPM", "V"]

# Streamlit app
st.title("Stock Data Dashboard")

# Dropdown to select a ticker symbol
selected_ticker = st.selectbox("Select a stock ticker:", ticker_symbols)

# Create a Ticker object based on selection
ticker = yf.Ticker(selected_ticker)

# Tabs for different data categories
tabs = st.tabs(["Overview", "Historical Data", "Financial Statements", "Shareholders", "Analyst Ratings", "Options", "News"])

# Overview tab
with tabs[0]:
    st.header(f"{selected_ticker} - Company Information")
    st.write(ticker.info)
    st.header("Calendar Events")
    st.write(ticker.calendar)

# Historical Data tab
with tabs[1]:
    st.header(f"{selected_ticker} - Historical Data (Last Month)")
    hist_data = ticker.history(period="1mo")
    st.line_chart(hist_data['Close'], width=0, height=400, use_container_width=True)
    st.write("Metadata for historical data:")
    st.write(ticker.history_metadata)
    
    # Plot Volume
    fig, ax = plt.subplots()
    ax.bar(hist_data.index, hist_data['Volume'], color='purple')
    ax.set_title(f"{selected_ticker} - Trading Volume (1 Month)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Volume")
    st.pyplot(fig)

    # Stock Actions
    st.header("Stock Actions")
    st.write(ticker.actions)
    st.write("Dividends:", ticker.dividends)
    st.write("Splits:", ticker.splits)

# Financial Statements tab
with tabs[2]:
    st.header(f"{selected_ticker} - Financial Statements")
    st.subheader("Income Statement")
    st.write(ticker.income_stmt)
    st.subheader("Quarterly Income Statement")
    st.write(ticker.quarterly_income_stmt)

    st.subheader("Balance Sheet")
    st.write(ticker.balance_sheet)
    st.subheader("Quarterly Balance Sheet")
    st.write(ticker.quarterly_balance_sheet)

    st.subheader("Cash Flow Statement")
    st.write(ticker.cashflow)
    st.subheader("Quarterly Cash Flow Statement")
    st.write(ticker.quarterly_cashflow)

# Shareholders tab
with tabs[3]:
    st.header(f"{selected_ticker} - Shareholders")
    st.subheader("Major Holders")
    st.write(ticker.major_holders)
    st.subheader("Institutional Holders")
    st.write(ticker.institutional_holders)
    st.subheader("Mutual Fund Holders")
    st.write(ticker.mutualfund_holders)
    st.subheader("Insider Transactions")
    st.write(ticker.insider_transactions)
    st.subheader("Insider Purchases")
    st.write(ticker.insider_purchases)
    st.subheader("Insider Roster Holders")
    st.write(ticker.insider_roster_holders)
    st.subheader("Sustainability")
    st.write(ticker.sustainability)

# Analyst Ratings tab
with tabs[4]:
    st.header(f"{selected_ticker} - Analyst Ratings and Recommendations")
    st.subheader("Recommendations")
    st.write(ticker.recommendations)
    st.subheader("Recommendations Summary")
    st.write(ticker.recommendations_summary)
    st.subheader("Upgrades and Downgrades")
    st.write(ticker.upgrades_downgrades)

    st.subheader("Analyst Data")
    st.write("Price Targets:", ticker.analyst_price_targets)
    st.write("Earnings Estimate:", ticker.earnings_estimate)
    st.write("Revenue Estimate:", ticker.revenue_estimate)
    st.write("Earnings History:", ticker.earnings_history)
    st.write("EPS Trend:", ticker.eps_trend)
    st.write("EPS Revisions:", ticker.eps_revisions)
    st.write("Growth Estimates:", ticker.growth_estimates)

# Options tab
with tabs[5]:
    st.header(f"{selected_ticker} - Options Data")
    st.write("Available Options Expiration Dates:", ticker.options)
    selected_date = st.selectbox("Select an expiration date:", ticker.options)
    if selected_date:
        opt_chain = ticker.option_chain(selected_date)
        st.subheader("Calls")
        st.write(opt_chain.calls)
        st.subheader("Puts")
        st.write(opt_chain.puts)

# News tab
with tabs[6]:
    st.header(f"{selected_ticker} - Latest News")
    st.write(ticker.news)

