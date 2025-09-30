import pandas as pd
from prophet import Prophet

# 1. Load the dataset
df = pd.read_excel("data/online_retail_II.xlsx")
print (df.columns)

# 2. Clean the data
df = df.dropna(subset=["Invoice", "InvoiceDate", "Quantity", "Price"])
df = df[(df["Quantity"] > 0) & (df["Price"] > 0)]
df["Revenue"] = df["Quantity"] * df["Price"]

# 3. Filter one country (UK has the most data)
df = df[df["Country"] == "United Kingdom"]

# 4. Aggregate daily revenue
daily = df.groupby(df["InvoiceDate"].dt.date).agg(Revenue=("Revenue","sum")).reset_index()

# 5. Forecast using Prophet
daily = daily.rename(columns={"InvoiceDate":"ds", "Revenue":"y"})
m = Prophet()
m.fit(daily)
future = m.make_future_dataframe(periods=90)  # forecast 90 days ahead
forecast = m.predict(future)

# 6. Save outputs
daily.to_csv("data/actuals.csv", index=False)
forecast[["ds","yhat","yhat_lower","yhat_upper"]].to_csv("data/forecast.csv", index=False)

print("✅ Done! Files saved in /data: actuals.csv & forecast.csv")

