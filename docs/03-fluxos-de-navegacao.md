# Fluxos de Navegação

> Mapa completo de como o usuário se move entre as telas do app.

---

## Estrutura de Navegação Principal

```
┌─────────────────────────────────────────────────────┐
│                   APP NAVIGATION                     │
├─────────────────────────────────────────────────────┤
│                                                      │
│  [Não autenticado]          [Autenticado]            │
│                                                      │
│  Splash                     Tab Bar                  │
│    ↓                        ├── Home / Dashboard     │
│  Login ←──────────────────→ ├── Treinos              │
│    ↓                        ├── Rotinas              │
│  Dashboard                  ├── Avaliações           │
│                             └── Perfil               │
└─────────────────────────────────────────────────────┘
```

---

## Fluxo 1 — Autenticação

```
[Splash Screen]
    │
    ├── Usuário JÁ logado → [Dashboard / Home]
    │
    └── Usuário NÃO logado
            │
            ↓
        [Login]
            │
            ├── Login com sucesso → [Dashboard]
            │
            ├── "Esqueci senha" → [Recuperar Senha]
            │       ↓
            │   Insere e-mail → E-mail enviado
            │       ↓
            │   [Redefinir Senha] (via link no e-mail)
            │       ↓
            │   Senha redefinida → [Login]
            │
            └── "Criar conta" → [Cadastro]
                    │
                    ├── Cadastro concluído → [Onboarding]
                    │       ↓
                    │   [Boas-vindas]
                    │       ↓
                    │   [Dados Pessoais]
                    │       ↓
                    │   [Objetivo / Meta]
                    │       ↓
                    │   [Nível de Experiência]
                    │       ↓
                    │   [Dashboard]
```

---

## Navegação Bottom Tab Bar

> Visível apenas para usuários autenticados

| Tab | Ícone | Tela |
|---|---|---|
| 1 | 🏠 Home | Dashboard |
| 2 | 💪 Treinos | Lista de Treinos |
| 3 | 📋 Rotinas | Lista de Rotinas |
| 4 | 📊 Evolução | Avaliações / Gráficos |
| 5 | 👤 Perfil | Meu Perfil |

---

## Modais e Sheets Recorrentes

| Modal | Disparado por | Conteúdo |
|---|---|---|
| Seleção de Exercício | Criar/Editar Rotina | Catálogo com busca e filtros |
| Timer de Descanso | Concluir série | Contador regressivo com som |
| Confirmar Saída | Botão voltar durante treino | "Deseja pausar ou abandonar?" |
| Adicionar Medida | Nova Avaliação | Campos de medidas + unidade |

---

## Fluxo 3 — Perfil do Aluno

```
[Meu Perfil]  ← Tab Bar (ícone Perfil)
    │
    ├── Toque na foto → [Modal: Atualizar Foto]
    │       ↓
    │   Câmera / Galeria → foto salva → [Meu Perfil]
    │
    ├── Card "Dados Pessoais" → [Editar Perfil]
    │       │
    │       ├── Salvar com sucesso → [Meu Perfil]
    │       └── Voltar (sem salvar) → alerta "Descartar?" → [Meu Perfil]
    │
    ├── Card "Avaliações" → [Lista de Avaliações]
    │       │
    │       ├── Nova Avaliação → seletor de tipo
    │       │       ├── "Avaliação Completa" → [Nova Avaliação Completa]
    │       │       └── "Anamnese" → [Nova Anamnese]
    │       │
    │       ├── Toque em avaliação existente → [Detalhe da Avaliação]
    │       │       └── Exibe último valor de cada campo registrado
    │       │
    │       ├── "Comparar" → [Comparar Avaliações]
    │       │       └── Usuário seleciona 2 avaliações → exibe comparação lado a lado
    │       │
    │       └── "Ver evolução" → [Evolução / Gráficos]
    │               └── Gráficos das últimas 4–5 avaliações
    │
    └── Card "Minha Dieta" (Pós-MVP) → [Minha Dieta]
            │
            └── "Ver histórico" → [Histórico de Dietas]
```

> ⚠️ Fluxo do Personal Trainer (como acessa o perfil do aluno) ainda não mapeado — aguarda decisão sobre vínculo PT-Aluno.

---

## ⚠️ Pontos Pendentes de Definição

- Haverá deep link por notificação push? (ex: lembrete de treino)
- Como funciona a navegação entre tabs durante um treino ativo?
- Haverá onboarding de feature (tooltips) além do onboarding inicial?
- Como Personal Trainer navega para o perfil de um aluno vinculado?
- Como Nutricionista acessa o app para cadastrar dietas?
