#!/usr/bin/env python
# encoding: utf-8

'''
global_specs sets up some global variables for the plots
'''

global_specs = {
    'plot_width': 8,
    'plot_height': 5.8,
    'dpi': 300,
    'font_name': 'Serif'
    }

'''
plot_details is a dictionary of lists. The lists are of the form:
 0. Plot type
 1. the file in which the data  is stored
 2. first column to plot
 3. second column to plot (or False, if none)
 4. title for x axis, or use False if no title to be shown
 5. rotation of x-axis tick labels (0 is horizontal)
 6. max length of x-axis tick labels before they start a new line
 7. title for y axis, or use False if no title to be shown
 8. title of chart, or use False if no title
 9. whether to show value labels on bars (True/False)
10. how many labels to remove after each one shown (or False to keep all)
11. fraction of chart dedicated to x-axis tick labels (0-1)
12. size of title font
13. size of axis fonts
14. size of value label font
'''


plot_details = {
    'rse1': {
            'filename': 'rse1.csv',
            'plot_type': 'bar',
            'y1_axis': 'percentage',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': 'Percentage',
            'chart_title': 'Do you write code?',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.15,
            'title_font_size': 24,
            'axis_font_size': 12,
            'value_font_size': 20
            },
    'rse3': {
            'filename': 'rse3.csv',
            'plot_type': 'bar',
            'y1_axis': 'percentage',
            'y2_axis': False,
            'x_title': False,
            'x_rot': 0,
            'x_max_len': 15,
            'y_title': 'Percentage',
            'chart_title': 'Who uses your code?',
            'show_values': True,
            'skip_labels': False,
            'bottom_size': 0.15,
            'title_font_size': 24,
            'axis_font_size': 14,
            'value_font_size': 24
            },
    }
    
    
    
    
    