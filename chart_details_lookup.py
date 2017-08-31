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
 0. the file in which the data  is stored
 1. which column to plot
 2. title for x axis, or use False if no title to be shown
 3. rotation of x-axis tick labels (0 is horizontal)
 4. max length of x-axis tick labels before they start a new line
 5. title for y axis, or use False if no title to be shown
 6. title of chart, or use False if no title
 7. whether to show value labels on bars (True/False)
 8. how labels to remove after each one shown (or False to keep all)
 9. fraction of chart dedicated to x-axis tick labels (0-1)
10. size of title font
11. size of axis fonts
12. size of value label font
'''

plot_details = {
#    'edu1':['edu1.csv', 'percentage', False, 0, 15, 'Percentage', 'Education level', True, 0.1, False,  24, 14, 24],
#    'edu2':['edu2.csv', 'percentage', False, 90, 20, 'Percentage', 'Education background', False, False, 0.3, 24, 10, 14],
#    'edu2p2':['edu2p2.csv', 'percentage', False, 90, 15, 'Percentage', 'Top 10 backgrounds', True, False, 0.28,  24, 14, 20],
#    'currentEmp1':['currentEmp1.csv', 'percentage', False, 45, 15, 'Percentage', 'Where do you work?', True, False, 0.28,  24, 12, 20],
#    'currentEmp13':['currentEmp13.csv', 'percentage', False, 90, 15, 'Percentage', 'In which field do you work?', False, 2, 0.28,  24, 12, 20],
#    'currentEmp13p2':['currentEmp13p2.csv', 'percentage', False, 90, 15, 'Percentage', 'To 10 fields of work', True, False, 0.28,  24, 12, 20],
#    'currentEmp10':['currentEmp10.csv', 'percentage', False, 0, 15, 'Percentage', 'What type of contract?', True, False, 0.15,  24, 12, 20],
#    'currentEmp10p2':['currentEmp10p2.csv', 'percentage', False, 0, 15, 'Percentage', 'What type of contract?', True, False, 0.15,  24, 12, 20],
#    'rse1':['rse1.csv', 'percentage', False, 0, 15, 'Percentage', 'Do you write code?', True, False, 0.15,  24, 12, 20],
#    'rse3':['rse3.csv', 'percentage', False, 0, 15, 'Percentage', 'Who uses your code?', True, False, 0.15,  24, 14, 20],
#    'paper1':['paper1.csv', 'percentage', False, 0, 15, 'Percentage', 'Has your code contributed to a publication?', True, False, 0.15,  24, 14, 20],
#    'paper1p2':['paper1p2.csv', 'percentage', False, 0, 15, 'Percentage', 'Were you acknowledged?', True, False, 0.15,  24, 14, 20],
#    'train1':['train1.csv', 'percentage', False, 0, 15, 'Percentage', 'Have you trained researchers?', True, False, 0.15,  24, 14, 20],
#    'stability1':['stability1.csv', 'percentage', False, 0, 15, 'Percentage', 'Bus factor', True, False, 0.15,  24, 14, 20],
#    'stability2':['stability2.csv', 'percentage', False, 0, 15, 'Percentage', 'Technical handover plan?', True, False, 0.15,  24, 14, 20],
#    'stability3':['stability3.csv', 'percentage', False, 0, 15, 'Percentage', 'Have you released under Open Source?', True, False, 0.15,  24, 14, 20]
#    'socio3':['socio3.csv', 'percentage', False, 45, 10, 'Percentage', 'Age', True, False, 0.2,  24, 14, 20],
#    'socio2':['socio2.csv', 'percentage', False, 0, 15, 'Percentage', 'Gender', True, False, 0.15,  24, 14, 20],
    'socio5':['socio5.csv', 'percentage', False, 45, 15, 'Percentage', 'Ethnic origin', True, False, 0.3,  24, 14, 20]
    }