import plotly.express as px
from core.context import DatasetContext


class VisualizationEngine:

    def correlation_heatmap(self, context: DatasetContext):

        if context.correlations is None:
            return None

        fig = px.imshow(
            context.correlations,
            text_auto=True,
            color_continuous_scale="RdBu",
            title="Correlation Heatmap"
        )

        return fig

    def numeric_distributions(self, context: DatasetContext):

        plots = {}

        for col in context.numeric_features:

            fig = px.histogram(
                context.dataframe,
                x=col,
                nbins=30,
                title=f"Distribution of {col}"
            )

            plots[col] = fig

        return plots