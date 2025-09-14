## 🏗️ Project Architecture (Schematic)

```mermaid
flowchart LR
    A[Data Source: Excel] --> B[Python ETL + Forecasting]
    B --> C[Cleaned Data: CSV files]
    C --> D[Power BI Dashboard]
    D --> E[Embedded Dashboard on Website]

