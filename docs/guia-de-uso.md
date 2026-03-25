# Guia de Uso — Documento de Requisitos do FitnessApp

## Para quem é este guia

Este guia ensina como usar o ambiente de trabalho do projeto FitnessApp para montar o documento de requisitos. Você não precisa saber programar — tudo é feito por conversa com o Claude (uma inteligência artificial que vai te guiar).

---

## O que você vai precisar

1. **VS Code** — editor de texto gratuito. Baixe em: https://code.visualstudio.com
2. **Extensão "Markdown All in One"** — instale dentro do VS Code (para visualizar os documentos formatados)
3. **Claude Code** — extensão do Claude para VS Code (plano Pro recomendado)
4. **O projeto** — a pasta `fitness-app-requirements` aberta no VS Code

---

## Como abrir o projeto

1. Abra o VS Code
2. Vá em **Arquivo → Abrir Pasta** e selecione a pasta `fitness-app-requirements`
3. No painel da esquerda você verá toda a estrutura de pastas e arquivos
4. Abra o painel do Claude Code (ele aparece como uma aba lateral ou inferior no VS Code)
5. Pronto — o Claude já leu o contexto do projeto automaticamente e sabe o que fazer

---

## Estrutura do projeto (o que é cada coisa)

```
docs/
├── 00-template-tela.md      ← Modelo padrão que toda tela segue
├── 01-visao-geral.md        ← Índice de TODAS as telas e o status de cada uma
├── 02-personas.md           ← Quem são os usuários do app
├── 03-fluxos-de-navegacao.md ← Mapa de como o usuário navega entre telas
├── 04-design-system.md      ← Cores, fontes, botões — visual do app
├── 06-mvp.md                ← O que entra na primeira versão vs futuro
└── screens/                 ← Pasta com todas as telas documentadas
    ├── auth/                ← Telas de login, cadastro, etc.
    ├── perfil/              ← Telas do perfil do aluno
    ├── avaliacoes/          ← Telas de avaliações
    ├── dieta/               ← Telas de dieta
    ├── treinos/             ← Telas de treino
    └── ...
```

O arquivo mais importante para acompanhar o progresso é o `docs/01-visao-geral.md` — ele lista todas as telas e mostra o status de cada uma:

- 🔴 NÃO INICIADO — ainda não foi documentada
- 🟡 EM ANDAMENTO — começou mas não terminou
- 🟠 PENDENTE REVISÃO — documentada mas tem pontos para confirmar
- 🟢 CONCLUÍDO — pronta para desenvolvimento

---

## Os comandos disponíveis

No painel do Claude Code, você digita comandos começando com `/`. Cada comando faz uma coisa específica. Abaixo está a explicação de cada um.

---

### /status

**O que faz:** Mostra um resumo rápido de como está o progresso do documento.

**Quando usar:** No início de cada sessão de trabalho, para saber onde parou e o que precisa ser feito.

**Como usar:**
```
/status
```

**O que acontece:** O Claude lê todos os arquivos e te mostra:
- Quantas telas estão prontas
- Quantas faltam
- Quais são as próximas telas sugeridas para documentar
- Se tem alguma decisão bloqueando o progresso

---

### /entrevistar-cliente

**O que faz:** Processa anotações de uma reunião ou conversa com o cliente e organiza tudo.

**Quando usar:** Depois de uma reunião com o cliente, quando você tem anotações para processar.

**Como usar:**
```
/entrevistar-cliente reunião sobre o módulo de Treinos
```

Depois de enviar o comando, cole as anotações da reunião na mesma mensagem ou na mensagem seguinte.

**O que acontece:** O Claude vai:
1. Separar o que está **confirmado** pelo cliente
2. Identificar o que ficou **incerto** e precisa ser perguntado de novo
3. Listar o que **não foi coberto** e é importante perguntar
4. Sugerir perguntas de follow-up para a próxima reunião
5. Indicar quais documentos do projeto precisam ser atualizados

---

### /mapear-fluxo

**O que faz:** Define como o usuário navega entre as telas de um módulo (por exemplo, como o aluno vai da tela de Treinos para a tela de Iniciar Treino).

