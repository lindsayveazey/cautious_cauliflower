import pandas
import numpy

data = pandas.read_csv('/home/lindsay/Downloads/softwareInventory.csv', encoding='latin1')
data.head(10)
data.columns

data.columns = ['ID', 'Device', 'Matched', 'Installation', 'Pathway', 'Application', 'Version']

# We don't need the 'Unnamed: 1' column (renamed 'Matched') that contains "matched" in every row- drop it:
data = data.drop(['Matched'], axis=1)
data.columns

# Identify missing data
empty = data.apply(lambda col: pandas.isnull(col))
empty.head(10)

#       ID  Device  Installation  Pathway  Application  Version
# 0   True    True          True     True         True     True
# 1  False   False         False     True        False    False
# 2   True    True          True     True         True     True

# Above, we see that the empty rows inherently encoded in the CSV are boolean True for pandas.isnull
# Let's drop all rows where Application is marked True- we know these are empty rows

data = data.dropna(subset=['Application'])

# Make a list of applications, then coerce to list of unique values
app_list = data['Application'].values
unique_app_list = numpy.unique(app_list)
# Oh...there are 844 elements here...best to bin by string occurrences by software

# Microsoft: 'Microsoft' 'Win', 'Windows' 'Visual Studio' 'vs_' 'VS' 'Office' 'SQL' 'sql'
# Oracle: 'Adobe' 'Java'
# Apple: 'Apple'
# Autodesk: 'Autodesk'
# CheckPoint: 'Check Point'
# Dell: 'Dell'
# Intel: 'Intel'
# Other

data['Software'] = numpy.where(data.Application.str.contains("Microsoft"), "Microsoft",
                   numpy.where(data.Application.str.contains("Win"), "Microsoft",
                   numpy.where(data.Application.str.contains("Windows"), "Microsoft",
                   numpy.where(data.Application.str.contains("Visual Studio"), "Microsoft",
                   numpy.where(data.Application.str.contains("vs_"), "Microsoft",
                   numpy.where(data.Application.str.contains("VS"), "Microsoft",
                   numpy.where(data.Application.str.contains("Office"), "Microsoft",
                   numpy.where(data.Application.str.contains("SQL"), "Microsoft",
                   numpy.where(data.Application.str.contains("sql"), "Microsoft",
                   numpy.where(data.Application.str.contains("Adobe"), "Oracle",
                   numpy.where(data.Application.str.contains("Java"), "Oracle",
                   numpy.where(data.Application.str.contains("Apple"), "Apple",
                   numpy.where(data.Application.str.contains("Autodesk"), "Autodesk",
                   numpy.where(data.Application.str.contains("Check Point"), "CheckPoint",
                   numpy.where(data.Application.str.contains("Dell"), "Dell",
                   numpy.where(data.Application.str.contains("Intel"), "Intel", "Other"))))))))))))))))

software_list = data['Software'].values
unique_software_list = numpy.unique(software_list, return_counts = True) # Looks reasonable

# Create a pie chart