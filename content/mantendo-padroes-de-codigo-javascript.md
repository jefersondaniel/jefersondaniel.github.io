Title: Mantendo padrões de código Javascript
Slug: mantendo-padroes-de-codigo-javascript
Date: 2016-05-01
Category: Dicas, Javascript

Um código desorganizado, com variáveis seguindo diferentes padrões de escrita, sem atenção para declarações e desuso de variáveis é muito propenso a erros. Para facilitar nossa vida existem ferramentas de lint como o [ESLint][1], que vou explicar nesse post.

O ESLint é uma ferramenta bastante flexível para análise de código que busca trechos problemáticos ou que não seguem padrões configurados. Por exemplo: identação, nomenclatura de variáveis e globais. Essa análise pode ser feita através da linha de comando ou até mesmo no seu editor de código. É preciso que você tenha o nodejs instalado em seu computador para poder instalar esse lint com o comando:

```
npm install -g eslint
```

Feito isso você pode criar um arquivo ".eslintrc" na pasta de seu projeto com as regras recomendadas e adicionar as suas preferências. Podemos testar a seguinte configuração para projetos frontend:

```json
{
  "extends": "eslint:recommended",
  "env": {
    "browser": true
  },
  "rules": {
    "semi": ["error", "never"],
    "camelcase": "warn"
  }
}
```

Esse arquivo estende um conjunto de regras recomendado e especifica o ambiente browser, isso serve que variaveis globais do navegador não sejam interpretadas como não definidas. Além disso o arquivo adiciona as seguintes regras:
* semi: Verifica se o código nunca usa ponto-e-virgula nos finais de linha,trata como erro linhas de código fora do padrão.
* camelcase: Verifica se as variaveis são nomeadas seguindo o padrão *camelCase*, trata como aviso linhas de código fora do padrão.

Você pode testar criando um arquivo "lala.js" e rodando o comando **eslint lala.js**:

```
var a = 1
var ugly_var = "2";
```

```
$ eslint lala.js

/home/jeferson/lala.js
  1:5   error    'a' is defined but never used               no-unused-vars
  2:5   warning  Identifier 'ugly_var' is not in camel case  camelcase
  2:5   error    'ugly_var' is defined but never used        no-unused-vars
  2:19  error    Extra semicolon                             semi
```

Viu como é fácil manter padrões de código? ainda existe bastante [regras][2] e [plugins][3] para esse linter. Espero que tenha se interessado, pois é uma ferramenta bastante útil e que fica melhor se configurada no seu editor de código. Com o Sublime, basta instalar os pacotes **Sublime-Linter** e **Sublime-Linter-contrib-eslint**

[1]: http://eslint.org
[2]: http://eslint.org/docs/rules
[3]: http://eslint.org/docs/user-guide/integrations
