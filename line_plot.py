import pandas as pd
import plotly.express as px

df=pd.read_csv("data2.csv")
print(df)

fig=px.line(df,x="Country",y="Per capita income",color="Year",title="Per capita income")
fig.show()
