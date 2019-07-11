#!/bin/bash
python src/step1/webserver.py & sleep 0.1s & src/step1/student.py & sleep 0.1s & python src/step1/client.py
sleep 1s
python src/step1/webserver.py & sleep 0.1s & src/step1/student.py & sleep 0.1s & python src/step1/client.py