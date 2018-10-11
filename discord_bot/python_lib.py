def log(message, log_severity, logger_obj):

    if log_severity is 'info':
        logger_obj.info(message)
        print(message)
    elif log_severity is 'error':
        logger_obj.error(message)
        print(message)
    else:
        logger_obj.error('Invalid logging severity passed to log method, please pass info or error')
        print('Invalid logging severity passed to log method, please pass info or error')
        return None
