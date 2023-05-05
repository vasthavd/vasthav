# -*- coding: utf-8 -*-
"""
Created on Thu May  4 14:45:35 2023

@author: vasth
"""

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


# Import the pandas library as pd
import pandas as pd

# Read 'police.csv' into a DataFrame named rhode_island
ri = pd.read_csv('ri.csv')

# Examine the head of the DataFrame
print(ri.head())

# Count the number of missing values in each column
print(ri.isnull().sum())

# Examine the shape of the DataFrame
print(ri.shape)

# Drop the 'county_name' and 'state' columns
ri.drop(['raw_row_number', 'department_id', 'type', 'vehicle_make',
         'vehicle_model', 'raw_BasisForStop', 'raw_OperatorRace', 
         'raw_OperatorSex', 'raw_SearchResultOne', 'raw_ResultOfStop',
         'raw_SearchResultTwo', 'raw_SearchResultThree' ], 
        axis='columns', inplace=True)

# Count the number of missing values in each column
print(ri.isnull().sum())

# Examine the shape of the DataFrame (again)
print(ri.head())

# Examine the head of the 'arrest_made' column
print(ri.arrest_made.head())

# Change the data type of 'arrest_made' to 'bool'
ri['arrest_made'] = ri.arrest_made.astype('bool')



# Check the data type of 'arrest_made' 
print(ri.arrest_made.head())

# Concatenate 'stop_date' and 'stop_time' (separated by a space)
combined = ri.date.str.cat(ri.time, sep = ' ')

# Convert 'combined' to datetime format
ri['stop_datetime'] = pd.to_datetime(combined)

# Examine the data types of the DataFrame
print(ri.dtypes)

# Set 'stop_datetime' as the index
ri.set_index('stop_datetime', inplace=True)

# Examine the index
print(ri.index)

# Examine the columns
print(ri.columns)

# Count the unique values in 'violation'
print(ri.reason_for_stop.value_counts())

# Express the counts as proportions
print(ri.reason_for_stop.value_counts(normalize=True))

# Create a DataFrame of female drivers
female = ri[ri['subject_sex'] == 'female']

# Create a DataFrame of male drivers
male = ri[ri['subject_sex'] == 'male']

# Compute the violations by female drivers (as proportions)
print(female.reason_for_stop.value_counts(normalize=True))

# Compute the violations by male drivers (as proportions)
print(male.reason_for_stop.value_counts(normalize=True))

# Create a DataFrame of female drivers stopped for speeding
female_and_speeding = ri[(ri.subject_sex == 'female') & (ri.reason_for_stop == 'Speeding')]

# Create a DataFrame of male drivers stopped for speeding
male_and_speeding = ri[(ri.subject_sex == 'male') & (ri.reason_for_stop == 'Speeding')]

# Compute the stop outcomes for female drivers (as proportions)
print(female_and_speeding.outcome.value_counts(normalize = True))

# Compute the stop outcomes for male drivers (as proportions)
print(male_and_speeding.outcome.value_counts(normalize = True))

# Check the data type of 'search_conducted'
print(ri.search_conducted.dtypes)

# Calculate the search rate by counting the values
print(ri.search_conducted.value_counts(normalize = True))

# Calculate the search rate by taking the mean
print(ri.search_conducted.mean())

# Calculate the search rate for both groups simultaneously
print(ri.groupby('subject_sex').search_conducted.mean())

# Calculate the search rate for each combination of gender and violation
print(ri.groupby(['reason_for_stop', 'subject_sex']).search_conducted.mean() * 100)


# Count the 'search_type' values
print(ri.reason_for_search.value_counts())

# Check if 'search_type' contains the string 'Protective Frisk'
ri['frisk'] = ri.reason_for_search.str.contains('Protective Frisk', na=False)

# Check the data type of 'frisk'
#print(ri.frisk.dtypes)

# Take the sum of 'frisk'
print(ri.frisk.sum())

# Create a DataFrame of stops in which a search was conducted
searched = ri[ri.search_conducted == True]

# Calculate the overall frisk rate by taking the mean of 'frisk'
#print(searched.frisk.mean())

# Calculate the frisk rate for each gender
#print(searched.groupby('subject_sex').frisk.mean())

# Calculate the overall arrest rate
print(ri.arrest_made.mean())

# Calculate the hourly arrest rate
print(ri.groupby(ri.index.hour).arrest_made.mean())

# Save the hourly arrest rate
hourly_arrest_rate = ri.groupby(ri.index.hour).arrest_made.mean()


# Create a line plot of 'hourly_arrest_rate'
#plt.plot(hourly_arrest_rate)

