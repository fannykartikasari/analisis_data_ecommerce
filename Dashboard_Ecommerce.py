import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Set the style for seaborn
sns.set(style='dark')

# Streamlit title and caption
st.title('E-commerce Dashboard')
st.caption('by Fanny Kartika Sari - m002b4kx1389@bangkit.academy')
st.text('Selamat datang. Dashboard ini dibuat untuk kebutuhan pemenuhan tugas Dicoding')

# Import Data
sellers_df = pd.read_csv("https://raw.githubusercontent.com/fannykartikasari/analisis_data_ecommerce/refs/heads/main/olist_sellers_df.csv")
customer_df = pd.read_csv("https://raw.githubusercontent.com/fannykartikasari/analisis_data_ecommerce/refs/heads/main/olist_customers_df.csv")
product_df = pd.read_csv("https://raw.githubusercontent.com/fannykartikasari/analisis_data_ecommerce/refs/heads/main/merged_orders_products_df.csv")
city_counts_df = pd.read_csv("https://raw.githubusercontent.com/fannykartikasari/analisis_data_ecommerce/refs/heads/main/city_counts_df.csv")

# Create Tabs for analysis
tab1, tab2, tab3 = st.tabs(["Region","Analisis Lanjut", "Product"])

# Tab 1: Best Performing Region
with tab1:
    st.header("Best Performing Region")
    st.write('Pada tab ini, kita bisa menentukan wilayah mana saja yang memberikan performa terbaik yang dapat dilihat dari jumlah seller dan jumlah customer')
    st.write('Silahkan gunakan filter sesuai kebutuhan dalam melakukan analisis')

    # Filter by state
    st.markdown("##### Filter by State")
    state_options = sellers_df['seller_state'].unique().tolist()
    selected_states = st.multiselect("Select States", options=state_options, default=state_options)

    # Filter datasets by selected states
    sellers_filtered = sellers_df[sellers_df['seller_state'].isin(selected_states)]
    customers_filtered = customer_df[customer_df['customer_state'].isin(selected_states)]

    # Plot Number of Sellers by City
    st.write("#### Plot Number of Sellers by City")
    seller_city_counts = sellers_filtered['seller_city'].value_counts().head(10)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=seller_city_counts.values, y=seller_city_counts.index, palette='viridis')
    plt.title('Top 10 Cities with Maximum Number of Sellers in Selected States')
    plt.xlabel('Number of Sellers')
    plt.ylabel('City')
    st.pyplot(plt)

    # Plot Number of Customers by City
    st.write("#### Plot Number of Customers by City")
    customer_city_counts = customers_filtered['customer_city'].value_counts().head(10)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=customer_city_counts.values, y=customer_city_counts.index, palette='viridis')
    plt.title('Top 10 Cities with Maximum Number of Customers in Selected States')
    plt.xlabel('Number of Customers')
    plt.ylabel('City')
    st.pyplot(plt)


    # Add insights section
    st.header("Insights")
    st.markdown("""
    
    **Problem Statement**
    Daerah mana yang best-perform berdasarkan number of seller dan number of customer? Berikan rekomendasi area jika seorang bussinesman ingin membuka toko offline baru.
    
    Dengan menggunakan semua row data (tidak ada filter yang diterapkan), diperoleh insigth berikut :

    **Top 5 Kota dengan jumlah seller terbanyak adalah**
    1. Sao Paulo
    2. Curitiba
    3. Rio de Janeiro
    4. Belo Horizonte
    5. Ribeirão

    5 kota selanjutnya menunjukkan jumlah seller yang relatif hampir sama, yaitu
                
    6. Guarulhos
    7. Ibitinga
    8. Santo Andre
    9. Campinas
    10. Maringá

    **Top 10 Kota dengan jumlah customer terbanyak adalah**
    1. Sao Paulo
    2. Rio de Janeiro
    3. Belo Horizonte
    4. Brasilia
    5. Curitiba

    5 kota selanjutnya menunjukkan jumlah customer yang relatif hampir sama, yaitu
                
    6. Campinas
    7. Porto Alegre
    8. Salvador
    9. Guarulhos
    10. Sao Bernardo Do Campo

    Dari visualisasi di atas, Sao Paulo memiliki performa yang sangat bagus dari segi jumlah seller dan jumlah customer dibandingkan daerah lainnya.

    Rio de Janeiro memiliki total seller di urutan ketiga, namun memiliki jumlah customer di urutan kedua. Sedangkan Curitiba memiliki total seller di urutan kedua, namun memiliki jumlah customer online di urutan kelima. Artinya Rio de Janeiro menunjukkan lebih best-performing dibandingkan Curitiba. Bisa dikatakan converting rate Rio de Janeiro lebih tinggi dibandingkan daerah lainnya.

    Oleh karena itu, perlu adanya analisis lebih lanjut agar mendapatkan 3 rekomendasi kota yang cocok untuk membuka toko baru.
    """)

