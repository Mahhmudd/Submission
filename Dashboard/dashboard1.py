import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# mengatur style
sns.set(style='whitegrid')

# Menyiapkan database day_df
day_df = pd.read_csv("Data/bike_day.csv")
day_df.head()

# Menghapus kolom yang tidak digunakan
drop_col = ['windspeed']

for i in day_df.columns:
  if i in drop_col:
    day_df.drop(labels=i, axis=1, inplace=True)

# ganti judul kolom
day_df.rename(columns={
    'dteday': 'dateday',
    'yr': 'year',
    'mnth': 'month',
    'weathersit': 'weather_cond',
    'cnt': 'count'
}, inplace=True)

# Mengubah kolom dan baris 
day_df['month'] = day_df['month'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
})
day_df['season'] = day_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})
day_df['weekday'] = day_df['weekday'].map({
    0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'
})
day_df['weather_cond'] = day_df['weather_cond'].map({
    1: 'Clear/Partly Cloudy',
    2: 'Misty/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Severe Weather'
})

def create_daily_rent_df(df):
    daily_rent_df = df.groupby(by='dateday').agg({
        'count': 'sum'
    }).reset_index()
    return daily_rent_df

def create_daily_casual_rent_df(df):
    daily_casual_rent_df = df.groupby(by='dateday').agg({
        'casual': 'sum'
    }).reset_index()
    return daily_casual_rent_df

def create_daily_registered_rent_df(df):
    daily_registered_rent_df = df.groupby(by='dateday').agg({
        'registered': 'sum'
    }).reset_index()
    return daily_registered_rent_df
    
def create_season_rent_df(df):
    season_rent_df = df.groupby(by='season')[['registered', 'casual']].sum().reset_index()
    return season_rent_df

def create_monthly_rent_df(df):
    monthly_rent_df = df.groupby(by='month').agg({
        'count': 'sum'
    })
    ordered_months = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]
    monthly_rent_df = monthly_rent_df.reindex(ordered_months, fill_value=0)
    return monthly_rent_df

# Menyiapkan weekday_rent_df
def create_weekday_rent_df(df):
    weekday_rent_df = df.groupby(by='weekday').agg({
        'count': 'sum'
    }).reset_index()
    return weekday_rent_df

# Menyiapkan workingday_rent_df
def create_workingday_rent_df(df):
    workingday_rent_df = df.groupby(by='workingday').agg({
        'count': 'sum'
    }).reset_index()
    return workingday_rent_df

# Menyiapkan holiday_rent_df
def create_holiday_rent_df(df):
    holiday_rent_df = df.groupby(by='holiday').agg({
        'count': 'sum'
    }).reset_index()
    return holiday_rent_df

# Menyiapkan weather_rent_df
def create_weather_rent_df(df):
    weather_rent_df = df.groupby(by='weather_cond').agg({
        'count': 'sum'
    })
    return weather_rent_df
  
# Membuat filter
min_date = pd.to_datetime(day_df['dateday']).dt.date.min()
max_date = pd.to_datetime(day_df['dateday']).dt.date.max()

# Mengambil start_date & end_date
start_date, end_date = st.date_input(
    label='Rentang Waktu',
    min_value= min_date,
    max_value= max_date,
    value=[min_date, max_date]
)

main_df = day_df[(day_df['dateday'] >= str(start_date)) & 
                (day_df['dateday'] <= str(end_date))]

st.divider()

# Menyiapkan database
daily_rent_df = create_daily_rent_df(main_df)
daily_casual_rent_df = create_daily_casual_rent_df(main_df)
daily_registered_rent_df = create_daily_registered_rent_df(main_df)
season_rent_df = create_season_rent_df(main_df)
monthly_rent_df = create_monthly_rent_df(main_df)
weekday_rent_df = create_weekday_rent_df(main_df)
workingday_rent_df = create_workingday_rent_df(main_df)
holiday_rent_df = create_holiday_rent_df(main_df)
weather_rent_df = create_weather_rent_df(main_df)  

# Membuat Dashboard

# Membuat judul
st.title('BIKE SHARING DASHBOARD')

# Membuat jumlah penyewaan sepeda harian
st.markdown("---")
st.header('1. Daily Rentals')

