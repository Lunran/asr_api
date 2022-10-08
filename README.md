# What's this?

- Flask API to use ASR engine
- Supposed to be used with https://github.com/Lunran/sts_cli


# Prerequisites

- Ubuntu 18.04.5 LTS


# How to setup

- Get source codes
  - $ git clone https://github.com/Lunran/asr_api.git
  - $ cd asr_api
- Install modules
  - $ python3 -m venv venv
  - $ . venv/bin/activate
  - $ pip install --upgrade pip
  - $ pip install -r requirements.txt
  - $ uudo apt install ffmpeg


# How to use

- $ python main.py
- $ curl -X POST -F file=@./tmp.wav http://localhost:8003/asr