with tab2:
    st.header("City Clustering Analysis")
    st.write("Pada tab ini, kita akan melihat hasil clustering dari kota-kota berdasarkan beberapa skor.")

    # Filter hanya kolom city, num_customer_score, dan cluster_score
    city_cluster_df = city_counts_df[['city', 'num_convert_score','num_customer_score', 'cluster_score']]

    # Menampilkan tabel di Streamlit
    st.write("#### Tabel Hasil Clustering Kota")
    st.dataframe(city_cluster_df)

    st.write("num_convert_score dihitung dari rasio antara jumlah customer dengan jumlah seller lalu discore dari 1 hingga 5 (terbaik)")
    st.write("num_customer_score dihitung dari klusterisai jumlah customer dari 1 hingga 5 (terbaik)")
    st.write("Cluster_score diperoleh dari pembobotan num_convert_score dan num_customer_score yaitu 0.25 dan 0.75. Hal ini karena adanya kecenderungan untuk memilih berdasarkan jumlah customer dibandingkan rasio antara jumlah customer dengan jumlah seller")

    # Add insights section
    st.header("Insights")
    st.markdown("""

    **Problem Statement**
    Daerah mana yang best-perform berdasarkan number of seller dan number of customer? Berikan rekomendasi area jika seorang bussinesman ingin membuka toko offline baru.
    
    Dengan menggunakan semua row data (tidak ada filter yang diterapkan), diperoleh insigth berikut : 

    **Top 5 Kota dengan jumlah seller terbanyak adalah**
    1. Sao Paulo
    2. Curitiba
    3. Rio de jenairo
    4. Belo Horizeonte
    5. Riberirao

    **Top 5 Kota dengan jumlah customer terbanyak adalah**
    1. Sao Paulo
    2. Rio de jenairo
    3. Belo Horizeonte
    4. Brasilia
    5. Curitiba

    Rekomendasi : 
    Berikut 3 rekomendasi kota berdasarkan jumlah customer dan jumlah seller. (rekomendasi ini didasarkan dengan asumsi adanya seller yang memiliki toko offline juga dikarenakan adanya korelasi positif antara jumlah seller dan jumlah customer dari setiap kota). 

    1. Sao Paulo, terlihat karena jumlah customer dan seller di Sao Paulo sangat tinggi dibandingkan daerah yang lain. Oleh karena itu, Sao Paulo bisa dikatakan city lead dalam bisnis.

    2. Rio de jenairo, jumlah seller di urutan ketiga namun jumlah customer di urutan kedua. Dan terlihat bahwa nilai converting rate nya cukup tinggi

    3. Belo Horizonte, jumlah seller di urutan keempat namun jumlah customer di urutan ketiga. Dan terlihat bahwa nilai converting rate nya cukup tinggi

    4. Brasilia. Belum begitu banyak seller dari daerah ini, namun jumlah customer di area sini cukup banyak terlihat juga dari convert skorenya yang sama dengan kota Rio de Jenairo dan Belo Horinze.
    """)

# Tab 3: Best Performing Product
with tab3:
    st.header("Best Performing Product")
    st.write('Pada tab ini, kita bisa menentukan kriteria produk apa saja yang memberikan performa terbaik yang dapat dilihat dari total value dan jumlah pembelian')
    st.write('Silahkan gunakan filter sesuai kebutuhan dalam melakukan analisis')

    # Filters for price and freight value
    st.markdown("##### Filter by Price and Freight Value")
    price_min, price_max = st.slider("Select Price Range", 
                                      float(product_df['payment_value'].min()), 
                                      float(product_df['payment_value'].max()), 
                                      (float(product_df['payment_value'].min()), float(product_df['payment_value'].max())))
    
    freight_min, freight_max = st.slider("Select Freight Value Range", 
                                          float(product_df['freight_value'].min()), 
                                          float(product_df['freight_value'].max()), 
                                          (float(product_df['freight_value'].min()), float(product_df['freight_value'].max())))

    # Filter product_df based on selected ranges
    filtered_product_df = product_df[
        (product_df['payment_value'] >= price_min) & 
        (product_df['payment_value'] <= price_max) & 
        (product_df['freight_value'] >= freight_min) & 
        (product_df['freight_value'] <= freight_max)
    ]

    col1, col2 = st.columns(2)    
    with col1:
        avg_payment_value = filtered_product_df['payment_value'].mean()
        st.metric("Average Payment Value", format_currency(avg_payment_value, currency='BRL'))
    with col2:
        avg_freight_value = filtered_product_df['freight_value'].mean()
        st.metric("Average Freight Value", format_currency(avg_freight_value, currency='BRL'))

    # Plot Total of Payment Value by Product Category
    st.write("#### Plot Total of Payment Value by Product")
    product_cat_sum = filtered_product_df.groupby('product_category_name')['payment_value'].sum().sort_values(ascending=False).head(10).reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(x=product_cat_sum['payment_value'], y=product_cat_sum['product_category_name'], palette='viridis')
    plt.title('Top 10 Product Categories by Payment Value')
    plt.xlabel('Payment Value')
    plt.ylabel('Product Category')
    st.pyplot(plt)

    # Plot Number of Orders by Product Category
    st.write("#### Plot Number of Orders by Product")
    product_cat_order_count = filtered_product_df.groupby('product_category_name')['order_id'].count().sort_values(ascending=False).head(10).reset_index()

    plt.figure(figsize=(10, 6))
    sns.barplot(x=product_cat_order_count['order_id'], y=product_cat_order_count['product_category_name'], palette='viridis')
    plt.title('Top 10 Product Categories by Number of Purchases')
    plt.xlabel('Number of Purchases')
    plt.ylabel('Product Category')
    st.pyplot(plt)



    # Add insights section
    st.header("Insights")
    st.markdown("""
    **Problem Statement**
    Kategori produk apa yang best-perform?
    
    Dengan menggunakan semua row data (tidak ada filter yang diterapkan), diperoleh insigth berikut :
                
    **5 kategori produk dengan nilai value tertinggi**

    1. cama_mesa_banho
    2. beleza_saude
    3. informatica_acessoris
    4. relogios_presentes
    5. moveis_decoracao

    **5 kategori produk dengan jumlah purchase tertinggi**

    1. cama_mesa_banho
    2. beleza_saude
    3. esporte_lazer
    4. moveis_decoracao
    5. informatica_acessorios
    """)