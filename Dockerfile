FROM python:3.7

ADD . .

run pip install --upgrade pip

cmd ["python", "-m", "unittest", "discover", "-s", "Tests"]
