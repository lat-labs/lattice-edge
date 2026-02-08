FROM rayproject/ray:2.9.0

USER root

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages for detection
RUN pip install --no-cache-dir \
    ultralytics \
    opencv-python-headless \
    pillow \
    torch torchvision --index-url https://download.pytorch.org/whl/cpu

# Create directories
RUN mkdir -p /app/models /app/cache

# Copy Ray service code
COPY ray_services/ /app/ray_services/
WORKDIR /app

# Set Python path
ENV PYTHONPATH=/app:$PYTHONPATH

USER ray

# Start Ray head with runtime environment
CMD ["ray", "start", "--head", \
     "--port=6379", \
     "--dashboard-host=0.0.0.0", \
     "--dashboard-port=8265", \
     "--num-cpus=2", \
     "--block"]