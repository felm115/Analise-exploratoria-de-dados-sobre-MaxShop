import pandas as pd
import os

# Caminhos
RAW_PATH = "data/raw/MaxShop.xlsx"
OUTPUT_PATH = "data/processed/MaxShop_tratado.xlsx"


# =========================
# LOAD
# =========================
def load_data(path):
    return pd.read_excel(path)


# =========================
# CLEAN
# =========================
def remover_linhas_vazias(df):
    return df.dropna(how="all")


def remover_duplicados(df):
    return df.drop_duplicates()


# =========================
# TRANSFORM
# =========================
def texto_padronizado(df):

    if "Produto" in df.columns:
        df["Produto"] = df["Produto"].astype("string").str.strip().str.title()

    if "Categoria" in df.columns:
        df["Categoria"] = df["Categoria"].astype("string").str.strip().str.title()

    if "Regiao" in df.columns:
        df["Regiao"] = df["Regiao"].astype("string").str.strip().str.title()

    if "Estado" in df.columns:
        df["Estado"] = df["Estado"].astype("string").str.strip().str.title()

    if "Avaliação do Cliente" in df.columns:
        df["Avaliação do Cliente"] = (
            df["Avaliação do Cliente"]
            .astype("string")
            .str.strip()
            .str.title()
        )

    return df


def tratar_data_venda(df):

    if "Data_Venda" in df.columns:
        df["Data_Venda"] = (
            pd.to_datetime(
                df["Data_Venda"],
                dayfirst=True,
                errors="coerce"
            )
            .dt.strftime("%d/%m/%Y")
        )

    return df


def tratar_preco_unitario(df):

    if "Preco_Unitario" in df.columns:
        df["Preco_Unitario"] = (
            pd.to_numeric(
                df["Preco_Unitario"],
                errors="coerce"
            )
            .fillna(0)
            .astype(int)
        )

    return df


def criar_coluna_faturamento(df):

    if (
        "Quantidade" in df.columns and
        "Preco_Unitario" in df.columns
    ):

        quantidade = pd.to_numeric(
            df["Quantidade"],
            errors="coerce"
        ).fillna(0)

        preco = pd.to_numeric(
            df["Preco_Unitario"],
            errors="coerce"
        ).fillna(0)

        df["Faturamento"] = quantidade * preco

    return df


# =========================
# PIPELINE
# =========================
def run_pipeline():

    if not os.path.exists(RAW_PATH):
        print("❌ Arquivo não encontrado.")
        return

    os.makedirs(
        os.path.dirname(OUTPUT_PATH),
        exist_ok=True
    )

    df = load_data(RAW_PATH)

    df = remover_linhas_vazias(df)
    df = remover_duplicados(df)

    df = texto_padronizado(df)
    df = tratar_data_venda(df)
    df = tratar_preco_unitario(df)
    df = criar_coluna_faturamento(df)

    df.to_excel(
        OUTPUT_PATH,
        index=False
    )

    print("✅ Pipeline executado com sucesso!")
    print(f"Linhas processadas: {len(df)}")


if __name__ == "__main__":
    run_pipeline()


    