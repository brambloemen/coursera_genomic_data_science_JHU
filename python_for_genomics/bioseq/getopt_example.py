import sys
import getopt


def get_start_and_end_dates():
    start_date = None
    end_date = None

    # first argument is the filename with an index of 0
    # so, we want to start with an index value of 1: other options
    argv = sys.argv[1:]

    try:
        # getopt method parses the options from the command line
        # colons indicate that option reauires us to input value
        opts, args = getopt.getopt(argv, "s:e:", ["start_date=", "end_date="])
    except getopt.GetoptError as err:
        print(err)  # will print something like "option -a not recognized"

    for opt, arg in opts:
        if opt in ["-s", "--start_date"]:
            start_date = arg
        elif opt in ["-e", "--end_date"]:
            end_date = arg

    print('start_date: {}'.format(start_date))
    print('end_date: {}'.format(end_date))


get_start_and_end_dates()
