import re

def format_reward(completions: list, **kwargs) -> list[float]:
    """Reward function that checks if the completion has a specific format."""
    
    pattern = r"^<think>.*?</think><answer>.*?</answer>$"
    completion_contents = [completion[0]["content"] for completion in completions]
    matches = [re.match(pattern, content) for content in completion_contents]
    
    return [1.0 if match else 0.0 for match in matches]

def accuracy_reward(completions: list, solutions: list[str], **kwargs) -> list[float]:
    """Reward function that checks if the completion matches the solution."""
    
    contents = [completion[0]["content"] for completion in completions]
    rewards = []
    
    for content, solution in zip(contents, solutions):
        extracted_list = re.findall("<answer>(.*?)</answer>", content)
        response = extracted_list[-1] if len(extracted_list) > 0 else ""
        rewards.append(1.0 if response == solution else 0.0)
        
    return rewards