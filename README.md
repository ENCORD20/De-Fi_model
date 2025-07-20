# 🧠 DeFi Wallet Credit Scoring using Machine Learning

This project builds a machine learning model that assigns **credit scores (0–1000)** to DeFi wallets based solely on their **historical transaction behavior** using data from the **Aave V2 protocol**. The scores reflect the financial behavior of wallets:
- Higher scores indicate **reliable, consistent, and responsible usage**
- Lower scores may suggest **risky, bot-like, or exploitative behavior**

---

## 📁 Dataset

- Format: CSV file with 100,000+ raw DeFi transactions
- Source: Aave V2 protocol
- Each row represents a wallet action like `deposit`, `borrow`, `repay`, etc.
- Key columns:
  - `userWallet`
  - `action`, `amount`, `assetSymbol`, `assetPriceUSD`
  - `timestamp_utc`, `protocol`, `network`, `txHash`, etc.

---

## ⚙️ Features Engineered

We aggregate transactions per wallet to generate features:
- **Transaction Frequency**: Count of actions per wallet
- **Total and Average Amount Transacted**
- **Volatility Metrics**: Standard deviation in amount and price
- **Price Behavior**: Average, max, min of `assetPriceUSD`

---

## 🤖 Model

- **Algorithm**: `RandomForestRegressor`
- **Target**: A simulated `credit_score` in range [300, 950]
- **Input Features**: Aggregated transaction statistics
- **Output**: `predicted_credit_score` for each wallet

---

## 📊 Visualization

- Plotted **unsorted credit scores** per wallet to visualize distribution
- Time-series graphs showing:
  - `amount` over time
  - `assetPriceUSD` over time

---

## 🚀 How to Run

1. Clone the repo  
   ```bash
   git clone https://github.com/yourusername/defi-wallet-credit-score.git
   cd defi-wallet-credit-score
