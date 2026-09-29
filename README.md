# Wave Metrics

A simple Python module for calculating metrics for wave model evaluation.

The module is designed to compare two already-matched datasets to perform **metric calculations**.

Data loading, time alignment, filtering, interpolation, spatial matching, and other data-processing steps are not included.

## Metrics

* Bias
* Normalized Mean Bias (NMB)
* Root Mean Square Error (RMSE)
* Scatter Index (SI)
* Correlation coefficient (r)

## Usage

Import the required functions from `wave_metrics.py`:

```python
from wave_metrics import bias, nmb, rmse, scatter_index, correlation, metrics
```

All standard metrics can be calculated at once using metrics function.

