import logging

# Logging configuration
def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename="amazon_flow_logs.log",
        filemode="w"
    )