from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from subprocess import run,PIPE
import numpy as np
import matplotlib.pyplot as plt



from pylab import *
import sys




def home(request):

    return render(request, 'blog/home.html')

def about(request):

    return render(request, 'blog/about.html')



def base(request):
    return render(request, 'blog/base.html')

from matplotlib.pylab import rcParams
rcParams['figure.figsize']=10,6
from pylab import *
from sklearn.metrics import mean_squared_error
from statsmodels.graphics.tsaplots import *
from statsmodels.tsa.arima_model import ARIMA
from plotly.offline import plot
from plotly.graph_objs import Scatter
import cufflinks as cf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import image

def chicagopizza(request):
    import matplotlib.pyplot as plt

    a=pd.read_excel('D:\Desktop\SC Python pizza-sales-data.xlsx')


    a['DATE'] = pd.to_datetime(a["DATE"].dt.strftime('%Y-%d-%m'))

    pd.to_datetime(a['DATE'])
    a = a.set_index(['DATE'])
    c = a.loc[a.CATEGORY == 'Chicago Pizza']
    indc = c.copy()
    indc.dropna(inplace=True)
    del indc['CATEGORY']
    series_value = indc.values
    indc_mean = indc.rolling(window=10).mean()
    value = pd.DataFrame(series_value)
    indc_df = pd.concat([value, value.shift(1)], axis=1)
    indc_df.columns = ['Actual_sales', 'Forecast_sales']

    indc_test = indc_df[1:]
    indc_error = mean_squared_error(indc_test.Actual_sales, indc_test.Forecast_sales)

    sales_train = indc[0:29]
    sales_test = indc[29:]
    sales_model = ARIMA(sales_train, order=(2, 2, 1))
    sales_model_fit = sales_model.fit()
    sales_model_fit.aic
    s = (input('Number of Steps: '))
    s = int(s)

    sales_forecast = sales_model_fit.forecast(steps=s)[0]
    sales_dataframe = pd.DataFrame(sales_forecast)
    sales_dataframe.columns = ['PREDICTED_SALES']
    result = indc.append([sales_dataframe])

    inp = input('do you want to download?  (YES/NO)  ')
    if (inp == 'YES'):
        result.to_csv('result_for_chicagopizza.csv', index=True)


    fig=Figure()
    ax = fig.add_subplot(111)
    result.plot(ax=ax)
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response


def neapolitanpizza(request):
    import matplotlib.pyplot as plt

    a=pd.read_excel('D:\Desktop\SC Python pizza-sales-data.xlsx')

    a['DATE'] = pd.to_datetime(a["DATE"].dt.strftime('%Y-%d-%m'))
    pd.to_datetime(a['DATE'])
    a = a.set_index(['DATE'])
    c = a.loc[a.CATEGORY == 'Neapolitan Pizza']
    indc = c.copy()
    indc.dropna(inplace=True)
    del indc['CATEGORY']
    series_value = indc.values
    indc_mean = indc.rolling(window=10).mean()
    value = pd.DataFrame(series_value)
    indc_df = pd.concat([value, value.shift(1)], axis=1)
    indc_df.columns = ['Actual_sales', 'Forecast_sales']

    indc_test = indc_df[1:]
    indc_error = mean_squared_error(indc_test.Actual_sales, indc_test.Forecast_sales)

    sales_train = indc[0:29]
    sales_test = indc[29:]
    sales_model = ARIMA(sales_train, order=(2, 2, 1))
    sales_model_fit = sales_model.fit()
    sales_model_fit.aic
    s = (input('Number of Steps: '))
    s = int(s)

    sales_forecast = sales_model_fit.forecast(steps=s)[0]
    sales_dataframe = pd.DataFrame(sales_forecast)
    sales_dataframe.columns = ['PREDICTED_SALES']
    result = indc.append([sales_dataframe])
    inp = input('do you want to download? (YES/NO)  ')
    if (inp == 'YES'):
        result.to_csv('result_for_neapolitanpizza.csv', index=True)
    fig = Figure()
    ax = fig.add_subplot(111)
    result.plot(ax=ax)
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def sicilianpizza(request):
    import matplotlib.pyplot as plt

    a=pd.read_excel('D:\Desktop\SC Python pizza-sales-data.xlsx')


    a['DATE'] = pd.to_datetime(a["DATE"].dt.strftime('%Y-%d-%m'))
    pd.to_datetime(a['DATE'])
    a = a.set_index(['DATE'])
    c = a.loc[a.CATEGORY == 'Sicilian Pizza']
    indc = c.copy()
    indc.dropna(inplace=True)
    del indc['CATEGORY']
    series_value = indc.values
    indc_mean = indc.rolling(window=10).mean()
    value = pd.DataFrame(series_value)
    indc_df = pd.concat([value, value.shift(1)], axis=1)
    indc_df.columns = ['Actual_sales', 'Forecast_sales']

    indc_test = indc_df[1:]
    indc_error = mean_squared_error(indc_test.Actual_sales, indc_test.Forecast_sales)

    sales_train = indc[0:29]
    sales_test = indc[29:]
    sales_model = ARIMA(sales_train, order=(2, 2, 1))
    sales_model_fit = sales_model.fit()
    sales_model_fit.aic
    s = (input('Number of Steps: '))
    s = int(s)

    sales_forecast = sales_model_fit.forecast(steps=s)[0]
    sales_dataframe = pd.DataFrame(sales_forecast)
    sales_dataframe.columns = ['PREDICTED_SALES']
    result = indc.append([sales_dataframe])
    inp = input('do you want to download?  (YES/NO)  ')
    if (inp == 'YES'):
        result.to_csv('result_for_sicilianpizza.csv', index=True)
    fig = Figure()
    ax = fig.add_subplot(111)
    result.plot(ax=ax)
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

def tomatopiepizza(request):
    import matplotlib.pyplot as plt

    a=pd.read_excel('D:\Desktop\SC Python pizza-sales-data.xlsx')


    a['DATE'] = pd.to_datetime(a["DATE"].dt.strftime('%Y-%d-%m'))
    pd.to_datetime(a['DATE'])
    a = a.set_index(['DATE'])
    c = a.loc[a.CATEGORY == 'Neapolitan Pizza']
    indc = c.copy()
    indc.dropna(inplace=True)
    del indc['CATEGORY']
    series_value = indc.values
    indc_mean = indc.rolling(window=10).mean()
    value = pd.DataFrame(series_value)
    indc_df = pd.concat([value, value.shift(1)], axis=1)
    indc_df.columns = ['Actual_sales', 'Forecast_sales']

    indc_test = indc_df[1:]
    indc_error = mean_squared_error(indc_test.Actual_sales, indc_test.Forecast_sales)

    sales_train = indc[0:29]
    sales_test = indc[29:]
    sales_model = ARIMA(sales_train, order=(2, 2, 1))
    sales_model_fit = sales_model.fit()
    sales_model_fit.aic
    s = (input('Number of Steps: '))
    s = int(s)

    sales_forecast = sales_model_fit.forecast(steps=s)[0]
    sales_dataframe = pd.DataFrame(sales_forecast)
    sales_dataframe.columns = ['PREDICTED_SALES']
    result = indc.append([sales_dataframe])
    inp = input('do you want to download?  (YES/NO)  ')
    if (inp == 'YES'):
        result.to_csv('result_for_tomatopiepizza.csv', index=True)
    fig = Figure()
    ax = fig.add_subplot(111)
    result.plot(ax=ax)
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/jpg')
    canvas.print_jpg(response)
    return response

