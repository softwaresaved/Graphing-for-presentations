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
 0. Plot type
 1. the file in which the data  is stored
 2. which column to plot
 3. title for x axis, or use False if no title to be shown
 4. rotation of x-axis tick labels (0 is horizontal)
 5. max length of x-axis tick labels before they start a new line
 6. title for y axis, or use False if no title to be shown
 7. title of chart, or use False if no title
 8. whether to show value labels on bars (True/False)
 9. how labels to remove after each one shown (or False to keep all)
10. fraction of chart dedicated to x-axis tick labels (0-1)
11. size of title font
12. size of axis fonts
13. size of value label font
'''

plot_details = {
#    'edu1':['bar', 'edu1.csv', 'percentage', False, 0, 15, 'Percentage', 'Education level', True, 0.1, False,  24, 14, 24],
#    'edu2':['bar', 'edu2.csv', 'percentage', False, 90, 20, 'Percentage', 'Education background', False, False, 0.3, 24, 10, 14],
#    'edu2p2':['bar', 'edu2p2.csv', 'percentage', False, 90, 15, 'Percentage', 'Top 10 backgrounds', True, False, 0.28,  24, 14, 20],
#    'currentEmp1':['bar', 'currentEmp1.csv', 'percentage', False, 45, 15, 'Percentage', 'Where do you work?', True, False, 0.28,  24, 12, 20],
#    'currentEmp13':['bar', 'currentEmp13.csv', 'percentage', False, 90, 15, 'Percentage', 'In which field do you work?', False, 2, 0.28,  24, 12, 20],
#    'currentEmp13p2':['bar', 'currentEmp13p2.csv', 'percentage', False, 90, 15, 'Percentage', 'To 10 fields of work', True, False, 0.28,  24, 12, 20],
#    'currentEmp10':['bar', 'currentEmp10.csv', 'percentage', False, 0, 15, 'Percentage', 'What type of contract?', True, False, 0.15,  24, 12, 20],
#    'currentEmp10p2':['bar', 'currentEmp10p2.csv', 'percentage', False, 0, 15, 'Percentage', 'What type of contract?', True, False, 0.15,  24, 12, 20],
#    'rse1':['bar', 'rse1.csv', 'percentage', False, 0, 15, 'Percentage', 'Do you write code?', True, False, 0.15,  24, 12, 20],
#    'rse3':['bar', 'rse3.csv', 'percentage', False, 0, 15, 'Percentage', 'Who uses your code?', True, False, 0.15,  24, 14, 20],
#    'paper1':['bar', 'paper1.csv', 'percentage', False, 0, 15, 'Percentage', 'Has your code contributed to a publication?', True, False, 0.15,  24, 14, 20],
#    'paper1p2':['bar', 'paper1p2.csv', 'percentage', False, 0, 15, 'Percentage', 'Were you acknowledged?', True, False, 0.15,  24, 14, 20],
#    'train1':['bar', 'train1.csv', 'percentage', False, 0, 15, 'Percentage', 'Have you trained researchers?', True, False, 0.15,  24, 14, 20],
#    'stability1':['bar', 'stability1.csv', 'percentage', False, 0, 15, 'Percentage', 'Bus factor', True, False, 0.15,  24, 14, 20],
#    'stability2':['bar', 'stability2.csv', 'percentage', False, 0, 15, 'Percentage', 'Technical handover plan?', True, False, 0.15,  24, 14, 20],
#    'stability3':['bar', 'stability3.csv', 'percentage', False, 0, 15, 'Percentage', 'Have you released under Open Source?', True, False, 0.15,  24, 14, 20]
    'socio3':['line', 'socio3.csv', 'percentage', False, 45, 10, 'Percentage', 'Age', True, False, 0.2,  24, 14, 20],
#    'socio2':['bar', 'socio2.csv', 'percentage', False, 0, 15, 'Percentage', 'Gender', True, False, 0.15,  24, 14, 20],
#    'socio5':['bar', 'socio5.csv', 'percentage', False, 45, 15, 'Percentage', 'Ethnic origin', True, False, 0.3,  24, 14, 20],
    }