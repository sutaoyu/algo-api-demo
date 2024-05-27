#!/bin/bash
gunicorn -D -c gunicorn.py main:app -n Algo_Backend
