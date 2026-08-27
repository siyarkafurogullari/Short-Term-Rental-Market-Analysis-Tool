"""
Kısa Dönem Kiralama Fiyat & Doluluk Analiz Aracı
--------------------------------------------------
Herhangi bir şehir için Inside Airbnb "listings.csv" ve "calendar.csv"
dosyalarını yükle, otomatik olarak 4 temel analizi gör:

1. Mahalleye göre ortalama fiyat vs doluluk
2. Aylık mevsimsellik (doluluk oranı)
3. Rakip karşılaştırması (oda tipi + kapasiteye göre)
4. Tahmini kayıp gelir (kendi peer-grubuna göre az performans gösteren ilanlar)

Çalıştırmak için:
    pip install streamlit pandas plotly
    streamlit run app.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Kısa Dönem Kiralama Analiz Aracı", layout="wide")

st.title("📊 Kısa Dönem Kiralama Fiyat & Doluluk Analiz Aracı")
st.caption(
    "Inside Airbnb (http://insideairbnb.com) verisiyle çalışır. "
    "Bir şehrin listings.csv ve calendar.csv dosyalarını yükleyin."
)

# ---------------------------------------------------------------
# 1. Veri yükleme
# ---------------------------------------------------------------
col1, col2 = st.columns(2)
with col1:
    listings_file = st.file_uploader("listings.csv", type=["csv"])
with col2:
    calendar_file = st.file_uploader("calendar.csv", type=["csv"])

if not listings_file or not calendar_file:
    st.info("Devam etmek için her iki dosyayı da yükleyin.")
    st.stop()


@st.cache_data(show_spinner="Veri işleniyor...")
def load_data(listings_file, calendar_file):
    listings = pd.read_csv(listings_file, low_memory=False)
    calendar = pd.read_csv(calendar_file, low_memory=False)

    listings["price_num"] = (
        listings["price"].astype(str).replace(r"[\$,]", "", regex=True).astype(float)
    )
    listings = listings[(listings["price_num"] > 0) & (listings["price_num"] < 5000)].copy()

    calendar["date"] = pd.to_datetime(calendar["date"])
    calendar["month"] = calendar["date"].dt.to_period("M").astype(str)
    calendar["unavailable"] = (calendar["available"] == "f").astype(int)

    return listings, calendar


listings, calendar = load_data(listings_file, calendar_file)

neighbourhood_col = (
    "neighbourhood_cleansed" if "neighbourhood_cleansed" in listings.columns else "neighbourhood"
)

# Sidebar filtreleri
st.sidebar.header("Filtreler")
room_types = st.sidebar.multiselect(
    "Oda tipi", options=sorted(listings["room_type"].dropna().unique()),
    default=sorted(listings["room_type"].dropna().unique()),
)
min_listings = st.sidebar.slider("Mahalle başına minimum ilan sayısı", 1, 20, 5)

filtered = listings[listings["room_type"].isin(room_types)].copy()

# ---------------------------------------------------------------
# 2. Mahalleye göre fiyat vs doluluk
# ---------------------------------------------------------------
st.header("1️⃣ Mahalleye Göre Fiyat vs Doluluk")

neigh = (
    filtered.groupby(neighbourhood_col)
    .agg(
        ort_fiyat=("price_num", "mean"),
        ort_doluluk=("estimated_occupancy_l365d", "mean"),
        ilan_sayisi=("id", "count"),
    )
    .query("ilan_sayisi >= @min_listings")
    .sort_values("ort_doluluk", ascending=False)
    .round(1)
)

fig1 = px.scatter(
    neigh.reset_index(),
    x="ort_fiyat",
    y="ort_doluluk",
    size="ilan_sayisi",
    text=neighbourhood_col,
    labels={"ort_fiyat": "Ortalama Gecelik Fiyat ($)", "ort_doluluk": "Yıllık Ortalama Dolu Gece"},
)
fig1.update_traces(textposition="top center")
st.plotly_chart(fig1, use_container_width=True)
st.dataframe(neigh, use_container_width=True)

# ---------------------------------------------------------------
# 3. Mevsimsellik
# ---------------------------------------------------------------
st.header("2️⃣ Mevsimsellik — Aylık Doluluk Oranı")

season = calendar.groupby("month")["unavailable"].mean().reset_index()
season["doluluk_yuzde"] = (season["unavailable"] * 100).round(1)

fig2 = px.bar(
    season, x="month", y="doluluk_yuzde",
    labels={"month": "Ay", "doluluk_yuzde": "Dolu/Bloke %"},
)
st.plotly_chart(fig2, use_container_width=True)
st.caption(
    "Not: Bu oran gelecek 12 ay için host'un takviminde 'müsait değil' işaretli "
    "gün yüzdesidir (rezervasyon + host bloklaması dahil). Talep mevsimselliğinin "
    "yaklaşık bir göstergesidir."
)

# ---------------------------------------------------------------
# 4. Rakip karşılaştırması
# ---------------------------------------------------------------
st.header("3️⃣ Rakip Karşılaştırması")

c1, c2 = st.columns(2)
with c1:
    sel_room_type = st.selectbox("Oda tipi", sorted(filtered["room_type"].dropna().unique()))
with c2:
    acc_range = st.slider("Kapasite (kişi)", 1, 16, (2, 4))

comp = filtered[
    (filtered["room_type"] == sel_room_type)
    & (filtered["accommodates"].between(acc_range[0], acc_range[1]))
]

comp_stats = (
    comp.groupby(neighbourhood_col)["price_num"]
    .agg(ortalama="mean", medyan="median", ilan_sayisi="count")
    .query("ilan_sayisi >= 3")
    .round(1)
    .sort_values("medyan", ascending=False)
)
st.dataframe(comp_stats, use_container_width=True)

# ---------------------------------------------------------------
# 5. Tahmini kayıp gelir
# ---------------------------------------------------------------
st.header("4️⃣ Tahmini Kayıp Gelir")
st.caption(
    "Her ilan, aynı mahalle + oda tipindeki emsallerinin üst çeyrek (top %25) "
    "doluluk oranına kıyaslanır. Bu benchmark'ın altında kalan her ilan için "
    "'yakalanabilecek ek gelir' hesaplanır."
)

filtered["occ_rate"] = filtered["estimated_occupancy_l365d"] / 365
filtered["benchmark_occ"] = filtered.groupby([neighbourhood_col, "room_type"])["occ_rate"].transform(
    lambda x: x.quantile(0.75)
)
filtered["gap_nights"] = (filtered["benchmark_occ"] - filtered["occ_rate"]).clip(lower=0) * 365
filtered["tahmini_kayip_gelir"] = filtered["gap_nights"] * filtered["price_num"]

underperform = filtered[filtered["tahmini_kayip_gelir"] > 0]

m1, m2, m3 = st.columns(3)
m1.metric("Az performans gösteren ilan", f"{len(underperform)} / {len(filtered)}")
m2.metric("Toplam yıllık kayıp gelir potansiyeli", f"${underperform['tahmini_kayip_gelir'].sum():,.0f}")
m3.metric("İlan başına medyan kayıp", f"${underperform['tahmini_kayip_gelir'].median():,.0f}")

st.dataframe(
    underperform[[neighbourhood_col, "room_type", "price_num", "estimated_occupancy_l365d", "tahmini_kayip_gelir"]]
    .sort_values("tahmini_kayip_gelir", ascending=False)
    .head(20)
    .round(1),
    use_container_width=True,
)

st.divider()
st.caption(
    "Bu araç, host'lara gönderilecek kişiselleştirilmiş 'ücretsiz ön analiz' "
    "demo'sunu hızlıca üretmek için tasarlanmıştır. Şehir değiştirmek için "
    "sadece o şehrin Inside Airbnb dosyalarını yükleyin."
)
