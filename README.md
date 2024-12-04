Final Project Emil Bournigal

Investment Portfolio Tracker Final Project Emil Bournigal
1. Project Overview
I made a web app for tracking stock investmets. The user can input the stock symbol, amount of shares bought, purchase price and then see how the stock is performing for them. Also has a pie chart that gives you a better overview of the portfolio.

Features to add in the future:
I would like to add a way to sell stocks in the portfolio and for that to account as "cash"
Also maybe incorporate some risk analysis.
Also another thing that I could not incorporate and I acknowledge is a major flaw of the project is that if you add the same amount of stock twice it counts as 2 different stocks in the pie chart. 

2. Usage Guidelines
To use the application:

Run the main.py or just in the terminal run: uvicorn main:app --reload
Then access the page in browser.

When inside the page
Enter the stock symbol.
Enter the number of shares and purchase price.
Click the "Add Stock" button.

3. Dependencies
fastapi
uvicorn
yfinance
pandas
matplotlib
jinja2

4. Project Structure
Static Folder that contains:
style.css to style the index.html
allocation.png which is the pie chart image and going to be generated and updated as the pie chart is change in homepage.

Templates folder that contains:
index.html which is the HTML file homepage

Then files outside folders:
.gitignore
main.py which is the main code for the web app
readme.md which is this file

5. Collaboration Information
I did this project individually

6. Acknowledgments
ChatGPT: For brainstorming ideas, understanding libraries mainly the yfinance and mathplotlib, and debugging.

7. Reflection
I think this project in general went well, it was interesting to see how to apply all the skills learnt in the semester into one "big" project. I would have liked to start a bit sooner since I felt like I wanted to add more things. This project really showed me the importance of separating what I want to do with the code into different parts since for example when I was writing the code for the input of the data, I was thinking about how it would work with the pie chart when I had to take it 1 step at a time. I think what went well in the project is all the math involved is correct and the website looks clean and its easy to understand.

 I also faced many challenges for example my graph was not refreshing in the homepage because of browser caching. I had to use the help of ChatGPT to solve this. Also at first it was hard to understand how to use yfinance but ChatGPT helped me a lot with this. Also as I mentioned, I acknowledge that it is a major flaw that if you add the same amount of stock twice it counts as 2 different stocks in the pie chart. I have to recognize that when I tried to style the website on my own it looked messy and had to use the help of ChatGPT a lot specially in the styles.css file. I definetely enjoy more programming the "logical" or back end part of the project than the front end of the website.
