FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install rdkit==2022.9.3
RUN pip install datamol==0.8.8

WORKDIR /repo
COPY . /repo
