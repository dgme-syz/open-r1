import re

import numexpr

def format_reward(completions: list, **kwargs) -> list[float]:
    """Reward function that checks if the completion has a specific format."""
    
    pattern = r"^<think>.*?</think><answer>.*?</answer>$"
    completion_contents = [completion[0]["content"] for completion in completions]
    matches = [re.match(pattern, content) for content in completion_contents]
    
    return [1.0 if match else 0.0 for match in matches]

def accuracy_reward(prompts: list, completions: list, **kwargs) -> list[float]:
    """Reward function that checks if the completion matches the solution."""
    
    contents = [completion[0]["content"] for completion in completions]
    rewards = []
    
    print(contents, prompts)
    for content, problem in zip(contents, prompts):
        print(content, problem)
        extracted_list = re.findall("<answer>(.*?)</answer>", content)
        response = extracted_list[-1] if len(extracted_list) > 0 else None
        
        rewards.append(0.0)
        if response:
            # number warpped by ('1,2,3')
            nums = re.findall("\(`(.*)`\)", problem)[0].split(',') # char
            target = re.findall("target `(\d*)`\.", problem)[0]
            # check response has shape 1+2-3
            rep = response.replace(" ", "")
            if bool(re.fullmatch("\d([+-]\d)+", rep)):
                nums_out = re.findall("\d+", rep)
                if (
                    sorted(nums) == sorted(nums_out)
                    and numexpr.evaluate(rep) == int(target)
                ):
                    rewards[-1] = 1.0
        
    return rewards