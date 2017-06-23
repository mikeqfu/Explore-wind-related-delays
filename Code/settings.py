""" Settings """

from matplotlib import pyplot, rcParamsDefault
from numpy.core import arrayprint
from pandas import reset_option, set_option


# Set preferences for displaying results =============================================================================
def pd_preferences(reset=False):
    if not reset:
        set_option('expand_frame_repr', False)  # Set the representation of DataFrame NOT to wrap
        set_option('display.width', 560)  # Set the display width
        # set_option('precision', 4)
        set_option('display.max_columns', 100)
        set_option('display.max_rows', 10)
        set_option('io.excel.xlsx.writer', 'xlsxwriter')
        set_option('mode.chained_assignment', None)
    else:
        reset_option('all')


# Set preferences for displaying results =============================================================================
def np_preferences(reset=False):
    if not reset:
        arrayprint._line_width = 120
    else:
        arrayprint._line_width = 80  # 75


# Set preferences for plotting =======================================================================================
def mpl_preferences(use_cambria=False, reset=False):
    """

    # import matplotlib as mpl
    # mpl.rc('font', family='Times New Roman')

    # Get a list of supported file formats for matplotlib savefig() function
    # plt.gcf().canvas.get_supported_filetypes()
    # plt.gcf().canvas.get_supported_filetypes_grouped()
    # (Aside: "gcf" is short for "get current fig" manager)

    """
    if not reset:
        pyplot.style.use('ggplot')
        if use_cambria:  # Use the font, 'Cambria'
            # Set 'font.family' to 'serif', so that matplotlib will use that list
            pyplot.rcParams['font.family'] = 'serif'
            # Add 'Cambria' to the front of the 'font.serif' list
            pyplot.rcParams['font.serif'] = ['Cambria'] + pyplot.rcParams['font.serif']
            pyplot.rcParams['font.serif'] = ['Cambria Math'] + pyplot.rcParams['font.serif']
        pyplot.rcParams['font.size'] = 13
        pyplot.rcParams['font.weight'] = 'normal'
        pyplot.rcParams['legend.labelspacing'] = 0.85
        # pyplot.rcParams['hatch.linewidth'] = 2.2
        # pyplot.rcParams['hatch.color'] = '#dcdcdc'
        # pyplot.rcParams['legend.scatterpoints'] = 1
    else:
        pyplot.style.use('classic')
        pyplot.rcParams = rcParamsDefault


pd_preferences(reset=False)
np_preferences(reset=False)
mpl_preferences(use_cambria=True, reset=False)
