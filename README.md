<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6;">

  <header style="text-align: center; padding: 20px; background-color: #f4f4f4;">
        <h1>Identificação de Pneumonia em Imagens de Raios-X utilizando Redes Neurais Convolucionais</h1>
        <p>Este projeto utiliza redes neurais convolucionais (CNNs) para identificar a presença de pneumonia em imagens de raios-X.</p>
    </header>

   <section style="padding: 20px;">
        <h2>Índice</h2>
        <ul>
            <li><a href="#sobre">Sobre</a></li>
            <li><a href="#objetivo">Objetivo</a></li>
            <li><a href="#tecnologias">Tecnologias Utilizadas</a></li>
            <li><a href="#conjunto-de-dados">Conjunto de Dados</a></li>
            <li><a href="#arquitetura">Arquitetura do Modelo</a></li>
            
            
</ul>
    </section>

  <section id="sobre" style="padding: 20px;">
        <h2>Sobre</h2>
        <p>
            Este projeto visa aplicar redes neurais convolucionais (CNN) para a detecção de pneumonia, uma infecção que afeta os pulmões e pode ser diagnosticada através de imagens médicas. Usando um conjunto de imagens de raios-X, o objetivo é construir um modelo de aprendizado de máquina capaz de classificar automaticamente essas imagens como indicativas de pneumonia ou não.
          *Vale sempre informar que essas imagens foram fornecidas por (kaggle.com), e que não tem como objetivo uma comprovação medica.*
        </p>
    </section>

   <section id="objetivo" style="padding: 20px;">
        <h2>Objetivo</h2>
        <p>
            O objetivo principal é classificar imagens de raios-X em duas categorias: pneumonia ou saudável. O modelo de rede neural convolucional é treinado com imagens de raios-X de um conjunto de dados rotulado.
        </p>
    </section>

   <section id="tecnologias" style="padding: 20px;">
        <h2>Tecnologias Utilizadas</h2>
        <p>
            O projeto foi desenvolvido utilizando as seguintes tecnologias:
        </p>
        <ul>
            <li>Python</li>
            <li>TensorFlow / Keras</li>
            <li>OpenCV</li>
            <li>Matplotlib / Seaborn</li>
            <li>Pandas / NumPy</li>
            <li>Scikit-learn</li>
        </ul>
    </section>
    
   <section id="conjunto-de-dados" style="padding: 20px;">
        <h2>Conjunto de Dados</h2>
        <p>
            O conjunto de dados utilizado contém imagens de raios-X de pacientes diagnosticados com pneumonia ou saudáveis. As imagens estão organizadas em pastas, sendo uma para cada classe: <strong>pneumonia</strong> e <strong>saudável</strong>. O conjunto de dados é dividido da seguinte forma:
        </p>
        <ul>
            <li><strong>Conjunto de Teste:</strong> 80% das imagens para treinamento.</li>
            <li><strong>Conjunto de Validação:</strong> 20% das imagens para validação do modelo.</li>
        </ul>
        <p>Os dados podem ser obtidos no [link para o conjunto de dados].</p>
    </section>

   <section id="arquitetura" style="padding: 20px;">
        <h2>Arquitetura do Modelo</h2>
        <p>
            O modelo é uma rede neural convolucional (CNN) composta pelas seguintes camadas:
        </p>
        <ul>
            <li><strong>Camadas Convolucionais (Conv2D):</strong> Para extração de características das imagens.</li>
            <li><strong>Camadas de Pooling:</strong> Para redução da dimensionalidade e extração das características mais importantes.</li>
            <li><strong>Camadas Completamente Conectadas:</strong> Para realizar a classificação final da imagem.</li>
            <li><strong>Camada de Saída:</strong> Uma camada com uma unidade de saída e função de ativação <strong>sigmoid</strong> para classificação binária.</li>
        </ul>
        <p>
            O modelo é treinado com imagens de raios-X e avaliado em um conjunto de validação.
        </p>
    </section>

 

</body>
</html>
