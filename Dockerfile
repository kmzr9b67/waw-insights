FROM python:3.11-slim

# Step 2. Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . $APP_HOME

# Step 3. Install production dependencies.
RUN pip install -r requirements.txt

# Step 4: Run the web service on container startup using gunicorn webserver.
CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker --timeout 0 --threads 8 main:app
