import streamlit as st
from customer_segmentation import customer_segmentation
from energy_generation_planning import energy_generation_planning
from inventory_management import inventory_management
from sales_prediction import sales_prediction

# Call the functions to get the data and forecasts
customer_segmentation_result = customer_segmentation()
sales_prediction_result = sales_prediction()
inventory_management_result = inventory_management()
energy_generation_planning_result = energy_generation_planning()

# Display the data and forecasts
st.title('My Data Dashboard')

st.header('Customer Segmentation')
st.write(customer_segmentation_result['segmentation_results'])
st.pyplot(customer_segmentation_result['segmentation_plot'])

st.header('Sales & Revenue Prediction')
st.write(sales_prediction_result)

st.header('Inventory Management')
st.subheader('Inventory Data')
st.write(inventory_management_result['inventory_data'])

st.subheader('Reorder Dates')
st.write(inventory_management_result['reorder_dates'])

st.subheader('Inventory Plot')
st.pyplot(inventory_management_result['inventory_plot'])

st.header('Energy Generation Planning')
st.subheader('Average Solar Production')
st.write(energy_generation_planning_result['average_solar_production'])

st.subheader('Average Energy Consumption')
st.write(energy_generation_planning_result['average_energy_consumption'])

st.subheader('Energy Plots')
st.pyplot(energy_generation_planning_result['fig'])
