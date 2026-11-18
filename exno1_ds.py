import pandas as pd
import numpy as np

# Create the employee dataset (from the supplied Colab notebook)
emp = {
    "Emp_ID": ["E101", "E102", "E103", "E104", "E105", "E106", "E107", "E108", "E109", "E110"],
    "Name": ["Arjun", "Priya", "Karthik", "Divya", "Rahul", "Sneha", "Vignesh", "Ananya", "Sanjay", "Meena"],
    "Dept": ["IT", "HR", "Finance", "IT", "Marketing", "HR", "Finance", "IT", "Sales", "Marketing"],
    "Age": [25, 28, np.nan, 24, 32, 27, 35, np.nan, 26, 31],
    "Salary": [35000, 42000, 50000, np.nan, 55000, 40000, 65000, 48000, np.nan, 52000],
    "Experience": [2, 4, 6, 1, np.nan, 3, 10, 5, 2, 6],
    "City": ["Chennai", "Bangalore", "Coimbatore", "Chennai", "Mumbai", np.nan, "Salem", "Bangalore", "Chennai", "Trichy"]
}
df = pd.DataFrame(emp)
print("Initial employee dataset:")
print(df)

# Select columns, rows, and individual values
print("\nSalary column:")
print(df["Salary"])
print("\nSelected columns:")
print(df[["Name", "Salary", "Age"]])
print("\nRows from label 2:")
print(df.loc[2:])
print("\nRows from position 2:")
print(df.iloc[2:])
print("\nValue at row 2, column 4:", df.iloc[2, 4])
print("\nRow at position 2:")
print(df.iloc[2])
print("\nValue at row 3, column 2:", df.iloc[3, 2])
print("\nDescending label slice:")
print(df.loc[3:1])

# Check missing values
print("\nMissing-value matrix:")
print(df.isnull())
print("\nMissing values per column:")
print(df.isnull().sum())
print("\nColumns containing missing values:")
print(df.isnull().any())

# Fill missing salary with the mean and missing experience with zero
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Experience"] = df["Experience"].fillna(0)
print("\nMissing values after filling:")
print(df.isnull().sum())

# Demonstrate renaming (the returned DataFrame is displayed, not assigned)
print("\nRenamed-column view:")
print(df.rename(columns={"Salary": "Monthly_Salary"}))

# Create calculated columns
df["Annual_Salary"] = df["Salary"] * 12
df["Bonus"] = df["Salary"] * 0.10
print("\nEmployee data with annual salary and bonus:")
print(df)

# Filter records and group by department
print("\nSalary greater than 5000:")
print(df[df["Salary"] > 5000])
print("\nIT employees with salary greater than 5000:")
print(df[(df["Salary"] > 5000) & (df["Dept"] == "IT")])
print("\nAverage salary by department:")
print(df.groupby("Dept")["Salary"].mean())
print("\nUnique departments:")
print(df["Dept"].unique())
print("\nMaximum salary by department:")
print(df.groupby("Dept")["Salary"].max())
print("\nEmployee count by department:")
print(df["Dept"].value_counts())

# NumPy operations
print("\nMissing Age values:")
print(np.isnan(df["Age"]))
print("\nMean salary:", np.mean(df["Salary"]))
print("Maximum salary:", np.nanmax(df["Salary"]))

# Add bonus, performance, grade, revised salary, and experience in months
df["Bonus"] = np.round(df["Salary"] * 0.10, 3)
df["Performance"] = np.where(df["Salary"] > 50000, "Excellent", "Good")
df["Grade"] = np.select(
    [df["Salary"] >= 60000, df["Salary"] >= 50000, df["Salary"] >= 40000],
    ["A", "B", "C"],
    default="D"
)
df["New Salary"] = np.multiply(df["Salary"], 1.10)
df["Experience Months"] = np.multiply(df["Experience"], 12)

print("\nFinal employee dataset:")
print(df)
