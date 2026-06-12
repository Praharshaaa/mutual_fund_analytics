
import pandas as pd

scheme_performance = pd.read_csv(r"C:\Users\PRAHARSHA\mutual_fund_analytics\data\raw\07_scheme_performance.csv")

def recommend_funds(risk_appetite):
    if risk_appetite == "Low":
        filtered = scheme_performance[scheme_performance["risk_grade"].isin(["Low", "Low to Moderate"])]
    elif risk_appetite == "Moderate":
        filtered = scheme_performance[scheme_performance["risk_grade"].isin(["Moderate", "Moderately High"])]
    else:
        filtered = scheme_performance[scheme_performance["risk_grade"].isin(["High", "Very High"])]

    top3 = filtered.nlargest(3, "sharpe_ratio")[["scheme_name", "sharpe_ratio", "risk_grade", "return_3yr_pct"]]
    return top3

if __name__ == "__main__":
    print("LOW RISK:")
    print(recommend_funds("Low"))
    print("\nMODERATE RISK:")
    print(recommend_funds("Moderate"))
    print("\nHIGH RISK:")
    print(recommend_funds("High"))
