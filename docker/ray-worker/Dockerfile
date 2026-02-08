FROM rayproject/ray:2.9.0

USER root

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install detection requirements
COPY docker/ray-worker/requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Create directories
RUN mkdir -p /app/models /app/cache

# Copy Ray service code
COPY ray_services/ /app/ray_services/
WORKDIR /app

# Set Python path
ENV PYTHONPATH=/app:$PYTHONPATH

USER ray

# Worker startup will be handled by docker-compose
CMD ["ray", "start", "--address=ray-head:6379", "--block"]