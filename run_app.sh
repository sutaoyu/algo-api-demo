#!/bin/bash
gunicorn -D -c gunicorn.py app.main:app -n Algo_Backend
