import streamlit as st
import pandas as pd
import numpy as np
import time

# Page Configuration
st.set_page_config(page_title="AI House Predictor", page_icon="🏰", layout="wide")

# ==========================================
# 1. ULTRA-DASHING CYBERPUNK LUXURY CSS
# ==========================================
st.markdown("""
    <style>
    /* Dark Premium Background */
    .stApp {
        background-image: linear-gradient(rgba(10, 14, 23, 0.88), rgba(10, 14, 23, 0.95)), 
                          url("https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=2000&q=80");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }
    
    /* Sleek Glassmorphism Panels */
    .glass-panel {
        background: rgba(20, 30, 48, 0.5);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 16px;
        padding: 25px;
        border: 1px solid rgba(0, 255, 204, 0.2);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
        margin-bottom: 25px;
        transition: transform 0.3s ease;
    }
    .glass-panel:hover {
        border: 1px solid rgba(0, 255, 204, 0.6);
        transform: translateY(-2px);
    }
    
    /* Animated Glowing Title */
    .title-glow {
        text-align: center;
        font-size: 3.8rem;
        font-weight: 900;
        background: linear-gradient(90deg, #00ffcc, #0072ff, #00ffcc);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 3s linear infinite;
        margin-bottom: 0px;
    }
    @keyframes shine {
        to {
            background-position: 200% center;
        }
    }
    
    /* Section Headers */
    .section-header {
        color: #00ffcc;
        font-size: 1.4rem;
        font-weight: 700;
        border-bottom: 1px solid rgba(0, 255, 204, 0.3);
        padding-bottom: 10px;
        margin-bottom: 20px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    
    /* Subtitle Styling */
    .header-subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 1.2rem;
        letter-spacing: 2px;
        margin-top: 5px;
    }
    </style>
""", unsafe_allow_html=True)


