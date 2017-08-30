#!/usr/bin/env python
# encoding: utf-8

import pandas as pd
from pandas import ExcelWriter
import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager
import math
import seaborn as sns
from textwrap import wrap

from chart_details_lookup import plot_details
from chart_details_lookup import global_specs

DATASTORE = './data/'
STOREFILENAME = './output/'

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


def plot_bar_matplot(df,plot_col, x_title, y_title):
    """
    Create a basic plot for each question. Plots of more specific interest will
    be created in a separate function, because it's impossible to automate it.
    Uses Seaborn to try and make things prettier
    :params: a dict of dataframe, the imported plot details
    :return: A list of saved charts
    """

    # If you want to know what fonts are available, uncomment the following four lines
#    flist = matplotlib.font_manager.get_fontconfig_fonts()
#    names = [matplotlib.font_manager.FontProperties(fname=fname).get_name() for fname in flist]
#    names.sort()
#    print(names)


    # Title's from the lookup table
#    title = plot_details[key][0]

    # Set the labels
    labels = df.index

    # If labels are long, wrap 'em
    labels = [ '\n'.join(wrap(l, 15)) for l in labels ]

    my_colors = [(x/10.0, x/20.0, 0.75) for x in range(len(df))]

    # Now plot
    fig = df['percentages'].plot(kind='bar',    # Plot a bar chart
                legend=False,    # Turn the Legend off
                width=0.75,      # Set bar width as 75% of space available
                figsize=(8,5.8),  # Set size of plot in inches
                colormap='Paired')

    # Add labels to the bars
    for p in fig.patches:
        fig.annotate(str(int(round(p.get_height(),0))) + '%',     # Get the height of the bar and round it to a nice looking value
         (p.get_x()+p.get_width()/2, p.get_height()),  # Locate the mid point of the bar and it's height
         ha='center',                                  # Start plotting at the centre of the horizotal coord
         va='center',                                  # ...and the centre of the vertical coord
         xytext=(0, 12),                               # Change these to move the text positioning to suit
         textcoords='offset points',                   # Dunno what this does
         fontname="Adobe Garamond Pro",                # Set font
         fontsize=24)                                  # Set font size

    # Make plot scale to fit plot area
    plt.tight_layout()
    
    

    

#    plt.figure(figsize=(global_specs['plot_width'], global_specs['plot_height'])) 
    # Use bespoke labels, and rotate them so they're horizontal
    fig.set_xticklabels(labels, rotation=0, fontname="Adobe Garamond Pro", fontsize=18)

    # Turn off the spines
    fig.spines['left'].set_visible(False)
    fig.spines['right'].set_visible(False)
    fig.spines['top'].set_visible(False)


    # Read in th axis class so that we can manipulate it
    x_axis = fig.axes.get_xaxis()
    x_axis.label.set_visible(False)    #Turn off x axis title

    y_axis = fig.axes.get_yaxis()
    y_axis.set_visible(False)    #Turn off x axis title
    
    # Make gap at bottom bigger for labels (it's a fraction, not a measurement)
    plt.subplots_adjust(bottom=0.15)
    

#    plt.tick_params(
#        axis='both',       # which axis to apply changes to
#        which='both',      # major ticks, minor ticks or both
#        bottom='off',      # ticks along the bottom edge are off
#        left='off',
#        top='off')         # ticks along the top edge are off

    plt.savefig(STOREFILENAME + 'bob' + '.png', format = 'png', dpi = 300)
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
        df.set_index('answers', inplace=True)

        # Plot stuff
#        plot_basic_seaborn(df,plot_col, value_col, x_title, y_title)
        plot_bar_matplot(df,plot_col, x_title, y_title)

if __name__ == '__main__':
    main()