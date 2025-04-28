import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# إعداد صفحة التطبيق
st.set_page_config(page_title="Light Book Analysis", page_icon="📚", layout="centered")

# تحميل الداتا
@st.cache_data
def load_data():
    df = pd.read_csv("books_full_data_cleaned.csv")
    return df

df = load_data()

# العنوان والمقدمة
st.title("📚 Light Book Price & Rating Analysis")
st.write("A simple, fast app to explore book data interactively.")

# ملخص سريع
st.header("📊 Quick Stats")
col1, col2, col3 = st.columns(3)
col1.metric("Avg Price (£)", f"{df['Price'].mean():.2f}")
col2.metric("Max Price (£)", f"{df['Price'].max():.2f}")
col3.metric("Min Price (£)", f"{df['Price'].min():.2f}")

# اختيار Rating وتصفية الداتا
st.header("🔍 Filter Books")
rating_filter = st.selectbox("Select Rating", sorted(df["Rating"].dropna().unique()))
availability_filter = st.checkbox("Show only available books")

filtered_df = df[df["Rating"] == rating_filter]

if availability_filter:
    filtered_df = filtered_df[filtered_df["Availability"] == True]

st.dataframe(filtered_df[["Title", "Price", "Availability", "Category"]].head(10))  # نعرض 10 كتب بس

# ----------------------------------------
# رسومات إضافية
st.header("📈 Visualizations")

# 1. توزيع عدد الكتب حسب التقييم
st.subheader("⭐ Book Count by Rating")
fig1, ax1 = plt.subplots(figsize=(5, 3))
sns.countplot(x="Rating", data=df, palette="pastel", ax=ax1)
ax1.set_xlabel("Rating")
ax1.set_ylabel("Number of Books")
st.pyplot(fig1)

# 2. توزيع الأسعار
st.subheader("💵 Price Distribution")
fig2, ax2 = plt.subplots(figsize=(5, 3))
sns.histplot(df["Price"], bins=20, color="skyblue", kde=True, ax=ax2)
ax2.set_xlabel("Price (£)")
ax2.set_ylabel("Frequency")
st.pyplot(fig2)

# 3. متوسط السعر حسب التقييم
st.subheader("📊 Average Price per Rating")
avg_price_by_rating = df.groupby("Rating")["Price"].mean().reset_index()
fig3, ax3 = plt.subplots(figsize=(5, 3))
sns.barplot(x="Rating", y="Price", data=avg_price_by_rating, palette="muted", ax=ax3)
ax3.set_xlabel("Rating")
ax3.set_ylabel("Average Price (£)")
st.pyplot(fig3)

# ----------------------------------------

# الخاتمة
st.markdown("---")
st.caption("Developed by legends 🚀 ")
