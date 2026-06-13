# Tela: Editar Perfil

---

## Metadados
| Campo | Valor |
|---|---|
| **Nome da tela** | Editar Perfil |
| **Modulo** | Perfil |
| **Prioridade** | 🔵 MVP |
| **Status** | 🟡 EM ANDAMENTO |
| **Ultima atualizacao** | 2026-06-08 |

---

## 1. Objetivo da Tela
> O que o usuario consegue fazer nesta tela? Qual problema ela resolve?

Permite ao Aluno **editar seus dados pessoais e a foto de perfil**. O Aluno altera os campos editaveis e confirma com o botao **Salvar**, recebendo feedback de sucesso ou erro. Alguns campos sao apenas leitura (E-mail, @ treinador.vela e Objetivo), pois sao alterados em outros fluxos ou definidos automaticamente.

---

## 2. Quem Acessa / Pre-condicoes
> Quem pode ver esta tela? Quais condicoes precisam ser verdadeiras?

- **Usuario:** Aluno autenticado (edita apenas o proprio perfil)
- **Pre-condicoes:**
  - Usuario deve estar logado
  - Chega a esta tela a partir do Meu Perfil
- **Permissoes especiais:** Nenhuma

---

## 3. Layout e Componentes Visuais
> Descreva a estrutura visual da tela de cima para baixo.

### 3.1 Header / Cabecalho
- Conteudo: Botao voltar (← / "Cancelar") + Titulo "Editar Perfil"
- Comportamento: Fixo no topo. Ao voltar com alteracoes pendentes, exibe alerta de descarte (ver RN).

### 3.2 Corpo Principal
> Descrever secoes da tela, na ordem que aparecem

**Secao 1 — Foto de Perfil**
- Componente: Avatar (foto atual) com **icone de lapis** sobreposto sobre a foto
- Conteudo: Texto abaixo da foto: **"Foto obrigatoria"**
- Comportamento: Campo obrigatorio. Ao clicar no icone de lapis, abre as opcoes: **Tirar foto** (camera) e **Escolher foto** (galeria).

**Secao 2 — Dados Editaveis (Formulario)**
- Componente: Formulario
- Conteudo (campos editaveis): Nome completo, WhatsApp, Pais, Data de nascimento, Sexo, @ instagram, @ aluno.vela
- Comportamento: Validacao por campo; botao Salvar ao final

**Secao 3 — Dados Somente Leitura**
- Componente: Lista de campos desabilitados/somente leitura
- Conteudo:
  - E-mail (alteravel apenas na tela Configuracoes, via confirmacao por e-mail)
  - @ treinador.vela (preenchido automaticamente quando o treinador monta o treino do Aluno)
  - Objetivo (proveniente da Anamnese; alteracao deve ser alinhada com o treinador no proximo treino/avaliacao)
- Comportamento: Exibicao apenas; nao editavel nesta tela

### 3.3 Footer / Rodape
- Conteudo: Botao primario **"Salvar"** (e, opcionalmente, "Cancelar")
- Comportamento: Botao Salvar fixo na parte inferior (ou ao final do formulario)

---

## 4. Campos e Formularios

> Preencher apenas se a tela tiver campos de entrada (inputs, selects, etc.)

| # | Nome do Campo | Tipo | Obrigatorio | Placeholder | Validacao | Mensagem de Erro |
|---|---|---|---|---|---|---|
| 1 | Nome completo | Texto | Sim | "Seu nome completo" | Apenas letras (e espacos); minimo 2 caracteres; nao vazio | "Digite seu nome usando apenas letras" |
| 2 | WhatsApp | Telefone | Sim | "+55 (11) 90000-0000" | Numero valido com DDI/DDD; mascara aplicada | "Digite um numero de WhatsApp valido" |
| 3 | Pais | Seletor (dropdown com busca) | Sim | "Selecione seu pais" | Deve selecionar um item da lista | "Selecione um pais" |
| 4 | Data de nascimento | Texto (digitavel, com mascara) | Sim | "DD/MM/AAAA" | Formato obrigatorio **DD/MM/AAAA**; nao pode ser data futura; sem idade minima | "Digite uma data valida no formato DD/MM/AAAA" |
| 5 | Sexo | Seletor (dropdown) | Sim | "Selecione" | Opcoes: Feminino, Masculino e Nao Informar | "Selecione uma opcao" |
| 6 | @ instagram | Texto | Nao | "@seuinstagram" | Sem espacos | "Usuario do Instagram invalido" |
| 7 | @ aluno.vela | Texto | Sim | "@seuusuario" | Apenas letras minusculas e numeros, sem espacos/caracteres especiais; unico no sistema; sem palavras ofensivas | "Esse @ ja esta em uso" / "Use apenas letras minusculas e numeros" |

