import json
import sys
from lib.logic import load_data, load_watchlist, load_config
from lib.plotter import plot_case_pct, plot_case_pct_anim

ecdc_api = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"
config = load_config('config.ini')
watchlist = load_watchlist('data/watchlist.json')
comparison_countries = ["China"] # baseline countries to compare to in all plots


cmd_args = sys.argv
if (len(cmd_args) > 1):

    if "-a" in cmd_args:
        # output an animated graph
        data, curr_date, start_date = load_data(ecdc_api, cached_date=config["cached_date"], trim_start=False, metric=config["metric"])
        plot_case_pct_anim(data, watchlist, comparison_countries, start_date, fps=config["fps"], metric=config["metric"])

    elif "-o" in cmd_args:
        # render an animated video
        data, curr_date, start_date = load_data(ecdc_api, cached_date=config["cached_date"], trim_start=False, metric=config["metric"])
        plot_case_pct_anim(data, watchlist, comparison_countries, start_date, fps=config["fps"], metric=config["metric"], render=True)
else:
    # graph cases as a percentage of population by day since the first reported case
    # for each of our regions - see watchlist.json
    data, curr_date, start_date = load_data(ecdc_api, cached_date=config["cached_date"], trim_start=True, metric=config["metric"])
    plot_case_pct(data, watchlist, comparison_countries, curr_date, metric=config["metric"])