col1, col2, col3 = st.columns(3)

with col1:
    daily_rent_casual = daily_casual_rent_df['casual'].sum()
    st.metric('Casual User', value= daily_rent_casual)

with col2:
    daily_rent_registered = daily_registered_rent_df['registered'].sum()
    st.metric('Registered User', value= daily_rent_registered)
 
with col3:
    daily_rent_total = daily_rent_df['count'].sum()
    st.metric('Total User', value= daily_rent_total)

# jumlah penyewaan sepeda bulanan
st.markdown("---")
st.header('2. Monthly Rentals')

fig, ax = plt.subplots(figsize=(24, 8))
ax.plot(
    monthly_rent_df.index,
    monthly_rent_df['count'],
    marker='o', 
    linewidth=2,
    color='tab:orange'
)

for index, row in enumerate(monthly_rent_df['count']):
    ax.text(index, row + 1, str(row), ha='center', va='bottom', fontsize=16)

ax.set_xlabel('Month', fontsize=20)
ax.set_ylabel('Rent', fontsize=20)
ax.tick_params(axis='x', labelsize=16, rotation=45)
ax.tick_params(axis='y', labelsize=16)
st.pyplot(fig)
st.divider()

#  jumlah penyewaan berdasarkan musiman
st.header('3. Seasonly Rentals')

fig, ax = plt.subplots(figsize=(14, 8))

sns.barplot(
    x='season',
    y='registered',
    data=season_rent_df,
    label='Registered',
    color='tab:red',
    ax=ax
)

sns.barplot(
    x='season',
    y='casual',
    data=season_rent_df,
    label='Casual',
    color='tab:orange',
    ax=ax
)

for index, row in season_rent_df.iterrows():
    ax.text(index, row['registered'], str(row['registered']), ha='center', va='bottom', fontsize=16)
    ax.text(index, row['casual'], str(row['casual']), ha='center', va='bottom', fontsize=16)

ax.set_xlabel('Season', fontsize=20)
ax.set_ylabel('Rent', fontsize=20)
ax.tick_params(axis='x', labelsize=16, rotation=0)
ax.tick_params(axis='y', labelsize=16)
ax.legend()
st.pyplot(fig)
st.divider()

# Penyewaan berdasarkan kondisi cuaca
st.header('4. Weatherly Rentals')

fig, ax = plt.subplots(figsize=(14, 8))

colors=["tab:orange", "tab:red", "tab:green"]

sns.barplot(
    x=weather_rent_df.index,
    y=weather_rent_df['count'],
    palette=colors,
    ax=ax
)

for index, row in enumerate(weather_rent_df['count']):
    ax.text(index, row + 1, str(row), ha='center', va='bottom', fontsize=12)

ax.set_xlabel('Weather', fontsize=20)
ax.set_ylabel('Rent', fontsize=20)
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)
st.pyplot(fig)

# Jumlah penyewaan berdasarkan weekday, workingday, and holiday rentals

st.markdown("---")
st.header('5. Weekday, Workingday, and Holiday Rentals by Season')

# Plotting the data
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(15, 22))

colors1 = ["tab:orange", "tab:red", "tab:green", "tab:purple"]
colors2 = ["tab:orange", "tab:red"]
colors3 = ["tab:red", "tab:pink", "tab:blue", "tab:green", "tab:purple", "tab:brown", "tab:orange"]

# Working Day by Season
f, ax = plt.subplots(figsize=(8, 12))
sns.despine(f)
sns.barplot(
    x='season',
    y='count',
    hue='workingday',
    data=workingday_season_df,
    palette=colors1,
    ax=axes[0]
)

for index, row in workingday_season_df.iterrows():
    axes[0].text(index, row['count'] + 1, str(row['count']), ha='center', va='bottom', fontsize=12)

axes[0].set_title('Working Day Rentals by Season')
axes[0].axhline(y=axes[0].get_ylim()[1] + 0.1, xmin=0, xmax=1, color='black', linewidth=2)
axes[0].set_ylabel(None)
axes[0].tick_params(axis='x', labelsize=16)
axes[0].tick_params(axis='y', labelsize=16)
axes[0].legend(loc='upper left')

st.caption('Rifki Muhammad 2024')