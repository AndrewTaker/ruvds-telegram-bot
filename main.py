import logging
import bot
import os
import sys

DEFAULT_APP_LOG_NAME: str = "BOT"


def check_variables() -> list[str]:
    required = [
        "BOT_TOKEN",
        "RUVDS_TOKEN",
        "SERVER_ID",
        "PAYMENT_URL",
    ]

    missing_vars = [var for var in required if not os.getenv(var)]
    return missing_vars


def set_up_logging() -> logging.Logger:
    logger = logging.getLogger(DEFAULT_APP_LOG_NAME)

    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        logger.propagate = False

    return logger


def main():
    missing_variables = check_variables()
    if missing_variables:
        sys.exit(f"missing vars {' '.join(missing_variables)}")

    logger = set_up_logging()
    logger.info("logger instanciated, main start")

    bot.run_bot()


if __name__ == "__main__":
    main()
