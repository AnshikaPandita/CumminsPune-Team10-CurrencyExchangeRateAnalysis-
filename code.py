import pandas as pd
import streamlit as st
import plotly.express as px
import glob

# Function to fill missing data
def fill_missing():
    path = "Users\Hp\Downloads\Exchange_Rate_Report_2012"
    files = glob.glob(path + "/*.csv")

    for fname in files:
        print(fname)
        df = pd.read_csv(fname)
        print(df)
        for column in df:
            df[column] = df[column].fillna(method='ffill')

        for column in df:
            if column == 'Date':
                continue
            else:
                mean = df[column].mean()
                df[column] = df[column].fillna(mean)

        print(df)
        df.to_csv(fname, index=False)

# Function to get monthly data
def get_monthly_data(df, option):
    data = df[[df.columns[0], option]].copy()
    data['month'] = pd.DatetimeIndex(data[df.columns[0]]).month
    avg = data.groupby(pd.PeriodIndex(data[df.columns[0]], freq="M"))[option].mean()
    avg = avg.to_frame()
    avg['mon'] = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]

    avg = avg.set_index(avg['mon'])
    dat = avg[[option]].copy()
    return dat

# Function to get quarterly data
def get_quarterly_data(df, option):
    data = df[[df.columns[0], option]].copy()
    data['month'] = pd.DatetimeIndex(data[df.columns[0]]).month
    avg = data.groupby(pd.PeriodIndex(data[df.columns[0]], freq="M"))[option].mean()
    avg = avg.to_frame()
    avg['mon'] = [0,1,2,3,4,5,6,7,8,9,10,11]
    avg = avg.set_index(avg['mon'])
    dat = avg[[option]].copy()
    temp = list(map(int, avg[option]))
    quarter = []
    sum = 0
    for x in avg['mon']:
        if x % 4 == 0:
            if x == 0:
                sum = 0
            else:
                sum = sum / 4 
                quarter.append(sum)
                sum = 0
        sum = sum + temp[x]
    sum = sum / 4
    quarter.append(sum)
    quar = dat[option].copy()
    value = pd.DataFrame()
    value['val'] = quarter
    return value

# Function to get yearly data
def get_yearly_data(df, option):
    years = ['2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']
    values = []
    for i in range(len(years)):
        path = "Exchange_Rate_Report_{}.csv".format(years[i])
        df = pd.read_csv(path)
        values.append(df[option].mean())
    values = pd.DataFrame(values, index=years, columns=[option])
    return values

# Main function
def main():
    st.set_page_config(page_title="Exchange Rate Analysis", page_icon=":bar_chart:", layout="wide")
    st.subheader("Hi, we are Team 10! :wave:")
    fill_missing()

    # Header
    st.title("Currency Exchange Rate Analysis")
    # Currency Selection
    st.markdown("### Currency Selection")
    # Load initial data
    df = pd.read_csv("Exchange_Rate_Report_2012.csv")

    columns = st.columns(2)
    with columns[0]:
        c1 = st.selectbox('Select Currency-1', df.columns[1:], key="currency_1")
    with columns[1]:
        c2 = st.selectbox('Select Currency-2', df.columns[1:], key="currency_2")

    # Year and Time Frame Selection
    st.markdown("### Year and Time Frame Selection")

    year = st.selectbox('Select Year', ('2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022'))
    
    path = "Exchange_Rate_Report_{}.csv".format(year)
    df = pd.read_csv(path)

    left_column, middle_column, right_column = st.columns(3)
    
    time_frame = st.selectbox("Select Time Frame", ["Weekly", "Monthly", "Quarterly", "Yearly"], key="visibility", index=1)

    # Currency Conversion Result
    currency_data = pd.read_csv(path)  # Load currency data for the selected year
    cu = list(map(float, currency_data[c1]))
    cu1 = list(map(float, currency_data[c2]))
    temp, temp1 = cu[5], cu1[5]
    cal = (1 / float(temp)) * float(temp1)

    st.info("1 {} = {:.5f} {}".format(c1, cal, c2))

    
    # Data Processing and Visualization
    st.markdown("### Data Visualization")
    
    if st.checkbox("Show Raw Data"):
        st.write(df)  # Display raw data if checkbox is selected

    if time_frame == "Weekly":
        data = df[[df.columns[0], c1]].copy()
        row = len(df.axes[0])
        data[data.columns[0]] = pd.date_range(data[df.columns[0]].iloc[0], data[df.columns[0]].iloc[-1], periods=row)
        data = data.set_index(df.columns[0])
        minimum, maximum = data.min(), data.max()
        l, r = st.columns(2)
        with l:
            st.info("MIN value: {}".format(minimum.iloc[0]))
        with r:
            st.info("MAX value: {}".format(maximum.iloc[0]))
        st.line_chart(data)

    elif time_frame == "Monthly":
        data_month = get_monthly_data(df, c1)
        minimum, maximum = data_month.min(), data_month.max()
        l, r = st.columns(2)
        with l:
            st.info("MIN value: {}".format(minimum.iloc[0]))
        with r:
            st.info("MAX value: {}".format(maximum.iloc[0]))
        st.line_chart(data_month)

    elif time_frame == "Quarterly":
        data_quarter = get_quarterly_data(df, c1)
        minimum, maximum = data_quarter.min(), data_quarter.max()
        l, r = st.columns(2)
        with l:
            st.info("MIN value: {}".format(minimum.iloc[0]))
        with r:
            st.info("MAX value: {}".format(maximum.iloc[0]))
        st.line_chart(data_quarter)

    elif time_frame == "Yearly":
        data_year = get_yearly_data(df, c1)
        minimum, maximum = data_year.min(), data_year.max()
        l, r = st.columns(2)
        with l:
            st.info("MIN value: {}".format(minimum.iloc[0]))
        with r:
            st.info("MAX value: {}".format(maximum.iloc[0]))
        st.line_chart(data_year)

# Team Members
    st.markdown("### Team Members")
    st.markdown("Anshika Pandita")
    st.markdown("Isha More")
    st.markdown("Aditi Vijay Phunse")
    st.markdown("Mili Jha")
    st.markdown("Shrimayee Adkar")

if __name__ == "__main__":
    main()
