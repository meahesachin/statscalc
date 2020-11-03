FROM python:3.7

ADD . .
ADD Tests/testdata /testdata

run pip install --upgrade pip

cmd ["python", "-m", "unittest", "discover", "-s", "Tests"]
