################################################################################
#establish DB connection to SQL Server
import pyodbc
import os
# Establish the connection to MS SQL Server
ctx = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'\
         'SERVER=SERVERNAME;'\
         'DATABASE=DATABASENAME;'\
         'Authentication=ActiveDirectoryInteractive;'\
         'Uid=user@user.com.au;') 
row = ctx.cursor().execute('SELECT @@VERSION').fetchone()
print(f'Connected. Version of SQL Server: {row}')

################################################################################

#NOTE: Use these functions in Anaconda Prompt - the upgrade functions require admin access
#upgrade pip
python.exe -m pip install --upgrade pip --trusted-host pypi.org --trusted-host files.pythonhosted.org
#install packages
pip install pandasql --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host github.com
#upgrade packages to a specific version
pip3 install --user --upgrade pandas==0.25.3 --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host github.com
#reverting pandas to a specific version
pip3 install pandas==0.25.3 --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host github.com
#upgrade cython
pip3 install --user --upgrade cython --trusted-host pypi.org --trusted-host files.pythonhosted.org --trusted-host github.com

################################################################################

#Checking pandas version
import pandas as pd
pd.__version__

################################################################################

#Using SQL in pandas
from pandasql import *
pysqldf = lambda q: sqldf(q, globals())
q = """
SELECT 
ID_Number

FROM df
where Insurer = 'A'
limit 10
"""
df = pysqldf(q)
display(df)

################################################################################

#check datatypes
df_sit.dtypes

################################################################################

#count of rows
df_sit.count()

################################################################################

#Finding out which IDs are not in the other DF
df = df_sit[~df_sit['ID_Number'].isin(df2['ID_Number'])]
display(df)

################################################################################

#Individual column totals
Total = df['Payment'].sum()
print(Total)

################################################################################

#Joining 2 dataframes together - this is the same as a join in SQL
df_combined = pd.merge(df_sit, df2, how='inner', left_on=['ID_Number'], right_on=['ID_Number'], indicator=True)
display(df_combined)

################################################################################

#Comparing differences

import numpy as np
#Compare amounts
df_combined['Match?'] = (df_combined.ColumnA == df_combined.ColumnC)
#select only ones that don't match
df_amount = df_combined.loc[df_combined['Match?'] == False]    

display(df_amount)

################################################################################

#Select specific columns
header = df2.loc[:, ["ID","ColumnA"]]
#Exporting results to CSV file with specific columns only
df2.to_csv(r'S:/User/Lisa/Missing.csv', columns = header, index = False)

