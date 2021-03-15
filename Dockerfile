FROM python

RUN pip install python-sonarqube-api tqdm

WORKDIR /app
COPY init-sonar.py .
