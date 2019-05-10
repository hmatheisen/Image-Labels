# Image Labels

A script I made to change the training data of a collection in Visual Recognition

## Create a virtual env (optional)

1. Create the venv folder

    ```bash
    virtualenv -p python3 ./venv
    ```

2. Activate the venv

    ```bash
    source ./venv/bin/activate
    ```

## Install dependencies

```
pip install -r requirments.txt
```

## Use your credentials

1. Create a `.env` file:

    ```bash
    cp .env.example .env
    ```
 
2. Fill it with your own Visual Recognition Credentials

## Run the script

```
python3 ./main.py
```

## Images Folders

The `image` folder corresponds to the old collection and he `new_images` folder corresponds to the images with their training data updated by the script.
