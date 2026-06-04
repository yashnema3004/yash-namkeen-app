import streamlit as st
import random
import string
import datetime

# --- CONFIGURATION & THEME SETUP ---
st.set_page_config(page_title="Yash Namkeen & Sweets", page_icon="🪔", layout="wide")

# Custom CSS for the festive look, card styling, and clean token boxes
st.markdown("""
<style>
    .brand-banner {
        background: linear-gradient(135deg, #8B0000 0%, #B22222 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 25px;
        border-bottom: 5px solid #FFD700;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .brand-title {
        font-size: 3.2rem !important;
        font-weight: bold !important;
        font-family: 'Georgia', serif;
        margin: 0;
        color: #FFD700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    .brand-subtitle {
        font-size: 1.2rem;
        margin-top: 5px;
        opacity: 0.9;
        letter-spacing: 1px;
    }
    .status-card {
        background-color: #F8F9FA;
        border-left: 5px solid #8B0000;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .token-box {
        background-color: #FFF9E6;
        border: 2px dashed #D4AF37;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# --- DATABASE SETUP ---
if "inventory" not in st.session_state:
    st.session_state.inventory = {
        "Premium Kaju Katli (per Kg)": {"price": 800, "stock": 100},
        "Special Festival Gujiya (per Box)": {"price": 350, "stock": 40},
        "Signature Shahi Mixture (per 500g)": {"price": 150, "stock": 150},
        "Aloo Bhujia / Sev (per 500g)": {"price": 120, "stock": 80}
    }

if "orders" not in st.session_state:
    st.session_state.orders = {}

def generate_token(prefix="YASH"):
    return f"{prefix}-" + "".join(random.choices(string.ascii_uppercase + string.digits, k=6))

# --- BRAND HEADER BANNER ---
st.markdown("""
<div class="brand-banner">
    <h1 class="brand-title">✨ YASH NAMKEEN ✨</h1>
    <p class="brand-subtitle">Pure Taste, Sweet Celebrations • Smart Counter Assistant</p>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.markdown("### 🎛️ Control Panel")
app_mode = st.sidebar.radio("Switch View:", ["🛒 Customer Storefront", "👨‍🍳 Dad's Admin Panel"])
st.sidebar.write("---")
st.sidebar.caption("Yash Namkeen v2.0 - Festival Edition")

# ==========================================
# 🛒 CUSTOMER STOREFRONT
# ==========================================
if app_mode == "🛒 Customer Storefront":
    
    tab1, tab2 = st.tabs(["🛍️ Instant Counter Pickup", "📦 Advance Bulk Booking (Events)"])
    
    # TAB 1: INSTANT PICKUP
    with tab1:
        st.write("### Place Your Counter Order")
        st.info("💡 **How it works:** Submit your request below. Your dad will check the trays instantly. Once he approves, you pay digitally via UPI and grab your automated token!")
        
        with st.form("instant_form"):
            cart = {}
            st.markdown("#### Today's Fresh Menu")
            for item, details in st.session_state.inventory.items():
                col1, col2, col3 = st.columns([2, 1, 1])
                with col1:
                    st.markdown(f"**{item}**")
                    st.markdown(f"Price: ₹{details['price']}")
                with col2:
                    if details['stock'] == 0:
                        st.error("Sold Out")
                    elif details['stock'] <= 15:
                        st.warning(f"Only {details['stock']} left")
                    else:
                        st.success("Fresh Batch Ready")
                with col3:
                    cart[item] = st.number_input(f"Quantity", min_value=0, max_value=int(details['stock']), value=0, key=f"inst_{item}", label_visibility="collapsed")
            
            st.write("---")
            submit_instant = st.form_submit_button("Send Order to Counter for Approval")
            
        if submit_instant:
            final_cart = {k: v for k, v in cart.items() if v > 0}
            if not final_cart:
                st.error("Please add at least one delicious item to your cart.")
            else:
                total = sum(final_cart[item] * st.session_state.inventory[item]["price"] for item in final_cart)
                token = generate_token("REQ")
                st.session_state.orders[token] = {
                    "type": "Instant",
                    "items": final_cart,
                    "total": total,
                    "advance": total,
                    "status": "Pending Counter Approval",
                    "time": datetime.datetime.now().strftime("%I:%M %p")
                }
                st.warning(f"📩 **Request Sent!** Give this code to the counter: **{token}**. Keep checking the tracking status below to pay once approved!")

    # TAB 2: ADVANCE BULK BOOKING
    with tab2:
        st.write("### 🎉 Bulk Event Bookings (Orders larger than 10 Units)")
        st.info("📦 Planning a major function or gifting? Book well ahead. Pay a 30% advance deposit after our review, and clear the rest at pickup.")
        
        with st.form("bulk_form"):
            pickup_date = st.date_input("When do you need the items delivered?", min_value=datetime.date.today() + datetime.timedelta(days=2))
            bulk_cart = {}
            
            for item, details in st.session_state.inventory.items():
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"**{item}** (₹{details['price']})")
                with col2:
                    bulk_cart[item] = st.number_input(f"Quantity", min_value=0, value=0, key=f"bulk_{item}", label_visibility="collapsed")
            
            st.write("---")
            submit_bulk = st.form_submit_button("Submit Bulk Request to Management")
            
        if submit_bulk:
            final_bulk = {k: v for k, v in bulk_cart.items() if v > 0}
            total_qty = sum(final_bulk.values())
            
            if total_qty < 10:
                st.error("⚠️ For regular smaller purchases, please use the 'Instant Counter Pickup' tab above.")
            else:
                total = sum(final_bulk[item] * st.session_state.inventory[item]["price"] for item in final_bulk)
                advance_needed = round(total * 0.30, 2)
                token = generate_token("YASH-BULK")
                st.session_state.orders[token] = {
                    "type": "Bulk",
                    "items": final_bulk,
                    "total": total,
                    "advance": advance_needed,
                    "status": "Pending Counter Approval",
                    "date": str(pickup_date),
                    "time": datetime.datetime.now().strftime("%I:%M %p")
                }
                st.success(f"✅ **Bulk Request Received!** Tracking Code: **{token}**. We will confirm production status shortly.")

    # --- TRACKING SECTOR ---
    st.markdown("---")
    st.write("### 🔍 Live Order Status & UPI Payment")
    search_token = st.text_input("Enter your Request Code to pay or track:").strip().upper()
    
    if search_token in st.session_state.orders:
        ord_info = st.session_state.orders[search_token]
        
        st.markdown(f"""
        <div class="status-card">
            <h4>Order Status for {search_token}</h4>
            <p><strong>Current State:</strong> {ord_info['status']}</p>
            <p><strong>Order Type:</strong> {ord_info['type']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if ord_info['status'] == "Approved - Awaiting Payment":
            st.markdown(f"### 💰 Secure Payment Required: **₹{ord_info['advance']}**")
            if ord_info['type'] == "Bulk":
                st.caption(f"Remaining Balance to be paid in cash at counter during pickup: ₹{ord_info['total'] - ord_info['advance']}")
            
            if st.button("Simulate UPI Payment (GPay/PhonePe)", type="primary", use_container_width=True):
                st.session_state.orders[search_token]["status"] = "Paid & Confirmed ✅"
                if ord_info['type'] == "Instant":
                    for itm, q in ord_info['items'].items():
                        st.session_state.inventory[itm]["stock"] -= q
                st.balloons()
                st.rerun()
                
        elif ord_info['status'] == "Paid & Confirmed ✅":
            st.markdown(f"""
            <div class="token-box">
                <h2 style="color: #8B0000; margin:0;">🎟️ PICKUP TOKEN CONFIRMED</h2>
                <h1 style="font-size: 3.5rem; color: #1E7E34; font-family: monospace; margin: 10px 0;">{search_token}</h1>
                <p style="color: #555;">Show this screen to Yash's father at the billing desk to pick up your package instantly!</p>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# 👨‍🍳 DAD'S ADMIN PANEL
# ==========================================
elif app_mode == "👨‍🍳 Dad's Admin Panel":
    st.write("### 👨‍🍳 Counter Control & Stock Desk")
    
    col_dash1, col_dash2 = st.columns(2)
    
    with col_dash1:
        pending_reqs = [k for k, v in st.session_state.orders.items() if v["status"] == "Pending Counter Approval"]
        st.subheader(f"📥 New Requests ({len(pending_reqs)})")
        
        if not pending_reqs:
            st.caption("No pending approval requests. Counter is fully clear!")
        else:
            for tok in pending_reqs:
                info = st.session_state.orders[tok]
                with st.expander(f"🔔 {tok} | {info['type']} | Total: ₹{info['total']}"):
                    if info['type'] == "Bulk":
                        st.markdown(f"📅 **Target Delivery Date: {info['date']}**")
                    st.write("**Items requested:**")
                    for itm, q in info["items"].items():
                        st.write(f"- {itm} : **{q} units** (Available: {st.session_state.inventory[itm]['stock']})")
                    
                    c1, c2 = st.columns(2)
                    with c1:
                        if st.button("Approve & Send Payment Link", key=f"acc_{tok}", use_container_width=True):
                            st.session_state.orders[tok]["status"] = "Approved - Awaiting Payment"
                            st.rerun()
                    with c2:
                        if st.button("Decline Order", key=f"rej_{tok}", use_container_width=True):
                            st.session_state.orders[tok]["status"] = "Rejected due to festival rush"
                            st.rerun()
                            
    with col_dash2:
        confirmed_orders = [k for k, v in st.session_state.orders.items() if v["status"] == "Paid & Confirmed ✅"]
        st.subheader(f"📦 Paid Handover Queue ({len(confirmed_orders)})")
        
        if not confirmed_orders:
            st.caption("No items packed waiting for pickup right now.")
        else:
            for tok in confirmed_orders:
                info = st.session_state.orders[tok]
                with st.expander(f"🟢 Token {tok} (Ready)"):
                    if info['type'] == "Bulk":
                        st.warning(f"🛑 **Collect Remaining Dues: ₹{info['total'] - info['advance']}**")
                    st.write("**Pack these items:**")
                    for itm, q in info["items"].items():
                        st.write(f"- 📦 **{q}x** {itm}")
                    if st.button("Handed Over (Clear Token)", key=f"delv_{tok}", type="primary", use_container_width=True):
                        st.session_state.orders[tok]["status"] = "Delivered & Closed"
                        st.success("Cleared!")
                        st.rerun()

    # --- STOCK UPDATER ---
    st.markdown("---")
    st.subheader("📊 Kitchen Stock Management")
    st.caption("Whenever a fresh batch of sweets arrives from the kitchen, update the inventory numbers below.")
    
    for item, details in st.session_state.inventory.items():
        col_name, col_stock = st.columns([3, 1])
        with col_name:
            st.write(f"📁 {item}")
        with col_stock:
            new_stock = st.number_input("Update Stock", min_value=0, value=int(details['stock']), key=f"admin_{item}", label_visibility="collapsed")
            st.session_state.inventory[item]["stock"] = new_stock