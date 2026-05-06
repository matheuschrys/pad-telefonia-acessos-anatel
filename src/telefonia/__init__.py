"""Ferramentas para análise dos acessos de telefonia móvel da Anatel."""

from .analysis import (
    DATA_FILE,
    DATA_RAW_DIR,
    PROJECT_ROOT,
    add_date_column,
    load_telefonia_data,
    summarize_by_state,
    summarize_by_technology,
    summarize_time_evolution,
)

__all__ = [
    "DATA_FILE",
    "DATA_RAW_DIR",
    "PROJECT_ROOT",
    "add_date_column",
    "load_telefonia_data",
    "summarize_by_state",
    "summarize_by_technology",
    "summarize_time_evolution",
]
