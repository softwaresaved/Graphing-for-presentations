#!/usr/bin/env python
# encoding: utf-8

import pandas as pd
from pandas import ExcelWriter
import numpy as np
import csv
import matplotlib.pyplot as plt
import math
import seaborn as sns
from textwrap import wrap

from chart_details_lookup import plot_details
from chart_details_lookup import global_specs

DATASTORE = './data/'


def import_csv_to_df(filename):
    """
    Imports a csv file into a Pandas dataframe
    :params: get an xls file and a sheetname from that file
    :return: a df
    """
    
    return pd.read_csv(filename)


def plot_basic_seaborn(df,plot_col, value_col, x_title, y_title):
    """
    Create a basic plot for each question. Plots of more specific interest will
    be created in a separate function, because it's impossible to automate it.
    Uses Seaborn to try and make things prettier
    :params: a dict of dataframe, the imported plot details
    :return: A list of saved charts
    """

    # Title's from the lookup table
#    title = plot_details[key][0]

    # Set the labels
    labels = df[value_col]

    # If labels are long, wrap 'em
    labels = [ '\n'.join(wrap(l, 15)) for l in labels ]

    # Choose a pretty colour palette
    sns.set_palette('husl')
    
    # Set the size of the chart via the look up table
    plt.figure(figsize=(global_specs['plot_width'], global_specs['plot_height'])) 

    # Now plot
    sns.barplot(x = labels, y = df[plot_col], data = df) #.set_title(chart_title)
    # Make gap at bottom bigger for labels (it's a fraction, not a measurement)

    plt.subplots_adjust(bottom=0.15)
    sns.despine(bottom=True, left=True)
    
    plt.xlabel(x_title)
    plt.ylabel(y_title)

    plt.tick_params(
        axis='both',       # which axis to apply changes to
        which='both',      # major ticks, minor ticks or both
        bottom='off',      # ticks along the bottom edge are off
        left='off',
        top='off')         # ticks along the top edge are off
    
#    plt.xticks(rotation=90)
#    plt.savefig(STOREFILENAME + 'basic_counts/' + key + '.png', format = 'png', dpi = 150)
    plt.show()
    # Funnliy enough, Seaborn seems a bit sticky. There's a weird kind of
    # colour bleed from one plot to the next. However, by explicitly clearing the 
    # frame in the following step, it's all sorted
    plt.clf()

    return


def plot_bar_matplot(df,plot_col, value_col, x_title, y_title):
    """
    Create a basic plot for each question. Plots of more specific interest will
    be created in a separate function, because it's impossible to automate it.
    Uses Seaborn to try and make things prettier
    :params: a dict of dataframe, the imported plot details
    :return: A list of saved charts
    """

    # Title's from the lookup table
#    title = plot_details[key][0]

    # Set the labels
    labels = df[value_col]

    # If labels are long, wrap 'em
    labels = [ '\n'.join(wrap(l, 15)) for l in labels ]


    # Set the size of the chart via the look up table
#    plt.figure(figsize=(global_specs['plot_width'], global_specs['plot_height'])) 

    # Now plot
    plt.bar(x = labels, y = df[plot_col], data=df, color="blue")    

    # Make gap at bottom bigger for labels (it's a fraction, not a measurement)
    plt.subplots_adjust(bottom=0.15)
    
    plt.xlabel(x_title)
    plt.ylabel(y_title)

    plt.tick_params(
        axis='both',       # which axis to apply changes to
        which='both',      # major ticks, minor ticks or both
        bottom='off',      # ticks along the bottom edge are off
        left='off',
        top='off')         # ticks along the top edge are off
    
#    plt.xticks(rotation=90)
#    plt.savefig(STOREFILENAME + 'basic_counts/' + key + '.png', format = 'png', dpi = 150)
    plt.show()
    # Funnliy enough, Seaborn seems a bit sticky. There's a weird kind of
    # colour bleed from one plot to the next. However, by explicitly clearing the 
    # frame in the following step, it's all sorted
    plt.clf()

    return
    
    
def main():
    """
    Main function to run program
    """
    
    for current_chart in plot_details:
        filename = plot_details[current_chart][0]
        value_col = plot_details[current_chart][1]
        plot_col = plot_details[current_chart][2]
        x_title = plot_details[current_chart][3]
        y_title = plot_details[current_chart][4]
        chart_title = plot_details[current_chart][5]
        # Read survey data from csv
        df = import_csv_to_df(DATASTORE + filename)

        # Plot stuff
#        plot_basic_seaborn(df,plot_col, value_col, x_title, y_title)
        plot_bar_matplot(df,plot_col, value_col, x_title, y_title)

if __name__ == '__main__':
    main()