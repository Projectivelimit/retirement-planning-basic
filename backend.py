import pandas as pd


def simulate_retirement_planning(start_age, retirement_age, end_age, 
                        monthly_contribution, monthly_spending, 
                        annual_return, initial_savings,
                        inflation_rate = 2.0, 
                        inflation_adjustment = True):
    age_range = list(range(start_age, end_age + 1))
    savings = []
    current_balance = initial_savings

    # Adjust return for inflation if selected
    real_annual_return = ((1 + annual_return / 100) / (1 + inflation_rate / 100) - 1) * 100

    monthly_contribution_incl_infl = monthly_contribution

    monthly_return = (1 + real_annual_return / 100) ** (1/12) - 1

    for age in age_range:
        savings.append(current_balance)
        for _ in range(12): 
            if age < retirement_age:
                current_balance += monthly_contribution_incl_infl
            else:
                current_balance -= monthly_spending
            current_balance *= (1 + monthly_return)
        if inflation_adjustment == True:
            monthly_contribution_incl_infl *= (1 + inflation_rate/100)

    return pd.DataFrame({'Age': age_range, 'Balance': savings})