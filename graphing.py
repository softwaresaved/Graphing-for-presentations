#!/usr/bin/env python
# encoding: utf-8

import pandas as pd
from pandas import ExcelWriter
import numpy as np
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager
import math
import argparse

from textwrap import wrap

from chart_details_lookup import plot_details
from chart_details_lookup import global_specs

DATASTORE = './data/'
STOREFILENAME = './output/'

mpl.rc('font',family='Serif')

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

    data = pd.read_csv(filename)
    data.answers = data.answers.map(str)
    return data


def plot_bar_matplot(df, current_chart):
    """
    Create a basic plot for each question.
    :params: a dict of dataframe, the imported plot details
    :return: A list of saved charts
    """

    # To cut down on verbosity, rename the look_up dictionary
    current_plot = plot_details[current_chart]

    percent_symbol = '%'

    # Set the labels
    labels = df.index

    # If labels are long, wrap 'em
    labels = [ '\n'.join(wrap(l, current_plot['x_max_len'])) for l in labels ] # Change the number to change the max number of characters per line

    # Soemtimes there are simply too many x-labels. Based on a parameter
    # from the lookup table, this removes some labels to give the others roo
    if current_plot['skip_labels'] != False:
        count = 0
        for x in range(0,len(labels)):
            if count%(current_plot['skip_labels']+1) != 0:
                labels[count]=''
            count+=1

    # This sets parameters to ensure that charts look good with one
    # set of bars or two sets of bars
    if current_plot['y2_axis'] == False:
        y_values = [current_plot['y1_axis']]
        colourmap = [plt.cm.Paired(np.arange(len(df)))]
        legend_or_not = False
    else:
        y_values = [current_plot['y1_axis'], current_plot['y2_axis']]
        colourmap = [plt.cm.Spectral(np.arange(len(df))), plt.cm.coolwarm(np.arange(len(df)))]
        legend_or_not = True
        mpl.rcParams['legend.fontsize'] = current_plot['value_font_size'] 

        
    # Now plot
    fig = df.plot(kind='bar',                      # Plot a bar chart
                y = y_values,
                legend=legend_or_not,                                   # Turn the Legend off
                width=0.75,                                     # Set bar width as 75% of space available
                figsize=(global_specs['plot_width'],global_specs['plot_height']),  # Set size of plot in inches
                color=colourmap)      # cm is colormap, 'Paired' is the set of colours I chose


    # Add labels to the bars
    if current_plot['show_values'] == True:
        for p in fig.patches:
            round_dp = current_plot.get('round_dp', 0)  # Allow user to set rounding, assume round to integer
            if round_dp > 0:
                label_text = str(round(p.get_height(), round_dp))  # Get the height of the bar and round it to a nice looking value
            else:
                label_text = str(int(round(p.get_height(), 0)))    # Get the height of the bar and round it to a nice looking value

            if current_plot.get('y_is_percent', True):  # Assume numbers are percentages unless told otherwise
                label_text += percent_symbol

            fig.annotate(label_text,
             (p.get_x()+p.get_width()/2, p.get_height()),  # Locate the mid point of the bar and it's height
             ha='center',                                  # Start plotting at the centre of the horizotal coord
             va='center',                                  # ...and the centre of the vertical coord
             xytext=(4, 12),                               # Change these to move the text positioning to suit
             textcoords='offset points',                   # Dunno what this does
             fontsize=current_plot['value_font_size'])           # Set font size

    if current_plot['chart_title'] != False:
        plt.title(current_plot['chart_title'], fontsize=current_plot['title_font_size'], y=1.08)  # y increases the spacing between the title
                                                                                                 # and plot content

    # Make plot scale to fit plot area
    plt.tight_layout()

    # Use the bespoke labels, and rotate them if necessary
    fig.set_xticklabels(labels, rotation=current_plot['x_rot'], fontsize=current_plot['axis_font_size'])

    # Turn off the spines
    fig.spines['left'].set_visible(False)
    fig.spines['right'].set_visible(False)
    fig.spines['top'].set_visible(False)
    fig.axes.tick_params(top=False)

    # Read in the axis classes that may be used in the following
    # if statements to set axis-related stuff
    x_axe_class = fig.axes.get_xaxis()
    y_axe_class = fig.axes.get_yaxis()

    # X axis title
    if current_plot['x_title'] == False:
        x_axe_class.label.set_visible(False)    #Turn off x axis title
    else:
        fig.set_xlabel(current_plot['x_title'])

    # Y axis title
    if current_plot['y_title'] == False:
        y_axe_class.label.set_visible(False)    #Turn off y axis title
    else:
        fig.set_ylabel(current_plot['y_title'])

    # Remove the y-axis stuff
    y_axe_class.set_visible(False)

    # Make gap at bottom bigger for labels
    plt.subplots_adjust(bottom=current_plot['bottom_size'])

    # Save the figure
    plt.savefig(STOREFILENAME + current_chart + '.png', format = 'png', dpi = global_specs['dpi'])

    # Show the figure
