import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("2003_2017_waste.csv")

# Clean column names and drop NA
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
df = df.dropna()

# Create not recycled column
df['not_recycled'] = df['total_waste_generated_tonne'] - df['total_waste_recycled_tonne']

st.title("♻️ Waste Data Analysis Dashboard")

# Waste type vs recycling rate
st.subheader("Waste Type vs Recycling Rate")
fig1 = plt.figure()
sns.barplot(data=df, x='waste_type', y='recycling_rate')
plt.xticks(rotation=45)
plt.xlabel('Waste Type')
plt.ylabel('Recycling Rate')
st.pyplot(fig1)

# Not recycled trend
st.subheader("Not Recycled Waste Over the Years")
fig2 = plt.figure()
sns.lineplot(data=df, x='year', y='not_recycled', marker='o')
plt.ylabel('Amount of Not Recycled Waste')
st.pyplot(fig2)

# Recycling rate over time by waste type
st.subheader("Recycling Rate Over Time by Waste Type")
fig3 = plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="year", y="recycling_rate", hue="waste_type", marker="o")
plt.title("Recycling Rate by Waste Type")
plt.grid(True)
st.pyplot(fig3)

# Total Waste per year
st.subheader("Total Waste Generated per Year")
total_by_year = df.groupby("year")["total_waste_generated_tonne"].sum().reset_index()
fig4 = plt.figure()
sns.barplot(data=total_by_year, x="year", y="total_waste_generated_tonne", palette="viridis")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig4)
