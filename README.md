# CogMath: Assessing LLMs' Authentic Mathematical Ability from a Human Cognitive Perspective

[![Data License](https://img.shields.io/badge/Data%20License-CC%20By%20NC%204.0-red.svg)](https://github.com/Ljyustc/CogMath/blob/main/LICENSE/DATA_LICENSE)

This is the repo for paper ["CogMath: Assessing LLMs' Authentic Mathematical Ability from a Human Cognitive Perspective" (ICML'2025)]

## CogMath Evaluation Datasets
- [`MATH.json`](MATH.json) 
- [`GSM8K.json`](GSM8K.json)
- [`MExam.json`](MExam.json)

In each dataset, `ori_question` and `ori_answer` represent the original question and answer from the source dataset. For each evaluation dimension (from `Dimension 1` to `Dimension 9`), `inquiry` refers to the specific query designed for that dimension, and `inquiry_answer` is the corresponding answer. 

For `Dimension 1` and `Dimension 4`, the expected answer to the `inquiry` is the `original answer`. For `Dimension 2` and `Dimension 3`, since they are based on a counterfactual setting, the expected response is "unsolvable". Therefore, for these four dimensions, we do not include the `inquiry_answer` field in the data.

## CogMath Evaluation Results
| Model                |   MATH   |  GSM8K   |  MExam   |
|:---------------------|:--------:|:--------:|:--------:|
| LLaMA2-13B           |   0.8    |   6.4    |   2.4    |
| LLaMA3-8B            |   5.6    |   34.2   |   9.6    |
| Mixtral-8x7BInstruct |   9.2    |   21.2   |   13.3   |
| Gemini-1.5-Flash     |   29.1   |   50.0   |   33.8   |
| GPT-3.5-Turbo        |   17.6   |   42.4   |   19.2   |
| GPT-4                |   39.3   |   67.1   |  36.4    |
| DeepSeek-V2.5        |   36.8   |   64.6   |   34.2   |
| DeepSeek-R1          |   44.8   |   70.3   |    -     |

## Reference
If you find this repository helpful, please cite our paper.
```
@inproceedings{liu2025cogmath,
  title={CogMath: Assessing LLMs' Authentic Mathematical Ability from a Human Cognitive Perspective},
  author={Liu, Jiayu and Huang, Zhenya and Dai, Wei and Cheng, Cheng and Wu, Jinze and Sha, Jing and Li, Song and Liu, Qi and Wang, Shijin and Chen, Enhong},
  booktitle={Proceedings of the 42nd International Conference on Machine Learning},
  year={2025}
}
```