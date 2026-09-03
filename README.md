# Inspect Evals Sandbox: Readme

## Purpose

This repo contains Inspect evals performed as a skill-building and learning exercise, not a research finding. Built to demonstrate LLM evaluation practice with registered predictions and commit logs.

## Overview

Inspect evals GSM8K, TruthfulQA, and XSTest were run on Claude Haiku 4.5 20251001 and a local Qwen 3.6 35b a3b UDQ3_K_M. Each was run n = 100 times once per model, temperature = 0 with reasoning off, and predictions were registered before the runs were completed. The Lab Notebook discusses the full setup, results, and limitations.

## Files

- README.md
- LICENSE
- requirements-lock.txt
- PREDICTIONS.md
- logs/
- LAB_NOTEBOOK.md
- results_table.py

## License

This project is released under the MIT License included in the repo.

## Tooling

Claude Code was used for advising and scaffolding results_table.py.

All prose, predictions, and interpretation are the author's.
