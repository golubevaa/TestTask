from typing import Callable
from venv import logger

from allure import step as allure_step

def step_with_logging(description: str) -> Callable:
    def decorated_step(func: Callable) -> Callable:

        def wrap(*args, **kwargs):
            step_description = description
            if "{}" in description:
                step_description = description.format(*args[1:], **kwargs)
            with allure_step(step_description):
                logger.info(step_description)
                return func(*args, **kwargs)

        return wrap
    return decorated_step

