<h1 align="center">📈 Indexized</h1>

<p align="center">
  <em>A sleek, data-driven stock tracking desktop app built with Python.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/UI-PySide6-orange?style=flat-square&logo=qt" />
  <img src="https://img.shields.io/badge/Data-yfinance-green?style=flat-square&logo=yahoo" />
  <img src="https://img.shields.io/badge/Database-SQLite-lightgrey?style=flat-square&logo=sqlite" />
  <img src="https://img.shields.io/badge/Charts-matplotlib-blueviolet?style=flat-square&logo=plotly" />
</p>

---

## 🖼️ Preview

> 💡 *Add an image of your app’s interface here (e.g., a screenshot or GIF).*

<p align="center">
  <img src="assets/screenshot.png" alt="Indexized UI Preview" width="800">
</p>

---

## 🧠 Overview

**Indexized** is a **modern desktop stock tracking and portfolio management app**, designed to make financial insights simple, visual, and interactive.  
It combines the power of **Yahoo Finance**, **PySide6 UI**, **SQLite storage**, and **Matplotlib** visualization — all wrapped in a clean interface.

---

## ⚙️ Features

### 🏠 **Home Tab**
Your dashboard for quick insights:
- Personalized greeting: `"Hello, <user>!"`
- Random inspirational quote fetched dynamically.
- Three sub-tabs for market summaries:
  - **Top Gainers:** Displays the 5 best-performing stocks.
  - **Top Losers:** Shows the 5 weakest stocks.
  - **Currencies:** Lists top 5 global currency exchange rates.

---

### 📊 **Stock Tracker**
Visualize and explore any stock:
- Select a **ticker** to track.
- View **historical evolution** and **live data**.
- Choose timeframes like `1d`, `5d`, `1mo`, `3mo`, `6mo`, `1y`, etc.
- Interactive **matplotlib charts** show price trends and movements.
- Additional company and market metrics for deeper insight.

---

### 💼 **Portfolio Manager**
Manage your personalized investment portfolio:
- Add or remove assets easily.
- Track asset quantities and total portfolio value.
- Four main controls:
  - ➕ **Add:** Add a specified amount of the selected ticker.
  - ➖ **Subtract:** Remove a specified amount.
  - 🗑️ **Delete:** Remove a ticker entirely.
  - 🔴 **Reset:** Clear the portfolio with one click.
- All data is securely stored in an **SQLite** database for persistence.

---

### 📚 **Asset Library**
Explore all supported assets, neatly categorized:
- Browse **whitelisted tickers** grouped by sector or category.
- Ensures only valid, verified assets can be tracked or added.

---

## 🧩 Tech Stack

| Component | Description |
|------------|-------------|
| **Python** | Core programming language |
| **PySide6** | GUI framework (Qt for Python) |
| **yfinance** | Fetches real-time and historical stock/currency data |
| **SQLite** | Local database for portfolio storage |
| **Matplotlib** | Plots and visualizes stock data |
| **SQLAlchemy** *(optional)* | ORM layer for database handling |

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/Indexized.git
cd Indexized
