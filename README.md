# Hydra Demo

[![View the Article](https://img.shields.io/badge/CodeCut-View%20the%20Article-blue)](https://codecut.ai/stop-hard-coding-in-a-data-science-project-use-configuration-files-instead/)  

## Set up the environment

1. Install [uv](https://github.com/astral-sh/uv)
1. Set up the environment:

```bash
uv sync
```

## Download the data

1. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009?resource=download)

2. Move the downloaded file to `data/raw/`

## Run the scripts

Run the data processing script:

```bash
uv run src/process.py
```

Run the model training script:

```bash
uv run src/train_model.py
```

Both scripts use Hydra for configuration management. The default configurations are in the `conf/main.yaml` file. You can override any configuration parameter using the command line. For example:

```bash
# Override test size in process.py
uv run src/process.py process.test_size=0.3

# Override hyperparameters in train_model.py
uv run src/train_model.py train.hyperparameters.svm__C=10
```

To see all available configuration options, you can use the `--help` flag:

```bash
# View configuration options for process.py
uv run src/process.py --help

# View configuration options for train_model.py
uv run src/train_model.py --help
```