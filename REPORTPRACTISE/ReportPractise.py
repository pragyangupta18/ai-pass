#pip3 install pandas-profiling
#pip3 isntall pandas
#pip3 install ydata_profiling
import pandas as pd
df = pd.read_csv('housing.csv')
print(df)

from pandas_profiling import ProfileReport

# Generate a report
profile = ProfileReport(df)
#profile = ProfileReport(df,minimal=True)
profile.to_file(output_file="housing.html")
# to_file(self, output_file, silent)


