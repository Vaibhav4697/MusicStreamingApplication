"""
Copyright (c) 2016-2019 we-get developers (https://github.com/rachmadaniHaryono/we-get/)
See the file 'LICENSE' for copying permission
"""

from we_get.core.we_get import WG
from we_get.core.utils import msg_error


def main():
    we_get = WG()
    we_get.parse_arguments()
    try:
        we_get.start()
    except (EOFError, KeyboardInterrupt):
        msg_error("[KeyboardInterrupt]", True)
