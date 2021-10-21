# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
#Oil Pipeline Leaks and Spills 
#A Cost Prediction Model

The costs associated with accidents at pipelines can range from minimal to catastrophic.

To better understand the resulting costs from future accidents, I utillized the published data from the Pipeline and Hazardous Materials Safety Administration available on Kaggle [Dataset](https://www.kaggle.com/usdot/pipeline-accidents).

##Target Variable

Many costs are associated with leaks and spills at oil pipelines.  The dataset focuses on several main categories like environmental remediation costs, emergency response costs, and lost commodity costs, to name a few.  For my model, I selected the cumulative total costs as my target variable.

##Establishing a Baseline

###Model One

I planned to use regression models to predict future costs.  The first thing I had to do was set up a baseline for the model.  Using the mean absolute error of my target data frame, I established a baseline of 1,255,588.  

###Model Two

As an additional predictor, I thought it would be interesting to build a model for all costs when gross cost did not in exceed 10,000,000 dollars.  I established a baseline using mean absolute error, as well.  The modified dataset had a baseline of 313,592 dollars.

##Data Leakage

During dataset exploration, I noted that maintaining any column with a direct dollar cost as a feature could be problematic.  The columns represented a high potential for data leakage.  I built an initial model maintaining the cost columns, and it proved itself out.  

The second problem using dollar costs is whether the model would be predictive.  It is challenging to include cost as a component to predict the total cost.  The model would need to wait for charges to accumulate.

There are plenty of other exciting data columns that can assist in prediction.  Still, rather than lose the cost columns entirely, I found a way to save some information.

An initial assessment post leak or spill would tell an individual whether or not to expect to incur costs of specific categories.  I converted the columns that could easily be assessed to binary columns.  I assigned a value of one when expenses were incurred and zero when they were not.

##Model Uses

The model is helpful in a variety of different ways, depending on your need.  For example, a quick loss reserve can be established and posted to the account for an insurance company adjuster.  Insurance companies have to explain how loss reserves are established.  The model could be valuable when dealing with auditing firms and taxing authorities.  

In addition, it can be a valuable baseline to help understand whether the costs coming in are in line with initial expectations.  An adjuster might ask him or herself the question of whether he is overpaying for certain services.

For pipeline risk managers, the model can assist in developing insurance liability requirements for third-party pipeline contractors.  In addition, it can help in post-spill risk financing response.

##Other Uses?

Feel free to DM me on [LinkedIn](https://www.linkedin.com/in/michaeljpetrus/) and let me know other ways the model might be valuable. 

        ),

    ],
)

layout = dbc.Row([column1])