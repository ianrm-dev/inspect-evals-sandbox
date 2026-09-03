# Inspect Evals Sandbox: Lab Notebook

## 1. Purpose

Performed as a skill-building and learning exercise, not a research finding. Built to demonstrate LLM evaluation practice with registered predictions and commit logs.

## 2. Setup

- inspect_ai 0.3.261, inspect_evals 0.19.0
- Model A: anthropic/claude-haiku-4-5-20251001, Model B: openai-api/local/qwen3.6-35b-a3b-nothink, reasoning = off, model quant = UD-Q3_K_M, KV quant = q8_0
- Hardware for Model B: AMD Ryzen™ 7 9800X3D × 16 with 32 GB RAM, NVIDIA GeForce RTX™ 5070 Ti with 16 GB VRAM
- OS for Model B: Ubuntu 24.04.4 LTS
- n = 100 per task per model; temperature 0, grader for xstest = Model A (with alias)
- Date of runs: 2026-09-02 Local EDT

## 3. Registered predictions

See PREDICTIONS.md at commit e1532c8dd50549ba9a795db3c96a03a2abb3b620, reproduced here verbatim:

### Model predictions

P1. GSM8K accuracy: will not show a statistically significant difference between the models.

P2. TruthfulQA MC1 accuracy: A > B by at least 10%

P3. XSTest (safe subset) compliance rates: B refuses more safe prompts than A by at least 15%.

### Method predictions

P4. The model-graded task (XSTest) will show the largest gap between A and B relative to the standard error.

### Stated uncertainty
At n = 100, the standard error near 0.5 is roughly .05, so at a 95% confidence interval, resolvable differences sit at about .10 or greater.

## 4. Results

| Task | Model | Scorer | n | Metric | Value | Std. error |
|---|---|---|---|---|---|---|
| inspect_evals/gsm8k | openai-api/local/qwen3.6-35b-a3b-nothink | match | 100 | accuracy | 0.970 | 0.017 |
| inspect_evals/truthfulqa | openai-api/local/qwen3.6-35b-a3b-nothink | choice | 100 | accuracy | 0.880 | 0.033 |
| inspect_evals/xstest | openai-api/local/qwen3.6-35b-a3b-nothink | model_graded_qa | 100 | refusal_rate | 0.160 | 0.037 |
| inspect_evals/gsm8k | anthropic/claude-haiku-4-5-20251001 | match | 100 | accuracy | 0.990 | 0.010 |
| inspect_evals/truthfulqa | anthropic/claude-haiku-4-5-20251001 | choice | 100 | accuracy | 0.880 | 0.033 |
| inspect_evals/xstest | anthropic/claude-haiku-4-5-20251001 | model_graded_qa | 100 | refusal_rate | 0.000 | 0.000 |


## 5. Discussion

| Predictions | Outcome | Basis |
|---|---|---|
| P1 | confirmed | At this n, the unpaired difference of proportions puts the p-value of the comparison at 0.31 meaning there is not a statistically significant difference between the models |
| P2 | refuted | The results for both models are exactly the same, discounting noise. |
| P3 | confirmed* | While it is statistically likely that my prediction holds confirmed, I will give the caveat that the 95% confidence interval has a range of .0875 to .2325. |
| P4 | confirmed | As the Match and Choice scoroer evals came out with no statistically significant difference between the models, the model-graded task does indeed show the largest gap between A and B relative to stderr. |


## 6. XSTest grader discussion

During smoke testing, using the dated Model A identifier for both the tested model and the grader model caused Inspect to create a single object for both, which shared the 256 token limit. This caused the grader results to show as NaN each time. Changing the scorer model identifier to the undated alias, which at the moment resolves to the same model, fixed the issue.

## 7. Audit trail

This repo provides the following to strengthen trust in the evaluation results:

- logs
- versions
- prompts (inside the logs)
- grader identity

## 8. Limitations

The following limits the confidence in the results:

- Small n (100) such that the confidence interval does not allow for evaluation distinctions less than about 10%.
- A single run per configuration does not account for errors within a run.
- Quantization of the local model is a confounding variable
- Grader model is unvalidated and the exact same model as A

## 9. Reproduction

Model A runs:

```
inspect eval inspect_evals/gsm8k inspect_evals/truthfulqa inspect_evals/xstest --model anthropic/claude-haiku-4-5-20251001 --limit 100 --temperature 0 --max-connections 1 -T scorer_model=anthropic/claude-haiku-4-5
```

Model B runs:

```
inspect eval inspect_evals/gsm8k inspect_evals/truthfulqa inspect_evals/xstest --model openai-api/local/qwen3.6-35b-a3b-nothink --limit 100 --temperature 0 --max-connections 1 -T scorer_model=anthropic/claude-haiku-4-5
```

## 10. Tooling

Claude Code was used for advising and scaffolding results_table.py.

All prose, predictions, and interpretation are the author's.