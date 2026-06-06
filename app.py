import streamlit as st
import random

# --- CONFIGURATION & PAGE SETUP ---
st.set_page_config(
    page_title="Yash Namkeen | Authentic Premium Taste", 
    page_icon="✨", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- UNIFIED PREMIUM LIGHT BLACK & GOLD PLAYFAIR DISPLAY THEME ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap');
    
    /* 1. Global Dark Theme & Universal Playfair Font Override */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [class*="css"], .stText, .stMarkdown {
        font-family: 'Playfair Display', serif !important;
        background-color: #1A1A1A !important; /* Premium Light Black / Charcoal */
        color: #FFFFFF !important;
    }
    
    /* 2. Primary Heading Configuration */
    h1, h2, h3, h4, h5, h6, .gold-title {
        font-family: 'Playfair Display', serif !important;
        color: #D4AF37 !important; /* Elegant Gold headers */
        font-weight: 700 !important;
    }
    
    /* 3. Global Labels and Paragraphs Typography Settings */
    label, p, span, sm, .stWidgetFormLabel, div[data-testid="stMarkdownContainer"] p, [data-testid="stMetricValue"], [data-testid="stMetricLabel"] {
        font-family: 'Playfair Display', serif !important;
        color: #E6C687 !important; /* Soft, readable lighter gold text */
        font-weight: 500 !important;
    }
    
    /* 4. Dropdowns, Inputs, and Number Boxes Font Overrides */
    div[data-baseweb="select"], div[data-baseweb="input"], input, [data-testid="stNumberInput"], select, option, textarea {
        font-family: 'Playfair Display', serif !important;
        background-color: #262626 !important; /* Dark contrast fill */
        color: #FFFFFF !important; /* Bright white text for absolute typing visibility */
        border: 1px solid #D4AF37 !important; /* Golden borders */
    }
    
    /* Fix form input placeholder text font */
    input::placeholder {
        font-family: 'Playfair Display', serif !important;
        color: #888888 !important;
        opacity: 1;
    }

    /* 5. Navigation Tabs Playfair Styling */
    button[data-baseweb="tab"] {
        background-color: transparent !important;
        border-bottom: 2px solid #333333 !important;
    }
    button[data-baseweb="tab"] div p {
        font-family: 'Playfair Display', serif !important;
        color: #A0A0A0 !important; /* Muted gray for inactive tabs */
    }
    button[aria-selected="true"] {
        border-bottom: 2px solid #D4AF37 !important;
    }
    button[aria-selected="true"] div p {
        color: #D4AF37 !important; /* Radiant Gold for active tab */
        font-weight: bold !important;
    }
    
    /* 6. Sidebar Font and Color Sync */
    [data-testid="stSidebar"], [data-testid="stSidebar"] [data-testid="stSidebarNav"] {
        background-color: #111111 !important;
        border-right: 1px solid #D4AF37;
    }
    [data-testid="stSidebar"] p, [data-testid="stSidebar"] label, [data-testid="stSidebar"] span, [data-testid="stSidebar"] button {
        font-family: 'Playfair Display', serif !important;
        color: #D4AF37 !important;
    }
    
    /* 7. Premium Brand Header Banner */
    .gold-header {
        text-align: center;
        padding: 35px 20px 25px 20px;
        background-color: #111111;
        border: 1px solid #333333;
        border-bottom: 3px solid #D4AF37;
        margin-bottom: 30px;
        border-radius: 8px;
    }
    .gold-header h1 {
        font-size: 3rem;
        margin: 0 0 5px 0;
        letter-spacing: 4px;
    }
    .gold-header p {
        font-size: 0.9rem;
        color: #E6C687 !important;
        text-transform: uppercase;
        letter-spacing: 5px;
        font-weight: 600;
        margin: 0;
    }
    
    /* 8. Luxury Product Cards Layout */
    .gold-card {
        background-color: #111111;
        padding: 25px 15px;
        border-radius: 6px;
        border: 1px solid #333333;
        text-align: center;
        transition: all 0.3s ease;
        margin-bottom: 20px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        min-height: 230px; 
    }
    .gold-card:hover {
        box-shadow: 0 10px 25px rgba(212, 175, 55, 0.15);
        border-color: #D4AF37;
        transform: translateY(-2px);
    }
    .gold-price {
        font-size: 1.2rem;
        font-weight: 700;
        color: #FFFFFF !important; 
        margin-bottom: 10px;
    }
    .gold-status {
        font-family: 'Playfair Display', serif !important;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 600;
        padding: 4px 12px;
        border-radius: 4px;
        display: inline-block;
    }
    
    /* 9. Luxury Centered Checkout Presentation Box */
    .checkout-box {
        background-color: #111111;
        padding: 30px;
        border: 2px solid #D4AF37;
        text-align: center;
        border-radius: 6px;
        max-width: 400px;
        margin: 25px auto;
    }
    .checkout-badge {
        font-size: 1.3rem;
        color: #D4AF37 !important;
        font-weight: bold;
        border-bottom: 1px solid #333333;
        padding-bottom: 8px;
        margin-bottom: 15px;
        letter-spacing: 1px;
    }

    /* 10. Solid Premium Buttons - Text Centering and Contrast Overrides */
    .stButton>button {
        font-family: 'Playfair Display', serif !important;
        background-color: #D4AF37 !important;
        color: #000000 !important; /* Bold black text on buttons for top-tier readability */
        font-weight: bold !important;
        font-size: 1.05rem !important;
        border: none !important;
        border-radius: 4px !important;
        padding: 10px 20px !important;
        transition: all 0.3s !important;
        letter-spacing: 1px;
    }
    .stButton>button:hover {
        background-color: #FFF0C2 !important;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4) !important;
        color: #000000 !important;
    }
    
    table, th, td {
        font-family: 'Playfair Display', serif !important;
    }
</style>
""", unsafe_allow_html=True)

# --- INITIALIZE GLOBAL STATES (DATABASE) ---
if "inventory" not in st.session_state:
    st.session_state.inventory = {
        "Premium Kaju Katli (1kg)": {"price": 800, "stock": 15, "emoji": "✨"},
        "Special Festival Gujiya (1kg)": {"price": 400, "stock": 20, "emoji": "🥟"},
        "Signature Shahi Mixture (500g)": {"price": 150, "stock": 50, "emoji": "📦"},
        "Ratlami Sev (500g)": {"price": 120, "stock": 40, "emoji": "🔥"}
    }

if "basket" not in st.session_state:
    st.session_state.basket = {}

if "orders_log" not in st.session_state:
    st.session_state.orders_log = []

if "reset_trigger" not in st.session_state:
    st.session_state.reset_trigger = 0

if "current_active_reg_id" not in st.session_state:
    st.session_state.current_active_reg_id = None

if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None 

# --- VISUAL BRAND HEADER ---
st.markdown("""
<div class="gold-header">
    <h1>YASH NAMKEEN</h1>
    <p>A Unique Blend of Authentic Taste & Quality</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────
# 🔑 LOGIN FORM LAYER
# ─────────────────────────────────────────────────────────────────
if st.session_state.logged_in_user is None:
    st.markdown("<h2 style='text-align: center; color: #D4AF37; margin-bottom: 25px;'>Welcome to our Smart Portal</h2>", unsafe_allow_html=True)
    
    login_tab1, login_tab2 = st.tabs(["🛒 Customer Login", "👨‍🍳 Dad / Owner Login"])
    
    with login_tab1:
        st.markdown("<h3 style='color: #D4AF37;'>Guest Quick-Access</h3>", unsafe_allow_html=True)
        st.write("Enter your phone number to browse the counter and place orders from home.")
        cust_phone = st.text_input("Mobile Number:", placeholder="Enter 10-digit number", key="cust_phone_input")
        
        if st.button("Enter Boutique Storefront 🚀", use_container_width=True):
            if len(cust_phone.strip()) >= 10:
                st.session_state.logged_in_user = "Customer"
                st.rerun()
            else:
                st.error("Please enter a valid active 10-digit mobile number.")
        
    with login_tab2:
        st.markdown("<h3 style='color: #D4AF37;'>Admin Verification Gate</h3>", unsafe_allow_html=True)
        st.write("Authorized access only.")
        owner_user = st.text_input("Username:", placeholder="Enter admin ID", key="owner_user_input")
        owner_pass = st.text_input("Password:", type="password", placeholder="••••••••", key="owner_pass_input")
        
        if st.button("Unlock Management Dashboard 👨‍🍳", use_container_width=True):
            if owner_user.strip() == "admin" and owner_pass == "yash2026":
                st.session_state.logged_in_user = "Owner"
                st.rerun()
            else:
                st.error("Invalid secure console credentials. Access denied.")

# ─────────────────────────────────────────────────────────────────
# 🚪 ROUTING HUB ENGINE
# ─────────────────────────────────────────────────────────────────
else:
    st.sidebar.markdown(f"<h3 style='color: #D4AF37; text-align: center; margin-top:15px;'>Navigation</h3>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<p style='text-align: center;'>Role: <b>{st.session_state.logged_in_user}</b></p>", unsafe_allow_html=True)
    
    if st.session_state.logged_in_user == "Owner":
        view_mode = st.sidebar.radio("Go To View Mode:", ["👨‍🍳 Administration Panel", "🛒 Boutique Storefront"])
    else:
        view_mode = "🛒 Boutique Storefront"
        st.sidebar.success("Securely Connected")
        
    st.sidebar.write("---")
    
    if st.sidebar.button("🔒 Disconnect / Logout", use_container_width=True):
        st.session_state.logged_in_user = None
        st.session_state.basket = {}
        st.session_state.current_active_reg_id = None
        st.rerun()

    # 🛒 VIEW 1: STOREFRONT
    if view_mode == "🛒 Boutique Storefront":
        tab1, tab2 = st.tabs(["🛍️ Handpicked Menu Items", "🔍 Track Bulk Orders"])
        
        with tab1:
            st.markdown("<h4 style='color:#D4AF37; font-weight:500; margin-bottom: 20px;'>Our Premium Selection</h4>", unsafe_allow_html=True)
            
            # Dynamic grid structure that supports newly appended item lines seamlessly
            items_list = list(st.session_state.inventory.items())
            chunk_size = 4
            for i in range(0, len(items_list), chunk_size):
                chunk = items_list[i:i + chunk_size]
                cols = st.columns(len(chunk))
                for idx, (item, details) in enumerate(chunk):
                    with cols[idx]:
                        if details['stock'] > 0:
                            stock_html = f'<span class="gold-status" style="background-color: #1B3821; color: #7CE68A; border: 1px solid #2E7D32;">In Stock ({details["stock"]})</span>'
                        else:
                            stock_html = '<span class="gold-status" style="background-color: #3D1C1C; color: #FFA1A1; border: 1px solid #C62828;">Sold Out</span>'
                            
                        st.markdown(f"""
                        <div class="gold-card">
                            <div style="font-size: 1.8rem;">{details['emoji']}</div>
                            <div>
                                <div class="gold-title">{item}</div>
                                <div class="gold-price">₹{details['price']}</div>
                            </div>
                            {stock_html}
                        </div>
                        """, unsafe_allow_html=True)
            
            st.write("---")
            st.markdown("<h4 style='color:#D4AF37; font-weight:500;'>Select Delicacies</h4>", unsafe_allow_html=True)
            
            col_select, col_qty = st.columns([2, 1])
            menu_options = ["Select Item..."] + list(st.session_state.inventory.keys())
            
            with col_select:
                selected_item = st.selectbox(
                    "Choose standard pack variant:", 
                    options=menu_options,
                    index=0,
                    key=f"item_dropdown_{st.session_state.reset_trigger}"
                )
            with col_qty:
                quantity = st.number_input(
                    "Enter total packet units:", 
                    min_value=0, 
                    max_value=100, 
                    value=0,
                    key=f"quantity_input_{st.session_state.reset_trigger}"
                )
                
            if st.button("➕ Add Selection to Basket", use_container_width=True):
                if selected_item == "Select Item...":
                    st.error("Please pick an item variant before adding.")
                elif quantity <= 0:
                    st.error("Select an amount greater than zero.")
                else:
                    max_stock = st.session_state.inventory[selected_item]["stock"]
                    
                    if max_stock == 0:
                        st.error("Item currently unavailable on factory display lines.")
                    elif quantity > max_stock and quantity < 15:
                        st.error(f"Cannot add item pack. Only {max_stock} items remaining on shelves.")
                    else:
                        if selected_item in st.session_state.basket:
                            st.session_state.basket[selected_item] += quantity
                        else:
                            st.session_state.basket[selected_item] = quantity
                        
                        st.toast(f"Added {quantity}x {selected_item} to basket.", icon="✨")
                        st.session_state.reset_trigger += 1
                        st.rerun()

            # RENDER THE SHOPPING BASKET
            if st.session_state.basket:
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("<h4 style='color:#D4AF37; margin-bottom:15px;'>Your Carefully Curated Basket</h4>", unsafe_allow_html=True)
                
                regular_items = {}
                bulk_items = {}
                
                for item, qty in list(st.session_state.basket.items()):
                    item_price = st.session_state.inventory[item]["price"]
                    subtotal = item_price * qty
                    
                    if qty >= 15:
                        bulk_items[item] = {"qty": qty, "subtotal": subtotal}
                    else:
                        regular_items[item] = {"qty": qty, "subtotal": subtotal}
                    
                    b_col1, b_col2, b_col3, b_col4 = st.columns([3, 1, 1, 1])
                    with b_col1:
                        st.markdown(f"<span style='font-size:1.1rem; font-weight:600; color:#D4AF37;'>✦ {item}</span>", unsafe_allow_html=True)
                    with b_col2:
                        st.write(f"**{qty} Packs** " + ("📦 *(Bulk)*" if qty >= 15 else "⚡ *(Express)*"))
                    with b_col3:
                        st.write(f"₹{subtotal}")
                    with b_col4:
                        if st.button("Wipe ❌", key=f"rem_{item}"):
                            del st.session_state.basket[item]
                            st.rerun()
                
                st.write("---")
                
                m_col1, m_col2 = st.columns(2)
                reg_total = sum(d["subtotal"] for d in regular_items.values()) if regular_items else 0
                bulk_total = sum(d["subtotal"] for d in bulk_items.values()) if bulk_items else 0
                
                with m_col1:
                    st.metric(label="⚡ Retail Subtotal Amount Due", value=f"₹{reg_total}")
                with m_col2:
                    if bulk_total > 0:
                        st.metric(label="📦 Bulk Manufacturing Reserve Total", value=f"₹{bulk_total}")
                        event_date = st.date_input("🗓️ Specify target event delivery date slot:", key="bulk_date_picker")

                if st.button("🚀 Confirm & Proceed to Payment", type="primary", use_container_width=True):
                    req_id_base = random.randint(1000, 9999)
                    
                    if regular_items:
                        can_fulfill = True
                        for item, data in regular_items.items():
                            if data["qty"] > st.session_state.inventory[item]["stock"]:
                                st.error(f"Cannot fulfill instantly. Only {st.session_state.inventory[item]['stock']} remaining for {item}.")
                                can_fulfill = False
                        
                        if can_fulfill:
                            for item, data in regular_items.items():
                               st.session_state.inventory[item]["stock"] -= data["qty"]
                            
                            reg_summary = ", ".join([f"{d['qty']}x {i}" for i, d in regular_items.items()])
                            generated_reg_id = f"REG-{req_id_base}"
                            
                            st.session_state.orders_log.append({
                                "id": generated_reg_id,
                                "item": reg_summary,
                                "qty": sum(d["qty"] for d in regular_items.values()),
                                "total": reg_total,
                                "type": "Regular Retail",
                                "status": "Awaiting Counter Payment"
                            })
                            st.session_state.current_active_reg_id = generated_reg_id
                    
                    if bulk_items:
                        generated_blk_id = f"BLK-{req_id_base}"
                        bulk_summary = ", ".join([f"{d['qty']}x {i}" for i, d in bulk_items.items()])
                        st.session_state.orders_log.append({
                            "id": generated_blk_id,
                            "item": bulk_summary,
                            "qty": sum(d["qty"] for d in bulk_items.values()),
                            "total": bulk_total,
                            "advance": round(bulk_total * 0.30, 2),
                            "type": "Bulk Request",
                            "status": "Pending Approval",
                            "date": str(event_date)
                        })
                        st.toast(f"Bulk Request {generated_blk_id} logged to kitchen queue.", icon="📩")
                    
                    st.session_state.basket = {}
                    st.rerun()
            else:
                if not st.session_state.current_active_reg_id:
                    st.info("ℹ️ Your digital order basket list is currently empty.")

            # ─── ACTIVE CHECKOUT PAYMENT PANEL ───
            if st.session_state.current_active_reg_id:
                st.write("---")
                
                active_id = st.session_state.current_active_reg_id
                order_data = next((o for o in st.session_state.orders_log if o.get("id") == active_id), None)
                
                if order_data and order_data["status"] == "Awaiting Counter Payment":
                    st.markdown(f"<h4 style='text-align:center;'>Boutique Fast-Checkout Counter</h4>", unsafe_allow_html=True)
                    st.write(f"📋 **Items Summary:** {order_data['item']}")
                    
                    st.markdown(f"""
                    <div class="checkout-box">
                        <div class="checkout-badge">YASH NAMKEEN ESCROW</div>
                        <div style="font-size: 1.5rem; font-weight: bold; color: #FFFFFF; margin: 15px 0;">Total Value: <span style="color:#D4AF37;">₹{order_data['total']}</span></div>
                        <div style="border: 1px dashed #D4AF37; padding: 20px; margin: 15px 0; background: #262626; font-size: 0.9rem; letter-spacing: 1px; font-weight: 600; color: #D4AF37;">
                            [ DIGITAL UPI QR CODE PLACEHOLDER ]
                        </div>
                        <span style="font-size: 0.8rem; color:#E6C687; font-style: italic;">Scan to route transaction directly to shop balance registry</span>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if st.button(f"Click After Paying Complete Balance", type="primary", use_container_width=True):
                        order_data["status"] = "Paid & Ready for Pickup ✅"
                        st.rerun()
                else:
                    completed_order = next((o for o in st.session_state.orders_log if o.get("id") == active_id), None)
                    if completed_order:
                        st.balloons()
                        
                        st.markdown(f"""
                        <div style="background-color: #111111; border: 1px solid #D4AF37; padding: 30px; text-align: center; margin: 25px 0; box-shadow: 0 10px 30px rgba(212,175,55,0.15);">
                            <h2>✔ Order Manifest Verified Successfully</h2>
                            <p style="font-size: 1rem; color:#E6C687; margin-top:5px;">Your items have been pre-packed and set aside at the window counter.</p>
                            <div style="font-size: 1.8rem; font-weight: bold; color: #000000; background-color: #D4AF37; display: inline-block; padding: 12px 30px; border-radius: 4px; margin-top: 15px; font-family: monospace; letter-spacing:1px;">
                                TOKEN NO: {completed_order['id']}
                            </div>
                            <p style="font-size: 0.85rem; color: #E6C687; margin-top: 15px; max-width:450px; margin-left:auto; margin-right:auto;">Present this token data code block at the counter layout grid to grab your box instantly.</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        if st.button("Initialize Fresh Basket Order 🛍️", use_container_width=True):
                            st.session_state.current_active_reg_id = None
                            st.rerun()

        # ─── TAB 2: BULK TRACKING ───
        with tab2:
            st.markdown("<h4 style='color:#D4AF37; font-weight:500; margin-bottom:15px;'>Catering & Event Order Status Terminal</h4>", unsafe_allow_html=True)
            search_id = st.text_input("Input alphanumeric BLK tracking index:").strip().upper()
            
            found = False
            for order in st.session_state.orders_log:
                if "id" in order and order["id"] == search_id:
                    found = True
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    st.markdown(f"""
                    <div style="background-color: #111111; padding: 25px; border-radius: 4px; border: 1px solid #333333; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">
                        <h4 style="margin: 0 0 15px 0; font-size:1.25rem;">Contract Document ID: {search_id}</h4>
                        <p style="margin: 5px 0; color:#FFFFFF;"><b>Selected Profile Match:</b> {order['item']}</p>
                        <p style="margin: 5px 0; color:#FFFFFF;"><b>Total Evaluated Value:</b> ₹{order['total']}</p>
                        <p style="margin: 5px 0; color:#FFFFFF;"><b>Current Production Pipeline State:</b> <span style="background-color: #262626; color: #D4AF37; padding: 3px 10px; font-size:0.8rem; font-weight: bold; border-radius:3px; border: 1px solid #D4AF37;">{order['status']}</span></p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if order["status"] == "Approved - Waiting Advance Payment":
                        st.markdown(f"""
                        <div class="checkout-box" style="border-color:#D4AF37;">
                            <div class="checkout-badge" style="border-color:#333333;">ADVANCE PROCESSING ESCROW</div>
                            <div style="font-size: 1.25rem; font-weight: bold; color: #FFFFFF; margin: 10px 0;">30% Booking Advance Due: ₹{order['advance']}</div>
                            <div style="border:1px dashed #D4AF37; padding:15px; margin: 10px 0; background:#262626; font-size:0.85rem; color:#D4AF37; font-weight:bold;">[ SECURE BANK ADVANCE QR CODE ]</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        if st.button("Confirm Advance Deposit Paid", key=f"pay_bulk_{order['id']}", use_container_width=True):
                            order["status"] = "Advance Paid - Kitchen Preparing"
                            st.success("Manufacturing contract verified. Processing schedule locked.")
                            st.rerun()
                            
            if search_id and not found:
                st.error("No active tracking configuration blocks identified matching that verification index tag.")

    # ─────────────────────────────────────────────────────────────────
    # 👨‍🍳 VIEW 2: DAD'S ADMIN PANEL (UPDATED SYSTEM CONTROLS)
    # ─────────────────────────────────────────────────────────────────
    else:
        st.markdown("<h2 style='color:#D4AF37;'>Back-Office Factory Console</h2>", unsafe_allow_html=True)
        
        # Admin Operations Sub-Tabs
        admin_tab1, admin_tab2, admin_tab3 = st.tabs([
            "📊 Dashboard & Approvals", 
            "🛠️ Inventory & Catalog Management",
            "📋 Master Sales Database"
        ])
        
        # ─── SUB-TAB 1: STOCK METRICS & INCOMING BULK ORDERS ───
        with admin_tab1:
            st.subheader("📦 Live Storefront Display Stock Tally Metrics")
            inv_cols = st.columns(min(len(st.session_state.inventory), 4))
            for i, (item, details) in enumerate(st.session_state.inventory.items()):
                col_idx = i % 4
                with inv_cols[col_idx]:
                    st.metric(label=item, value=f"{details['stock']} units", delta=f"₹{details['price']}/ea")
                
            st.write("---")
            st.subheader("📥 Action Queue: Bulk Catering Production Requests (Items ≥ 15 units)")
            
            pending_bulk = [o for o in st.session_state.orders_log if o.get("status") == "Pending Approval"]
            
            if not pending_bulk:
                st.success("🎉 Manufacturing pipelines clear. No outstanding validation tasks pending.")
            else:
                for order in pending_bulk:
                    with st.container():
                        st.markdown(f"""
                        <div style="background-color: #111111; border-left: 3px solid #D4AF37; border-top:1px solid #333333; border-bottom:1px solid #333333; border-right:1px solid #333333; padding: 20px; margin-bottom: 15px;">
                            <strong style="font-size: 1.15rem; color: #D4AF37;">⚠️ Large Event Request Code: {order['id']}</strong><br><br>
                            📝 <b>Product Batches Ordered:</b> {order['item']}<br>
                            🗓️ <b>Target Deliverable Target Date Log:</b> {order.get('date', 'N/A')}<br>
                            💵 <b>Contract Value Matrix:</b> ₹{order['total']}
                        </div>
                        """, unsafe_allow_html=True)
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            if st.button(f"✅ Authorize Manufacturing Run Slot", key=f"app_{order['id']}", use_container_width=True):
                                order["status"] = "Approved - Waiting Advance Payment"
                                st.rerun()
                        with col2:
                            if st.button(f"❌ Cancel/Deny Request Allocation", key=f"rej_{order['id']}", use_container_width=True):
                                order["status"] = "Rejected"
                                st.rerun()
                        st.write("---")

        # ─── SUB-TAB 2: BRAND NEW STOCK ADDITION & PRICING CONTROLS ───
        with admin_tab2:
            st.subheader("🛠️ Product Catalog & Inventory Operations")
            
            edit_col, add_col = st.columns(2)
            
            # Form A: Modify Stock & Price of an existing snack profile
            with edit_col:
                st.markdown("<h4 style='color:#D4AF37;'>🔄 Restock or Update Pricing</h4>", unsafe_allow_html=True)
                target_item = st.selectbox("Select snack variant to modify:", options=list(st.session_state.inventory.keys()))
                
                current_price = st.session_state.inventory[target_item]["price"]
                current_stock = st.session_state.inventory[target_item]["stock"]
                
                st.write(f"ℹ️ Currently on shelves: **{current_stock} units** | Price: **₹{current_price}**")
                
                new_price = st.number_input("Set New Price (₹):", min_value=1, value=int(current_price))
                added_stock = st.number_input("Add Stock Units (Brought from Kitchen):", min_value=0, value=0)
                
                if st.button("Apply Changes", use_container_width=True):
                    st.session_state.inventory[target_item]["price"] = new_price
                    st.session_state.inventory[target_item]["stock"] += added_stock
                    st.success(f"Successfully modified **{target_item}** metrics!")
                    st.rerun()
            
            # Form B: Completely create a new snack catalog entry lines
            with add_col:
                st.markdown("<h4 style='color:#D4AF37;'>✨ Launch New Snack Variant</h4>", unsafe_allow_html=True)
                new_item_name = st.text_input("New Item Name:", placeholder="e.g., Special Shahi Peda (1kg)")
                new_item_price = st.number_input("Set Base Retail Price (₹):", min_value=1, value=200)
                new_item_stock = st.number_input("Initial Kitchen Stock Level:", min_value=1, value=20)
                new_item_emoji = st.selectbox("Select Display Icon Emoji:", options=["✨", "🍬", "🥟", "🍿", "🔥", "🥢", "🏵️", "🌶️"])
                
                if st.button("Add Variant to Storefront Catalog", use_container_width=True):
                    if new_item_name.strip() == "":
                        st.error("Item configuration requires a title name descriptor profile.")
                    elif new_item_name.strip() in st.session_state.inventory:
                        st.error("This product entry variant already exists inside inventory databases.")
                    else:
                        st.session_state.inventory[new_item_name.strip()] = {
                            "price": new_item_price,
                            "stock": new_item_stock,
                            "emoji": new_item_emoji
                        }
                        st.success(f"🎉 **{new_item_name.strip()}** has been securely launched on live customer storefront arrays!")
                        st.rerun()

        # ─── SUB-TAB 3: COMPLETE ORDER ARCHIVE LOGS ───
        with admin_tab3:
            st.subheader("📋 Comprehensive Core Analytics Sales Ledger Database")
            if st.session_state.orders_log:
                for o in st.session_state.orders_log:
                    status_emoji = "🟡" if "Pending" in o["status"] else ("🟢" if "✅" in o["status"] or "Preparing" in o["status"] else "🔵")
                    st.markdown(f"{status_emoji} **Receipt Index ID:** `{o.get('id', 'N/A')}` | `{o['status']}` | Value: **₹{o['total']}** | *Products Inbound:* {o['item']}")
            else:
                st.info("No counter transactions have compiled inside database storage records yet today.")