### Regras de Preenchimento
- **Nome:** aceita apenas letras e espacos (sem numeros ou caracteres especiais).
- **WhatsApp:** incluir DDI (codigo de pais), considerando alunos de diferentes nacionalidades; aplicar mascara.
- **Pais:** selecao via dropdown com busca, exibindo bandeira + nome do pais. (A exibicao no Meu Perfil mostra apenas a bandeira ao lado do @.)
- **Data de nascimento:** campo **digitavel** (sem date picker), com mascara no formato obrigatorio **DD/MM/AAAA**; bloquear datas futuras; sem restricao de idade minima.
- **Sexo:** seletor no mesmo formato do campo Pais (dropdown), com as opcoes Feminino, Masculino e Nao Informar.
- **@ aluno.vela:** validacao de padrao e unicidade ocorre **ao sair do campo (on blur) e ao salvar**, exibindo erro abaixo do campo. Ao salvar a alteracao, o novo @ deve refletir automaticamente em todos os lugares do app.
- **Foto:** obrigatoria.

---

## 5. Botoes e Acoes

| # | Componente | Label / Icone | Posicao | Estado Inicial | Acao ao Clicar |
|---|---|---|---|---|---|
| 1 | Botao voltar | ← / "Cancelar" | Header (esquerda) | Ativo | Volta para Meu Perfil. Se houver alteracoes pendentes, exibe alerta "Descartar alteracoes?" |
| 2 | Icone | Lapis (sobre a foto) | Secao 1 (sobre o avatar) | Ativo | Abre as opcoes: **Tirar foto** (camera) e **Escolher foto** (galeria) |
| 3 | Botao primario | "Salvar" | Rodape | **Desabilitado** ate haver alteracao valida | Valida os campos → mostra loading → persiste alteracoes → toast de sucesso → volta ao Meu Perfil |

---

## 6. Estados da Tela

### 6.1 Estado Inicial / Vazio
- Formulario carregado com os dados atuais do Aluno.
- Botao "Salvar" **desabilitado** ate que haja alguma alteracao valida.

### 6.2 Estado de Carregamento (Loading)
- **Carregar a tela:** skeleton loader nos campos enquanto os dados sao buscados.
- **Salvar:** spinner sobre o botao "Salvar"; botao e campos desabilitados durante a requisicao.

### 6.3 Estado de Erro
- **Erro de campo:** borda vermelha + mensagem abaixo do campo (ver tabela de validacoes).
- **@ aluno.vela indisponivel:** mensagem abaixo do campo "Esse @ ja esta em uso".
- **Erro de rede:** toast "Sem conexao. Tente novamente."
- **Erro da API ao salvar:** toast "Nao foi possivel salvar. Tente novamente." (mantem os dados no formulario).

### 6.4 Estado de Sucesso
- Toast "Perfil atualizado com sucesso!" + redirecionamento para o Meu Perfil com os dados atualizados.

### 6.5 Estado Desabilitado / Bloqueado *(se aplicavel)*
- Botao "Salvar" desabilitado enquanto nao houver alteracao valida.
- Campos somente leitura (E-mail, @ treinador.vela, Objetivo) sempre desabilitados.

---

## 7. Fluxo de Navegacao

### De onde o usuario chega nesta tela
| Origem | Gatilho |
|---|---|
| Meu Perfil | Clica em "Editar perfil" no header |

### Para onde o usuario pode ir desta tela
| Destino | Gatilho |
|---|---|
| Meu Perfil | Salvar com sucesso |
| Meu Perfil | Cancelar / voltar (com alerta de descarte se houver alteracoes pendentes) |

