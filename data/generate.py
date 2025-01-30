import os

import jsonlines
import numpy as np
from tqdm import tqdm

PROBLEM_TRMPLATE = (
    "Given list of integers (`{numbers}`) must be combined using `+` or `-` between adjacent numbers "
    "to reach the target `{target}`.Only `+` or `-` can be used between numbers. The final expression "
    "must equal `{target}`.**Example:** Given `3,7,2,5` and target `13`, the solution is `3+7-2+5`."
)

def generate_one(n_counts: int, min_range: int, max_range: int):
    """ Generate a list of peompts and their solutions, [min, max) """
    
    if n_counts < 1:
        raise ValueError("n_counts must be a positive integer and >= 2")
                    
    nums = np.random.randint(min_range, max_range, n_counts)
    nums_str = nums.astype(str)
    # next combine all the states
    
    tot = np.sum(nums)
    for i in range(1 << (n_counts - 1)):
        sign = list(map(int, bin(i)[2:].zfill(n_counts)))
        subsum = tot - 2 * sum(sign * nums)
        yield {
                "prompt": PROBLEM_TRMPLATE.format(
                    numbers=",".join(nums_str),
                    target=str(subsum),
                ), 
            }


def sample(
    max_count: int, 
    min_range: int, 
    max_range: int,
    save_path: str = "./data/files/prompts.jsonl",
    batch_size: int = 5000, 
    num_samples: int = 100000,
) -> None:
    """ setting [min, max), and sample averagely 10w prompt, write to JSON """
    
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    
    sample_size = []
    sample_cnt = 0
    for i in range(2, max_count + 1):
        if i == 2:
            sample_size += [num_samples // (max_count - 1) // 2]
        else:
            sample_size += [sample_size[-1] // 2]
        sample_cnt += sample_size[-1] * (1 << (i - 1))

    buffer = [] # buffer to store the prompts
    with jsonlines.open(save_path, "w") as f:
        print(f"Generating prompts to {save_path}")
        pbar = tqdm(total=sample_cnt)
        for num_count in range(2, max_count + 1):
            for _ in range(sample_size[num_count - 2]):
                for x in generate_one(num_count, min_range, max_range):
                    buffer += [x]
                    if len(buffer) >= batch_size:
                        f.write_all(buffer)
                        buffer = []
                        
                        
                    pbar.update(1)
    
        if buffer: 
            f.write_all(buffer)
    del buffer
    
    print(f"{sample_cnt} samples saved.")
    
                        
        
        