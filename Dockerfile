FROM python:3.9-slim
WORKDIR /app
COPY microbiome_analysis.py /app/microbiome_analysis.py
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "microbiome_analysis.py"]