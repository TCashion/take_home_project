# The python image is only pinned to a minor version without defining a particular distribution. 
# This means that a different distribution might be pulled in between builds, which may lead to issues.
# Also, slim distributions are lighter weight (~1.25GB vs ~300MB). 
# We should leave the patch version undefined, though, so that new builds pull in the latest patch. 
FROM python:3.12-slim-bookworm

WORKDIR /app

# We should install dependencies before copying files so that image cacheing works correctly for dependencies. 
# I found this here: https://hasura.io/blog/how-to-write-dockerfiles-for-python-web-apps-6d173842ae1d
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COPY . . copies everything, including tests, readme, etc. into the production build, which is unnecessary.
COPY /src /src

CMD ["python", "src/adls_client.py"]