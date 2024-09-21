import streamlit as st

# Title and description
st.title("Marketing Analysis Tool")
st.write("Calculate customer acquisition costs and optimize your marketing strategy.")

# Customer Lifetime Value Input
clv = st.number_input("Customer Lifetime Value (ZAR)", min_value=0.0, value=100.0)

# WhatsApp marketing inputs
whatsapp_messages = st.number_input("Number of WhatsApp Messages Sent", min_value=0, value=1000)
delivery_rate = st.slider("Delivery Rate (%)", min_value=0.0, max_value=100.0, value=90.0)
conversion_rate = st.slider("Conversion Rate (%)", min_value=0.0, max_value=100.0, value=10.0)
cost_per_message = st.number_input("Cost per WhatsApp Message (ZAR)", min_value=0.0, value=0.8)

# Free burrito and marketing costs
cost_per_burrito = st.number_input("Cost per Free Burrito (ZAR)", min_value=0.0, value=27.0)
additional_marketing_cost = st.number_input("Additional Marketing Costs (ZAR)", min_value=0.0, value=0.0)

# Target revenue and profit
target_revenue = st.number_input("Target Revenue (ZAR)", min_value=0.0, value=50000.0)
target_profit = st.number_input("Target Profit (ZAR)", min_value=0.0, value=10000.0)
average_sale_value = st.number_input("Average Sale Value (ZAR)", min_value=0.0, value=100.0)

# Calculate number of converted customers
delivered_messages = whatsapp_messages * (delivery_rate / 100)
converted_customers = delivered_messages * (conversion_rate / 100)

# Calculate cost per acquisition (CPA)
total_marketing_cost = (whatsapp_messages * cost_per_message) + (converted_customers * cost_per_burrito) + additional_marketing_cost
cpa = total_marketing_cost / converted_customers if converted_customers > 0 else 0

# Calculate net revenue
net_revenue = (converted_customers * average_sale_value) - total_marketing_cost

# Calculate break-even sales and target profit sales
break_even_sales = total_marketing_cost / average_sale_value if average_sale_value > 0 else 0
target_profit_sales = (target_profit + total_marketing_cost) / average_sale_value if average_sale_value > 0 else 0

# Display results
st.subheader("Results")
st.write(f"Cost per Acquisition (CPA): ZAR {cpa:.2f}")
st.write(f"Net Revenue: ZAR {net_revenue:.2f}")
st.write(f"Break-even Sales: {break_even_sales:.0f} sales")
st.write(f"Sales Needed for Target Profit: {target_profit_sales:.0f} sales")
