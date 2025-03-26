from logging import getLogger, config
import json
import os
import traceback

script_dir = os.path.dirname(os.path.abspath(__file__))
logfile_path = os.path.join(script_dir, 'logger.log')
conf_path = os.path.join(script_dir, 'logger_conf.json')
with open(conf_path, 'r', encoding="utf-8") as f:
    config_param = json.load(f)

print(logfile_path)
config_param['handlers']['file_handler']['filename'] = logfile_path

config.dictConfig(config_param)

stream_logger = getLogger("stream_logger")
file_logger = getLogger("file_logger")

try:
    stream_logger.info('This is a log message')
    1 / 0
except Exception as e:
    stream_logger.error('An error occurred')
    stack_trace = traceback.format_exc()
    file_logger.error('stack trace: %s', stack_trace)
