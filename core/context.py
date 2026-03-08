from dataclasses import dataclass, field
import pandas as pd


@dataclass
class DatasetContext:
    
    # raw dataset
    dataframe: pd.DataFrame | None = None
    
    # metadata
    rows: int = 0
    columns: int = 0
    column_names: list = field(default_factory=list)

    # feature types
    numeric_features: list = field(default_factory=list)
    categorical_features: list = field(default_factory=list)
    datetime_features: list = field(default_factory=list)

    # analysis results
    missing_values: dict = field(default_factory=dict)
    correlations: pd.DataFrame | None = None
    summary_stats: dict = field(default_factory=dict)

    # pattern detection
    patterns: dict = field(default_factory=dict)

    # ML recommendations
    recommended_models: list = field(default_factory=list)

    # visualization objects
    visualizations: dict = field(default_factory=dict)