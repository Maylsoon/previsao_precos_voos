   Previsão de Preços de Passagens Aéreas
   
📌 1. Objetivo do Projeto

Este projeto tem como objetivo desenvolver um modelo de Machine Learning capaz de prever o preço de passagens aéreas com base nas características do voo, como companhia aérea, duração, número de paradas e origem/destino.

A proposta simula um cenário real de negócio, onde a previsão de preços pode auxiliar em estratégias de precificação, análise de mercado e tomada de decisão.

📊 2. Dataset
Base: Flight Price Prediction (Kaggle)
Contém informações como:
Companhia aérea
Origem e destino
Data da viagem
Horários
Número de paradas
Duração do voo
Preço da passagem (target)

🔍 3. Análise Exploratória (EDA)

Principais insights:

A maior parte das passagens concentra-se em torno de ~9.000
Existem outliers relevantes, incluindo valores muito acima da média
A companhia Jet Airways apresenta maior faturamento e preços mais elevados
Voos mais longos e com mais paradas tendem a ser mais caros
Diferenças entre volume e faturamento indicam estratégias distintas entre companhias

🛠️ 4. Feature Engineering

Foram criadas variáveis relevantes a partir dos dados originais:

Extração de:
Dia e mês da viagem
Hora de partida e chegada
Conversão de duração total do voo
Transformação da variável Total_Stops em formato numérico
Tratamento de colunas redundantes ou pouco informativas

⚙️ 5. Modelagem
🔹 Baseline
Modelo: Decision Tree Regressor
Resultado:
R² ≈ 0.64

👉 Serviu como referência inicial

🔹 Modelo Final
Modelo mais robusto XGBoost
Ajustes realizados:
Controle de overfitting
Validação com Cross Validation
Remoção de feature rara (evitando overfitting localizado)
Correção de pipeline (encoding consistente)

📈 6. Resultados Finais
R²: 0.82
MAE: ~1172
RMSE: ~1907

👉 O modelo demonstrou boa capacidade de generalização na base de teste.

📉 7. Análise de Erros
O modelo captura bem a tendência central dos dados
Presença de heterocedasticidade:
erros maiores em passagens mais caras
Resíduos aproximadamente centrados em zero
Maior dificuldade em prever valores extremos

📊 8. Importância das Variáveis

As variáveis mais relevantes para o modelo foram:

Duração total do voo
Número de paradas
Companhia aérea
Data da viagem

👉 Indica que o preço está fortemente relacionado a características operacionais do voo.

💡 9. Insights de Negócio
Voos mais longos e complexos tendem a ter preços mais elevados
Diferenças entre companhias indicam estratégias distintas de precificação
Companhias com maior volume nem sempre possuem maior faturamento
Previsão de preços pode auxiliar em:
análise competitiva
definição de preços
recomendação de ofertas

⚠️ 10. Limitações
Modelo apresenta maior erro em passagens de alto valor
Algumas categorias possuem poucos dados (ex: companhias raras)
Dataset não contém variáveis externas relevantes, como:
demanda
distância real
sazonalidade completa

🚀 11. Próximos Passos
Testar modelos mais avançados (tuning mais profundo)
Aplicar técnicas como:
Target Encoding
Feature Selection
Incluir dados externos (ex: distância, demanda)
Deploy do modelo (API ou aplicação)

🧠 12. Aprendizados
Importância de evitar data leakage
Necessidade de pipeline consistente entre treino e teste
Impacto de features raras no overfitting
Diferença entre modelo bom e modelo que generaliza
