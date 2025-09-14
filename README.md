## 🏗️ Project Architecture (Schematic)

```mermaid
flowchart LR
    A[📊 Data Source\n(Excel - Online Retail II)] --> B[🐍 Python\nETL + Forecasting (Prophet)]
    B --> C[💾 Cleaned Data\n(actuals.csv, forecast.csv)]
    C --> D[📈 Power BI Dashboard\n(Trends, KPIs, Forecast)]
    D --> E[🌐 Embedded Dashboard\n(on Website)]
    
    A:::data
    B:::process
    C:::storage
    D:::dashboard
    E:::embed

classDef data fill:#fef3c7,stroke:#333,stroke-width:1px;
classDef process fill:#fde68a,stroke:#333,stroke-width:1px;
classDef storage fill:#c7f9cc,stroke:#333,stroke-width:1px;
classDef dashboard fill:#bae6fd,stroke:#333,stroke-width:1px;
classDef embed fill:#f9d5e5,stroke:#333,stroke-width:1px;
