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
        print(data_frame)
        
        # Fill missing values using forward fill
        for column in data_frame:
            data_frame[column] = data_frame[column].fillna(method='ffill')

        # Fill missing values with column mean (except for the 'Date' column)
        for column in data_frame:
            if column == 'Date':
                continue
            else:
                column_mean = data_frame[column].mean()
                data_frame[column] = data_frame[column].fillna(column_mean)

        print(data_frame)
        data_frame.to_csv(file_path, index=False)

# Function to get monthly data
def get_monthly_data(data_frame, selected_option):
    selected_data = data_frame[[data_frame.columns[0], selected_option]].copy()
    selected_data['month'] = pd.DatetimeIndex(selected_data[data_frame.columns[0]]).month
    average_data = selected_data.groupby(pd.PeriodIndex(selected_data[data_frame.columns[0]], freq="M"))[selected_option].mean()
    average_data = average_data.to_frame()
    average_data['mon'] = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]

    average_data = average_data.set_index(average_data['mon'])
    monthly_data = average_data[[selected_option]].copy()
    return monthly_data

# Function to get quarterly data
def get_quarterly_data(data_frame, selected_option):
    selected_data = data_frame[[data_frame.columns[0], selected_option]].copy()
    selected_data['month'] = pd.DatetimeIndex(selected_data[data_frame.columns[0]]).month
    average_data = selected_data.groupby(pd.PeriodIndex(selected_data[data_frame.columns[0]], freq="M"))[selected_option].mean()
    average_data = average_data.to_frame()
    average_data['mon'] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    average_data = average_data.set_index(average_data['mon'])
    quarterly_data = average_data[[selected_option]].copy()
    
    temp_values = list(map(int, average_data[selected_option]))
    quarterly_values = []
    temp_sum = 0
    
    for x in average_data['mon']:
        if x % 4 == 0:
            if x == 0:
                temp_sum = 0
            else:
                temp_sum = temp_sum / 4 
                quarterly_values.append(temp_sum)
                temp_sum = 0
        temp_sum = temp_sum + temp_values[x]
    
    temp_sum = temp_sum / 4
    quarterly_values.append(temp_sum)
    
    quarterly_result = quarterly_data[selected_option].copy()
    result_dataframe = pd.DataFrame()
    result_dataframe['val'] = quarterly_values
    
    return result_dataframe

# Function to get yearly data
def get_yearly_data(data_frame, selected_option):
    years = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
    yearly_values = []
    
    for i in range(len(years)):
        file_path = "Exchange_Rate_Report_{}.csv".format(years[i])
        data_frame = pd.read_csv(file_path)
        yearly_values.append(data_frame[selected_option].mean())
    
    yearly_values_df = pd.DataFrame(yearly_values, index=years, columns=[selected_option])
    return yearly_values_df

# Main function
def main():
    st.set_page_config(page_title="Exchange Rate Analysis", page_icon=":bar_chart:", layout="wide")
    st.subheader("Hi, we are Team 10! :wave:")
    fill_missing_data()

    # Header
    st.title("Currency Exchange Rate Analysis")
    # Currency Selection
    st.markdown("### Currency Selection")
    # Load initial data
    initial_data_frame = pd.read_csv("Exchange_Rate_Report_2012.csv")

    columns_selector = st.columns(2)
    with columns_selector[0]:
        selected_currency_1 = st.selectbox('Select Currency-1', initial_data_frame.columns[1:], key="currency_1")
    with columns_selector[1]:
        selected_currency_2 = st.selectbox('Select Currency-2', initial_data_frame.columns[1:], key="currency_2")

    # Year and Time Frame Selection
    st.markdown("### Year and Time Frame Selection")

    selected_year = st.selectbox('Select Year', ('2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'))
    
    file_path_selected_year = "Exchange_Rate_Report_{}.csv".format(selected_year)
    data_frame_selected_year = pd.read_csv(file_path_selected_year)

    left_column, middle_column, right_column = st.columns(3)
    
    selected_time_frame = st.selectbox("Select Time Frame", ["Weekly", "Monthly", "Quarterly", "Yearly"], key="visibility", index=1)

    # Currency Conversion Result
    currency_data_frame = pd.read_csv(file_path_selected_year)  # Load currency data for the selected year
    currency_values_1 = list(map(float, currency_data_frame[selected_currency_1]))
    currency_values_2 = list(map(float, currency_data_frame[selected_currency_2]))
    selected_temp, temp_1 = currency_values_1[5], currency_values_2[5]
    calculated_result = (1 / float(selected_temp)) * float(temp_1)

    st.info("1 {} = {:.5f} {}".format(selected_currency_1, calculated_result, selected_currency_2))

    # Data Processing and Visualization
    st.markdown("### Data Visualization")
    
    if st.checkbox("Show Raw Data"):
        st.write(data_frame_selected_year)  # Display raw data if checkbox is selected

    if selected_time_frame == "Weekly":
        weekly_data = data_frame_selected_year[[data_frame_selected_year.columns[0], selected_currency_1]].copy()
        row_count = len(data_frame_selected_year.axes[0])
        weekly_data[weekly_data.columns[0]] = pd.date_range(weekly_data[data_frame_selected_year.columns[0]].iloc[0], weekly_data[data_frame_selected_year.columns[0]].iloc[-1], periods=row_count)
        weekly_data = weekly_data.set_index(data_frame_selected_year.columns[0])
        minimum_weekly, maximum_weekly = weekly_data.min(), weekly_data.max()
        left_weekly, right_weekly = st.columns(2)
        with left_weekly:
            st.info("MIN value: {}".format(minimum_weekly.iloc[0]))
        with right_weekly:
            st.info("MAX value: {}".format(maximum_weekly.iloc[0]))
        st.line_chart(weekly_data)

    elif selected_time_frame == "Monthly":
        monthly_result = get_monthly_data(data_frame_selected_year, selected_currency_1)
        minimum_monthly, maximum_monthly = monthly_result.min(), monthly_result.max()
        left_monthly, right_monthly = st.columns(2)
        with left_monthly:
            st.info("MIN value: {}".format(minimum_monthly.iloc[0]))
        with right_monthly:
            st.info("MAX value: {}".format(maximum_monthly.iloc[0]))
        st.line_chart(monthly_result)

    elif selected_time_frame == "Quarterly":
        quarterly_result = get_quarterly_data(data_frame_selected_year, selected_currency_1)
        minimum_quarterly, maximum_quarterly = quarterly_result.min(), quarterly_result.max()
        left_quarterly, right_quarterly = st.columns(2)
        with left_quarterly:
            st.info("MIN value: {}".format(minimum_quarterly.iloc[0]))
        with right_quarterly:
            st.info("MAX value: {}".format(maximum_quarterly.iloc[0]))
        st.line_chart(quarterly_result)

    elif selected_time_frame == "Yearly":
        yearly_result = get_yearly_data(data_frame_selected_year, selected_currency_1)
        minimum_yearly, maximum_yearly = yearly_result.min(), yearly_result.max()
        left_yearly, right_yearly = st.columns(2)
        with left_yearly:
            st.info("MIN value: {}".format(minimum_yearly.iloc[0]))
        with right_yearly:
            st.info("MAX value: {}".format(maximum_yearly.iloc[0]))
        st.line_chart(yearly_result)

    # Team Members
    st.markdown("### Team Members")
    st.markdown("Anshika Pandita")
    st.markdown("Isha More")
    st.markdown("Aditi Vijay Phunse")
    st.markdown("Mili Jha")
    st.markdown("Shrimayee Adkar")

if __name__ == "__main__":
    main()
