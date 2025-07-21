# ECommerce_Agent
A FastAPI-based AI agent that answers natural language questions about e-commerce data using SQLite. It translates queries to SQL, returns results, and generates charts for visual insights. No internet or cloud API required—fully local.

E-commerce AI Agent – Natural Language Query API
This project builds an AI-powered agent that answers natural language questions about e-commerce data (like sales, ad spend, and product eligibility) using a custom FastAPI backend, SQL database, and optional chart visualization.

Features
Accepts human language questions (like "What is my total sales?")
 Converts questions into SQL queries
 Queries a local SQLite database
 Returns clean, readable responses
 (Bonus) Generates charts for visualizable queries
Built with FastAPI, SQLite, and Python

Example Questions It Can Answer
What is my total sales?

Calculate the RoAS (Return on Ad Spend)

Which product had the highest CPC?

Show sales per product (with bar chart)

Which eligible products performed best?

🧱 Tech Stack
Layer	Technology
Backend API	FastAPI
Database	SQLite (with CSV-loaded tables)
Logic Engine	Rule-based SQL builder (llm_interface.py)
Charts	Matplotlib
Server	Uvicorn
Language	Python 3.x
