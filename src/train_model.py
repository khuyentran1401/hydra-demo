import hydra
from omegaconf import DictConfig, OmegaConf


@hydra.main(config_path="../conf", config_name="main", version_base=None)
def train_model(config: DictConfig):
    # Converts the entire config object to a YAML string for readable output
    print(OmegaConf.to_yaml(config))


if __name__ == "__main__":
    train_model()
