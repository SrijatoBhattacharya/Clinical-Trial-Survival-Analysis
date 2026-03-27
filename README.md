# Clinical Trial Survival Analysis 🧬📊

### Objective
To analyze clinical trial data and calculate the survival probabilities of patient cohorts using the Kaplan-Meier estimator. This pipeline evaluates the efficacy of an experimental treatment (Drug A) against a standard treatment (Drug B).

### The Dataset
The dataset consists of anonymized patient records containing:
* `Patient_ID`: Unique identifier
* `Treatment`: Assigned cohort (Drug A or Drug B)
* `Months_Survived`: Time duration from treatment start to the event or censoring
* `Death_Event`: Binary indicator (1 = Death observed, 0 = Censored/Survived)

### Tech Stack
* **Language:** Python 3
* **Data Wrangling:** Pandas
* **Statistical Modeling:** Lifelines (KaplanMeierFitter)
* **Visualization:** Matplotlib
* **Statistical Testing:** Log-Rank Test for P-value calculation

### Output / Results
*(Note for Srijato: Once you save the README, edit it again and drag-and-drop your `survival_curve.png` right here so the graph actually shows up on the page).*

The resulting survival curves indicate a clear divergence in outcomes, visualizing the comparative duration of survival between the two treatment groups over a 36-month period.