# Add the xlabel, ylabel, and title
#plt.xlabel('Hour')
#plt.ylabel('Arrest Rate')
#plt.title('Arrest Rate by Time of Day')

# Display the plot
#plt.show()

# Calculate the annual rate of drug-related stops
print(ri.contraband_drugs.resample('A').mean())

# Save the annual rate of drug-related stops
annual_drug_rate = ri.contraband_drugs.resample('A').mean()

# Create a line plot of 'annual_drug_rate'
#annual_drug_rate.plot()


# Display the plot
#plt.show()


# Calculate and save the annual search rate
annual_search_rate = ri.search_conducted.resample('A').mean()

# Concatenate 'annual_drug_rate' and 'annual_search_rate'
annual = pd.concat([annual_drug_rate, annual_search_rate], axis='columns')

# Create subplots from 'annual'
#annual.plot(subplots=True)

# Display the subplots
#plt.show()

# Create a frequency table of districts and violations
print(pd.crosstab(ri.zone, ri.reason_for_stop))

# Save the frequency table as 'all_zones'
all_zones = pd.crosstab(ri.zone, ri.reason_for_stop)

# Select rows 'Zone K1' through 'Zone K3'
print(all_zones.loc['K1' : 'K3'])

# Save the smaller table as 'k_zones'
k_zones = all_zones.loc['K1' : 'K3']

# Create a bar plot of 'k_zones'
#k_zones.plot(kind = 'bar')

# Move the# legend outside the plot using bbox_to_anchor
#plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3)

# Display the plot
#plt.show()


# Import seaborn module
import seaborn as sns
from matplotlib.gridspec import GridSpec


# Create subplots with 2 rows and 2 columns
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(10, 10))

grid = GridSpec(3, 3, wspace=0.4, hspace=0.3)

# Add heading line
fig.suptitle("Analyzing Law Enforcement Trends in Rhode Island", fontsize=24, fontweight='bold', color='#4C72B0', y=0.99)

# Calculate the hourly arrest rate
hourly_arrest_rate = ri.groupby(ri.index.hour).arrest_made.mean() * 100

# Create a line plot of 'hourly_arrest_rate'
sns.lineplot(x=hourly_arrest_rate.index, y=hourly_arrest_rate.values, ax=axes[0, 0])
axes[0, 0].set_xlabel('Hour (24-Format)', fontsize=12, fontweight='bold', fontstyle='italic', fontfamily='serif')
axes[0, 0].set_ylabel('Arrest Rate', fontsize=12, fontweight='bold', fontstyle='italic', fontfamily='serif')
axes[0, 0].set_title('Arrest Rate by Time', fontsize=14, fontweight='bold', fontstyle='italic', fontfamily='serif')
axes[0, 0].tick_params(axis='both', which='major', labelsize=10)


# Calculate the annual rate of drug-related stops
annual_drug_rate = ri.contraband_drugs.resample('A').mean() * 100

# Create a line plot of 'annual_drug_rate'
sns.lineplot(x=annual_drug_rate.index, y=annual_drug_rate.values, ax=axes[0, 1])
axes[0, 1].set_xlabel('Year', fontsize=12, fontweight='bold', fontstyle='italic', fontfamily='serif')
axes[0, 1].set_ylabel('Drug-Related Stop Rate', fontsize=12, fontweight='bold', fontstyle='italic', fontfamily='serif')
axes[0, 1].set_title('Annual Drug-Related Stop Rate', fontsize=14, fontweight='bold', fontstyle='italic', fontfamily='serif')
axes[0, 1].set_xticks(annual_search_rate.index)
axes[0, 1].set_xticklabels(annual_drug_rate.index.strftime('%Y'), rotation=45, ha='right', fontsize=10)
axes[0, 1].tick_params(axis='both', which='major', labelsize=10)

# Calculate and save the annual search rate
annual_search_rate = ri.search_conducted.resample('A').mean() * 100

# Create a line plot of 'annual_search_rate'
sns.lineplot(x=annual_search_rate.index, y=annual_search_rate.values, ax=axes[0, 2])
axes[0, 2].set_xlabel('Year', fontsize=12, fontweight='bold', fontstyle='italic', fontfamily='serif')
axes[0, 2].set_ylabel('Search Rate', fontsize=12, fontweight='bold', fontstyle='italic', fontfamily='serif')
axes[0, 2].set_title('Annual Search Rate', fontsize=14, fontweight='bold', fontstyle='italic', fontfamily='serif')
axes[0, 2].set_xticks(annual_search_rate.index)
axes[0, 2].set_xticklabels(annual_search_rate.index.strftime('%Y'), rotation=45, ha='right', fontsize=10)
axes[0, 2].tick_params(axis='both', which='major', labelsize=10)


