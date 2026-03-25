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

## ⚠️ Pontos Pendentes de Definição

- Haverá deep link por notificação push? (ex: lembrete de treino)
- Como funciona a navegação entre tabs durante um treino ativo?
- Haverá onboarding de feature (tooltips) além do onboarding inicial?
- 