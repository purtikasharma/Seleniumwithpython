# Logging means - You can add logs to the Failure, Information, Error
# Warning to the Users

import logging


def test_print_logs():
    #logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
    LOGGER = logging.getLogger(__name__)
    LOGGER.debug('This message should go to the log file')
    LOGGER.info('So should this')
    LOGGER.warning('And this, too')
    LOGGER.error('And non-ASCII stuff, too, like Øresund and Malmö')
