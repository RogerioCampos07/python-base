#!/usr/bin/env python3

import os

current_language = os.getenv("LANG")[:5]

msg = 'Hello, world'

if current_language == 'pt_BR':
    msg = 'Olá mundo'
elif current_language == 'it_IT':
    msg = 'Ciao, Mondo'

print(msg)