import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# File paths
DATA_FILE = "data/sample_lfg_monitoring_data.csv"
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

# Load data
df = pd.read_csv(DATA_FILE)

# --- Alert Logic ---
def classify_alert(row):
    if row["oxygen_percent"] > 5:
        return "High O₂ - Possible air intrusion"
    elif row["methane_percent"] < 40:
        return "Low CH₄ - Reduced gas quality"
    elif row["flow_scfm"] < 20:
        return "Low flow - Check well"
    elif row["vacuum_inches_wc"] > -3:
        return "Weak vacuum"
    elif row["condensate_issue"] in ["Yes", "Possible"]:
        return "Condensate follow-up needed"
    else:
        return "Normal"

def health_score(row):
    score = 100

    if row["oxygen_percent"] > 5:
        score -= 25
    if row["methane_percent"] < 40:
        score -= 25
    if row["flow_scfm"] < 20:
        score -= 20
    if row["vacuum_inches_wc"] > -3:
        score -= 15
    if row["condensate_issue"] == "Yes":
        score -= 10
    elif row["condensate_issue"] == "Possible":
        score -= 5

    return max(score, 0)

df["alert"] = df.apply(classify_alert, axis=1)
df["health_score"] = df.apply(health_score, axis=1)

# Save summary report
df.to_csv("outputs/wellfield_analysis_output.csv", index=False)

# --- Chart 1: Methane by Well ---
plt.figure(figsize=(8, 5))
plt.bar(df["well_id"], df["methane_percent"])
plt.title("Methane Concentration by Well")
plt.xlabel("Well ID")
plt.ylabel("Methane (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/methane_by_well.png")
plt.close()

# --- Chart 2: Oxygen by Well ---
plt.figure(figsize=(8, 5))
plt.bar(df["well_id"], df["oxygen_percent"])
plt.title("Oxygen Concentration by Well")
plt.xlabel("Well ID")
plt.ylabel("Oxygen (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/oxygen_by_well.png")
plt.close()

# --- Chart 3: Health Score by Well ---
plt.figure(figsize=(8, 5))
plt.bar(df["well_id"], df["health_score"])
plt.title("Well Health Score by Well")
plt.xlabel("Well ID")
plt.ylabel("Health Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/well_health_score.png")
plt.close()

print("Analysis complete. Charts saved to outputs folder.")
