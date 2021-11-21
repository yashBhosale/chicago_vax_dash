from sodapy import Socrata
import pandas as pd
import matplotlib.pyplot as plt

client = Socrata("data.cityofchicago.org", "yNbNYpik7ktt3NVRTtUq6FqL2")

results = client.get("naz8-j4nc", select="lab_report_date, cases_total,deaths_total,hospitalizations_total", limit=2000)
results_df = pd.DataFrame.from_records(results)
results_df.sort_values("lab_report_date", inplace=True)
print(results_df)
for col in ["cases_total","deaths_total","hospitalizations_total"]:
    print(col)
    results_df[col] = results_df[col].astype("string").astype("Int32")
results_df["cases_total_rolling"] = results_df["cases_total"].rolling(7).mean()
results_df["lab_report_date"] = pd.to_datetime( results_df["lab_report_date"].astype("str"),infer_datetime_format=True)
#results_df.set_index("lab_report_date", inplace=True)
#print(results_df)
#ax = results_df.plot(kind="line",x="lab_report_date", y=["cases_total" ])
results_df.plot(kind="bar",x="lab_report_date",y="cases_total_rolling")
plt.show()
