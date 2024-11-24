# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "simulated_employee_lifecycle.csv"  
data = pd.read_csv(file_path)

# 1. Overview of the Data
print("First few rows of the dataset:")
print(data.head())

print("\nSummary statistics:")
print(data.describe())

print("\nMissing values in each column:")
print(data.isnull().sum())

# 2. Attrition Analysis
# Overall attrition rate
attrition_rate = data['Attrition'].value_counts(normalize=True) * 100
print("\nOverall Attrition Rate:")
print(attrition_rate)

# Attrition by Department
attrition_by_department = data.groupby('Department')['Attrition'].value_counts(normalize=True).unstack() * 100
print("\nAttrition Rate by Department:")
print(attrition_by_department)

# Visualization: Attrition by Department
attrition_by_department.plot(kind='bar', stacked=True, figsize=(10, 6), color=['skyblue', 'orange'])
plt.title('Attrition Rate by Department', fontsize=16)
plt.ylabel('Percentage', fontsize=12)
plt.xlabel('Department', fontsize=12)
plt.legend(title="Attrition", labels=['No', 'Yes'], fontsize=10)
plt.tight_layout()
plt.show()

# 3. Satisfaction Level vs Attrition
# Average Satisfaction Level by Attrition
satisfaction_by_attrition = data.groupby('Attrition')['SatisfactionLevel'].mean()
print("\nAverage Satisfaction Level by Attrition:")
print(satisfaction_by_attrition)

# Visualization: Satisfaction Level Distribution by Attrition
plt.figure(figsize=(10, 6))
sns.boxplot(x='Attrition', y='SatisfactionLevel', data=data, palette='pastel')
plt.title('Satisfaction Level vs Attrition', fontsize=16)
plt.xlabel('Attrition', fontsize=12)
plt.ylabel('Satisfaction Level', fontsize=12)
plt.tight_layout()
plt.show()

# 4. Impact of Age on Attrition
# Visualization: Age Distribution by Attrition
plt.figure(figsize=(10, 6))
sns.boxplot(x='Attrition', y='Age', data=data, palette='pastel')
plt.title('Impact of Age on Attrition', fontsize=16)
plt.xlabel('Attrition', fontsize=12)
plt.ylabel('Age', fontsize=12)
plt.tight_layout()
plt.show()

# 5. Years at Company vs Attrition
# Average Years at Company by Attrition
years_at_company_by_attrition = data.groupby('Attrition')['YearsAtCompany'].mean()
print("\nAverage Years at Company by Attrition:")
print(years_at_company_by_attrition)

# Visualization: Years at Company by Attrition
plt.figure(figsize=(10, 6))
sns.boxplot(x='Attrition', y='YearsAtCompany', data=data, palette='pastel')
plt.title('Years at Company vs Attrition', fontsize=16)
plt.xlabel('Attrition', fontsize=12)
plt.ylabel('Years at Company', fontsize=12)
plt.tight_layout()
plt.show()

# 6. Attrition by Job Role
# Attrition Rate by Job Role
attrition_by_job_role = data.groupby('JobRole')['Attrition'].value_counts(normalize=True).unstack() * 100
print("\nAttrition Rate by Job Role:")
print(attrition_by_job_role)

# Visualization: Attrition Rate by Job Role
attrition_by_job_role.plot(kind='bar', stacked=True, figsize=(12, 6), color=['skyblue', 'orange'])
plt.title('Attrition Rate by Job Role', fontsize=16)
plt.ylabel('Percentage', fontsize=12)
plt.xlabel('Job Role', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend(title="Attrition", labels=['No', 'Yes'], fontsize=10)
plt.tight_layout()
plt.show()



# Correlation analysis: Select relevant numeric columns
correlation_columns = ['SatisfactionLevel', 'YearsAtCompany', 'WorkLifeBalance', 'PerformanceScore', 'Age']
correlation_matrix = data[correlation_columns].corr()

print("Correlation Matrix:")
print(correlation_matrix)

# Visualization: Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap: Factors Impacting Satisfaction', fontsize=16)
plt.tight_layout()
plt.show()

# Visualization: Satisfaction level vs Work-Life Balance
plt.figure(figsize=(10, 6))
sns.boxplot(x='WorkLifeBalance', y='SatisfactionLevel', data=data, palette='pastel')
plt.title('Satisfaction Level vs Work-Life Balance', fontsize=16)
plt.xlabel('Work-Life Balance', fontsize=12)
plt.ylabel('Satisfaction Level', fontsize=12)
plt.tight_layout()
plt.show()

# Visualization: Satisfaction level vs Performance Score
plt.figure(figsize=(10, 6))
sns.boxplot(x='PerformanceScore', y='SatisfactionLevel', data=data, palette='pastel')
plt.title('Satisfaction Level vs Performance Score', fontsize=16)
plt.xlabel('Performance Score', fontsize=12)
plt.ylabel('Satisfaction Level', fontsize=12)
plt.tight_layout()
plt.show()

# Visualization: Satisfaction level vs Years at Company
plt.figure(figsize=(10, 6))
sns.scatterplot(x='YearsAtCompany', y='SatisfactionLevel', data=data, alpha=0.6)
plt.title('Satisfaction Level vs Years at Company', fontsize=16)
plt.xlabel('Years at Company', fontsize=12)
plt.ylabel('Satisfaction Level', fontsize=12)
plt.tight_layout()
plt.show()

data.columns = data.columns.str.strip()  # Remove spaces around column names
print(data.columns)  # Confirm column names are correctly formatted




#############
# 1. Pairplot: Relationship between satisfaction and other numerical factors
sns.pairplot(data, vars=['SatisfactionLevel', 'YearsAtCompany', 'Age', 'PerformanceScore', 'WorkLifeBalance'],
             hue='Attrition', palette='coolwarm', diag_kind='kde', markers=["o", "s"])
plt.suptitle('Pairplot: Satisfaction and Related Factors', y=1.02, fontsize=16)
plt.show()

# 2. Satisfaction vs Department with Attrition split
plt.figure(figsize=(12, 6))
sns.boxplot(x='Department', y='SatisfactionLevel', hue='Attrition', data=data, palette='coolwarm')
plt.title('Satisfaction Level vs Department (Attrition Split)', fontsize=16)
plt.xlabel('Department', fontsize=12)
plt.ylabel('Satisfaction Level', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Attrition', fontsize=10)
plt.tight_layout()
plt.show()

# 3. Satisfaction vs Age with Attrition split
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='SatisfactionLevel', hue='Attrition', data=data, alpha=0.6, palette='coolwarm')
plt.title('Satisfaction Level vs Age (Attrition Split)', fontsize=16)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Satisfaction Level', fontsize=12)
plt.legend(title='Attrition', fontsize=10)
plt.tight_layout()
plt.show()

# 4. Satisfaction Heatmap by Performance and WorkLifeBalance
pivot_table = data.pivot_table(index='PerformanceScore', columns='WorkLifeBalance', values='SatisfactionLevel', aggfunc='mean')
plt.figure(figsize=(8, 6))
sns.heatmap(pivot_table, annot=True, cmap='viridis', fmt=".2f", linewidths=0.5)
plt.title('Heatmap: Satisfaction by Performance and WorkLifeBalance', fontsize=16)
plt.xlabel('Work-Life Balance', fontsize=12)
plt.ylabel('Performance Score', fontsize=12)
plt.tight_layout()
plt.show()





