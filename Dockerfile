FROM python:3.9-slim

# Create user
RUN useradd -m -u 1000 user
# Set environment for pip
ENV PATH="/home/user/.local/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TRANSFORMERS_NO_ADVISORY_WARNINGS=1 \
    HF_HUB_DISABLE_SYMLINKS_WARNING=1
USER user
WORKDIR /app

# Install dependencies
COPY --chown=user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy source
COPY --chown=user . /app

# Start with thread worker, increased timeout
CMD ["gunicorn", "-w", "1", "-k", "gthread", "-t", "300", "-b", "0.0.0.0:7860", "app:app"]