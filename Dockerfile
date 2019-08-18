FROM python:3.6-alpine

WORKDIR /app

COPY . .

RUN apk --no-cache add curl

RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 8000

ENV PYTHONPATH "${PYTHONPATH}:src"

CMD ["pipenv", "run", "gunicorn", "web.start:app"]
