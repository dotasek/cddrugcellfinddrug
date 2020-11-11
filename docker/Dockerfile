FROM continuumio/miniconda3

RUN conda install -y pytorch torchvision cpuonly -c pytorch

RUN mkdir /tmp/cdgprofiler
COPY dist/*.whl /tmp/cdgprofiler/

RUN pip install /tmp/cdgprofiler/cdgprofilergenestoterm*whl

RUN rm -rf /tmp/cdgprofiler

RUN mkdir /opt/drugcell

ENTRYPOINT ["/opt/conda/bin/cdgprofilergenestotermcmd.py"]
CMD ["--help"]
