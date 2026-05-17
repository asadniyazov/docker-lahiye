# ========================================================
#  Stage 1 – Builder
# ========================================================
FROM python:3.10-slim AS builder

WORKDIR /build

COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# ========================================================
#  Stage 2 – Runtime
# ========================================================
FROM python:3.10-slim AS runtime

LABEL org.opencontainers.image.title="Asad Task Manager"
LABEL org.opencontainers.image.version="1.0.0"

# Kitabxanaları köçürürük
COPY --from=builder /install /usr/local

WORKDIR /app

# Requirements yüklənir
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Layihə strukturunu olduğu kimi qorumaq üçün hər şeyi nöqtə ilə köçürürük:
COPY . .

ENV PORT=5000

EXPOSE 5000

# Gunicorn ilə işə salırıq
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT} --workers 1 run:app"]