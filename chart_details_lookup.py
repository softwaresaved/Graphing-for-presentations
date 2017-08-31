#!/usr/bin/env python
# encoding: utf-8

'''
global_specs sets up some global variables for the plots
'''

global_specs = {
    'plot_width': 8,
    'plot_height': 5.8,
    'font_name': 'Serif'
    }

'''
plot_details is a dictionary of lists. The lists are of the form:
 1. the file in which the data  is stored
 2. which column to plot
 3. title for x axis, or use False if no title to be shown
 4. rotation of x-axis tick labels (0 is horizontal)
 5. max length of x-axis tick labels before they start a new line
 6. title for y axis, or use False if no title to be shown
 7. title of chart, or use False if no title
 8. whether to show value labels on bars (True/False)
 9. how many labels to skip to clean up x axis (or False to skip none)
 9. fraction of chart dedicated to x-axis tick labels (0-1)
10. size of title font
11. size of axis fonts
12. size of value label font
'''

plot_details = {
#    'edu1':['edu1.csv', 'percentage', False, 0, 15, 'Percentage', 'Education level', True, 0.1,  24, 14, 24],
#    'edu2':['edu2.csv', 'percentage', False, 90, 20, 'Percentage', 'Education background', False, 0.3, 24, 10, 14],
#    'edu2p2':['edu2p2.csv', 'percentage', False, 90, 15, 'Percentage', 'Top five education backgrounds', True, 0.28,  24, 14, 20],
#    'currentEmp1':['currentEmp1.csv', 'percentage', False, 45, 15, 'Percentage', 'Where do you work?', True, 0.28,  24, 12, 20],
    'currentEmp13':['currentEmp13.csv', 'percentage', False, 90, 15, 'Percentage', 'Where do you work?', False, 0.28,  24, 12, 20]
    }