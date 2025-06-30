import streamlit as st
import pandas as pd
import altair as alt








st.subheader("Projected Account Balance Over Time")
    #st.line_chart(df.set_index('Age')['Balance'])
    
    # Split data into positive and negative parts
    df_pos = df[df['Balance'] >= 0].copy()
    df_neg = df[df['Balance'] < 0].copy()

    # Base line chart
    line = alt.Chart(df).mark_line().encode(
        x = alt.X('Age:Q', scale=alt.Scale(domain=[initial_age, end_age])),
        y = alt.Y('Balance:Q'),
        tooltip=['Age', 'Balance']  
    )

    # Area for positive and negative balances
    charts = [line]
    
    if not df_pos.empty:
        area_pos = alt.Chart(df_pos).mark_area(opacity=0.3, color='green').encode(
            x = alt.X('Age:Q', scale=alt.Scale(domain=[initial_age, end_age])),
            y = 'Balance:Q'
        )
        charts.append(area_pos)
    if not df_neg.empty:    
        area_neg = alt.Chart(df_neg).mark_area(opacity=0.3, color='red').encode(
            x = alt.X('Age:Q', scale=alt.Scale(domain=[initial_age, end_age])),
            y = 'Balance:Q'
        )
        charts.append(area_neg)

    # Composing charts
    chart = alt.layer(*charts).properties(
        width = 700,
        height = 400,
        title = "Retirement Savings Projection (inflation adjusted)"
    )

    # Convert chart to Vega-Lite spec and display it 
    chart_spec = chart.to_dict()
    st.vega_lite_chart(chart_spec, use_container_width=True)