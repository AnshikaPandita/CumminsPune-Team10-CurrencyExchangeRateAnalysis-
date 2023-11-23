import pandas as pd
import streamlit as st
import plotly.express as px
import glob

# Function to fill missing data
def fill_missing_data():
    directory_path = "Users\Hp\Downloads\Exchange_Rate_Report_2012"
    files = glob.glob(directory_path + "/*.csv")

    for file_path in files:
        print(file_path)
        data_frame = pd.read_csv(file_path)

        # Fill missing values using forward fill
        data_frame = data_frame.fillna(method='ffill')

        # Fill missing values with column mean (except for the 'Date' column)
        for column in data_frame.columns:
            if column == 'Date':
                continue
            else:
                column_mean = data_frame[column].mean()
                data_frame[column] = data_frame[column].fillna(column_mean)

        print(data_frame)
        data_frame.to_csv(file_path, index=False)

# Main function
def main():
    st.set_page_config(page_title="Exchange Rate Analysis", page_icon=":bar_chart:", layout="wide")
    st.subheader("Hi, we are Team 10! :wave:")
    fill_missing_data()

    # Header
    st.title("Currency Exchange Rate Analysis")
    # Currency Selection
    st.markdown("### Currency Selection Comparison to USD")
    # Load initial data
    initial_data_frame = pd.read_csv("Exchange_Rate_Report_2012.csv")

    columns_selector = st.columns(2)
    
    selected_currency_1 = initial_data_frame.columns[50]
    
    selected_currency_2 = st.selectbox('Select Currency-2', initial_data_frame.columns[1:], key="currency_2")

    # Year and Time Frame Selection
    st.markdown("### Year and Time Frame Selection")

    selected_year = st.selectbox('Select Year', ('2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'))
    
    file_path_selected_year = f"Exchange_Rate_Report_{selected_year}.csv"
    data_frame_selected_year = pd.read_csv(file_path_selected_year)

    left_column, middle_column, right_column = st.columns(3)
    
    selected_time_frame = st.selectbox("Select Time Frame", ["Daily"], key="visibility", index=0)

    # # Currency Conversion Result
    currency_data_frame = pd.read_csv(file_path_selected_year)  # Load currency data for the selected year
    usd_values = list(map(float, currency_data_frame[selected_currency_1]))
    selected_currency_values = list(map(float, currency_data_frame[selected_currency_2]))

# Calculate the conversion rate for each data point
    conversion_rate = [1 / usd * selected_currency for usd, selected_currency in zip(usd_values, selected_currency_values)]

# Create a new DataFrame for the graph
    graph_data = pd.DataFrame({
    'Date': currency_data_frame['Date'],
    'Conversion Rate': conversion_rate
})

    st.info("1 {} = {:.5f} {}".format(selected_currency_1, conversion_rate[5], selected_currency_2))

# Data Processing and Visualization
    st.markdown("### Data Visualization")

    if st.checkbox("Show Raw Data"):
       st.write(graph_data)  # Display raw data if checkbox is selected

# Display the graph
    st.area_chart(graph_data.set_index('Date'))

    # Team Members
    st.markdown("### Team Members")
    st.markdown("Anshika Pandita")
    st.markdown("Isha More")
    st.markdown("Aditi Vijay Phunse")
    st.markdown("Mili Jha")
    st.markdown("Shrimayee Adkar")

if __name__ == "__main__":
    main()
