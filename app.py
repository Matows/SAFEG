#!/usr/bin/env python3    
# -*- coding: utf-8 -*-

import website
from threading import Thread

try:
    webserver = Thread(target=website.run, daemon=False)
    webserver.start()
    webserver.join() #?
except KeyboardInterrupt:
    exit()
