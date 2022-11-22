from datetime import datetime
import time

def format_datetime(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')
    
def format_compact_datetime(dt):
    return dt.strftime('%Y%m%d%H%M%S')

def format_date(dt):
    return dt.strftime('%Y-%m-%d')

def format_sql_datetime(dt):
    return str(dt) if isinstance(dt, datetime) else dt

def format_time_ms(float_time):
    local_time = time.localtime(float_time)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (float_time - int(float_time)) * 1000
    return "%s.%03d" % (data_head, data_secs)