**Quando usar:** Quando for começar a trabalhar em um módulo novo. Faça isso ANTES de documentar as telas individuais.

**Como usar:**
```
/mapear-fluxo Treinos
```

**O que acontece:** O Claude vai te fazer perguntas sobre:
- Como o usuário chega nesse módulo
- Quais telas existem dentro dele
- Como as telas se conectam entre si
- Quais ações abrem modais ou janelas flutuantes

No final, ele gera um diagrama visual do fluxo e lista todas as telas que precisam ser documentadas.

---

### /mapear-tela

**O que faz:** Documenta uma tela específica do app, do zero.

**Quando usar:** Quando você já sabe quais telas existem (depois do `/mapear-fluxo`) e quer detalhar cada uma.

**Como usar:**
```
/mapear-tela Login
```

**O que acontece:** O Claude te faz perguntas em 3 blocos:

1. **Contexto:** O que essa tela faz? Quem acessa?
2. **Interface:** O que aparece na tela? Campos? Botões? O que cada botão faz?
3. **Navegação e Regras:** De onde o usuário vem? Para onde vai? Tem alguma regra especial?

As perguntas são objetivas — geralmente com opções A, B, C para você escolher. Depois de responder tudo, o Claude gera o arquivo da tela completo e salva no lugar certo.

---

### /mapear-modulo

**O que faz:** Mapeia um módulo inteiro de uma vez — primeiro o fluxo, depois todas as telas. É uma combinação do `/mapear-fluxo` + vários `/mapear-tela` em sequência.

**Quando usar:** Quando tiver uma sessão longa e quiser fazer um módulo do começo ao fim.

**Como usar:**
```
/mapear-modulo Avaliações
```

**O que acontece:** O Claude conduz tudo em 4 fases:
1. Entende o propósito do módulo
2. Mapeia o fluxo de navegação
3. Documenta cada tela (fazendo perguntas para cada uma)
4. Valida se está tudo consistente entre as telas

É o comando mais demorado, mas o mais completo.

---

### /revisar-tela

**O que faz:** Revisa uma tela que já foi documentada e ajuda a completar o que ficou pendente.

**Quando usar:** Quando uma tela tem itens marcados com ⚠️ PENDENTE, ou quando o cliente trouxe respostas novas para perguntas que estavam em aberto.

**Como usar:**
```
/revisar-tela docs/screens/auth/login.md
```

(Informe o caminho do arquivo da tela)

**O que acontece:** O Claude lê a tela, lista tudo que está incompleto, e faz perguntas objetivas para cada item pendente. No final, atualiza o documento e muda o status.

---

### /validar-consistencia

**O que faz:** Verifica se existe alguma contradição ou erro entre as telas documentadas.

**Quando usar:** Periodicamente, especialmente antes de entregar o documento. Recomendado: depois de documentar cada 5-10 telas.

**Como usar:**
```
/validar-consistencia
```

Para validar só um módulo específico:
```
/validar-consistencia Treinos
```

**O que acontece:** O Claude lê todos os documentos e procura problemas como:
- Tela A diz que vai para Tela B, mas Tela B não existe
- O mesmo campo tem nomes diferentes em telas diferentes
- Uma tela tem ação de "salvar" mas não documenta o que acontece se der erro
- O índice de telas está desatualizado

Gera um relatório com os problemas encontrados e sugestões de correção.

---

### /gerar-resumo

**O que faz:** Gera documentos de resumo em diferentes formatos, dependendo do público.

**Como usar (4 variantes):**

```
/gerar-resumo cliente
```
Gera um resumo executivo para apresentar ao cliente — linguagem simples, sem termos técnicos, com a lista de decisões que o cliente ainda precisa tomar.

```
/gerar-resumo dev
```
Gera um briefing técnico para o time de desenvolvimento — arquitetura de telas, pontos de atenção, o que está confirmado vs pendente.

```
/gerar-resumo status
```
Mostra um relatório de progresso — parecido com o `/status` mas mais detalhado.

```
/gerar-resumo lovable
```
Gera o prompt em inglês para colar no Lovable (ferramenta que vai gerar a base do projeto). Use quando o documento de requisitos estiver completo.

