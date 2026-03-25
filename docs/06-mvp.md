# Definicao de MVP

> O que entra na primeira versao do app (MVP) vs o que fica para versoes futuras.
> Esta definicao guia a priorizacao de telas e o escopo do prompt para o Lovable.
> ⚠️ PENDENTE: Validar com o cliente as definicoes abaixo.

---

## Criterio de MVP

O MVP deve permitir que um aluno de musculacao:
1. Crie uma conta e faca login
2. Monte ou siga uma rotina de treino
3. Registre seu treino (series, reps, carga)
4. Veja seu historico de treinos
5. Acompanhe sua evolucao basica

> **Principio:** Se o usuario consegue ir a academia, abrir o app, treinar registrando tudo, e ver que esta evoluindo — o MVP esta pronto.

---

## Escopo por Modulo

### 🔵 MVP — Primeira Versao

#### Autenticacao
| Tela | Justificativa |
|---|---|
| Login | Essencial — entrada no app |
| Cadastro | Essencial — criacao de conta |
| Recuperar Senha | Essencial — usuario esquece senha |

#### Onboarding
| Tela | Justificativa |
|---|---|
| Boas-vindas | Primeira impressao + configuracao basica |
| Dados Pessoais | Nome, peso, altura — minimo para personalizar |
| Objetivo / Meta | Direcionar a experiencia do usuario |

#### Dashboard
| Tela | Justificativa |
|---|---|
| Home | Tela principal — ponto de partida de todas as jornadas |

#### Treinos
| Tela | Justificativa |
|---|---|
| Lista de Treinos | Hub do modulo de treinos |
| Iniciar Treino | Comecar a treinar |
| Treino em Andamento | Core do app — registrar series |
| Finalizar Treino | Fechar o treino, ver resumo |
| Historico de Treinos | Acompanhar frequencia |

#### Rotinas
| Tela | Justificativa |
|---|---|
| Lista de Rotinas | Ver rotinas criadas |
| Criar Rotina | Montar o plano de treino |
| Detalhe da Rotina | Ver exercicios da rotina |

#### Exercicios
| Tela | Justificativa |
|---|---|
| Catalogo de Exercicios | Buscar exercicios ao montar rotina |
| Detalhe do Exercicio | Ver como executar o exercicio |

#### Perfil
| Tela | Justificativa |
|---|---|
| Meu Perfil | Ver seus dados |

---

### 🟣 Pos-MVP — Segunda Versao

| Modulo | Tela | Justificativa |
|---|---|---|
| Auth | Redefinir Senha | Fluxo via link no e-mail — pode ser simplificado no MVP |
| Onboarding | Nivel de Experiencia | Enriquece a personalizacao mas nao bloqueia uso |
| Treinos | Detalhe do Treino (historico) | Ver detalhes de um treino passado — pode vir depois do basico |
| Rotinas | Editar Rotina | No MVP o usuario cria, mas para editar pode recriar |
| Exercicios | Busca de Exercicios | No MVP, busca pode ser integrada no catalogo sem tela separada |
| Avaliacoes | Lista de Avaliacoes | Modulo inteiro fica pos-MVP |
| Avaliacoes | Nova Avaliacao | Modulo inteiro fica pos-MVP |
| Avaliacoes | Detalhe da Avaliacao | Modulo inteiro fica pos-MVP |
| Avaliacoes | Evolucao / Graficos | Modulo inteiro fica pos-MVP |
| Perfil | Editar Perfil | No MVP, editar pode ser via re-onboarding |
| Perfil | Minhas Metas | Feature de engajamento — pos-MVP |

---

### ⚪ Futuro — Versoes Posteriores

| Feature | Descricao | Depende de |
|---|---|---|
| Login Social (Google/Apple) | OAuth com provedores | Decisao do cliente |
| Role de Personal Trainer | Painel do PT, vincular alunos | Decisao do modelo de negocio |
| Modo Offline | Treinar sem internet, sync depois | Arquitetura de sync |
| Notificacoes Push | Lembrete de treino, motivacao | Infra de push notifications |
| Tema Escuro | Dark mode | Design system finalizado |
| Gamificacao | Conquistas, streaks, desafios | Definir mecanicas |
| Plano Premium | Funcionalidades pagas | Modelo de negocio definido |
| Admin de Academia (B2B) | Painel para academias | Modelo de negocio definido |
| Integracao com Wearables | Apple Watch, smartbands | API dos dispositivos |

---

## Resumo Numerico

| Categoria | Telas |
|---|---|
| 🔵 MVP | 15 telas |
| 🟣 Pos-MVP | 10 telas |
| ⚪ Futuro | Features avulsas |
| **Total mapeado** | **25+ telas** |

---

## ⚠️ Decisoes Pendentes que Afetam o MVP

1. Login social entra no MVP? (impacto: auth + backend OAuth)
2. Catalogo de exercicios vem pre-populado? (impacto: precisa de seed data)
3. Rotinas pre-prontas para iniciantes? (impacto: onboarding + seed data)
4. Timer de descanso entre series? (impacto: treino em andamento)
5. Fotos de progresso entram no MVP? (impacto: storage + camera)
