import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu


def read_data(
        dataset_name: str
) -> pd.DataFrame:
    dku_dataset = dataiku.Dataset(dataset_name)
    df = dku_dataset.get_dataframe()

    return df


def process_revenue_loss(
        df: pd.DataFrame,
        revenue_type: str
) -> pd.DataFrame:
    important_cols = ['State', 'revenue_loss', 'loss_type']

    if revenue_type == 'Expected':

        df['loss_type'] = 'Expected'

    elif revenue_type == 'Actual':

        churn_filter = df.Churn == 1
        df = df[churn_filter]
        df['loss_type'] = 'Current'
        df.rename(columns={'Total_Charge': 'revenue_loss'}, inplace=True)

    df = df[important_cols]
    return df


def stack_dfs(df1: pd.DataFrame,
              df2: pd.DataFrame
              ) -> pd.DataFrame:
    df = pd.concat([df1, df2])

    return df


def create_total_revenue_loss(
        loss_predictions: str,
        historic_losses: str
) -> pd.DataFrame:
    loss_predictions_df = read_data(loss_predictions)
    historic_losses_df = read_data(historic_losses)

    loss_predictions_df = process_revenue_loss(loss_predictions_df, 'Expected')
    historic_losses_df = process_revenue_loss(historic_losses_df, 'Actual')

    total_rev_loss = stack_dfs(loss_predictions_df, historic_losses_df)

    return total_rev_loss

