from datetime import datetime

def format_datetime(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def format_date(dt):
    return dt.strftime('%Y-%m-%d')

def format_sql_datetime(dt):
    return str(dt) if isinstance(dt, datetime) else dt