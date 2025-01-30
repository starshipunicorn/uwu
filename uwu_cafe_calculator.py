import streamlit as st
import streamlit.components.v1 as components

# Apply custom styling
st.markdown(
    """
    <style>
        body {
            background-color: #9966CC;
            color: white;
        }
        .stApp {
            background-color: #9966CC;
        }
        .stButton>button {
            background-color: #7A4D99;
            color: white;
            border-radius: 5px;
        }
        .stNumberInput>div>div>input {
            background-color: white;
            color: black;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# UWU Cat Cafe Menu with Prices
menu = {
    "Mains": {
        "sushi": 116,
        "buddha bowl": 124,
        "miso soup": 88,
    },
     "Desserts": {
        "kitty doughnut": 69,
        "kitty brownie": 63,
        "kitty cupcake": 69,
        "pancake": 84,
        "chocolate sandy": 78,
        "vanilla sandy": 78
    },
    "Bubble Teas": {
        "bubble tea blue berry": 64,
        "bubble tea mint": 64,
        "bubble tea rose": 64,
    },
    "Regular Teas": {
        "black tea": 20,
        "lemon lime iced tea": 33,
        "green tea": 25,
        "strawberry lemonade": 36,
        "classic uwu tea": 39,
        "blueberry tea": 33,
        "matcha tea": 33,
        "choco tea": 33,
        "peach iced tea": 33,
        "classic uwu tea": 39,
    },
    "Coffee": {
     "iced coffee": 33,
    }
}

# Function to calculate total price
def calculate_total(order, discount=0, fee=0):
    subtotal = sum(menu[category][item] * quantity for (category, item), quantity in order.items())
    discount_amount = subtotal * (discount / 100)
    subtotal_after_discount = subtotal - discount_amount
    fee_amount = subtotal_after_discount * (fee / 100)
    total = subtotal_after_discount + fee_amount
    return round(subtotal, 2), round(total, 2)

# Streamlit UI
st.title("🐱 UWU Cat Cafe Calculator 🍵")

st.sidebar.title("Settings")
discount = st.sidebar.slider("Discount (%)", 0, 100, 0)
fee = st.sidebar.slider("Additional Fee (%)", 0, 100, 0)

order = {}
cols = st.columns(2)

# First Column - Mains & Desserts
with cols[0]:
    st.subheader("🍽️ Mains")
    for item, price in menu["Mains"].items():
        quantity = st.number_input(f"{item} (${price})", min_value=0, max_value=500, step=1, key=item)
        if quantity > 0:
            order[("Mains", item)] = quantity
    
    st.subheader("🍰 Desserts")
    for item, price in menu["Desserts"].items():
        quantity = st.number_input(f"{item} (${price})", min_value=0, max_value=500, step=1, key=item)
        if quantity > 0:
            order[("Desserts", item)] = quantity

# Second Column - Teas & Coffee
with cols[1]:
    st.subheader("🧋 Bubble Teas")
    for item, price in menu["Bubble Teas"].items():
        quantity = st.number_input(f"{item} (${price})", min_value=0, max_value=500, step=1, key=item)
        if quantity > 0:
            order[("Bubble Teas", item)] = quantity
    
    st.subheader("🍵 Regular Teas")
    for item, price in menu["Regular Teas"].items():
        quantity = st.number_input(f"{item} (${price})", min_value=0, max_value=500, step=1, key=item)
        if quantity > 0:
            order[("Regular Teas", item)] = quantity
    
    st.subheader("☕ Coffee")
    for item, price in menu["Coffee"].items():
        quantity = st.number_input(f"{item} (${price})", min_value=0, max_value=500, step=1, key=item)
        if quantity > 0:
            order[("Coffee", item)] = quantity

if st.button("Calculate Total"):
    subtotal, total_price = calculate_total(order, discount=discount, fee=fee)
    st.markdown(f"## Subtotal: **${subtotal}**")
    st.markdown(f"## 🧾 Total Price: **${total_price}**")
    
    st.subheader("Order Summary")
    for (category, item), quantity in order.items():
        st.markdown(f"- {item} ({category}): {quantity} @ ${menu[category][item]} each")
