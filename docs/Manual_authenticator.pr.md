



# authenticator
  
Obtenha o código de Fator de Autenticação Dupla do tipo TOPT (Time-based One Time Password) como Google and Microsoft Authenticator  

*Read this in other languages: [English](Manual_authenticator.md), [Português](Manual_authenticator.pr.md), [Español](Manual_authenticator.es.md)*
  
![banner](imgs/Banner_authenticator.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  



## Como usar este módulo

O módulo tem 2 opções para obter o código de autenticação:
1. Obtenha o código do Secret
2. Obtenha o código do QR
Alguns aplicativos concedem explicitamente o segredo ou permitem que o usuário o defina e, em outros casos, fornece apenas um código QR que, ao ser lido, registra o aplicativo no Autenticador. Para testar as duas opções, você pode usar sua conta do Google que fornece QR e Secret:
   1. Digite "Gerenciar sua conta do Google"
   2. Entre na seção "Segurança"
   3. Selecione "Verificação em duas etapas" na caixa "Como você faz login no Google"
   4. Selecione "Aplicativo autenticador"
   5. Clique em "+ Configurar Autenticador"
   6. A imagem de um código QR aparecerá, clique com o botão direito e salve a imagem.
   7. Para obter o segredo gerado, clique em "Você não pode digitalizá-lo?" e copie o código aí indicado.

## Descrição do comando

### Obter código
  
Obtenha o código de autenticação.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Secret|Digite a senha.|secret32|
|Número de dígitos (opcional)|Quantidade de dígitos que terá o código retornado.|6|
|Intervalo|Quantidade de dígitos que terá o código retornado.|30|
|Atribuir resultado a variável|Atribuir resultado da conexão a variável.|result|

### Obter código de QR
  
Leia um código QR de um arquivo PNG e obtenha o código de autenticação.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho da imagem QR|Caminho para o arquivo PNG com código QR.|C:\Users\user\Documents\QR_image.png|
|Atribuir resultado a variável|Atribuir resultado da conexão a variável.|result|
