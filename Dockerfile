FROM apache/airflow:2.5.3

USER root


# Set JAVA_HOME
ENV JAVA_HOME /opt/airflow/jdk8/
RUN export JAVA_HOME

USER airflow

# install pip Requirements (작성된 requirements.txt 파일에 있는 패키지들을 일괄 설치한다.)
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
