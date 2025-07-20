import json
import csv
from datetime import datetime

# Load the raw JSON file
with open("user-wallet-transactions.json", "r") as f:
    data = json.load(f)

# Open a CSV file to write to
with open("wallet_transactions.csv", "w", newline="") as f:
    writer = csv.writer(f)

    # Write the header
    writer.writerow([
        "userWallet",
        "network",
        "protocol",
        "action",
        "amount",
        "assetSymbol",
        "assetPriceUSD",
        "poolId",
        "timestamp_utc",
        "txHash",
        "logId"
    ])

    # Write each row
    for tx in data:
        ad = tx["actionData"]
        writer.writerow([
            tx["userWallet"],
            tx["network"],
            tx["protocol"],
            tx["action"],
            float(ad["amount"]) / 1e6,  
            ad["assetSymbol"],
            ad["assetPriceUSD"],
            ad["poolId"],
            datetime.utcfromtimestamp(tx["timestamp"]).isoformat(),
            tx["txHash"],
            tx["logId"]
        ])

print("✅ Converted to wallet_transactions.csv")