#    plt.show()
    # Clear figure so that parameters can be set clean by next figure
    plt.close()

    return


def plot_line_matplot(df, current_chart):
    """
    Create a basic plot for each question. Plots of more specific interest will
    be created in a separate function, because it's impossible to automate it.
    Uses Seaborn to try and make things prettier
    :params: a dict of dataframe, the imported plot details
    :return: A list of saved charts
    """

    # To cut down on verbosity, rename the look_up dictionary
    current_plot = plot_details[current_chart]

    # Set the labels
    labels = df.index

    # If labels are long, wrap 'em
    labels = [ '\n'.join(wrap(l, current_plot['x_max_len'])) for l in labels ] # Change the number to change the max number of characters per line

    # Set x and y ticks
    x_tick_values = range(0,len(df))
    y_max = int(df[current_plot['y1_axis']].max())
    if current_plot.get("flexible_y_tick_interval", False):
        # Y ticks are spaced by interval that is closest to 1/8 of Ymax
        y_interval_options = [1, 100, 1000]
        y_tick_interval = sorted(y_interval_options, key=lambda x: abs(y_max/8-x))[0]
        y_tick_values = range(0,y_max+y_tick_interval,y_tick_interval)
    else:
        y_tick_values = range(0,y_max,20)

    if current_plot['skip_labels'] != False:
        count = 0
        for x in range(0,len(labels)):
            if count%(current_plot['skip_labels']+1) != 0:
                labels[count]=''
            count+=1
    
    fig = df[current_plot['y1_axis']].plot(kind='line',                      # Plot a bar chart
                legend=False,                                   # Turn the Legend off
                xticks = x_tick_values,
                yticks = y_tick_values,
                figsize=(global_specs['plot_width'],global_specs['plot_height']))

    fig.axes.lines[0].set_linewidth(8)

    if current_plot['chart_title'] != False:
        plt.title(current_plot['chart_title'], fontsize=current_plot['title_font_size'], y=1.08)  # y increases the spacing between the title and plot content

    # Make plot scale to fit plot area
    plt.tight_layout()

    # Use the bespoke labels, and rotate them if necessary
    fig.set_xticklabels(labels, rotation=current_plot['x_rot'], fontsize=current_plot['axis_font_size'])
    fig.set_yticklabels(y_tick_values, fontsize=current_plot['axis_font_size'])

    # Turn off the spines
    fig.spines['left'].set_visible(False)
    fig.spines['right'].set_visible(False)
    fig.spines['top'].set_visible(False)

    # Turn off spare axis ticks
    fig.axes.tick_params(top=False, right=False)

    # Read in the axis classes that may be used in the following
    # if statements to set axis-related stuff
    x_axe_class = fig.axes.get_xaxis()
    y_axe_class = fig.axes.get_yaxis()

    # X axis title
    if current_plot['x_title'] == False:
        x_axe_class.label.set_visible(False)    #Turn off x axis title
    else:
        fig.set_xlabel(current_plot['x_title'])

    # Y axis title
    if current_plot['y_title'] == False:
        y_axe_class.label.set_visible(False)    #Turn off y axis title
    else:
        fig.set_ylabel(current_plot['y_title'], fontsize=current_plot['axis_font_size'])

    # Remove the y-axis stuff
    y_axe_class.set_visible(True)  

    # Make gap at bottom bigger for labels
    plt.subplots_adjust(bottom=current_plot['bottom_size'])

    # Save the figure
    plt.savefig(STOREFILENAME + current_chart + '.png', format = 'png', dpi = global_specs['dpi'])

    # Show the figure
    # plt.show()
    # Clear figure so that parameters can be set clean by next figure
    plt.clf()

    return

    
def main(figure=None):
    """
    Main function to run program
    """
    if figure is not None:
        subset_plot_details = {figure: plot_details[figure]}
    else:
        subset_plot_details = plot_details
    
    # Go through all charts in the lookup table
    for current_chart in subset_plot_details:
        # Read survey data for current chart from csv
        df = import_csv_to_df(DATASTORE + plot_details[current_chart]['filename'])
        # Set the first column as the index
        df.set_index('answers', inplace=True)
        print('Currently working on: ' + current_chart)
        # Plot
        if plot_details[current_chart]['plot_type'] == 'line':
            plot_line_matplot(df, current_chart)
        else:
            plot_bar_matplot(df, current_chart)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Simon's plotting script")
    parser.add_argument("-f", "--figure", type=str, default=None,
                        help="Optional: Single figure name in chart_details_lookup to plot")

    args = parser.parse_args()
    main(args.figure)
