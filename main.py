from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
# Import all things necessary for web app
import yfinance as yf 
# Import Yahoo Finance Library
import pandas as pd
# Import Library for the necessary calculations (Got the idea from ChatGPT)
import matplotlib.pyplot as plt
# Import the Library for the pie chart (Stil not really comfortable with the data visualization used ChatGPT's help a lot for the pie chart incorporation)
app = FastAPI()

# Set up templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

portfolio = []


def fetch_stock_price(symbol):
    """
    This part of the code is designed for the user to input the stock they are looking at
    and the code will get the stock price using the yfinance library
    """
    try:
        stock = yf.Ticker(symbol)
        price = stock.history(period="1d")["Close"].iloc[-1] # For Close and iloc had to use the help of ChatGPT to understand how to use yfinance, Close refers to the price at the end of the trading session, iloc gets the most recent closing price of the Close prices
        return round(price, 2) # Rounding to 2 decimal places to make it easier to read
    except:
        return None # Not return anything if Ticket is not found in yfinance library

def calculate_portfolio_value(portfolio):
    """
    This part of the code is designed calculate the portfolios value by multiplying the number of stocks owned by the current price for each respective stock
    """
    total_value = 0 # Starts value at 0 
    for stock in portfolio:
        total_value += stock["current_price"] * stock["shares"]
    return round(total_value, 2) # Round to 2 decimal places to make it easier to read

def plot_portfolio_allocation(portfolio, output_file="static/allocation.png"):
    """
    This is the part of the code where the pice chart is created showing the percentage of the portfolio that each stock has
    """
    if len(portfolio) == 0:
        return
    symbols = [stock["symbol"] for stock in portfolio]
    values = [stock["current_price"] * stock["shares"] for stock in portfolio]
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=symbols, autopct="%1.1f%%")
    plt.title("Portfolio Allocation")
    plt.savefig(output_file)
    plt.close()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """
    This part of the code renders the homepage getting the data from the index.hmtl file and also the inputed portfolio data
    """
    if len(portfolio) > 0:
        plot_portfolio_allocation(portfolio) # Making sure no chart is created with 0 stocks inputed
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "portfolio": portfolio,
        "total_value": calculate_portfolio_value(portfolio)
    })


@app.post("/add-stock", response_class=HTMLResponse)
def add_stock(request: Request, symbol: str = Form(...), shares: int = Form(...), purchase_price: float = Form(...)):
    # I had to use the help of ChatGPT to get the Form(...) solution because without it there was some issues with the code
    """
    This part of the code is responsible for adding new stock prices
    """
    current_price = fetch_stock_price(symbol)
    
    if not current_price: 
        return templates.TemplateResponse("index.html", {
            "request": request,
            "portfolio": portfolio,
            "error": f"Could not fetch price for {symbol}",
            "total_value": calculate_portfolio_value(portfolio)
        }) # In case of error
    
    # Calculate gain or loss
    gain_loss = (current_price - purchase_price) * shares
    
    stock_data = {
        "symbol": symbol,
        "shares": shares,
        "purchase_price": purchase_price,
        "current_price": current_price,
        "gain_loss": round(gain_loss, 2),
        "color": "green" if gain_loss >= 0 else "red"  # Decide color based on gain or loss
    }
    portfolio.append(stock_data)
    
    # Update the pie chart because now there would be at least more than 0 stocks added
    if len(portfolio) > 0:
        plot_portfolio_allocation(portfolio)
    
    # Reloads page with updated data
    return templates.TemplateResponse("index.html", {
        "request": request,
        "portfolio": portfolio,
        "total_value": calculate_portfolio_value(portfolio)
    })
