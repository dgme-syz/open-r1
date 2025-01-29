from dataclasses import dataclass, field

@dataclass
class DataConfig:
    """ Configuration for data """
    
    # default everyone $\in [10, 20]$
    max_varibles: int = field(
        default=6, 
        metadata={
            "help": (
                "The maximum number of variables in the prompt."
            )
        }   
    )
    
    generate_num: int = field(
        default=100_000, 
        metadata={
            "help": (
                "The number of samples to generate."
            )
        }   
    )
    
    