import argparse

from trl import GRPOTrainer

from hprams import DataConfig
from utils import accuracy_reward, format_reward
from hprams import TrainConfig
from utils import make_conversation

def main(train_config: TrainConfig, data_config: DataConfig):
    print(f"Train config: {train_config}\nData config: {data_config}")
    
    # Get Generated Data
    
    # Format

    # GRPO Trainer
    trainer = GRPOTrainer(
        model=train_config.model_name_or_path, 
        reward_funcs=[format_reward, accuracy_reward],
        args=,
        train_dataset=,
        eval_dataset=,
    )
    
    trainer.train()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    pass