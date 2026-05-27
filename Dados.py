import pandas as pd
import os

# Arquivo tratado gerado pelo main.py
INPUT_PATH = "data/processed/MaxShop_tratado.xlsx"


# =========================
# LOAD
# =========================
def load_data(path):
    return pd.read_excel(path)


# =========================
# ANALISES
# =========================
def total_vendas_por_id(df):

    total = pd.DataFrame({
        "Total_IDs_Distintos": [
            df["ID_Venda"].nunique()
        ]
    })

    print("\nTOTAL DE IDS DISTINTOS")
    print(total)

    return total


def faturamento_por_ano(df):

    df["Data_Venda"] = pd.to_datetime(
        df["Data_Venda"],
        dayfirst=True,
        errors="coerce"
    )

    df["Ano"] = (
        df["Data_Venda"]
        .dt.year
        .astype("Int64")
    )

    faturamento = (
        df.groupby("Ano")["Faturamento"]
        .sum()
        .astype(int)
        .reset_index()
    )

    faturamento["Ano"] = (
        faturamento["Ano"]
        .astype(int)
    )

    print("\nFATURAMENTO POR ANO")
    print(faturamento)

    return faturamento


def faturamento_por_regiao(df):

    faturamento = (
        df.groupby("Regiao")["Faturamento"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    print("\nFATURAMENTO POR REGIAO")
    print(faturamento)

    return faturamento


def faturamento_por_estado(df):

    faturamento = (
        df.groupby("Estado")["Faturamento"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    print("\nFATURAMENTO POR ESTADO")
    print(faturamento)

    return faturamento


def faturamento_produto_categoria(df):

    faturamento = (
        df.groupby(
            ["Categoria", "Produto"]
        )["Faturamento"]
        .sum()
        .reset_index()
        .sort_values(
            by="Faturamento",
            ascending=False
        )
    )

    print("\nFATURAMENTO POR PRODUTO E CATEGORIA")
    print(faturamento)

    return faturamento


def avaliacao_total(df):

    avaliacao = (
        df["Avaliação do Cliente"]
        .value_counts()
        .reset_index()
    )

    avaliacao.columns = [
        "Avaliação",
        "Total"
    ]

    print("\nAVALIACAO TOTAL")
    print(avaliacao)

    return avaliacao


def avaliacao_por_estado(df):

    avaliacao = (
        df.groupby(
            [
                "Estado",
                "Avaliação do Cliente"
            ]
        )
        .size()
        .unstack(fill_value=0)
    )

    print("\nAVALIACAO POR ESTADO")
    print(avaliacao)

    return avaliacao


# =========================
# RUN ANALISE
# =========================
def run_analise():

    if not os.path.exists(INPUT_PATH):
        print(
            "❌ Arquivo tratado não encontrado."
        )
        print(
            "Execute o main.py primeiro."
        )
        return

    df = load_data(INPUT_PATH)

    total_vendas_por_id(df)
    faturamento_por_ano(df)
    faturamento_por_regiao(df)
    faturamento_por_estado(df)
    faturamento_produto_categoria(df)
    avaliacao_total(df)
    avaliacao_por_estado(df)

    print("\n✅ Analise concluida!")


if __name__ == "__main__":
    run_analise()


    

    