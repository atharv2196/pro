import streamlit as st
import time

def fuel_available():

    left_co, cent_co, last_co = st.columns(3)#made 3 equal column
    
    with cent_co:
        st.image('icon.jpg')  #inseted image for logo
        st.write("### **Welcome to Invictus Fuel Station!**")
        
        for i in range(3):
            time.sleep(1)  # created animation effect
            st.write("\n")  

        st.write("\n Types of fuel available: \n")
        st.write("1. CNG : 84 rs/kg")
        st.write("2. Petrol : 110 rs/lit")
        st.write("3. Diesel : 90 rs/lit")
        st.write("4. EV Charge : 4 rs/kWh")

def fuel_cost(fuel_type):
    cost = {
        "CNG": 84,
        "Petrol": 110,
        "Diesel": 90,
        "EV Charge": 4
    }
    return cost.get(fuel_type, 0)

def main():
    st.image('icon.jpg', width=200)
    st.title("Invictus Fuel Station")

    fuel_available()

    # Select fuel type
    fuel_choice = st.selectbox(
        "Please select a fuel type:",
        ["CNG", "Petrol", "Diesel", "EV Charge"]
    )

    st.write(f"You have selected: {fuel_choice}")

    # Choose how to fill the fuel
    fill_type = st.radio(
        "How would you like to fill the fuel?",
        ("By money", "By quantity")
    )

    if fill_type == "By money":
        money = st.number_input(f"Enter the amount of money to fill {fuel_choice}:", min_value=0.0, step=1.0)
        if money > 0:
            cost = fuel_cost(fuel_choice)
            if fuel_choice == "CNG":
                st.write(f"You will receive {money / cost} kg of CNG.")
            elif fuel_choice == "Petrol":
                st.write(f"You will receive {money / cost} liters of Petrol.")
            elif fuel_choice == "Diesel":
                st.write(f"You will receive {money / cost} liters of Diesel.")
            elif fuel_choice == "EV Charge":
                st.write(f"You will receive {money / cost} kWh of EV Charge.")
        else:
            st.write("Please enter a valid amount of money.")

    elif fill_type == "By quantity":
        quantity = st.number_input(f"Enter the quantity of {fuel_choice} to fill:", min_value=0.0, step=0.1)
        if quantity > 0:
            cost = fuel_cost(fuel_choice)
            st.write(f"The total cost for {quantity} units of {fuel_choice} is {quantity * cost} rs.")
        else:
            st.write("Please enter a valid quantity.")

    st.write("\nThank you for visiting the fuel station! Please drive safely.")
    

if __name__ == "__main__":
    main()