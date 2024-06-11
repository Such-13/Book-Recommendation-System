import logging

def setup_logging():
    # Clear any existing handlers associated with the root logger
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("app.log", mode='w'),  # Overwrite the log file each time
            logging.StreamHandler()
        ]
    )
