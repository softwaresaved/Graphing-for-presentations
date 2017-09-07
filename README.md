# Graphing for presentations

## Summary

I'm getting tired of never getting the kind of charts I want out of Matplotlib. It\'s so damned fiddly. I put this together to do plotting in a way that I need for presentations and things. At the moment, it works on a set of csvs, but it could easily be copied into existing code.

## What's what?

There are two folders: data and output.

* Data: holds a set of csv files that you want plotted.
* Output: holds a set of pngs
* ```chart_details_lookup.py``` is a lookup table. It tells the script which csvs you want plotted and how you want them plotted (more details below).
* ```graphing.py``` is the script that produces the charts based on the details in the lookup table.
* ```requirements.txt``` holds the details of the libraries used by the scripts

## Set up

### Prepare for running Python:

Prepare for running Python:
1. If not already installed, [install virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/):
   * ```pip install virtualenv```
1. Create a project folder:
   * ```virtualenv -p <location of Python3 install directory> <name of project>```
1. Activate the virtual environment:
   * ```source <name of project>/bin/activate ```
1. Install libraries:
   * ```pip install -r requirements.txt ```
   
 ### Set up the lookup file

 ```chart_details_lookup.py``` holds all details about the plots you want.
 
1. At the top of the lookup are ```global_specs``` that specify the size of the charts, the resolution of the saved charts, and the font used in the charts. Change these to suit your preferences.
1. ```plot_details``` is set up as a dictionary of dictionaries. It contains all data about the charts you want. It's liable to change, but the current set up is as follows:

```
     '<name of chart>': {
            'filename': 'foo.csv',     # the name of the csv in the data directory
            'plot_type': 'bar',           # currently only does bar charts, but this will change in the future
            'y1_axis': 'percentage',      # Name of the column you want plotted
            'y2_axis': False,             # Name of a second column you want plotted (or False, if there isn't one)
            'x_title': False,             # A title for the x-axis, or False if you don't want a title
            'x_rot': 0,                   # Rotation of x-axis tick labels (0 is horizontal)
            'x_max_len': 15,              # Max length of x-axis tick labels before they start a new line
            'y_title': 'Percentage',      # Title for y axis, or use False if you don't want a title
            'chart_title': 'Which OS do you use at work?',     # Chart title, or use False if you don't want a title
            'show_values': True,          # If True, show value on bars, if False, nothing
            'skip_labels': False,         # If False, print all x-axis labels. If set to a number, print an x-tick label, then skip that number of labels before printing the next x-axis label. (Allows you to deal with having too many x-tick labels to show neatly).
            'bottom_size': 0.15,          # Fraction of chart dedicated to x-axis tick labels (must be in range 0 - 1)
            'title_font_size': 24,        # Size of title font
            'axis_font_size': 14,         # Size of axis fonts
            'value_font_size': 20         # Size of value label font
             },
```

### Create charts

1. If you want to see the charts as they are created, open ```python graphing.py``` and uncomment the following line:
 * ```#    plt.show()```
 * Note: you will now have to close each chart after it's opened by the script
1. Run the script:
 * ```python graphing.py```
1. Your charts will appear in the output folder as png files.

### Archiving

Once you're finished, you can archive your files by copying the ```chart_details_lookup.py``` file, and the ```data``` and ```output``` directories into the ```archived_presentations``` directory under an appriately named sub-directory.
