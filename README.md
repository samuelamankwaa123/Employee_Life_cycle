# Employee_Life_cycle
Project Title: Employee Lifecycle Analysis - Attrition and Satisfaction Insights
Project Description:
This project analyzes simulated employee lifecycle data to understand key factors influencing attrition rates and satisfaction levels in an organization. The analysis focuses on visualizing trends, identifying correlations, and deriving actionable insights for better workforce management.

Data Description:
Dataset: simulated_employee_lifecycle.csv
Key Columns:
Attrition: Indicates whether an employee has left the company (Yes or No).
SatisfactionLevel: Employee's satisfaction score (numeric).
Age: Employee's age.
Department: Department where the employee works.
JobRole: Specific job role within the department.
YearsAtCompany: Tenure of the employee at the organization.
WorkLifeBalance: Employee's work-life balance score (scale 1–4).
PerformanceScore: Performance evaluation score (scale 1–5).
Analyses and Visualizations:
Overview of Data:

Displayed first few rows, summary statistics, and missing values for initial exploration.
Attrition Analysis:

Overall attrition rate calculated and displayed.
Attrition rates analyzed by:
Department
Job Role
Visualizations:
Stacked bar charts to display attrition rates by department and job role.
Satisfaction Analysis:

Comparison of average satisfaction levels for employees who left (Yes) vs. stayed (No).
Visualizations:
Boxplots to show satisfaction level distribution by attrition and other factors such as:
Work-Life Balance
Performance Score
Years at Company
Age
Department (split by Attrition)
Impact of Age and Years at Company:

Boxplots to understand the impact of employee age and tenure on attrition rates.
Correlation Analysis:

A heatmap visualizing correlations between satisfaction levels, years at the company, work-life balance, performance scores, and age.
Advanced Visualizations:

Pairplot showing relationships between satisfaction and other numerical factors with attrition as the hue.
Heatmap to show average satisfaction levels based on performance score and work-life balance.
How to Run the Code:
Ensure you have Python installed with the following libraries:

pandas
matplotlib
seaborn
Place the simulated_employee_lifecycle.csv file in the same directory as the script.

Run the script to generate insights and visualizations:

View statistical summaries, missing value checks, and visual insights.
Explore correlations and advanced satisfaction analysis through heatmaps and pairplots.
Key Insights:
Attrition Patterns:
Specific departments and job roles show higher attrition rates.
Younger employees or those with shorter tenures are more likely to leave.
Satisfaction Trends:
Employees with lower satisfaction levels, poor work-life balance, or low performance scores are more likely to leave.
Departments with higher satisfaction rates see lower attrition rates.
Future Improvements:
I will enhance the dataset with more features like salary, commute distance, or management feedback.
Include predictive modeling to forecast attrition and identify at-risk employees.
