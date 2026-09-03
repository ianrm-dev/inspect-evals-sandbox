import math
import statistics
from pathlib import Path
from inspect_ai.log import read_eval_log
from inspect_ai.scorer import value_to_float

to_float = value_to_float()
rows = []
for path in sorted(Path("logs").glob("*.eval")):
    log = read_eval_log(str(path))              # parse log file into an EvalLog object
    if log.status != "success":                 # skip aborted runs
        continue
    task = log.eval.task                        # e.g. "inspect_evals/gsm8k"
    model = log.eval.model                      # provider/model string
    samples = log.samples
    n = len(samples) if samples else 0
    for score in log.results.scores:            # one entry per scorer used by the task
        if "accuracy" in score.metrics:         # for gsm8k and truthfulqa
            metric = "accuracy"
            value = score.metrics[metric].value
            se = score.metrics["stderr"].value
        elif "refusal_rate" in score.metrics:   # for xstest
            metric = "refusal_rate"
            value = score.metrics[metric].value / 100
            refused = []
            nan_count = 0
            for sample in samples:
                v = to_float(sample.scores[score.name].value)
                if math.isnan(v):               # ungraded sample
                    nan_count += 1
                    continue
                refused.append(1.0 if v in (0.0, 0.5) else 0.0)
            se = statistics.stdev(refused) / math.sqrt(len(refused))
            if nan_count:
                print(f"NOTE: {path.name}: {nan_count} NaN grade(s); "
                      f"excluded from SE, but the task's refusal_rate still divides by n={n}")
        else:
            raise KeyError(f"{path.name}: scorer {score.name} has metrics {list(score.metrics)}, no handler")
        rows.append((task, model, score.name, n, metric, value, se))

print("| Task | Model | Scorer | n | Metric | Value | Std. error |")
print("|---|---|---|---|---|---|---|")
for task, model, scorer, n, metric, value, se in rows:
    print(f"| {task} | {model} | {scorer} | {n} | {metric} | {value:.3f} | {se:.3f} |")