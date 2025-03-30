FROM python:3.12-slim

WORKDIR /latency-checker

COPY ./requirements.txt ./requirements.txt
COPY ./latency_checker_edit.py ./latency_checker.py

RUN pip install -r requirements.txt

RUN echo "alias latency-checker='python /latency-checker/latency_checker.py'" >> ~/.bashrc
RUN echo "alias lc='python /latency-checker/latency_checker.py'" >> ~/.bashrc
RUN echo "source ~/.bashrc"