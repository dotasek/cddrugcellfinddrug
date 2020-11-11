FROM continuumio/miniconda3

RUN conda install -y pytorch torchvision cpuonly -c pytorch

RUN mkdir /tmp/drugcell
COPY dist/*.whl /tmp/drugcell/

RUN pip install /tmp/drugcell/drugcellfinddrug*whl

RUN rm -rf /tmp/drugcell

RUN mkdir /opt/drugcell



ENTRYPOINT ["/opt/conda/bin/drugcellfinddrugcmd.py"]
CMD ["--help"]
