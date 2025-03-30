FROM python:3.12-slim

WORKDIR /latency-checker

COPY . .

RUN pip install -r requirements.txt

RUN echo "alias latency-checker='python /latency-checker/latency_checker_edit.py'" >> ~/.bashrc
RUN echo "alias lc='python /latency-checker/latency_checker_edit.py'" >> ~/.bashrc
RUN echo "source ~/.bashrc"