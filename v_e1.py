import streamlit as st
import pandas as pd
import plotly.express as px

st.title('My favorite Holidays Experience')

# Add two empty lines for spacing
st.write('\n')
st.write('\n')

# Initialize session state for counts
if 'counts' not in st.session_state:
    st.session_state.counts = {'Sea Trip': 0, 'Mountain Trip': 0, 'Country Trip': 0}

# Function to update counts
def update_counts(trip_type):
    st.session_state.counts[trip_type] += 1

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Two weeks by the sea'):
        update_counts('Sea Trip')

with col2:
    if st.button('Mountain Trip'):
        update_counts('Mountain Trip')

with col3:
    if st.button('Holidays by my Grandma'):
        update_counts('Country Trip')

# Convert counts to dataframe
df = pd.DataFrame(list(st.session_state.counts.items()), columns=['Trip', 'Count'])

st.write('\n')

# Add a button to check the results
check_now = st.button('Let check now')

# Display bar chart if total counts exceed 30 or button is pressed
if df['Count'].sum() > 30 or check_now:
    st.subheader('Summary of Votes')
    fig = px.bar(df, x='Count', y='Trip', orientation='h', color='Trip', text='Count',
                 color_discrete_sequence=px.colors.qualitative.Plotly)
    fig.update_layout(showlegend=False)
    fig.update_traces(textposition='outside')
    st.plotly_chart(fig, use_container_width=True)