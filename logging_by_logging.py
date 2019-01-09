import logging

"""
We usually use print to log messages. The logging is better than print because:
1. Easy to put a timestamp in each message
2. Different levels, easy to filter
3. Can separate log messages from real print
4. Easy to print log on screen and save log in files.

"""


def init_logger():
    # logger is a global var, call init_logger at begin of your program.
    _logger = logging.getLogger()
    _logger.setLevel(logging.DEBUG)

    # define log formatter
    """
    %a  Locale’s abbreviated weekday name.   
    %A  Locale’s full weekday name.  
    %b  Locale’s abbreviated month name.     
    %B  Locale’s full month name.    
    %c  Locale’s appropriate date and time representation.   
    %d  Day of the month as a decimal number [01,31].    
    %H  Hour (24-hour clock) as a decimal number [00,23].    
    %I  Hour (12-hour clock) as a decimal number [01,12].    
    %j  Day of the year as a decimal number [001,366].   
    %m  Month as a decimal number [01,12].   
    %M  Minute as a decimal number [00,59].  
    %p  Locale’s equivalent of either AM or PM. (1)
    %S  Second as a decimal number [00,61]. (2)
    %U  Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.    (3)
    %w  Weekday as a decimal number [0(Sunday),6].   
    %W  Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.    (3)
    %x  Locale’s appropriate date representation.    
    %X  Locale’s appropriate time representation.    
    %y  Year without century as a decimal number [00,99].    
    %Y  Year with century as a decimal number.   
    %z  Time zone offset indicating a positive or negative time difference from UTC/GMT of the form +HHMM or -HHMM, where H represents decimal hour digits and M represents decimal minute digits [-23:59, +23:59].  
    %Z  Time zone name (no characters if no time zone exists).   
    %%  A literal '%' character.     
    """
    date_fmt_str = '%Y-%m-%d %H:%M:%S'
    log_fmt_str = '[%(levelname)s] [%(asctime)s.%(msecs)03d] [%(module)s %(filename)s %(lineno)s %(funcName)30s()] : %(message)s'
    formatter = logging.Formatter(fmt=log_fmt_str, datefmt=date_fmt_str)

    # log to file by adding file handler
    fh = logging.FileHandler('test_logging_demo.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    _logger.addHandler(fh)

    # log on screen by adding stream handler
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(formatter)
    _logger.addHandler(sh)


def test_logger():
    logger_in_func = logging.getLogger()
    logger_in_func.info("in test logger")


if __name__ == '__main__':
    init_logger()
    logger = logging.getLogger()
    logger.debug('hello world')
    test_logger()

