{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Samarth375-hub/Emotion-detection-classifier/blob/main/app.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ItylHdUOpNpf",
        "outputId": "4acf1ae7-e9bd-421a-b156-d900860e6602"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting gradio\n",
            "  Downloading gradio-4.38.1-py3-none-any.whl (12.4 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m12.4/12.4 MB\u001b[0m \u001b[31m18.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting aiofiles<24.0,>=22.0 (from gradio)\n",
            "  Downloading aiofiles-23.2.1-py3-none-any.whl (15 kB)\n",
            "Collecting altair<6.0,>=5.0 (from gradio)\n",
            "  Downloading altair-5.3.0-py3-none-any.whl (857 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m857.8/857.8 kB\u001b[0m \u001b[31m24.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting fastapi (from gradio)\n",
            "  Downloading fastapi-0.111.1-py3-none-any.whl (92 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m92.2/92.2 kB\u001b[0m \u001b[31m15.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting ffmpy (from gradio)\n",
            "  Downloading ffmpy-0.3.2.tar.gz (5.5 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Collecting gradio-client==1.1.0 (from gradio)\n",
            "  Downloading gradio_client-1.1.0-py3-none-any.whl (318 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m318.1/318.1 kB\u001b[0m \u001b[31m15.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting httpx>=0.24.1 (from gradio)\n",
            "  Downloading httpx-0.27.0-py3-none-any.whl (75 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m75.6/75.6 kB\u001b[0m \u001b[31m12.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: huggingface-hub>=0.19.3 in /usr/local/lib/python3.10/dist-packages (from gradio) (0.23.5)\n",
            "Requirement already satisfied: importlib-resources<7.0,>=1.3 in /usr/local/lib/python3.10/dist-packages (from gradio) (6.4.0)\n",
            "Requirement already satisfied: jinja2<4.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (3.1.4)\n",
            "Requirement already satisfied: markupsafe~=2.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (2.1.5)\n",
            "Requirement already satisfied: matplotlib~=3.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (3.7.1)\n",
            "Requirement already satisfied: numpy<3.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (1.25.2)\n",
            "Collecting orjson~=3.0 (from gradio)\n",
            "  Downloading orjson-3.10.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (141 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m141.1/141.1 kB\u001b[0m \u001b[31m13.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: packaging in /usr/local/lib/python3.10/dist-packages (from gradio) (24.1)\n",
            "Requirement already satisfied: pandas<3.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (2.0.3)\n",
            "Requirement already satisfied: pillow<11.0,>=8.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (9.4.0)\n",
            "Requirement already satisfied: pydantic>=2.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (2.8.2)\n",
            "Collecting pydub (from gradio)\n",
            "  Downloading pydub-0.25.1-py2.py3-none-any.whl (32 kB)\n",
            "Collecting python-multipart>=0.0.9 (from gradio)\n",
            "  Downloading python_multipart-0.0.9-py3-none-any.whl (22 kB)\n",
            "Requirement already satisfied: pyyaml<7.0,>=5.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (6.0.1)\n",
            "Collecting ruff>=0.2.2 (from gradio)\n",
            "  Downloading ruff-0.5.3-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (10.1 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m10.1/10.1 MB\u001b[0m \u001b[31m25.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting semantic-version~=2.0 (from gradio)\n",
            "  Downloading semantic_version-2.10.0-py2.py3-none-any.whl (15 kB)\n",
            "Collecting tomlkit==0.12.0 (from gradio)\n",
            "  Downloading tomlkit-0.12.0-py3-none-any.whl (37 kB)\n",
            "Requirement already satisfied: typer<1.0,>=0.12 in /usr/local/lib/python3.10/dist-packages (from gradio) (0.12.3)\n",
            "Requirement already satisfied: typing-extensions~=4.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (4.12.2)\n",
            "Requirement already satisfied: urllib3~=2.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (2.0.7)\n",
            "Collecting uvicorn>=0.14.0 (from gradio)\n",
            "  Downloading uvicorn-0.30.1-py3-none-any.whl (62 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.4/62.4 kB\u001b[0m \u001b[31m7.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: fsspec in /usr/local/lib/python3.10/dist-packages (from gradio-client==1.1.0->gradio) (2023.6.0)\n",
            "Collecting websockets<12.0,>=10.0 (from gradio-client==1.1.0->gradio)\n",
            "  Downloading websockets-11.0.3-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (129 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m129.9/129.9 kB\u001b[0m \u001b[31m11.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<6.0,>=5.0->gradio) (4.19.2)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<6.0,>=5.0->gradio) (0.12.1)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.10/dist-packages (from httpx>=0.24.1->gradio) (3.7.1)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx>=0.24.1->gradio) (2024.7.4)\n",
            "Collecting httpcore==1.* (from httpx>=0.24.1->gradio)\n",
            "  Downloading httpcore-1.0.5-py3-none-any.whl (77 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m77.9/77.9 kB\u001b[0m \u001b[31m6.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: idna in /usr/local/lib/python3.10/dist-packages (from httpx>=0.24.1->gradio) (3.7)\n",
            "Requirement already satisfied: sniffio in /usr/local/lib/python3.10/dist-packages (from httpx>=0.24.1->gradio) (1.3.1)\n",
            "Collecting h11<0.15,>=0.13 (from httpcore==1.*->httpx>=0.24.1->gradio)\n",
            "  Downloading h11-0.14.0-py3-none-any.whl (58 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m58.3/58.3 kB\u001b[0m \u001b[31m5.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.19.3->gradio) (3.15.4)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.19.3->gradio) (2.31.0)\n",
            "Requirement already satisfied: tqdm>=4.42.1 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.19.3->gradio) (4.66.4)\n",
            "Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib~=3.0->gradio) (1.2.1)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.10/dist-packages (from matplotlib~=3.0->gradio) (0.12.1)\n",
            "Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.10/dist-packages (from matplotlib~=3.0->gradio) (4.53.1)\n",
            "Requirement already satisfied: kiwisolver>=1.0.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib~=3.0->gradio) (1.4.5)\n",
            "Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.10/dist-packages (from matplotlib~=3.0->gradio) (3.1.2)\n",
            "Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.10/dist-packages (from matplotlib~=3.0->gradio) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3.0,>=1.0->gradio) (2023.4)\n",
            "Requirement already satisfied: tzdata>=2022.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3.0,>=1.0->gradio) (2024.1)\n",
            "Requirement already satisfied: annotated-types>=0.4.0 in /usr/local/lib/python3.10/dist-packages (from pydantic>=2.0->gradio) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.20.1 in /usr/local/lib/python3.10/dist-packages (from pydantic>=2.0->gradio) (2.20.1)\n",
            "Requirement already satisfied: click>=8.0.0 in /usr/local/lib/python3.10/dist-packages (from typer<1.0,>=0.12->gradio) (8.1.7)\n",
            "Requirement already satisfied: shellingham>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from typer<1.0,>=0.12->gradio) (1.5.4)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.10/dist-packages (from typer<1.0,>=0.12->gradio) (13.7.1)\n",
            "Collecting starlette<0.38.0,>=0.37.2 (from fastapi->gradio)\n",
            "  Downloading starlette-0.37.2-py3-none-any.whl (71 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m71.9/71.9 kB\u001b[0m \u001b[31m1.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting fastapi-cli>=0.0.2 (from fastapi->gradio)\n",
            "  Downloading fastapi_cli-0.0.4-py3-none-any.whl (9.5 kB)\n",
            "Collecting email_validator>=2.0.0 (from fastapi->gradio)\n",
            "  Downloading email_validator-2.2.0-py3-none-any.whl (33 kB)\n",
            "Collecting dnspython>=2.0.0 (from email_validator>=2.0.0->fastapi->gradio)\n",
            "  Downloading dnspython-2.6.1-py3-none-any.whl (307 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m307.7/307.7 kB\u001b[0m \u001b[31m26.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6.0,>=5.0->gradio) (23.2.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6.0,>=5.0->gradio) (2023.12.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6.0,>=5.0->gradio) (0.35.1)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6.0,>=5.0->gradio) (0.19.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.7->matplotlib~=3.0->gradio) (1.16.0)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->typer<1.0,>=0.12->gradio) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->typer<1.0,>=0.12->gradio) (2.16.1)\n",
            "Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio->httpx>=0.24.1->gradio) (1.2.2)\n",
            "Collecting httptools>=0.5.0 (from uvicorn>=0.14.0->gradio)\n",
            "  Downloading httptools-0.6.1-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (341 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m341.4/341.4 kB\u001b[0m \u001b[31m24.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting python-dotenv>=0.13 (from uvicorn>=0.14.0->gradio)\n",
            "  Downloading python_dotenv-1.0.1-py3-none-any.whl (19 kB)\n",
            "Collecting uvloop!=0.15.0,!=0.15.1,>=0.14.0 (from uvicorn>=0.14.0->gradio)\n",
            "  Downloading uvloop-0.19.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.4 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m3.4/3.4 MB\u001b[0m \u001b[31m30.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting watchfiles>=0.13 (from uvicorn>=0.14.0->gradio)\n",
            "  Downloading watchfiles-0.22.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.2 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.2/1.2 MB\u001b[0m \u001b[31m31.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface-hub>=0.19.3->gradio) (3.3.2)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer<1.0,>=0.12->gradio) (0.1.2)\n",
            "Building wheels for collected packages: ffmpy\n",
            "  Building wheel for ffmpy (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for ffmpy: filename=ffmpy-0.3.2-py3-none-any.whl size=5584 sha256=f59411bd8a76041cba545bb931d250540a4e4ccb91b7e9b4ba78a81f3d486b83\n",
            "  Stored in directory: /root/.cache/pip/wheels/bd/65/9a/671fc6dcde07d4418df0c592f8df512b26d7a0029c2a23dd81\n",
            "Successfully built ffmpy\n",
            "Installing collected packages: pydub, ffmpy, websockets, uvloop, tomlkit, semantic-version, ruff, python-multipart, python-dotenv, orjson, httptools, h11, dnspython, aiofiles, watchfiles, uvicorn, starlette, httpcore, email_validator, httpx, gradio-client, fastapi-cli, altair, fastapi, gradio\n",
            "  Attempting uninstall: altair\n",
            "    Found existing installation: altair 4.2.2\n",
            "    Uninstalling altair-4.2.2:\n",
            "      Successfully uninstalled altair-4.2.2\n",
            "Successfully installed aiofiles-23.2.1 altair-5.3.0 dnspython-2.6.1 email_validator-2.2.0 fastapi-0.111.1 fastapi-cli-0.0.4 ffmpy-0.3.2 gradio-4.38.1 gradio-client-1.1.0 h11-0.14.0 httpcore-1.0.5 httptools-0.6.1 httpx-0.27.0 orjson-3.10.6 pydub-0.25.1 python-dotenv-1.0.1 python-multipart-0.0.9 ruff-0.5.3 semantic-version-2.10.0 starlette-0.37.2 tomlkit-0.12.0 uvicorn-0.30.1 uvloop-0.19.0 watchfiles-0.22.0 websockets-11.0.3\n"
          ]
        }
      ],
      "source": [
        "!pip install gradio"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "D39tKGz2JWPo",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "73ada14d-835c-474c-95e6-5f14cd9229ad"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ],
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "1hWRKHylpnFd"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import gradio as gr\n",
        "import tensorflow as tf\n",
        "from PIL import Image\n",
        "import cv2\n",
        "from tensorflow.keras.preprocessing import image\n",
        "import keras\n",
        "from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "id": "WDJtcq2bqvuA"
      },
      "outputs": [],
      "source": [
        "mymodel = keras.saving.load_model(\"/content/drive/MyDrive/final_model.keras\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "id": "2uXp6jPGprwX"
      },
      "outputs": [],
      "source": [
        "mymodel = tf.keras.models.load_model('/content/drive/MyDrive/final_model.keras')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 646
        },
        "id": "5f6ll4zpp1U5",
        "outputId": "06ec828c-baf1-4cf9-f7ec-ccd6c0f5f4aa"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Setting queue=True in a Colab notebook requires sharing enabled. Setting `share=True` (you can turn this off by setting `share=False` in `launch()` explicitly).\n",
            "\n",
            "Colab notebook detected. To show errors in colab notebook, set debug=True in launch()\n",
            "Running on public URL: https://94663761a5e49e3372.gradio.live\n",
            "\n",
            "This share link expires in 72 hours. For free permanent hosting and GPU upgrades, run `gradio deploy` from Terminal to deploy to Spaces (https://huggingface.co/spaces)\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "<div><iframe src=\"https://94663761a5e49e3372.gradio.live\" width=\"100%\" height=\"500\" allow=\"autoplay; camera; microphone; clipboard-read; clipboard-write;\" frameborder=\"0\" allowfullscreen></iframe></div>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": []
          },
          "metadata": {},
          "execution_count": 9
        }
      ],
      "source": [
        "emotion_labels = {'angry':0,'disgust':1,'fear':2,'happy':3,'neutral':4,'sad':5,'surprise':6,}\n",
        "index_to_emotion = {v: k for k, v in emotion_labels.items()}\n",
        "\n",
        "def prepare_image(img_pil):\n",
        "  img = img_pil.resize((224,224))\n",
        "  img_array = img_to_array(img)\n",
        "  img_array = np.expand_dims(img_array,axis =0)\n",
        "  img_array/= 255.0\n",
        "  return img_array\n",
        "\n",
        "\n",
        "\n",
        "def predict_emotion(image):\n",
        "  processed_image = prepare_image(image)\n",
        "  prediction = mymodel.predict(processed_image)\n",
        "  predicted_class = np.argmax(prediction,axis =1)\n",
        "  predicted_emotion = index_to_emotion.get(predicted_class[0])\n",
        "  return predicted_emotion\n",
        "\n",
        "\n",
        "interface = gr.Interface(\n",
        "    fn = predict_emotion,\n",
        "    inputs = gr.Image(type =\"pil\"),\n",
        "    outputs = \"text\",\n",
        "    title = \"Emotion Detection Classifier\",\n",
        "    description = \"Upload an image and see the predicted emotion\"\n",
        ")\n",
        "\n",
        "interface.launch()\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "QnZ_74dorsFO"
      },
      "outputs": [],
      "source": []
    }
  ],
  "metadata": {
    "accelerator": "GPU",
    "colab": {
      "gpuType": "T4",
      "provenance": [],
      "mount_file_id": "1bPHqyQjpD7-saaPtvJ8wrIos0zz4QqS5",
      "authorship_tag": "ABX9TyPa5fe2Cn7bZCZyvAS44xAg",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}