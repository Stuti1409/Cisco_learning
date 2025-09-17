"""
logger.py

This module configures application-wide logging for the Hospital Management System.
All logs are stored in 'hospital_app_logs.log' with timestamps and log levels.
"""

import logging

logging.basicConfig(
    filename="hospital_app_logs.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)
