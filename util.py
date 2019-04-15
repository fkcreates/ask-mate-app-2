import data_manager
import connection
from datetime import datetime


def vote_up_or_down(vote_number, vote_type):
    if vote_type == 'up':
        vote_number['vote_number'] += 1
    else:
        vote_number['vote_number'] -= 1
    return vote_number['vote_number']



'''def sort_data_by_time(data):
    sorted_data = sorted(data, key=lambda x: x["submission_time"], reverse=True)

    return sorted_data'''


