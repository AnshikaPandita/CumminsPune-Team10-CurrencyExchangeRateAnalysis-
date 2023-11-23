# CumminsPune-Team10-CurrencyExchangeRateAnalysis-

Welcome to the Currency Exchange Rate Analysis Dashboard project by **team 10!** 

## Project Overview

The project fulfills the following requirements:

### Definition

Exchange rate is the price of one currency in terms of another currency. A currency appreciates if it takes more of another currency to buy it and depreciates if it takes less of another currency to buy it.

### Problem Statement

Create a dashboard that allows users to analyze the exchange rates between two currencies over a period of time. Users have the option to select weekly, monthly, quarterly, and yearly charts. The dashboard displays the date on which the rate was at its peak (highest) and the date on which it was at its lowest.

### Tools Used

- [pandas](https://pandas.pydata.org/)
- [Streamlit](https://streamlit.io/)
- [plotly-express](https://plotly.com/python/plotly-express/)
- Code Editor: [VS Code](https://code.visualstudio.com/)

### Functional Tasks

-  Read and store the data from the file.
-  Create a user interface allowing users to select currency and desired duration.
-  Users can Daily charts.
-  Fetch data for the given currency and time duration, showing the trend.
### Input

Exchange Rate dataset is provided in a CSV file format, containing exchange rates as currency units per U.S. Dollar. 

### UI Requirements

- UI provides the option to select 2 currencies (Currency 1 and Currency 2).Currency 1 auto-populates with USD.
- Users can then select the year analysis.
- Converted currency is displayed based on user-provided data.
- Users can visualize the data in two forms: raw and area graph.
  
### Preview


![image](https://github.com/AnshikaPandita/CumminsPune-Team10-CurrencyExchangeRateAnalysis-/assets/96713901/498fbd26-91c1-4b5f-967d-239336ff3fed)
![image](https://github.com/AnshikaPandita/CumminsPune-Team10-CurrencyExchangeRateAnalysis-/assets/96713901/4b01ed83-893a-4c58-b224-ab9a1dded990)
![image](https://github.com/AnshikaPandita/CumminsPune-Team10-CurrencyExchangeRateAnalysis-/assets/96713901/0562cbab-9f8d-47d8-a894-983e7364d7f5)

### Recommendations/Guidelines

1. Followed clean coding practices.
2. Designed in a modular way for easy maintenance and extension.
3. Code is supplemented with automation tests.
4. Utilized Streamlit for the user interface.

###Work On Project In Future
- Users have the option to select weekly, monthly, quarterly, and yearly charts.
- The dashboard displays the date on which the rate was at its peak (highest) and the date on which it was at its lowest i.e.MIN-MAX values.
- Provide option to select currency-1 also as any currency rather than populating it as USD
always. Use USD as through currency and derive exchange rate between 2 currencies. For
instance, if Sterling (GBP) and Australian Dollar (AUD) are the 2 currencies selected then
derive direct exchange rate between GBP and USD. Once exchange rate is derived between
GBP and USD currency, use that as base to derive value for second currency which is AUD in
this example.
- Provide a Service/Component which will provide FX rates for all currencies considering a
base currency. For instance, USD as a base currency and value of all other currencies in
terms of USD for a given date.
- Provide a Service/Component to convert value of currency into another currency. For
instance, if the user provides base currency as USD and target currency as INR and amount
of 1000 and let’s say exchange rate is 79, component should convert amount into target
currency and result should be 79,000 INR
- UI screen to display all currencies along with the short code, description, and current
exchange rate
- Automate uploading of exchange rate data into database
  
## Team Members

- Anshika Pandita
- Isha More
- Aditi Vijay Phunse
- Mili Jha
- Shrimayee Adkar

## Getting Started

Follow these steps to run the Currency Exchange Rate Analysis Dashboard locally:


1. Clone the repository:

   ```bash
   [git clone https://github.com/yourusername/currency-exchange-dashboard.git
   cd currency-exchange-dashboard](https://github.com/AnshikaPandita/CumminsPune-Team10-Curre)
   
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt 


3. Run the Streamlit app:

     ```bash
   streamlit run app.py

4. Open your web browser and go to http://localhost:8501 to access the app.




