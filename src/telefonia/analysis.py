"""Funções reutilizáveis para a análise de acessos de telefonia móvel.

O módulo concentra as transformações que antes ficavam espalhadas pelo
notebook. Assim, o notebook passa a ser mais narrativo e o código pode ser
reutilizado em scripts, testes ou novas análises.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_RAW_DIR = PROJECT_ROOT / "data" / "raw"
DATA_FILE = DATA_RAW_DIR / "br_anatel_telefonia_movel_ddd.csv"

DEFAULT_MAIN_TECHNOLOGIES = (
    "GSM",
    "WCDMA",
    "LTE",
    "M2M",
    "M2M Padrão",
    "M2M Especial",
)


def load_telefonia_data(path: str | Path = DATA_FILE) -> pd.DataFrame:
    """Carrega o CSV de telefonia móvel e adiciona a coluna mensal ``data``.

    Parameters
    ----------
    path:
        Caminho do arquivo CSV. Por padrão, usa o arquivo versionado em
        ``data/raw``.

    Returns
    -------
    pandas.DataFrame
        Dados carregados com a coluna ``data`` do tipo ``datetime64``.
    """
    data = pd.read_csv(path)
    return add_date_column(data)


def add_date_column(data: pd.DataFrame) -> pd.DataFrame:
    """Retorna uma cópia dos dados com a coluna ``data`` no primeiro dia do mês."""
    result = data.copy()
    result["data"] = pd.to_datetime(
        {
            "year": result["ano"],
            "month": result["mes"],
            "day": 1,
        }
    )
    return result


def summarize_time_evolution(data: pd.DataFrame) -> pd.DataFrame:
    """Agrega o total mensal de acessos e cria a escala em milhões."""
    summary = (
        data.groupby("data", as_index=False)["acessos"]
        .sum()
        .sort_values("data")
    )
    summary["acessos_milhoes"] = summary["acessos"] / 1_000_000
    return summary


def summarize_by_technology(
    data: pd.DataFrame,
    technologies: Iterable[str] = DEFAULT_MAIN_TECHNOLOGIES,
) -> pd.DataFrame:
    """Agrega acessos por mês e tecnologia, filtrando tecnologias de interesse."""
    summary = (
        data.groupby(["data", "tecnologia"], as_index=False)["acessos"]
        .sum()
        .sort_values(["data", "tecnologia"])
    )
    summary["acessos_milhoes"] = summary["acessos"] / 1_000_000
    return summary[summary["tecnologia"].isin(tuple(technologies))]


def summarize_by_state(data: pd.DataFrame, year: int) -> pd.DataFrame:
    """Agrega o total anual de acessos por UF em escala de milhões."""
    year_data = data[data["ano"] == year]
    summary = (
        year_data.groupby("sigla_uf", as_index=False)["acessos"]
        .sum()
        .sort_values("acessos", ascending=False)
    )
    summary["acessos_milhoes"] = summary["acessos"] / 1_000_000
    return summary