---

## 8. Regras de Negocio
> Regras especificas que impactam o comportamento desta tela.

- **RN01:** O Aluno edita apenas o proprio perfil.
- **RN02:** Campos editaveis: Nome, WhatsApp, Pais, Data de nascimento, Sexo, @ instagram (opcional) e @ aluno.vela. Todos obrigatorios, **exceto @ instagram**.
- **RN03:** **E-mail** e somente leitura nesta tela. A alteracao de e-mail ocorre na tela **Configuracoes**, com **confirmacao por e-mail**.
- **RN04:** **@ treinador.vela** e somente leitura; preenchido **automaticamente** quando o treinador monta o treino do Aluno.
- **RN05:** **Objetivo** e somente leitura; vem da **Anamnese**. Para mudar o objetivo, o Aluno deve alinhar com o treinador no proximo treino/avaliacao.
- **RN06:** **Nome** aceita apenas **letras** (e espacos).
- **RN07:** **@ aluno.vela** deve ser **unico** no sistema; padrao: apenas **letras minusculas e numeros**, sem espacos/caracteres especiais e sem **palavras ofensivas**. Validacao **on blur** e **ao salvar**.
- **RN08:** Ao salvar a alteracao do **@ aluno.vela**, a mudanca reflete **automaticamente em todos os lugares do app** que fazem mencao ao @.
- **RN09:** **Foto de perfil** e obrigatoria.
- **RN10:** **Data de nascimento** e **digitavel** no formato obrigatorio **DD/MM/AAAA**; nao pode ser futura; **sem idade minima**.
- **RN11:** Ao tentar **sair sem salvar** com alteracoes pendentes, exibir alerta **"Descartar alteracoes?"** (confirmar para sair / cancelar para continuar editando).

---

## 9. Responsividade (Mobile vs Web)
> Diferencas de comportamento ou layout entre plataformas.

| Aspecto | Mobile | Web |
|---|---|---|
| Regras e comportamento | Identico | Identico |
| Layout | Tela cheia, campos empilhados; formulario sobe ao abrir teclado | Conteudo centralizado com largura maxima; campos podem usar colunas |
| Data de nascimento | Campo digitavel com mascara DD/MM/AAAA | Campo digitavel com mascara DD/MM/AAAA |

> As regras e o padrao de comportamento sao os mesmos em ambas as plataformas; apenas ajustes visuais e de layout sao aplicados.

---

## 10. Acessibilidade
> Consideracoes de acessibilidade para esta tela.

- Labels acessiveis em todos os campos do formulario.
- Mensagens de erro associadas ao campo (anunciadas por leitores de tela).
- Contraste de cores conforme WCAG 2.1 AA.
- Navegacao por teclado (tab order logica) no web.
- Texto alternativo na foto de perfil.
- Estados de foco visiveis nos campos e botoes.
- Feedback de sucesso/erro (toasts) tambem anunciado por leitores de tela.

---

## 11. Historico de Alteracoes

| Data | Autor | Descricao |
|---|---|---|
| 2026-06-08 | Equipe FitnessApp | Criacao inicial do documento (entrevista de mapeamento) |
| 2026-06-08 | Equipe FitnessApp | Ajustes: foto simplificada para apenas "foto obrigatoria" (removidas acoes Alterar/Remover e o "aplicada ao salvar"); Data de nascimento passou a campo digitavel com mascara DD/MM/AAAA (sem date picker); Sexo passou a seletor (dropdown) no mesmo formato do Pais; removida a RN sobre o botao Salvar desabilitado (informacao interna) |
| 2026-06-08 | Equipe FitnessApp | Recapitulacao foto: removida mencao residual a "Remover foto" no estado 6.5 (foto e obrigatoria, nao ha remocao); confirmada edicao da foto so nesta tela e exibicao no Meu Perfil |
| 2026-06-08 | Equipe FitnessApp | Removida a opcao de perfil sem foto/iniciais (RG01 excluida): foto obrigatoria desde o cadastro, perfil sempre tem foto |
