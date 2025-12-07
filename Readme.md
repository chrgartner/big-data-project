big data project about sourcing and quantifying ai-generated websites in the www.

# Setup
on first launch run
- docker compose build
- docker compose up

these containers provide a python environment, you need to run scripts manually

# Workflow
to install packages use
- docker exec -it container-name /bin/bash
to connect to the container
run pip install package-name

# Git
after pulling restart your containers with
- docker compose build
- docker compose up
# IF requirements.txt changed