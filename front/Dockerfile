FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY front/ /app/front/
WORKDIR /app/front
CMD streamlit run front.py --server.address 0.0.0.0 --server.port $PORT