# Create a count plot of the reason for the stop
sns.countplot(x='zone', data=ri, ax=axes[1, 0])
axes[1, 0].set_xlabel('District Zones', fontsize=12, fontweight='bold', fontstyle='italic', fontfamily='serif')
axes[1, 0].set_ylabel('Count', fontsize=12, fontweight='bold', fontstyle='italic', fontfamily='serif')
axes[1, 0].set_title('Count of Stops by Zone', fontsize=14, fontweight='bold', fontstyle='italic', fontfamily='serif')
axes[1, 0].tick_params(axis='both', which='major', labelsize=10)


# Create a pie plot of male and female arrest rates
arrest_rate_by_gender = ri.groupby('subject_sex').arrest_made.mean()
labels = ['Female', 'Male'] # custom labels
axes[1, 1].pie(arrest_rate_by_gender, labels=labels, autopct='%1.1f%%')
#axes[1, 1].set_title('Arrest Rate by Gender')
axes[1, 1].text(0.5, -0.2, "Arrest Rate by Gender", transform=axes[1, 1].transAxes, fontfamily='serif', fontsize=12, ha='center', font={'weight': 'bold', 'style': 'italic'})


# Create a pie plot of male and female search rates
search_rate_by_gender = ri.groupby('subject_sex').search_conducted.mean()
axes[1, 2].pie(search_rate_by_gender, labels=labels, autopct='%1.1f%%')
#axes[1, 2].set_title('Search Rate by Gender')
axes[1, 2].text(0.5, -0.2, "Search Rate by Gender", transform=axes[1, 2].transAxes, fontsize=12, fontfamily='serif', ha='center', font={'weight': 'bold', 'style': 'italic'})

"""
# create the plot in the bottom row
ax7 = fig.add_subplot(grid[2:, :])

# add the text box in the bottom right corner
text_box = ax7.text(0.95, 0.05, "Text Box", verticalalignment='bottom', horizontalalignment='right',
                    transform=ax7.transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.5, edgecolor='gray', boxstyle='round'))

# remove the tick labels and x-axis label from the bottom row
ax7.tick_params(axis='both', which='both', bottom=False, left=False, labelbottom=False, labelleft=False)
ax7.set_xlabel('')
ax7.axis('on')
"""
# Add the image to the last two rows of the grid
#a = Image.open(requests.get("http://matplotlib.sourceforge.net/_static/logo2.png", stream=True).raw)
ax_image = plt.subplot(grid[2:, :])
#ax_image.imshow(a)
# add the text box in the bottom right corner
# Add a text box to the plot
textr = "A study of law enforcement data in Rhode Island found \nthat men are searched more than twice as often as \nwomen during a stop, and that the number of vehicle \nstops due to drug-related suspicions has been on the rise \nsince 2008. The study also found that most arrests during \na stop happen between 8 PM and 6 AM, and \nthat gender does not have a significant impact on the likelihood \nof being arrested. Overall, the study suggests that there are \nsignificant disparities in law enforcement practices in Rhode Island, \nparticularly with respect to gender and drug-related suspicions. \n Submitted By: Vasthav Dandumenu-22032815."
text_box = ax_image.text(0.5, 0.5, textr, verticalalignment='center', horizontalalignment='center', fontsize=12, fontfamily='serif', bbox=dict(facecolor='white', alpha=0.5, edgecolor='gray', boxstyle='square,pad=0.5'), transform=ax_image.transAxes)
text_box.set_fontstyle('italic')
text_box.set_fontweight('bold')


# Remove tick labels and axis labels for the image subplot
ax_image.set_xticks([])
ax_image.set_yticks([])
ax_image.spines['top'].set_visible(False)
ax_image.spines['right'].set_visible(False)
ax_image.spines['bottom'].set_visible(False)
ax_image.spines['left'].set_visible(False)

# Create border line
for axes in axes.flat:
    axes.spines['top'].set_visible(False)
    axes.spines['right'].set_visible(False)
    axes.spines['bottom'].set_linewidth(2)
    axes.spines['left'].set_linewidth(2)
    
fig.subplots_adjust(hspace=0.4, wspace=0.3, left=0.1, right=0.9, top=0.9, bottom=0.1)

# add the border line to the figure
fig.add_artist(plt.Rectangle((0, 0), 1, 1, fill=False, edgecolor='black', linewidth=3))

# Add a text box to the plot
#axes[2, 0].text(0.5, 0.5, ' plot.', ha='left', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=1'))




# Adjust the spacing between the subplots
plt.tight_layout()

plt.savefig('22032815.png', dpi=500)

# Display the plot
plt.show()


