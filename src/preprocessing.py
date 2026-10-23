import pandas as pd
from sklearn.preprocessing import StandardScaler

def carregar_e_preparar_dados(caminho_csv):
    df = pd.read_csv(URL)
    # Criando a variavel alvo binaria
    df['target'] = (df['quality'] >= 7).astype(int)
    return df

def padronizar_features(x_train, x_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(x_train)
    X_test_scaled = scaler.transform(x_test)
    return X_train_scaled, X_test_scaled, scaler

