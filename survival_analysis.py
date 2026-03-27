import pandas as pd
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test  # <-- THE NEW WEAPON
import matplotlib.pyplot as plt

# 1. Load your raw CSV file 
df = pd.read_csv("clinical_trial.csv")

# 2. Split the data into the two cohorts
group_a = df[df['Treatment'] == 'Drug_A']
group_b = df[df['Treatment'] == 'Drug_B']

# 3. RUN THE LOG-RANK TEST (The Statistical Proof)
results = logrank_test(
    group_a['Months_Survived'], group_b['Months_Survived'],
    event_observed_A=group_a['Death_Event'], event_observed_B=group_b['Death_Event']
)

# Print the terminal report
print(f"Log-Rank Test P-value: {results.p_value:.4f}")
if results.p_value < 0.05:
    print("Verdict: The difference in survival is STATISTICALLY SIGNIFICANT.")
else:
    print("Verdict: The difference is NOT statistically significant.")

# 4. Initialize and plot the curves
kmf = KaplanMeierFitter()

kmf.fit(group_a['Months_Survived'], event_observed=group_a['Death_Event'], label='Drug A (Experimental)')
ax = kmf.plot_survival_function() 

kmf.fit(group_b['Months_Survived'], event_observed=group_b['Death_Event'], label='Drug B (Standard)')
kmf.plot_survival_function(ax=ax)

# 5. Print the P-value directly onto the graph
plt.text(2, 0.15, f"Log-Rank p-value: {results.p_value:.4f}", fontsize=11, 
         bbox=dict(facecolor='white', edgecolor='black', alpha=0.8))

# 6. Professional formatting
plt.title("Clinical Trial Survival Analysis: Drug A vs Drug B")
plt.ylabel("Probability of Survival")
plt.xlabel("Months After Treatment")
plt.grid(True, alpha=0.3) 
plt.show()
