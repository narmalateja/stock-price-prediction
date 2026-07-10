import pandas as pd
import matplotlib.pyplot as plt

# Sample stock data
days = [1, 2, 3, 4, 5]
prices = [100, 102, 101, 105, 107]

# Create DataFrame
df = pd.DataFrame({"Day": days, "Price": prices})

# Prediction using average
prediction = df["Price"].mean()

print("Predicted Next Day Price:", prediction)

# Plot graph
plt.plot(days, prices, marker='o')
plt.title("Stock Price Prediction")
plt.xlabel("Days")
plt.ylabel("Price")
plt.show()