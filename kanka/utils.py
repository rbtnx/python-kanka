"""
:mod: `kanka.utils` - Helper functions
"""

from datetime import datetime

def to_datetime(dict_date):
    """
    Convert json date entry to datetime.
    """
    t = dict_date.split(".")[0]
    return datetime.strptime(t, "%Y-%m-%dT%H:%M:%S")
