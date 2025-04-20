from latex2sympy2_extended import NormalizationConfig
from math_verify import LatexExtractionConfig, parse, verify


answer_parsed = parse(
    "<answer> 42 </answer>",
    extraction_mode="first_match",
)

print(answer_parsed)