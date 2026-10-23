from sklearn.ensemble import RandomForestClassifier

def treinar_random_forest(x_train, y_train):
    modelo = RandomForestClassifier(class_weight='balanced', random_state=42)
    modelo.fit(x_train, y_train)
    return modelo
