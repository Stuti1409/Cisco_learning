import logging 
# setup 
logging.basicConfig(
    filename = "flight_app_logs.log",
    level = logging.INFO,
    format = "%(asctime)s [%(levelname)s] %(message)s"
)