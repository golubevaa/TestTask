import logging
from typing import Callable
from allure import step as allure_step


logger = logging.getLogger(__name__)


def step_with_logging(description: str) -> Callable:
    def decorated_step(func: Callable) -> Callable:

        def wrap(*args, **kwargs):
            step_description = description.format(*args[1:], **kwargs) if "{}" in description  \
                else description
            with allure_step(step_description):
                logger.info(step_description)
                return func(*args, **kwargs)

        return wrap
    return decorated_step
