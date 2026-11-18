# Exno: 1
## Employee Data Analysis using Pandas and NumPy

# AIM
To create an employee dataset and perform data selection, missing-value handling, filtering, grouping, and numerical calculations using Pandas and NumPy.

# Explanation
Pandas is a Python library used to work with structured data in rows and columns. A DataFrame stores tabular data and supports selecting rows and columns, checking missing values, replacing missing values, filtering records, and grouping data.

NumPy provides numerical functions such as mean, maximum, conditional selection, rounding, and multiplication. In this experiment, an employee dataset containing employee ID, name, department, age, salary, experience, and city is created and analysed.

# Algorithm
STEP 1: Import the Pandas and NumPy libraries.
STEP 2: Create an employee dataset using a Python dictionary and convert it into a Pandas DataFrame.
STEP 3: Select columns, rows, and individual values using column indexing, loc, and iloc.
STEP 4: Identify missing values using isnull(), isnull().sum(), and isnull().any().
STEP 5: Fill missing salary values with the column mean and missing experience values with zero.
STEP 6: Create annual salary and bonus columns and demonstrate filtering of employee records.
STEP 7: Group employee records by department and calculate average salary, maximum salary, and department counts.
STEP 8: Use NumPy functions to check missing age values and calculate salary statistics.
STEP 9: Create performance labels, salary grades, revised salary, and experience in months.
STEP 10: Display the final employee DataFrame.

# Coding and Output

## 1. Dataset creation
The notebook creates a DataFrame with 10 employee records (E101 to E110) and the columns Emp_ID, Name, Dept, Age, Salary, Experience, and City. The initial data includes missing values in Age, Salary, Experience, and City.

## 2. Row and column selection
Operations demonstrated: df[Salary], df[[Name, Salary, Age]], df.loc[2:], df.iloc[2:], df.iloc[2,4], df.iloc[2], df.iloc[3,2], and df.loc[3:1].

Saved notebook outputs: df.iloc[2,4] returns 50000.0; df.iloc[3,2] returns IT; df.loc[3:1] returns an empty DataFrame.

## 3. Missing-value handling
Before filling, the saved notebook output reports Age = 2, Salary = 2, Experience = 1, and City = 1 missing values. Emp_ID, Name, and Dept have no missing values.

Missing Salary values are filled with the mean salary (48375.0). Missing Experience is filled with 0. After these operations, Age still has 2 missing values and City has 1; Salary and Experience have no missing values.

## 4. Rename a column and calculate salary values
The notebook demonstrates renaming Salary to Monthly_Salary, calculating Annual_Salary as Salary multiplied by 12, and calculating Bonus as 10 percent of Salary. The rename result is displayed but not assigned back to df, so later operations continue to use the Salary column.

## 5. Filter and group employee records
The notebook filters records using Salary > 5000 and combines this condition with Dept == IT. It also finds unique departments, average salary, maximum salary, and employee counts by department.

Average salary by department (saved notebook output):

    Finance      57500.000000
    HR           41000.000000
    IT           43791.666667
    Marketing    53500.000000
    Sales        48375.000000

Maximum salary by department (saved notebook output):

    Finance      65000.0
    HR           42000.0
    IT           48375.0
    Marketing    55000.0
    Sales        48375.0

## 6. NumPy operations and derived columns
NumPy operations include checking missing Age values, calculating the mean salary (48375.0), and finding the maximum salary (65000.0).

The final DataFrame includes Bonus (10 percent), Performance (Excellent when Salary > 50000, otherwise Good), Grade (A/B/C/D based on salary thresholds), New Salary (10 percent increase), and Experience Months (Experience multiplied by 12).

# Result
Thus, the employee dataset was created and analysed using Pandas and NumPy. The experiment demonstrated row and column selection, missing-value identification and handling, filtering, department-wise grouping, statistical operations, and the creation of calculated columns such as annual salary, bonus, performance, grade, revised salary, and experience in months.