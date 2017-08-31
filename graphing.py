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
    x_axis_label_rotation = plot_details[current_chart][3]
    x_axis_label_cutoff = plot_details[current_chart][4]
    y_axis_label = plot_details[current_chart][5]
    chart_title = plot_details[current_chart][6]
    show_values = plot_details[current_chart][7]
    skip_labels = plot_details[current_chart][8]
    bottom_size = plot_details[current_chart][9]
    title_size = plot_details[current_chart][10]
    body_size = plot_details[current_chart][11]
    label_size = plot_details[current_chart][12]

    # Set the labels
    labels = df.index

    # If labels are long, wrap 'em
    labels = [ '\n'.join(wrap(l, x_axis_label_cutoff)) for l in labels ] # Change the number to change the max number of characters per line

    if skip_labels != False:
        count = 0
        for x in range(0,len(labels)):
            if count%(skip_labels+1) != 0:
                labels[count]=''
            count+=1

    # Now plot
    fig = df[y_axis_name].plot(kind='bar',                      # Plot a bar chart
                legend=False,                                   # Turn the Legend off
                width=0.75,                                     # Set bar width as 75% of space available
                figsize=(global_specs['plot_width'],global_specs['plot_height']),  # Set size of plot in inches
                color=[plt.cm.Paired(np.arange(len(df)))])      # cm is colormap, 'Paired' is the set of colours I chose
                                                                # the last bit creates a range and matches it to the Paired colour range

    # Add labels to the bars
    if show_values == True:
        for p in fig.patches:
            fig.annotate(str(int(round(p.get_height(),0))) + percent_symbol,     # Get the height of the bar and round it to a nice looking value
             (p.get_x()+p.get_width()/2, p.get_height()),  # Locate the mid point of the bar and it's height
             ha='center',                                  # Start plotting at the centre of the horizotal coord
             va='center',                                  # ...and the centre of the vertical coord
             xytext=(0, 12),                               # Change these to move the text positioning to suit
             textcoords='offset points',                   # Dunno what this does
             fontname=global_specs['font_name'],           # Set font
             fontsize=label_size)           # Set font size

    if chart_title != False:
        plt.title(chart_title, fontname=global_specs['font_name'], fontsize=title_size, y=1.08)  # y increases the spacing between the title and
                                                                                                 #plot content

    # Make plot scale to fit plot area
    plt.tight_layout()

    # Use the bespoke labels, and rotate them if necessary
    
    fig.set_xticklabels(labels, rotation=x_axis_label_rotation, fontname=global_specs['font_name'], fontsize=body_size)


    # Turn off the spines
    fig.spines['left'].set_visible(False)
    fig.spines['right'].set_visible(False)
    fig.spines['top'].set_visible(False)

    # Read in the axis classes that may be used in the following
    # if statements to set axis-related stuff
    x_axe_class = fig.axes.get_xaxis()
    y_axe_class = fig.axes.get_yaxis()

    # X axis title
    if x_axis_label == False:
        x_axe_class.label.set_visible(False)    #Turn off x axis title
    else:
        fig.set_xlabel(x_axis_label)

    # Y axis title
    if y_axis_label == False:
        y_axe_class.label.set_visible(False)    #Turn off y axis title
    else:
        fig.set_ylabel(y_axis_label)

    # Remove the y-axis stuff
    y_axe_class.set_visible(False)  

    # Make gap at bottom bigger for labels
    plt.subplots_adjust(bottom=bottom_size)
    
    # Save the figure
    plt.savefig(STOREFILENAME + current_chart + '.png', format = 'png', dpi = 300)

    # Show the figure
    plt.show()
    # Clear figure so that parameters can be set clean by next figure
    plt.clf()

    return
    
    
def main():
    """
    Main function to run program
    """
    
    # Go through all charts in the lookup table
    for current_chart in plot_details:
        # Get the current chart name
        filename = plot_details[current_chart][0]
        # Read survey data from csv
        df = import_csv_to_df(DATASTORE + filename)
        # Set the first column as the index
        df.set_index('answers', inplace=True)
        # Plot
        plot_bar_matplot(df, current_chart)

if __name__ == '__main__':
    main()