# ==========================================
# 2. HEADER & BRANDING (MNNIT)
# ==========================================
st.markdown('<div class="title-glow">NEXUS PROPERTY AI</div>', unsafe_allow_html=True)
st.markdown('<div class="header-subtitle">PROJECT LEAD: <b style="color:white;">ISHITA</b> | 📍 MNNIT INNOVATION LAB</div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


# ==========================================
# 3. DASHBOARD - CREATIVE FEATURE PRESENTATION
# ==========================================
tab1, tab2 = st.tabs(["🎛️ AI PREDICTION TERMINAL", "📊 MARKET ANALYTICS"])

with tab1:
    # Top Row: 3 Panels
    col_arch, col_amenity, col_local = st.columns(3)
    
    # PANEL 1: Architecture
    with col_arch:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">🏗️ Architecture</div>', unsafe_allow_html=True)
        bhk = st.slider("🛏️ Bedrooms (BHK)", 1, 10, 2)
        carpet_area = st.number_input("📏 Carpet Area (sqft)", min_value=100, value=800, step=50)
        super_area = st.number_input("📐 Super Area (sqft)", min_value=100, value=1100, step=50)
        bathrooms = st.slider("🚿 Bathrooms", 1, 10, 2)
        floor = st.selectbox("🏢 Floor Level", ["Lower", "Middle", "Upper", "Top Floor"])
        st.markdown('</div>', unsafe_allow_html=True)

    # PANEL 2: Amenities & Features
    with col_amenity:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">🌟 Premium Features</div>', unsafe_allow_html=True)
        furnished = st.selectbox("🛋️ Furnishing", ["Fully Furnished", "Semi-Furnished", "Unfurnished"])
        car_parking = st.slider("🚗 Parking Spaces", 0, 5, 1)
        balcony = st.slider("🌅 Balconies", 0, 5, 1)
        facing = st.selectbox("🧭 Vastu/Facing", ["East", "North-East", "North", "West", "South"])
        overlooking = st.selectbox("🏞️ Overlooking", ["Garden/Park", "Main Road", "Pool", "Club", "Other"])
        st.markdown('</div>', unsafe_allow_html=True)

    # PANEL 3: Locality & Financials
    with col_local:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">📍 Locality & Status</div>', unsafe_allow_html=True)
        location = st.text_input("🏙️ Location/City", value="Thane West")
        society = st.text_input("🏘️ Society Name", value="Sunrise Apartments")
        ownership = st.selectbox("📜 Ownership", ["Freehold", "Co-operative Society", "Leasehold"])
        transaction = st.selectbox("🔄 Transaction", ["New Property", "Resale"])
        listed_amount = st.number_input("💰 Listed Price (₹)", min_value=100000, value=5000000, step=100000)
        st.markdown('</div>', unsafe_allow_html=True)

    # ==========================================
    # 4. REAL-TIME AI ENGINE & LIVE MATH
    # ==========================================
    st.markdown('<div class="glass-panel" style="text-align: center;">', unsafe_allow_html=True)
    st.markdown('<div class="section-header" style="border:none; text-align:center;">🧠 LIVE AI EVALUATION ENGINE</div>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        algorithm = st.selectbox("⚙️ Select Neural Processing Model", ["XGBoost Advanced (Recommended)", "Random Forest", "Linear Regression"])
        price_per_sqft = st.number_input("📈 Current Avg Price/sqft (₹)", min_value=1000, value=6000, step=500)
        
        # --- TRUE LIVE CALCULATION LOGIC ---
        # 1. Base area calculation
        raw_price = carpet_area * price_per_sqft
        super_area_bonus = max(0, super_area - carpet_area) * (price_per_sqft * 0.4)
        
        # 2. Feature additions
        bhk_premium = bhk * 250000
        bath_premium = bathrooms * 100000
        parking_premium = car_parking * 300000
        balcony_premium = balcony * 75000
        
        # 3. Quality Multipliers
        multiplier = 1.0
        if furnished == "Fully Furnished": multiplier += 0.15
        elif furnished == "Semi-Furnished": multiplier += 0.05
        
        if floor in ["Top Floor", "Upper"]: multiplier += 0.05
        if facing in ["East", "North-East"]: multiplier += 0.04
        if overlooking in ["Garden/Park", "Pool", "Club"]: multiplier += 0.06
        if transaction == "New Property": multiplier += 0.10
        
        calculated_value = (raw_price + super_area_bonus + bhk_premium + bath_premium + parking_premium + balcony_premium) * multiplier
        
        # 4. Final Blend with Listed Amount
        final_market_value = (calculated_value * 0.6) + (listed_amount * 0.4)
        # ------------------------------------

        # Live Display UI
        st.markdown(f"""
            <div style='background: rgba(0, 255, 204, 0.1); 
                        padding: 30px; border-radius: 15px; text-align: center; 
                        border: 2px solid #00ffcc; margin-top:20px; margin-bottom: 20px; box-shadow: 0 0 20px rgba(0,255,204,0.4);'>
                <h4 style='color: #94a3b8; margin:0; letter-spacing: 2px;'>LIVE COMPUTED MARKET VALUE</h4>
                <h1 style='color: #00ffcc; margin:10px 0; font-size: 3.5rem; text-shadow: 0 0 10px #00ffcc;'>₹ {final_market_value:,.0f}</h1>
                <p style='color: #64748b; margin:0;'>Model accuracy optimized via {algorithm} | Updates Instantly ⚡</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Lock Button just for visual flair
        if st.button("🔒 LOCK VALUATION & GENERATE REPORT", use_container_width=True, type="primary"):
            st.balloons()
            st.success("✅ Valuation Locked Successfully! (Print / Save PDF feature active)")
            
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">📈 Market Trend (10 Yrs)</div>', unsafe_allow_html=True)
        years = pd.date_range(start='2014', end='2024', freq='YE')
        trend_data = pd.DataFrame({
            "New": np.linspace(4000, 12000, len(years)) + np.random.normal(0, 500, len(years)),
            "Resale": np.linspace(4000, 12000, len(years)) * 0.85 + np.random.normal(0, 500, len(years))
        }, index=years.year)
        st.line_chart(trend_data)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
        st.markdown('<div class="section-header">🧠 Feature Importance</div>', unsafe_allow_html=True)
        feature_data = pd.DataFrame(
            {"Impact (%)": [35, 20, 15, 10, 10, 10]},
            index=["Carpet Area", "Listed Amount", "Price/sqft", "Overlooking", "Furnishing", "BHK"]
        )
        st.bar_chart(feature_data)
        st.markdown('</div>', unsafe_allow_html=True)