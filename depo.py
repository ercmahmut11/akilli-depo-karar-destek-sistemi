import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


st.set_page_config(page_title="Akıllı Depo Dashboard", layout="wide")

st.title(" Akıllı Depo Karar Destek Sistemi - Dashboard")
st.markdown("---")

st.sidebar.header("Simülasyon Kontrol Paneli")
siparis_hizi = st.sidebar.slider("Sipariş Geliş Hızı (Sipariş/Saat)", 10, 200, 50)
robot_sayisi = st.sidebar.slider("AGV Robot Kapasitesi", 1, 20, 8)
paketleme_hizi = st.sidebar.slider("Paketleme Kapasitesi (%)", 0, 100, 75)
toplam_islem = siparis_hizi * 8 
bekleme_p1 = max(1.5, 30.0 / robot_sayisi)
bekleme_p2 = max(4.0, 70.0 / robot_sayisi)
robot_doluluk = min(99.0, (siparis_hizi / (robot_sayisi * 10)) * 100)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Günlük Toplam İşlem", f"{toplam_islem} Adet")
with col2:
    st.metric("Ort. Hazırlanma Süresi", f"{round(bekleme_p1, 1)} dk", delta="-15%", delta_color="normal")
with col3:
    st.metric("Kaynak Verimliliği", f"%{round(robot_doluluk, 1)}", delta="Optimal" if 70 < robot_doluluk < 90 else "Riskli", delta_color="inverse")
with col4:
    st.metric("Sistem Durumu", "AKTİF" if robot_doluluk < 95 else "DARBOĞAZ", delta_color="off")

st.markdown("---")


c1, c2 = st.columns(2)

with c1:
    st.subheader(" Sipariş Öncelik Dağılımı")
    
    labels = ['Express (P1)', 'Standart (P2)', 'İade (P3)']
    sizes = [20, 55, 25]
    colors = ['#ff4b4b', '#ffaa00', '#00cc66']
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1)

with c2:
    st.subheader(" Önceliğe Göre Bekleme Analizi")
   
    fig2, ax2 = plt.subplots()
    bars = ax2.bar(labels, [bekleme_p1, bekleme_p2, bekleme_p2*1.2], color=colors)
    ax2.set_ylabel("Bekleme Süresi (Dakika)")
    st.pyplot(fig2)

st.markdown("---")


st.subheader(" Sistem Değerlendirme Raporu")
if robot_doluluk > 90:
    st.error(f"KRİTİK: Robot doluluk oranı %{round(robot_doluluk, 1)} seviyesine ulaştı. Mevcut sipariş hızıyla sistem kilitlenmek üzere!")
    st.info(" Tavsiye: AGV Robot sayısını en az 3 adet artırın veya sipariş kabul hızını sınırlayın.")
elif 70 < robot_doluluk <= 90:
    st.warning("DİKKAT: Sistem yüksek yük altında çalışıyor ancak kararlı.")
else:
    st.success("STABİL: Kaynaklar mevcut yük için fazlasıyla yeterli. Operasyonel maliyet optimizasyonu yapılabilir.")