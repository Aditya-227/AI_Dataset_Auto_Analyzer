def generate_report(context, recommendations):

    report = f"""
AI Dataset Auto Analyzer Report

Rows: {context.rows}
Columns: {context.columns}

Numeric Features:
{context.numeric_features}

Categorical Features:
{context.categorical_features}

Missing Values:
{context.missing_values}

Detected Patterns:
{context.patterns}

Recommended Problem Type:
{recommendations["problem_type"]}

Suggested Models:
{recommendations["models"]}
"""

    return report