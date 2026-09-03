# Registered predictions

Written and committed before full evaluation runs.

**Date:** 2026-09-02

**Models:** A = anthropic/claude-haiku-4-5-20251001; B = openai-api/local/qwen3.6-35b-a3b, reasoning = off, model quant = UD-Q3_K_M, KV quant = q8_0

**Tasks:** gsm8k (match, numeric), truthfulqa (choice, MC1), xstest (model-graded; grader = A)

> Note: For xstest, scorer_model is set to claude-haiku-4-5 which resolves to Model A, as the logs show. The decision is explained in detail in LAB_NOTEBOOK.md.

**Parameters:** n = 100 per task per model, temperature = 0

## Model predictions

P1. GSM8K accuracy: will not show a statistically significant difference between the models.

P2. TruthfulQA MC1 accuracy: A > B by at least 10%

P3. XSTest (safe subset) compliance rates: B refuses more safe prompts than A by at least 15%.

## Method predictions

P4. The model-graded task (XSTest) will show the largest gap between A and B relative to the standard error.

## Stated uncertainty
At n = 100, the standard error near 0.5 is roughly .05, so at a 95% confidence interval, resolvable differences sit at about .10 or greater.
