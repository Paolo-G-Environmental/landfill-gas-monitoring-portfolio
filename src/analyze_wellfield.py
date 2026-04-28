def health_score(row):
    score = 100

    # Air intrusion risk
    if row["oxygen_percent"] > 5:
        score -= 25

    # Poor methane quality
    if row["methane_percent"] < 40:
        score -= 25

    # Low flow
    if row["flow_scfm"] < 20:
        score -= 20

    # Weak vacuum (less negative = weaker)
    if row["vacuum_inches_wc"] > -3:
        score -= 15

    # Condensate issues
    if row["condensate_issue"] == "Yes":
        score -= 10
    elif row["condensate_issue"] == "Possible":
        score -= 5

    return max(score, 0)

Start = 100

O₂ > 5% → -25   (air intrusion risk)
CH₄ < 40% → -25 (poor gas quality)
Flow < 20 → -20 (possible blockage/inactive well)
Vacuum > -3 → -15 (weak extraction)
Condensate = Yes → -10
Condensate = Possible → -5

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.bar(df["well_id"], df["health_score"])
plt.title("Well Health Score by Well")
plt.xlabel("Well ID")
plt.ylabel("Health Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/well_health_score.png")
plt.close()

