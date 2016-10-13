#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/cybertronics.techtatva.in/")

from public_html import app as application
application.secret_key = 'ZRY235435Y6GBHYIU$%^%&^I^&*Dctuvybu^&CT23456'
