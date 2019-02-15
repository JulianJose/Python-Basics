#!/usr/bin/python3
#
# regex.py: Um programa para brincar com expressões regulares.

import re

phone_number_regex = re.compile(r'([0-9]{3}-){2}[0-9]{4}')

phone_number_regex.search("O número é 999-1234")