---

### /estimar-complexidade

**O que faz:** Analisa as telas documentadas e estima a dificuldade de desenvolvimento de cada uma.

**Quando usar:** Quando quiser ter uma noção de esforço antes de iniciar o desenvolvimento.

**Como usar:**
```
/estimar-complexidade
```

**O que acontece:** O Claude classifica cada tela como:
- 🟢 Simples — tela estática, poucos elementos
- 🟡 Média — formulários, validações, alguns estados
- 🔴 Complexa — gráficos, lógica pesada, muitos estados

E sugere a ordem em que as coisas devem ser implementadas.

---

## Fluxo de trabalho — passo a passo do dia a dia

### Sessão típica de trabalho

```
1. Abra o VS Code com o projeto
2. Abra o Claude Code
3. Digite: /status
4. Veja onde parou e o que precisa ser feito
5. Trabalhe nas telas pendentes usando os comandos
6. No final, salve tudo (o Claude faz isso automaticamente)
```

### Quando tiver uma reunião com o cliente

```
1. Anote tudo que o cliente falar (pode ser no bloco de notas)
2. Depois da reunião, abra o projeto
3. Use: /entrevistar-cliente [contexto da reunião]
4. Cole as anotações
5. O Claude organiza tudo e diz quais documentos atualizar
```

### Quando for documentar um módulo novo

```
1. /mapear-fluxo [nome do módulo]    ← Define a navegação
2. /mapear-tela [nome da tela]       ← Uma por uma
   OU
1. /mapear-modulo [nome do módulo]   ← Tudo de uma vez
```

### Quando for revisar telas pendentes

```
1. /status                           ← Veja quais telas têm pendências
2. /revisar-tela [caminho do arquivo] ← Complete cada uma
```

### Quando for entregar o documento

```
1. /validar-consistencia             ← Verifique erros
2. Corrija os problemas encontrados
3. /gerar-resumo cliente             ← Para apresentar ao cliente
4. /gerar-resumo lovable             ← Para iniciar o desenvolvimento
```

---

## Dicas importantes

1. **Responda com opções simples.** O Claude vai te dar opções A, B, C. Basta responder a letra. Se nenhuma opção serve, diga "Outro" e explique.

2. **Não tenha medo de dizer "não sei".** Se o Claude perguntar algo que você não sabe, diga "pendente" ou "preciso perguntar para o cliente". Ele marca como ⚠️ PENDENTE e segue em frente.

3. **Use `/status` sempre que começar.** É a forma mais rápida de saber onde está o progresso.

4. **Não edite os arquivos manualmente** (a não ser que saiba o que está fazendo). Deixe o Claude gerar e atualizar — ele mantém o padrão e a consistência.

5. **Salve tudo no Git.** Periodicamente, peça ao Claude: "faça um commit com as alterações". Isso garante que nada se perde.

6. **Uma tela por vez.** Não tente fazer tudo de uma vez. Documente uma tela, revise, e passe para a próxima. Qualidade é mais importante que velocidade.

7. **O arquivo `01-visao-geral.md` é seu painel de controle.** Abra-o a qualquer momento para ver o status de todas as telas do projeto.

---

## Resumo rápido dos comandos

| Comando | Para que serve | Quando usar |
|---|---|---|
| `/status` | Ver progresso geral | Início de cada sessão |
| `/entrevistar-cliente` | Processar anotações do cliente | Após reuniões |
| `/mapear-fluxo` | Definir navegação de um módulo | Antes de documentar telas |
| `/mapear-tela` | Documentar uma tela | Após ter o fluxo mapeado |
| `/mapear-modulo` | Fluxo + todas as telas de uma vez | Sessão longa e dedicada |
| `/revisar-tela` | Completar pendências de uma tela | Quando tiver respostas do cliente |
| `/validar-consistencia` | Checar erros entre documentos | A cada 5-10 telas documentadas |
| `/gerar-resumo` | Criar resumos para diferentes públicos | Antes de entregas |
| `/estimar-complexidade` | Estimar esforço de desenvolvimento | Antes de iniciar o dev |
