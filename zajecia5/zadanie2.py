import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Ustawienia strony
st.set_page_config(page_title="Sprzedaż - Aplikacja Webowa", layout="centered")

# Funkcja: połączenie z bazą
@st.cache_data
def load_data():
    conn = sqlite3.connect('sales.db')
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()
    return df

# Funkcja: dodanie rekordu
def add_record(product, quantity, price, date):
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO sales (product, quantity, price, date)
        VALUES (?, ?, ?, ?)
    """, (product, quantity, price, date))
    conn.commit()
    conn.close()

# --- Sekcja: dodanie rekordu ---
st.title("Aplikacja sprzedażowa (SQLite + Streamlit)")

st.header("+ Dodaj nową sprzedaż")
with st.form("add_form"):
    product = st.text_input("Produkt")
    quantity = st.number_input("Ilość", min_value=1, step=1)
    price = st.number_input("Cena jednostkowa (zł)", min_value=0.0, step=0.01)
    date = st.date_input("Data sprzedaży")
    submitted = st.form_submit_button("Dodaj rekord")
    if submitted:
        add_record(product, quantity, price, date.strftime("%Y-%m-%d"))
        st.success(f"Dodano: {product} x{quantity} za {price} zł ({date}) 🎉")
        st.balloons()

# --- Sekcja: wyświetlanie danych ---
st.header("Tabela sprzedaży")
df = load_data()

# Filtrowanie po produkcie
products = df['product'].unique().tolist()
selected_product = st.selectbox("Filtruj po produkcie", ["Wszystkie"] + products)

if selected_product != "Wszystkie":
    df = df[df['product'] == selected_product]

st.dataframe(df)

# --- Wykres 1: Sprzedaż dzienna (ilość × cena) ---
st.subheader("Wykres: Sprzedaż dzienna (wartość)")
df['sale_value'] = df['quantity'] * df['price']
daily_sales = df.groupby('date')['sale_value'].sum().reset_index()

fig1, ax1 = plt.subplots()
ax1.plot(daily_sales['date'], daily_sales['sale_value'], marker='o')
ax1.set_xlabel("Data")
ax1.set_ylabel("Wartość sprzedaży (zł)")
ax1.set_title("Sprzedaż dzienna")
st.pyplot(fig1)

# --- Wykres 2: Suma sprzedanych sztuk wg typu produktu ---
st.subheader("Wykres: Ilość sprzedanych produktów wg typu")
product_sales = df.groupby('product')['quantity'].sum().reset_index()

fig2, ax2 = plt.subplots()
ax2.bar(product_sales['product'], product_sales['quantity'], color='skyblue')
ax2.set_xlabel("Produkt")
ax2.set_ylabel("Liczba sprzedanych sztuk")
ax2.set_title("Suma sprzedanych produktów wg typu")
st.pyplot(fig2)

# Opcjonalny checkbox do odświeżenia danych
if st.checkbox("Odśwież dane"):
    st.experimental_rerun()
