import streamlit as st
import pandas as pd

st.header('LIFE BUSINESS FINANCIAL IMPLICATIONS')

user_units = int(st.number_input("Enter Number of Unit Managers"))
user_agents = int(st.number_input("Number of Agents Per Unit"))
user_policies = int(st.number_input("Enter the Number of Policies Per Month:"))
user_amount = int(st.number_input("Enter the Premium Per Policy"))
user_policy_term = int(st.number_input("Enter the Policy Term (For now 1 to 10 years)"))
user_persistency = float(st.number_input("Enter Pesistency as a Percentage eg. 80"))

policies = user_policies
years = user_policy_term
amount = user_amount
agents = user_agents
unit_managers = user_units
persistency = (user_persistency/100)

commission_rate_year_one = 0.4
commission_rate_year_two = 0.2
commission_rate_year_three_onwards = 0.05

premium_month_one = (policies*amount*agents*unit_managers*persistency)
comm_premium = 6*(premium_month_one + (premium_month_one + ((12-1) * premium_month_one))
st.markdown(comm_premium)

if st.button("Calculate"):
    def calculate_premium(years):   
        results1 = []
        from_previous_year = 0  # Initialize from_previous_year
        
        for year in range(1, years+1):
            # Calculate Premium
            if year == 1:
                premium = 6*(premium_month_one + (premium_month_one + ((12-1) * premium_month_one)))
                from_previous_year = 0
            else:
                
                from_previous_year = premium * persistency
                premium = from_previous_year + results1[-1]['current_year']
            
            
            results1.append({
                'year': year,
                'premium': premium,
                
                'current_year': results1[-1]['current_year'] if year > 1 else premium
            })

        return results1
    results1 = calculate_premium(years)

    table1 = pd.DataFrame(results1)
    # st.table(table1)
    
           
    
    def calculate_commission(years):             
        results = []
        for year in range(1, years+1):

            comm_premium = 6*(premium_month_one + (premium_month_one + ((12-1) * premium_month_one)))
          
            if year == 1:
                commission = (comm_premium * commission_rate_year_one)
            elif year == 2:
                commission = (comm_premium * 0.8 * commission_rate_year_two) + (comm_premium * commission_rate_year_one)
            elif year == 3:
                commission = (comm_premium * (0.8 ** (year - 1)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 2)) * commission_rate_year_two) + \
                            (comm_premium * commission_rate_year_one)
            elif year == 4:
                commission = (comm_premium * (0.8 ** (year - 1)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 2)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 3)) * commission_rate_year_two) + \
                            (comm_premium * commission_rate_year_one)
                            
            elif year == 5:
                commission = (comm_premium * (0.8 ** (year - 1)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 2)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 3)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 4)) * commission_rate_year_two) + \
                            (comm_premium * commission_rate_year_one)
                
            elif year == 6:
                commission = (comm_premium * (0.8 ** (year - 1)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 2)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 3)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 4)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 5)) * commission_rate_year_two) + \
                            (comm_premium * commission_rate_year_one)
            elif year == 7:
                commission = (comm_premium * (0.8 ** (year - 1)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 2)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 3)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 4)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 5)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 6)) * commission_rate_year_two) + \
                            (comm_premium * commission_rate_year_one)
                
            elif year == 8:
                commission = (comm_premium * (0.8 ** (year - 1)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 2)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 3)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 4)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 5)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 6)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 7)) * commission_rate_year_two) + \
                            (comm_premium * commission_rate_year_one)
                
            elif year == 9:
                commission = (comm_premium * (0.8 ** (year - 1)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 2)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 3)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 4)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 5)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 6)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 7)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 8)) * commission_rate_year_two) + \
                            (comm_premium * commission_rate_year_one)
                
            elif year == 10:
                commission = (comm_premium * (0.8 ** (year - 1)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 2)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 3)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 4)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 5)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 6)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 7)) * commission_rate_year_three_onwards) + \
                            (comm_premium * (0.8 ** (year - 8)) * commission_rate_year_three_onwards) + (comm_premium * (0.8 ** (year - 9)) * commission_rate_year_two) + (comm_premium * commission_rate_year_one)
                

            results.append({
                'year': year,
                'commission': commission,})

        return results
    
    results = calculate_commission(years)
    
    table = pd.DataFrame(results)   
    
        
    # st.table(table)
    
    merged = pd.merge(table1, table, on='year', how='inner')
    merged['Cumulative Premium'] = merged['premium'].cumsum()

    finalmerged = merged[['year', 'premium', 'commission', 'Cumulative Premium']].rename(columns={'year':'As at End of Year:', 'premium': 'Premium Received', 'commission': 'Commission Payable'})
    st.table(finalmerged)
    
        


