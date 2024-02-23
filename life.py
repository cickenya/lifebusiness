import streamlit as st
import pandas as pd


investment = {}
timeframe = 0
annual = 0

finaldf = {}

st.header('LIFE BUSINESS FINANCIAL IMPLICATIONS')

tab1, tab2, tab3, tab4 = st.tabs(["📈 Calculations",  "Premium and Commission", "Investment", "Maturity Claims"])

with tab1:
    
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
    comm_premium = 6*(premium_month_one + (premium_month_one + ((12-1) * premium_month_one)))
    annual = '{:,.0f}'.format(round(10 * (comm_premium + annual)))

    amended_premium = "{:,.0f}".format(comm_premium)
  


    if st.button("Calculate"):

        st.markdown(f"Annual Premium For New Business: {amended_premium}")
        
        def calculate_premium(years):   
            results1 = []
            from_previous_year = 0  # Initialize from_previous_year
            
            for year in range(1, years+1):
                # Calculate Premium
                if year == 1:
                    premium = round(6*(premium_month_one + (premium_month_one + ((12-1) * premium_month_one))))
                    from_previous_year = 0
                    
                else:
                    
                    from_previous_year = premium * persistency
                    premium = round(from_previous_year + results1[-1]['current_year'])

                  
                
                
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
                    commission = round(comm_premium * commission_rate_year_one)
                elif year == 2:
                    commission = round((comm_premium * 0.8 * commission_rate_year_two) + (comm_premium * commission_rate_year_one))
                elif year == 3:
                    commission = round((comm_premium * (0.8 ** (year - 1)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 2)) * commission_rate_year_two) + \
                                (comm_premium * commission_rate_year_one))
                elif year == 4:
                    commission = round((comm_premium * (0.8 ** (year - 1)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 2)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 3)) * commission_rate_year_two) + \
                                (comm_premium * commission_rate_year_one))
                                
                elif year == 5:
                    commission = round((comm_premium * (0.8 ** (year - 1)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 2)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 3)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 4)) * commission_rate_year_two) + \
                                (comm_premium * commission_rate_year_one))
                    
                elif year == 6:
                    commission = round((comm_premium * (0.8 ** (year - 1)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 2)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 3)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 4)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 5)) * commission_rate_year_two) + \
                                (comm_premium * commission_rate_year_one))
                elif year == 7:
                    commission = round((comm_premium * (0.8 ** (year - 1)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 2)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 3)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 4)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 5)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 6)) * commission_rate_year_two) + \
                                (comm_premium * commission_rate_year_one))
                    
                elif year == 8:
                    commission = round((comm_premium * (0.8 ** (year - 1)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 2)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 3)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 4)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 5)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 6)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 7)) * commission_rate_year_two) + \
                                (comm_premium * commission_rate_year_one))
                    
                elif year == 9:
                    commission = round((comm_premium * (0.8 ** (year - 1)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 2)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 3)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 4)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 5)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 6)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 7)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 8)) * commission_rate_year_two) + \
                                (comm_premium * commission_rate_year_one))
                    
                elif year == 10:
                    commission = round((comm_premium * (0.8 ** (year - 1)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 2)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 3)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 4)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 5)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 6)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 7)) * commission_rate_year_three_onwards) + \
                                (comm_premium * (0.8 ** (year - 8)) * commission_rate_year_three_onwards) + (comm_premium * (0.8 ** (year - 9)) * commission_rate_year_two) + (comm_premium * commission_rate_year_one))
                    

                results.append({
                    'year': year,
                    'commission': commission,})

            return results
        
        results = calculate_commission(years)
        
        table = pd.DataFrame(results)   
        
            
        # st.table(table)
        
        merged = pd.merge(table1, table, on='year', how='inner')
        merged['Cumulative Premium'] = round(merged['premium'].cumsum())
        merged['Cumulative Commission'] = round(merged['commission'].cumsum())
        

        finalmerged = merged[['year', 'premium', 'commission', 'Cumulative Premium', 'Cumulative Commission']].rename(columns={'year':'As at End of Year:', 'premium': 'Premium Received', 'commission': 'Commission Payable'})
        
        finalmerged['Salaries, ICT and Overhead Expenses'] = round((0.1 * finalmerged['Premium Received']) + 2000000)

        finalmerged['Investment Principal'] = round(finalmerged['Premium Received'] - (finalmerged['Commission Payable'] + finalmerged['Salaries, ICT and Overhead Expenses']))

        finalmerged = finalmerged[['Premium Received', 'Commission Payable','Salaries, ICT and Overhead Expenses', 'Investment Principal','Cumulative Premium', 'Cumulative Commission' ]]
        
        investment_data = finalmerged.to_dict(orient='records')
        investment = investment_data.copy()
        timeframe = user_policy_term + timeframe 

        df2 = pd.DataFrame(investment)

            

        df2['Interest Factor'] = (1 + (0.15/1))**(timeframe - df2.index.values)

        
        df2['Investment Amount After Maturity Period'] = round(df2['Investment Principal'] * df2['Interest Factor'])

        df2['Interest Earned'] = round(df2['Investment Amount After Maturity Period'] - df2['Investment Principal'])
            
        df2['Cumulative Amount In Investment Account'] = round(df2['Investment Amount After Maturity Period'].cumsum())

        newdf = df2[['Investment Principal', 'Interest Earned', 'Investment Amount After Maturity Period', 'Cumulative Amount In Investment Account']]
        
        newdf = newdf.round(0)

        final = newdf.to_dict(orient='records')
        finaldf = final.copy()

        


with tab2:   

    st.dataframe(investment)


    
with tab3:
    df3 = pd.DataFrame(finaldf)

    df3 = df3.round(0)
    
    # Display the styled DataFrame
    st.dataframe(df3)


with tab4:
    st.write('If the logic of the model is upheld we expect to start paying claims in the 11th year after inception')
    st.write('Claim Payable :')
    st.markdown(annual)
