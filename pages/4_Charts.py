import streamlit as st
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
df=st.session_state['dataframe']


#st.write(df)
df.rename(columns = {'Unnamed: 0':'Categories'}, inplace = True)
st.write(df)
gross_sales=df[df['Categories']=='Sales']
gross_sales=gross_sales.loc[:,'Categories':'Jul. 2022']
gross_sales=gross_sales.set_index('Categories').T.rename_axis('Categories').reset_index()
#st.write(gross_sales)


bar_graph=gross_sales




#st.write(bar_graph)
bar_graph['Sales']=bar_graph['Sales'].astype(float)
#bar_graph['Sales']=bar_graph['Sales'].round(0).map("{:,.1f}".format)
#bar_graph['Sales']=bar_graph['Sales'].round(0).map("{:,.0f}".format)
#st.write(bar_graph)
bar_graph['% Difference in Sales']=bar_graph.Sales.pct_change()*100
bar_graph['% Difference in Sales']=bar_graph['% Difference in Sales'].round(0)
bar_graph['% Difference in Sales']=bar_graph['% Difference in Sales'].round(0).map("{:,.0f}".format)

#st.write(bar_graph)
#st.bar_chart(bar_graph,x='Categories',y='Sales')

fig=go.Figure()

fig.add_trace(
    go.Scatter(
        x=bar_graph["Categories"],
        y=bar_graph["Sales"],

    ))

fig.add_trace(
    go.Bar(
        x=bar_graph["Categories"],
        y=bar_graph["Sales"]
    ))

#st.plotly_chart(fig, use_container_width=True)


st.write(bar_graph)
fig2=px.bar(
    bar_graph, x="Categories",y="Sales", title="Gross Sales - Bar Chart (2021-22)"
).add_traces(
    px.line(bar_graph,x="Categories",y="Sales",line_shape='spline',markers=True,text=bar_graph['% Difference in Sales']).update_traces(showlegend=True, name="Gross Sales",textposition="top center").data
)
fig2.update_layout(title = {
         'text': "Plot Title",
         'y':0.9, # new
         'x':0.5,
         'xanchor': 'center',
         'yanchor': 'top' # new
        })
#st.plotly_chart(fig2,use_container_width=True)

#---------------
fig3=px.line(x=bar_graph["Categories"],y=bar_graph["Sales"],labels="Gross Sales",line_shape='spline',markers=True,text=bar_graph['% Difference in Sales']+"%")
fig3.update_traces(textposition="top center")
fig4=px.bar(x=bar_graph["Categories"],y=bar_graph["Sales"],text="$"+bar_graph['Sales'].astype(str))
fig4.update_traces(textposition="inside",textfont_size=15)

fig5=go.Figure(data=fig3.data+fig4.data)
fig5.update_layout(title="Gross Sales - Bar Chart (2021-22)")
st.plotly_chart(fig5,use_container_width=True)

#---------------SALES/COGS/GM------------

df2=df[(df['Categories']=='Sales')|(df['Categories']=='COGS')|(df['Categories']=='GROSS PROFIT')]
df2=df2.loc[:,'Categories':'Jul. 2022']
df2=df2.set_index('Categories').T.rename_axis('Categories').reset_index()

#st.write(df2)
cols=[i for i in df2.columns if i not in ['Categories']]
for col in cols:
    df2[col]=pd.to_numeric(df2[col]).astype(float).round(0).map("{:,.0f}".format)
st.write(df2)

comp1=px.line(x=df2["Categories"],y=df2["Sales"],labels="Gross Sales",line_shape='spline',markers=True,text="$"+df2['Sales'].astype(str))
comp1.update_traces(textposition="top center",line_color='#d62728',textfont=dict(
        family="sans serif",
        size=10,
        color="white"
    ))


comp2=px.line(x=df2["Categories"],y=df2["COGS"],labels="Cost of Goods Sold",line_shape='spline',markers=True,text="$"+df2['COGS'].astype(str))
comp2.update_traces(textposition="top center",line_color="#2ca02c",textfont=dict(
        family="sans serif",
        size=10,
        color="white"
    ))

comp3=px.line(x=df2["Categories"],y=df2["GROSS PROFIT"],labels="GROSS PROFIT",line_shape='spline',markers=True,text="$"+df2['GROSS PROFIT'].astype(str))
comp3.update_traces(textposition="top center",line_color="#ff7f0e",textfont=dict(
        family="sans serif",
        size=10,
        color="white"
    ))

comp4=px.bar(x=df2["Categories"],y=df2["Sales"])
#comp4.update_traces(textposition="inside",textfont_size=15)


comp=go.Figure(data=comp1.data+comp2.data+comp3.data+comp4.data)
comp.update_layout(title="Sales Vs COGS/GP Margin - in $ (2021 - 22)",xaxis_title="Months",
    yaxis_title="Total Sales",
    legend_title="Legend Title",
    font=dict(
        family="sans serif",
        size=18,
        color="White"
    )
)
comp.update_layout(plot_bgcolor = "black",paper_bgcolor="Black")
comp.update_xaxes(showgrid=False)
comp.update_yaxes(showgrid=False)

st.plotly_chart(comp,use_container_width=True)