import hydra
from omegaconf import DictConfig


@hydra.main(config_path="../conf", config_name="example", version_base=None)
def process_data(config: DictConfig):
    print("Accessing with bracket notation:", config["process"]["cols_to_drop"])
    print("Accessing with dot notation:", config.process.cols_to_drop)


if __name__ == "__main__":
    process_data()
