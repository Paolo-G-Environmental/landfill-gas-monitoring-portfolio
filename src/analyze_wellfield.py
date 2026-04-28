import pandas as pd

# Load data
df = pd.read_csv("data/sample_lfg_monitoring_data.csv")

def classify_alert(row):
  if row["oxygen_percent"] > 5:
    return "High O2 - Possible air leak"
  elif row ["methane_percent"] < 40:
    return "Low CH4 - Poor gas quality"
  elif row["flow_scfm"] < 20:
    return "Lo flow - Check well"
  elif row["vacuum_inches_wc"] > -3:
    return "Low vacuum"
  elif row["con densate_issue"] in ["Yes", "Possible"]:
    return "condensate issue"
  else:
    return "Normal"
  
def health_score(row):
  score = 100
  if row["oxygen_percet"] > 5:
    score -= 25
  if row["methane_percent"] <40:
    score -= 25
  if row["flow_scfm"] < 20:
    score -= 20
  if row["vacuum_inches_wc"] > -3:
    score -= 15 
  return max(score, 0)

df["alert"] = df.apply(classify_alert, axis=1)
df["health_score"] = df.apply(health_score, axis=1)

print(df.head())
