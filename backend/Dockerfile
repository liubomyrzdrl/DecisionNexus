FROM python:3.13-slim

WORKDIR /app
# Встановлюємо uv
RUN pip install uv

# Копіюємо тільки залежності (для кешу)
COPY pyproject.toml uv.lock ./

# Встановлюємо залежності
RUN uv sync --frozen

# Копіюємо код
COPY . .

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]