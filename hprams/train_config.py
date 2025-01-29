from dataclasses import dataclass, field

@dataclass
class TrainConfig:
    """ Configuration for training """
    
    model_name_or_path: str = field(
        default='Qwen/Qwen2.5-0.5B', 
        metadata={
            "help": (
                "RL base model to use. "
            )
        }
    )
    
    output_dir: str = field(
        default="/saves", 
        metadata={
            "help": (
                "The output directory where the model checkpoints will be written."
            )
        }
    )
    
    save_steps: int = field(
        default=5, 
        metadata={
            "help": (
                "Save checkpoint every X updates steps."
            )
        }
    )
    
    logging_steps: int = field(
        default=10, 
        metadata={
            "help": (
                "Log every X updates steps."
            )
        }
    )
    
    logging_dir: str = field(
        default="/logs", 
        metadata={
            "help": (
                "The output directory where the logs will be written."
            )
        }
    )
    
    per_device_train_batch_size: int = field(
        default=2, 
        metadata={
            "help": (
                "The batch size per GPU for training."
            )
        }
    )
    
    per_device_eval_batch_size: int = field(
        default=4, 
        metadata={
            "help": (
                "The batch size per GPU for evaluation."
            )
        }
    )
    
    
    
    