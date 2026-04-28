# Landfill Gas Monitoring & Analytics Project

## Overview
This project demonstrates applied environmental science skills in landfill gas monitoring, data interpretation, and operational analysis. It integrates real-world landfill gas concepts with structured data analysis to evaluate wellfield performance, identify system issues, and support informed field decision-making.

The portfolio reflects practical experience aligned with landfill gas operations, environmental compliance, and infrastructure monitoring.

---

## Project Components

### 1. Calibration Procedure
- `docs/gem5000_calibration_sop.md`  

Standard operating procedure outlining the calibration process for a GEM5000 landfill gas analyzer.

---

### 2. Sample Datasets
- `data/sample_lfg_readings.csv`  
- `data/sample_lfg_monitoring_data.csv`  

Simulated landfill gas datasets used to demonstrate monitoring, interpretation, and analytical workflows.

---

### 3. Data Interpretation
- `reports/field_interpretation_summary.md`  

Provides detailed interpretation of:
- Methane (CH₄)
- Carbon dioxide (CO₂)
- Oxygen (O₂)
- Balance gas
- Vacuum pressure and flow conditions  

Focuses on identifying:
- Air intrusion  
- Declining gas quality  
- Inefficient extraction  
- Potential condensate impacts  

---

### 4. Wellfield Analytics Tool
- `src/analyze_wellfield.py`  

Python-based analysis tool that evaluates landfill gas monitoring data and generates:

- Operational alert flags  
- Well health scoring  
- Recommended field actions  

#### Example Conditions Evaluated:
- Oxygen > 5% → Potential air intrusion  
- Methane (CH₄) < 40% → Reduced gas quality  
- Low flow → Possible blockage or inactive well  
- Weak vacuum → Reduced extraction efficiency  
- Condensate issues → Maintenance required  

This component demonstrates the ability to translate raw environmental data into actionable insights.

---

### 5. Field Decsion Log
- `reports/field)decision_log.md`

Demonstrates how landfill gas monitoring data is translated into real-world field decisions and operational adjustments.

## Data Visualization
![Landfill Gas Example](images/landfill_gas_example.png)

This chart illustrates methane concentration trends across selected wells. Higher methane levels generally indicate strong gas production, while lower values may suggest system inefficiencies or potential air intrusion.

---

## Generated Analysis Charts

### Methane Concentration by Well
![Methane by Well](outputs/methane_by_well.png)

### Oxygen Concentration by Well
![Oxygen by Well](outputs/oxygen_by_well.png)

These charts are generated from the Python analysis script and provide a visual evaluation of landfill gas quality, potential air intrusion, and overall wellfield performance.

---

## Why This Project Matters
Effective landfill gas management is critical for:
- Maintaining regulatory compliance  
- Reducing greenhouse gas emissions  
- Optimizing gas collection efficiency  
- Protecting infrastructure systems  

This project demonstrates the ability to bridge **field operations and data-driven analysis**, a key skill in environmental consulting, municipal operations, and infrastructure management roles.

---

## Disclaimer
> This project uses simulated and generalized data for educational and portfolio purposes only. No confidential or site-specific information is included.
