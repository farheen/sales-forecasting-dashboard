## Project Architecture (Schematic)

```mermaid
flowchart LR
    A[Data Source (Excel - Online Retail II)] --> B[Python ETL + Forecasting (Prophet)]
    B --> C[Cleaned Data (actuals.csv, forecast.csv)]
    C --> D[Power BI Dashboard (Trends, KPIs, Forecast)]
    D --> E[Embedded Dashboard (Website iframe)]
    
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
