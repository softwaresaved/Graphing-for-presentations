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

# If you want to know what fonts are available, uncomment the following four lines
#flist = matplotlib.font_manager.get_fontconfig_fonts()
#names = [matplotlib.font_manager.FontProperties(fname=fname).get_name() for fname in flist]
#names.sort()
#print(names)




def import_csv_to_df(filename):
    """
    Imports a csv file into a Pandas dataframe
    :params: get an xls file and a sheetname from that file
    :return: a df
    """
    
    return pd.read_csv(filename)


def plot_bar_matplot(df, current_chart):
    """
    Create a basic plot for each question. Plots of more specific interest will
    be created in a separate function, because it's impossible to automate it.
    Uses Seaborn to try and make things prettier
    :params: a dict of dataframe, the imported plot details
    :return: A list of saved charts
    """

    percent_symbol = '%'

    # Get the chart params from the lookup table
    filename = plot_details[current_chart][0]
    y_axis_name = plot_details[current_chart][1]
    x_axis_label = plot_details[current_chart][2]
    y_axis_label = plot_details[current_chart][3]
    chart_title = plot_details[current_chart][4]
    show_values = plot_details[current_chart][5]

    # Set the labels
    labels = df.index
    # If labels are long, wrap 'em
    labels = [ '\n'.join(wrap(l, 15)) for l in labels ] # Change the number to change the max number of characters per line

    # Now plot
    fig = df[y_axis_name].plot(kind='bar',    # Plot a bar chart
                legend=False,    # Turn the Legend off
                width=0.75,      # Set bar width as 75% of space available
                figsize=(global_specs['plot_width'],global_specs['plot_height']),  # Set size of plot in inches
                color=[plt.cm.Paired(np.arange(len(df)))])

    # Add labels to the bars. This is way more complicated than it needs to be
    if show_values == True:
        for p in fig.patches:
            fig.annotate(str(int(round(p.get_height(),0))) + percent_symbol,     # Get the height of the bar and round it to a nice looking value
             (p.get_x()+p.get_width()/2, p.get_height()),  # Locate the mid point of the bar and it's height
             ha='center',                                  # Start plotting at the centre of the horizotal coord
             va='center',                                  # ...and the centre of the vertical coord
             xytext=(0, 12),                               # Change these to move the text positioning to suit
             textcoords='offset points',                   # Dunno what this does
             fontname=global_specs['font_name'],           # Set font
             fontsize=global_specs['title_size'])           # Set font size

    plt.title(chart_title, fontname=global_specs['font_name'], fontsize=global_specs['title_size'])

    # Make plot scale to fit plot area
    plt.tight_layout()
    

#    plt.figure(figsize=(global_specs['plot_width'], global_specs['plot_height'])) 
    # Use bespoke labels, and rotate them so they're horizontal
    fig.set_xticklabels(labels, rotation=0, fontname=global_specs['font_name'], fontsize=global_specs['body_size'])

    # Turn off the spines
    fig.spines['left'].set_visible(False)
    fig.spines['right'].set_visible(False)
    fig.spines['top'].set_visible(False)

    # Read in the axis classes that may be used in the following
    # if statements
    x_axe_class = fig.axes.get_xaxis()
    y_axe_class = fig.axes.get_yaxis()

    # X axis title
    if x_axis_label == False:
        x_axe_class.label.set_visible(False)    #Turn off x axis title
    else:
        fig.set_xlabel(x_axis_label)

    # Y axis title
    if y_axis_label == False:
        y_axe_class.label.set_visible(False)    #Turn off x axis title
    else:
        fig.set_ylabel(y_axis_label)

    # Remove the y-axis line
    y_axe_class.set_visible(False)    #Turn off y axis line

    # Make gap at bottom bigger for labels (it's a fraction, not a measurement)
    plt.subplots_adjust(bottom=0.15)
    
    # Save the figure
    plt.savefig(STOREFILENAME + current_chart + '.png', format = 'png', dpi = 300)

    # Show the figure
    plt.show()

    return
    
    
def main():
    """
    Main function to run program
    """
    
    # Get the chart params from the lookup table
    
    for current_chart in plot_details:
        filename = plot_details[current_chart][0]
        # Read survey data from csv
        df = import_csv_to_df(DATASTORE + filename)
        # Set the first column as the index
        df.set_index('answers', inplace=True)

        # Plot stuff
        plot_bar_matplot(df, current_chart)

if __name__ == '__main__':
    main()